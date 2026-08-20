import torch


def ablate_neurons(activation, indices):
    """Seçilen nöron boyutlarını sıfırlanmış olarak döndürür."""
    out = activation.clone()
    out[..., indices] = 0.0
    return out


def scale_neurons(activation, indices, factor):
    """Çarpımsal ölçekleme ile kontrollü aktivasyon müdahalesi uygular."""
    out = activation.clone()
    out[..., indices] *= factor
    return out


def make_ablation_hook(indices):
    """Seçilen aktivasyon boyutlarını sıfırlayan bir ileri geçiş kancası (forward hook) oluşturur."""
    def hook(module, inputs, output):
        return ablate_neurons(output, indices)
    return hook


def make_scale_hook(indices, factor):
    """Seçilen aktivasyon boyutlarını ölçekleyen bir ileri geçiş kancası (forward hook) oluşturur."""
    def hook(module, inputs, output):
        return scale_neurons(output, indices, factor)
    return hook
