import time, threading, sys, os, ctypes

# === GPU detection (ctypes OpenCL) ===
try:
    ocl = ctypes.cdll.LoadLibrary("libOpenCL.so")
    GPU_AVAILABLE = True

    # cek jumlah platform
    num_platforms = ctypes.c_uint()
    ocl.clGetPlatformIDs(0, None, ctypes.byref(num_platforms))
    DEVICE_INFO = f"OpenCL GPU Detected: {num_platforms.value} platform(s)"
except OSError:
    GPU_AVAILABLE = False
    DEVICE_INFO = "OpenCL (GPU/TPU) tidak tersedia"

def use_gpu_conditionally(data_size=10000):
    return GPU_AVAILABLE and data_size > 5000

# dummy array wrapper
def af_array(x):
    return x  # langsung kembalikan Python array

def gpu_dot(a, b):
    # dot product untuk 2D list
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError("Ukuran matrix tidak cocok")
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            s = 0
            for k in range(cols_a):
                s += a[i][k] * b[k][j]
            result[i][j] = s
    return result

def gpu_add(x, y):
    # x dan y list of list (matrix)
    return [[a + b for a, b in zip(row_x, row_y)] for row_x, row_y in zip(x, y)]

def gpu_mean(x):
    # x list angka
    return sum(x) / len(x) if x else 0.0

def gpu_info():
    return DEVICE_INFO if GPU_AVAILABLE else "GPU tidak aktif"

def is_gpu_on():
    return GPU_AVAILABLE

# === Dearning Processing Unit ===
class DearningProcessingUnit:
    _enabled = False
    _start_time = None
    _line_threshold = 450

    @classmethod
    def enable(cls):
        cls._enabled = True
        cls._start_time = time.time()
        print("⚡ Dearning Processing Unit diaktifkan...")
        monitor = threading.Thread(target=cls._monitor_usage)
        monitor.daemon = True
        monitor.start()

    @classmethod
    def _monitor_usage(cls):
        time.sleep(1)
        current_script = sys.argv[0]
        if not os.path.exists(current_script):
            return
        try:
            with open(current_script, "r") as f:
                lines = f.readlines()
                total_lines = len(lines)
        except Exception as e:
            print("❌ Gagal membaca script:", e)
            return

        print(f"📏 Total baris kode: {total_lines}")
        if total_lines > cls._line_threshold:
            print("⚙️ Kode panjang terdeteksi. Mengaktifkan optimasi...")
            cls._optimize_for_low_device()

    @classmethod
    def _optimize_for_low_device(cls):
        import builtins
        builtins.print = cls._light_print
        os.environ["DEARNING_OPTIMIZED"] = "1"

    @staticmethod
    def _light_print(*args, **kwargs):
        msg = " ".join(str(a) for a in args)
        if "✅" in msg or "❌" in msg or "⚠️" in msg:
            import builtins
            builtins.__dict__["print"](msg, **kwargs)

# Alias
Dpu = DearningProcessingUnit