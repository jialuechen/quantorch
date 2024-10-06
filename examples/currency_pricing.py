import torch
from torchquantlib.core.asset_pricing.money.currency_pricer import currency_pricer

domestic_rate = torch.tensor(0.05)
foreign_rate = torch.tensor(0.03)
spot = torch.tensor(1.0)
expiry = torch.tensor(1.0)

price = currency_pricer(domestic_rate, foreign_rate, spot, expiry)
print(f'Currency Price: {price.item()}')