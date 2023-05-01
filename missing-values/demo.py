import numpy as np
from random import randint
import seaborn as sns
import matplotlib.pyplot as plt

import task01, task02, task03

sns.set()
mu, sigma = 173, 10

heights = np.random.default_rng().normal(mu, sigma, 100)
heights = [ round(x) for x in heights ]

weights = [ x - randint(x//2 + 10, 110) for x in heights ]
weights = [ x if randint(1, 10) > 2 else np.NaN for x in weights ]

w_h = list(zip(heights, weights))

def add_k_layer(data, k, color):
    fixed = task03.impute_missing_values(data, k)
    heights = [ tuple[0] for tuple in fixed ]
    weights = [ tuple[1] for tuple in fixed ]
    sns.scatterplot(x=heights, y=weights, color=color, label=f"knn k={k}", alpha=0.5)
    plt.legend()

add_k_layer(w_h, 5, "green")

fixed = task01.impute_missing_values(weights)
sns.scatterplot(x=heights, y=fixed, color="orange", label=f"mean", alpha=0.5)
plt.legend()

fixed = task02.impute_missing_values(weights)
sns.scatterplot(x=heights, y=fixed, color="red", label=f"mode", alpha=0.5)
plt.legend()

sns.scatterplot(x=heights, y=weights)
plt.show()

