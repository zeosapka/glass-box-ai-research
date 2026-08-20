from collections import OrderedDict


def register_activation_hooks(model, layer_names):
    """Adı verilen modüllerin ileri geçiş aktivasyonlarını (forward activations) kaydeder."""
    activations = OrderedDict()
    handles = []
    modules = dict(model.named_modules())

    for name in layer_names:
        if name not in modules:
            raise ValueError(f"Unknown module: {name}")

        def hook(module, inputs, output, name=name):
            activations[name] = output.detach().cpu()

        handles.append(modules[name].register_forward_hook(hook))

    return activations, handles


def remove_hooks(handles):
    for handle in handles:
        handle.remove()
