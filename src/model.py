import torch
from torch import nn


class GlassBoxMLP(nn.Module):
    """İlk hafta Glass Box deneyleri için küçük ve kontrollü MLP."""

    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10),
        )

    def forward(self, x):
        return self.net(x)


def build_model(seed: int = 42):
    torch.manual_seed(seed)
    return GlassBoxMLP()
