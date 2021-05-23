# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:16:32 2021

@author: thund
"""

import numpy as np
import matplotlib.pyplot as plt
mu = 0.004
sigma = 0.01v
start_price = 5
np.random.seed(0)
returns = np.random.normal(loc=mu, scale=sigma, size=100)
price = start_price*(1+returns).cumprod()
plt.plot(price)
