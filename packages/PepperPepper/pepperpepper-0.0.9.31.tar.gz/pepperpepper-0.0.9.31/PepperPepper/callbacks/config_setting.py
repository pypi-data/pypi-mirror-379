from PepperPepper.environment import  ml_collections, torch, math, os, np, random, cudnn


def get_opt_config(opt = 'AdamW'):
    config = ml_collections.ConfigDict()
    assert opt in ['Adadelta', 'Adagrad', 'Adam', 'AdamW', 'Adamax', 'ASGD', 'RMSprop', 'Rprop','SGD'], 'Unsupported optimizer!'

    if opt == 'Adadelta':
        config.lr = 0.01  # default: 1.0 – coefficient that scale delta before it is applied to the parameters
        config.rho = 0.9  # default: 0.9 – coefficient used for computing a running average of squared gradients
        config.eps = 1e-6  # default: 1e-6 – term added to the denominator to improve numerical stability
        config.weight_decay = 0.05  # default: 0 – weight decay (L2 penalty)
    elif opt == 'Adagrad':
        config.lr = 0.01  # default: 0.01 – learning rate
        config.lr_decay = 0  # default: 0 – learning rate decay
        config.eps = 1e-10  # default: 1e-10 – term added to the denominator to improve numerical stability
        config.weight_decay = 0.05  # default: 0 – weight decay (L2 penalty)
    elif opt == 'Adam':
        config.lr = 0.001  # default: 1e-3 – learning rate
        config.betas = (
        0.9, 0.999)  # default: (0.9, 0.999) – coefficients used for computing running averages of gradient and its square
        config.eps = 1e-8  # default: 1e-8 – term added to the denominator to improve numerical stability
        config.weight_decay = 0.0001  # default: 0 – weight decay (L2 penalty)
        config.amsgrad = False  # default: False – whether to use the AMSGrad variant of this algorithm from the paper On the Convergence of Adam and Beyond
    elif opt == 'AdamW':
        config.lr = 0.001  # default: 1e-3 – learning rate
        config.betas = (
        0.9, 0.999)  # default: (0.9, 0.999) – coefficients used for computing running averages of gradient and its square
        config.eps = 1e-8  # default: 1e-8 – term added to the denominator to improve numerical stability
        config.weight_decay = 1e-2  # default: 1e-2 – weight decay coefficient
        config.amsgrad = False  # default: False – whether to use the AMSGrad variant of this algorithm from the paper On the Convergence of Adam and Beyond
    elif opt == 'Adamax':
        config.lr = 2e-3  # default: 2e-3 – learning rate
        config.betas = (
        0.9, 0.999)  # default: (0.9, 0.999) – coefficients used for computing running averages of gradient and its square
        config.eps = 1e-8  # default: 1e-8 – term added to the denominator to improve numerical stability
        config.weight_decay = 0  # default: 0 – weight decay (L2 penalty)
    elif opt == 'ASGD':
        config.lr = 0.01  # default: 1e-2 – learning rate
        config.lambd = 1e-4  # default: 1e-4 – decay term
        config.alpha = 0.75  # default: 0.75 – power for eta update
        config.t0 = 1e6  # default: 1e6 – point at which to start averaging
        config.weight_decay = 0  # default: 0 – weight decay
    elif opt == 'RMSprop':
        config.lr = 1e-2  # default: 1e-2 – learning rate
        config.momentum = 0  # default: 0 – momentum factor
        config.alpha = 0.99  # default: 0.99 – smoothing constant
        config.eps = 1e-8  # default: 1e-8 – term added to the denominator to improve numerical stability
        config.centered = False  # default: False – if True, compute the centered RMSProp, the gradient is normalized by an estimation of its variance
        config.weight_decay = 0  # default: 0 – weight decay (L2 penalty)
    elif opt == 'Rprop':
        config.lr = 1e-2  # default: 1e-2 – learning rate
        config.etas = (0.5,
                1.2)  # default: (0.5, 1.2) – pair of (etaminus, etaplis), that are multiplicative increase and decrease factors
        config.step_sizes = (1e-6, 50)  # default: (1e-6, 50) – a pair of minimal and maximal allowed step sizes
    elif opt == 'SGD':
        config.lr = 0.01  # – learning rate
        config.momentum = 0.9  # default: 0 – momentum factor
        config.weight_decay = 0.05  # default: 0 – weight decay (L2 penalty)
        config.dampening = 0  # default: 0 – dampening for momentum
        config.nesterov = False  # default: False – enables Nesterov momentum
    return config





def get_sch_config(sch = 'CosineAnnealingLR', epochs=600):
    config = ml_collections.ConfigDict()

    assert sch in ['StepLR', 'MultiStepLR', 'ExponentialLR', 'CosineAnnealingLR', 'ReduceLROnPlateau', 'CosineAnnealingWarmRestarts', 'WP_MultiStepLR', 'WP_CosineLR'], 'Unsupported schedule !'

    if sch == 'StepLR':
        config.step_size = epochs // 5  # – Period of learning rate decay.
        config.gamma = 0.5  # – Multiplicative factor of learning rate decay. Default: 0.1
        config.last_epoch = -1  # – The index of last epoch. Default: -1.
    elif sch == 'MultiStepLR':
        config.milestones = [60, 120, 150]  # – List of epoch indices. Must be increasing.
        config.gamma = 0.1  # – Multiplicative factor of learning rate decay. Default: 0.1.
        config.last_epoch = -1  # – The index of last epoch. Default: -1.
    elif sch == 'ExponentialLR':
        config.gamma = 0.99  # – Multiplicative factor of learning rate decay.
        config.last_epoch = -1  # – The index of last epoch. Default: -1.
    elif sch == 'CosineAnnealingLR':
        config.T_max = 50  # – Maximum number of iterations. Cosine function period.
        config.eta_min = 0.00001  # – Minimum learning rate. Default: 0.
        config.last_epoch = -1  # – The index of last epoch. Default: -1.
    elif sch == 'ReduceLROnPlateau':
        config.mode = 'min'  # – One of min, max. In min mode, lr will be reduced when the quantity monitored has stopped decreasing; in max mode it will be reduced when the quantity monitored has stopped increasing. Default: ‘min’.
        config.factor = 0.1  # – Factor by which the learning rate will be reduced. new_lr = lr * factor. Default: 0.1.
        config.patience = 10  # – Number of epochs with no improvement after which learning rate will be reduced. For example, if patience = 2, then we will ignore the first 2 epochs with no improvement, and will only decrease the LR after the 3rd epoch if the loss still hasn’t improved then. Default: 10.
        config.threshold = 0.0001  # – Threshold for measuring the new optimum, to only focus on significant changes. Default: 1e-4.
        config.threshold_mode = 'rel'  # – One of rel, abs. In rel mode, dynamic_threshold = best * ( 1 + threshold ) in ‘max’ mode or best * ( 1 - threshold ) in min mode. In abs mode, dynamic_threshold = best + threshold in max mode or best - threshold in min mode. Default: ‘rel’.
        config.cooldown = 0  # – Number of epochs to wait before resuming normal operation after lr has been reduced. Default: 0.
        config.min_lr = 0  # – A scalar or a list of scalars. A lower bound on the learning rate of all param groups or each group respectively. Default: 0.
        config.eps = 1e-08  # – Minimal decay applied to lr. If the difference between new and old lr is smaller than eps, the update is ignored. Default: 1e-8.
    elif sch == 'CosineAnnealingWarmRestarts':
        config.T_0 = 50  # – Number of iterations for the first restart.
        config.T_mult = 2  # – A factor increases T_{i} after a restart. Default: 1.
        config.eta_min = 1e-6  # – Minimum learning rate. Default: 0.
        config.last_epoch = -1  # – The index of last epoch. Default: -1.
    elif sch == 'WP_MultiStepLR':
        config.warm_up_epochs = 10
        config.gamma = 0.1
        config.milestones = [125, 225]
    elif sch == 'WP_CosineLR':
        config.warm_up_epochs = 20

    return config





def get_optimizer(config, model):
    assert config.opt in ['Adadelta', 'Adagrad', 'Adam', 'AdamW', 'Adamax', 'ASGD', 'RMSprop', 'Rprop', 'SGD'], 'Unsupported optimizer!'

    if config.opt == 'Adadelta':
        return torch.optim.Adadelta(
            model.parameters(),
            lr = config.lr,
            rho = config.rho,
            eps = config.eps,
            weight_decay = config.weight_decay
        )
    elif config.opt == 'Adagrad':
        return torch.optim.Adagrad(
            model.parameters(),
            lr = config.lr,
            lr_decay = config.lr_decay,
            eps = config.eps,
            weight_decay = config.weight_decay
        )
    elif config.opt == 'Adam':
        return torch.optim.Adam(
            model.parameters(),
            lr = config.lr,
            betas = config.betas,
            eps = config.eps,
            weight_decay = config.weight_decay,
            amsgrad = config.amsgrad
        )
    elif config.opt == 'AdamW':
        return torch.optim.AdamW(
            model.parameters(),
            lr = config.lr,
            betas = config.betas,
            eps = config.eps,
            weight_decay = config.weight_decay,
            amsgrad = config.amsgrad
        )
    elif config.opt == 'Adamax':
        return torch.optim.Adamax(
            model.parameters(),
            lr = config.lr,
            betas = config.betas,
            eps = config.eps,
            weight_decay = config.weight_decay
        )
    elif config.opt == 'ASGD':
        return torch.optim.ASGD(
            model.parameters(),
            lr = config.lr,
            lambd = config.lambd,
            alpha  = config.alpha,
            t0 = config.t0,
            weight_decay = config.weight_decay
        )
    elif config.opt == 'RMSprop':
        return torch.optim.RMSprop(
            model.parameters(),
            lr = config.lr,
            momentum = config.momentum,
            alpha = config.alpha,
            eps = config.eps,
            centered = config.centered,
            weight_decay = config.weight_decay
        )
    elif config.opt == 'Rprop':
        return torch.optim.Rprop(
            model.parameters(),
            lr = config.lr,
            etas = config.etas,
            step_sizes = config.step_sizes,
        )
    elif config.opt == 'SGD':
        return torch.optim.SGD(
            model.parameters(),
            lr = config.lr,
            momentum = config.momentum,
            weight_decay = config.weight_decay,
            dampening = config.dampening,
            nesterov = config.nesterov
        )
    else: # default opt is SGD
        return torch.optim.SGD(
            model.parameters(),
            lr = 0.01,
            momentum = 0.9,
            weight_decay = 0.05,
        )







def get_scheduler(config, optimizer):
    assert config.sch in ['StepLR', 'MultiStepLR', 'ExponentialLR', 'CosineAnnealingLR', 'ReduceLROnPlateau',
                        'CosineAnnealingWarmRestarts', 'WP_MultiStepLR', 'WP_CosineLR'], 'Unsupported scheduler!'
    if config.sch == 'StepLR':
        scheduler = torch.optim.lr_scheduler.StepLR(
            optimizer,
            step_size = config.step_size,
            gamma = config.gamma,
            last_epoch = config.last_epoch
        )
    elif config.sch == 'MultiStepLR':
        scheduler = torch.optim.lr_scheduler.MultiStepLR(
            optimizer,
            milestones = config.milestones,
            gamma = config.gamma,
            last_epoch = config.last_epoch
        )
    elif config.sch == 'ExponentialLR':
        scheduler = torch.optim.lr_scheduler.ExponentialLR(
            optimizer,
            gamma = config.gamma,
            last_epoch = config.last_epoch
        )
    elif config.sch == 'CosineAnnealingLR':
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer,
            T_max = config.T_max,
            eta_min = config.eta_min,
            last_epoch = config.last_epoch
        )
    elif config.sch == 'ReduceLROnPlateau':
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer,
            mode = config.mode,
            factor = config.factor,
            patience = config.patience,
            threshold = config.threshold,
            threshold_mode = config.threshold_mode,
            cooldown = config.cooldown,
            min_lr = config.min_lr,
            eps = config.eps
        )
    elif config.sch == 'CosineAnnealingWarmRestarts':
        scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(
            optimizer,
            T_0 = config.T_0,
            T_mult = config.T_mult,
            eta_min = config.eta_min,
            last_epoch = config.last_epoch
        )
    elif config.sch == 'WP_MultiStepLR':
        lr_func = lambda epoch: epoch / config.warm_up_epochs if epoch <= config.warm_up_epochs else config.gamma**len(
                [m for m in config.milestones if m <= epoch])
        scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lr_func)
    elif config.sch == 'WP_CosineLR':
        lr_func = lambda epoch: epoch / config.warm_up_epochs if epoch <= config.warm_up_epochs else 0.5 * (
                math.cos((epoch - config.warm_up_epochs) / (config.epochs - config.warm_up_epochs) * math.pi) + 1)
        scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lr_func)

    return scheduler



def set_seed(seed):
    # for hash
    os.environ['PYTHONHASHSEED'] = str(seed)
    # for python and numpy
    random.seed(seed)
    np.random.seed(seed)
    # for cpu gpu
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    # for cudnn
    cudnn.benchmark = False
    cudnn.deterministic = True



# def seed_everything(seed=46):
#     random.seed(seed)
#     np.random.seed(seed)
#     torch.manual_seed(seed)
#     torch.cuda.manual_seed(seed)
#     torch.cuda.manual_seed_all(seed)
#     torch.backends.cudnn.deterministic = True
#     torch.backends.cudnn.benchmark = False




if __name__ == '__main__':
    # config = get_opt_config()
    config = get_sch_config()
    print(config)
