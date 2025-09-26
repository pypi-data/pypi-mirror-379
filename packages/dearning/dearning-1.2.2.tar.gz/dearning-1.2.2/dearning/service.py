# dearning/serving.py
import http.server ,socketserver ,ssl ,json ,os
import sys ,base64 ,mmap ,threading ,asyncio
from pathlib import Path

# ------------ Konfigurasi ------------
MODEL_DIR = Path(os.environ.get("DEARNING_MODEL_DIR", "dm_models"))
MODEL_DIR.mkdir(parents=True, exist_ok=True)

# Password default (ganti di env atau argumen server)
DEFAULT_PASSWORD = os.environ.get("DEARNING_PASSWORD", "dearning_secure")

# Server defaults
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = int(os.environ.get("DEARNING_PORT", "8443"))
CERTFILE = os.environ.get("DEARNING_CERT", "server.crt")
KEYFILE = os.environ.get("DEARNING_KEY", "server.key")

# Cache sederhana (in-memory) untuk model kecil
_MAX_CACHE_BYTES = 2 * 1024 * 1024  # 2 MB threshold to auto-cache
_model_cache = {}  # key -> bytes

# ------------ DOMM (placeholder agil) ------------
async def domm_background_task(interval=5.0):
    """Task background sederhana: bisa dikembangkan untuk evict cache, audit log, dsb."""
    while True:
        try:
            # contoh: evict cache entries if memory/time heuristics (very simple)
            # (ini cuma demo; DOMM sesungguhnya harus cek mem usage, LRU, dll)
            if len(_model_cache) > 0:
                # keep small cache, print debug
                # print("[DOMM] cache entries:", len(_model_cache))
                pass
        except Exception:
            pass
        await asyncio.sleep(interval)

def start_domm_background_loop():
    """Start asyncio loop in thread to run domm background task."""
    def _run_loop():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.create_task(domm_background_task())
        loop.run_forever()
    t = threading.Thread(target=_run_loop, daemon=True)
    t.start()

# ------------ HTTP Handler ------------
class DearningHandler(http.server.BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    server_version = "DearningServer/0.1"
    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        if length <= 0:
            return None
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:
            return None
    def _send_json(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def do_POST(self):
        parsed_path = self.path
        data = self._read_json()
        if data is None:
            return self._send_json(400, {"error": "invalid json or empty body"})
        password = data.get("password")
        if password != getattr(self.server, "cloud_password", DEFAULT_PASSWORD):
            return self._send_json(403, {"error": "invalid password"})
        if parsed_path == "/import_model":
            return self._handle_import_model(data)
        elif parsed_path == "/load_model":
            return self._handle_load_model(data)
        else:
            return self._send_json(404, {"error": "unknown endpoint"})
    def _handle_import_model(self, data):
        fname = data.get("filename")
        content_b64 = data.get("content_b64")
        if not fname or not content_b64:
            return self._send_json(400, {"error": "missing filename or content_b64"})
        safe_name = os.path.basename(fname)
        path = MODEL_DIR / safe_name
        try:
            raw = base64.b64decode(content_b64)
        except Exception:
            return self._send_json(400, {"error": "invalid base64 content"})
        # write atomically: write to temp then move
        tmp = path.with_suffix(".tmp")
        with open(tmp, "wb") as fh:
            fh.write(raw)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
        # optional: auto-cache small model
        if path.stat().st_size <= _MAX_CACHE_BYTES:
            with open(path, "rb") as fh:
                _model_cache[safe_name] = fh.read()

        return self._send_json(200, {"status": "imported", "model": safe_name, "size": path.stat().st_size})
    def _handle_load_model(self, data):
        fname = data.get("filename")
        if not fname:
            return self._send_json(400, {"error": "missing filename"})
        safe_name = os.path.basename(fname)
        path = MODEL_DIR / safe_name
        if not path.exists():
            return self._send_json(404, {"error": "not found"})
        # if cached return cached base64
        if safe_name in _model_cache:
            content = _model_cache[safe_name]
            b64 = base64.b64encode(content).decode("ascii")
            return self._send_json(200, {"status": "ok", "filename": safe_name, "content_b64": b64, "cached": True})
        # use mmap to read file efficiently (stream if large)
        try:
            size = path.stat().st_size
            with open(path, "rb") as fh:
                mm = mmap.mmap(fh.fileno(), length=0, access=mmap.ACCESS_READ)
                data_bytes = mm[:]
                mm.close()
            b64 = base64.b64encode(data_bytes).decode("ascii")
            # optionally cache if small
            if size <= _MAX_CACHE_BYTES:
                _model_cache[safe_name] = data_bytes
            return self._send_json(200, {"status": "ok", "filename": safe_name, "content_b64": b64, "cached": False})
        except Exception as e:
            return self._send_json(500, {"error": "read_failed", "msg": str(e)})
    def log_message(self, format, *args):
        # minimal logging to avoid noisy stdout; could log to file instead
        return

# ------------ Server Runner ------------
class ThreadedHTTPSServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
def run_server(host=DEFAULT_HOST, port=DEFAULT_PORT, certfile=CERTFILE, keyfile=KEYFILE, password=DEFAULT_PASSWORD):
    httpd = ThreadedHTTPSServer((host, port), DearningHandler)
    httpd.cloud_password = password
    # wrap socket with ssl
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"[dearning] serving on https://{host}:{port} (models in {MODEL_DIR})")
    # start domm background
    start_domm_background_loop()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("shutting down server")
        httpd.shutdown()

# ------------ Client helpers (blocking) ------------
def _make_conn(host, port, use_ssl=True, timeout=30):
    if use_ssl:
        context = ssl.create_default_context()
        conn = http.client.HTTPSConnection(host, port=port, context=context, timeout=timeout)
    else:
        conn = http.client.HTTPConnection(host, port=port, timeout=timeout)
    return conn
def post(host, port, filename, model_path=None, model_bytes=None, password=DEFAULT_PASSWORD, use_ssl=True, timeout=60):
    """
    Upload model to server.
    Provide either model_path (path on disk) or model_bytes (bytes).
    Returns dict response parsed from server JSON.
    """
    if model_bytes is None:
        if model_path is None:
            raise ValueError("provide model_path or model_bytes")
        with open(model_path, "rb") as fh:
            model_bytes = fh.read()
    b64 = base64.b64encode(model_bytes).decode("ascii")
    payload = {"password": password, "filename": os.path.basename(filename), "content_b64": b64}
    body = json.dumps(payload).encode("utf-8")
    conn = _make_conn(host, port, use_ssl=use_ssl)
    try:
        conn.request("POST", "/import_model", body=body, headers={
            "Content-Type": "application/json",
            "Content-Length": str(len(body))
        })
        resp = conn.getresponse()
        data = resp.read()
        try:
            return json.loads(data.decode("utf-8"))
        except Exception:
            return {"status": "error", "http": resp.status, "raw": data.decode("latin1", errors="replace")}
    finally:
        conn.close()
def load(host, port, filename, password=DEFAULT_PASSWORD, use_ssl=True, timeout=60):
    """
    Download model from server. Returns bytes or raises.
    """
    payload = {"password": password, "filename": os.path.basename(filename)}
    body = json.dumps(payload).encode("utf-8")
    conn = _make_conn(host, port, use_ssl=use_ssl)
    try:
        conn.request("POST", "/load_model", body=body, headers={
            "Content-Type": "application/json",
            "Content-Length": str(len(body))
        })
        resp = conn.getresponse()
        data = resp.read()
        if resp.status != 200:
            # try parse error json
            try:
                return json.loads(data.decode("utf-8"))
            except Exception:
                raise RuntimeError(f"server error {resp.status}")
        j = json.loads(data.decode("utf-8"))
        b64 = j.get("content_b64")
        if not b64:
            raise RuntimeError("no content returned")
        return base64.b64decode(b64.encode("ascii"))
    finally:
        conn.close()

# ------------ Async wrappers ------------
async def async_post(*args, **kwargs):
    return await asyncio.to_thread(post, *args, **kwargs)
async def async_load(*args, **kwargs):
    return await asyncio.to_thread(load, *args, **kwargs)

# ------------ Small CLI for quick testing ------------
def _cli_run_server():
    host = DEFAULT_HOST
    port = DEFAULT_PORT
    cert = CERTFILE
    key = KEYFILE
    password = DEFAULT_PASSWORD
    if not Path(cert).exists() or not Path(key).exists():
        print("SSL cert/key not found. Generate server.crt/server.key or set DEARNING_CERT/DEARNING_KEY env.")
        sys.exit(1)
    run_server(host=host, port=port, certfile=cert, keyfile=key, password=password)

if __name__ == "__main__" and "serve" in sys.argv:
    _cli_run_server()
