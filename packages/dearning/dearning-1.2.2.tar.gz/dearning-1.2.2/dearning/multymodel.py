# dearning/multymodel.py
from .utils import preprocess_data   # pastikan versi pure python dipakai
from .AI_tools import DLP  # ganti dengan versi pure python DLP (tanpa TextBlob)

def lazy_import():
    from .model import CustomAIModel, Dense, Activation
    return CustomAIModel, Dense, Activation

class AImodel:
    def __init__(self):
        self.models = {}
        self.CustomAIModel, self.Dense, self.Activation = lazy_import()
        self.load_default_models()
        self.dlp = DLP()

    def load_default_models(self):
        self.models['simpleAI'] = self._build_simple_ai()

    def _build_simple_ai(self):
        model = self.CustomAIModel(loss="mse")
        model.add(self.Dense(10, 32))
        model.add(self.Activation("relu"))
        model.add(self.Dense(32, 16))
        model.add(self.Activation("tanh"))
        model.add(self.Dense(16, 6))  
        model.add(self.Activation("softmax"))
        model.memory = []
        return model

    def get_model(self, name):
        return self.models.get(name)

    def predict(self, model_name, data):
        model = self.get_model(model_name)
        if model:
            data = preprocess_data(data)  # harus sudah pure python
            return model.forward(data)
        return None

    def save_model(self, model_name, path):
        model = self.get_model(model_name)
        if model:
            model.save_model(path)

    def load_model(self, model_name, path):
        model = self.CustomAIModel.load_model(path)
        self.models[model_name] = model

    def available_models(self):
        return list(self.models.keys())

    def learn_from_mistake(self, model_name, state, wrong_output_idx):
        model = self.get_model(model_name)
        if model and hasattr(model, "memory"):
            label = [0.0]*6
            label[wrong_output_idx] = 0.1
            model.memory.append((state, label))

    def train_from_memory(self, model_name, correct_index):
        model = self.get_model(model_name)
        if model and hasattr(model, "memory") and model.memory:
            data = [m[0] for m in model.memory]
            labels = []
            for m in model.memory:
                lbl = m[1][:]
                lbl[correct_index] = 1.0
                labels.append(lbl)
            model.train(data, labels, epochs=1, learning_rate=0.01, batch_size=4, verbose=False)
            model.memory.clear()

    def analyze_text(self, text, use_dlp=True):
        features = [
            len(text),
            sum(c.isdigit() for c in text),
            sum(c.isupper() for c in text)
        ]
        while len(features) < 10:
            features.append(0)
        output = self.predict("simpleAI", [features])
        actions = ["respond", "classify_error", "fix_code", "calculate", "logic_check", "text_output"]
        if output is not None:
            top_idx, top_val = max(enumerate(output[0]), key=lambda x: x[1])
            return {"text": text, "output": actions[top_idx], "confidence": float(top_val)}
        if use_dlp:
            return self.dlp.process(text)  # versi pure python
        return {"text": text, "output": "unknown", "confidence": 0.0}