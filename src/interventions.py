import torch


def ablate_neurons(activation, indices):
    """Return a copy with selected neuron dimensions set to zero."""
    out = activation.clone()
    out[..., indices] = 0.0
    return out


def scale_neurons(activation, indices, factor):
    """Controlled activation intervention by multiplicative scaling."""
    out = activation.clone()
    out[..., indices] *= factor
    return out
