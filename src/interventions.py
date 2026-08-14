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


def make_ablation_hook(indices):
    """Create a forward hook that zeros selected activation dimensions."""
    def hook(module, inputs, output):
        return ablate_neurons(output, indices)
    return hook


def make_scale_hook(indices, factor):
    """Create a forward hook that scales selected activation dimensions."""
    def hook(module, inputs, output):
        return scale_neurons(output, indices, factor)
    return hook
