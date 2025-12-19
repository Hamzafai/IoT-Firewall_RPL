# detector/integration.py

import json
import sys
import os

from detector import RPLDetector
from extractor import extract_features
import warnings

# Ignore all warnings (including sklearn version and feature warnings)
warnings.filterwarnings("ignore")

# Resolve model path safely
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join("decision_tree_model.pkl")

detector = RPLDetector(MODEL_PATH)

def firewall_decision(packet):
    features = extract_features(packet)
    prediction = detector.predict(features)

    if prediction == 1:
        return "🚨 BLOCK – RPL ATTACK DETECTED"
    else:
        return "✅ ALLOW – NORMAL TRAFFIC"


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python detector/integration.py <packet.json>")
        sys.exit(1)

    json_path = sys.argv[1]

    try:
        with open(json_path, "r") as f:
            packet = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        sys.exit(1)

    decision = firewall_decision(packet)
    print(decision)

#  python integration.py safe.json  #  python integration.py attack.json