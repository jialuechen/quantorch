import torch
from quantorch.models.stochastic_volatility.heston_model import HestonModel

def test_heston_model():
    spot = torch.tensor(100.0)
    strike = torch.tensor(105.0)
    expiry = torch.tensor(1.0)
    rate = torch.tensor(0.05)
    kappa = torch.tensor(2.0)
    theta = torch.tensor(0.04)
    sigma = torch.tensor(0.1)
    rho = torch.tensor(-0.7)
    v0 = torch.tensor(0.04)

    model = HestonModel(spot, strike, expiry, rate, kappa, theta, sigma, rho, v0)
    price = model.price_option('call')
    assert price > 0