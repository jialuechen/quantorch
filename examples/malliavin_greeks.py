import torch
from torchquantlib.core.risk.greeks.greeks import MalliavinGreeks

option_price = torch.tensor(10.0)
underlying_price = torch.tensor(100.0)
volatility = torch.tensor(0.2)
expiry = torch.tensor(1.0)

greek = MalliavinGreeks(option_price, underlying_price, volatility, expiry)
print(f'Malliavin Greek: {greek.item()}')