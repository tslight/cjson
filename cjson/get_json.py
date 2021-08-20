import json
from pretty import ppdict

def get_json(path):
    with open(path) as f:
        return json.load(f)

