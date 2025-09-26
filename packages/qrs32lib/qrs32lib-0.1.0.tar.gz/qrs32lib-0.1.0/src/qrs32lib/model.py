# model.py
import torch

class QRSModel:
    def __init__(self):
        pass

    def predict(self, t):
        # Dummy example
        return torch.sin(torch.tensor(t))**2

def predict(t):
    model = QRSModel()
    return model.predict(t)
