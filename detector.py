# detector/detector.py

import joblib
import numpy as np

class RPLDetector:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, features):
        features = np.array(features).reshape(1, -1)
        return int(self.model.predict(features)[0])
