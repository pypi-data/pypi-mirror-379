import torch

from iclearn.model.machine_learning_model import Optimizer


def load_optimizer(params, opt: Optimizer):

    if opt.name == "torch.AdamW":
        return torch.optim.AdamW(params=params, lr=opt.learning_rate)
    elif opt.name == "torch.Adam":
        return torch.optim.Adam(params=params, lr=opt.learning_rate)
    elif opt.name == "torch.SGD":
        momentum = opt.extra.get("momentum", 0)
        return torch.optim.SGD(params=params, lr=opt.learning_rate, momentum=momentum)

    return None
