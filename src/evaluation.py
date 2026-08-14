import torch


def accuracy(model, loader, device="cpu"):
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            pred = model(x).argmax(dim=1)
            correct += (pred == y).sum().item()
            total += y.numel()
    return correct / total if total else 0.0


def probability_change(before_logits, after_logits):
    before = torch.softmax(before_logits, dim=-1)
    after = torch.softmax(after_logits, dim=-1)
    return (after - before).abs().mean().item()
