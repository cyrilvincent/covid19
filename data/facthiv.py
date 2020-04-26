import functools
import numpy as np
#n! / k!(n-k)! = 30000! / 30!(29930)! = produit(29931..30000)
a = functools.reduce(lambda acc,cur: acc*cur, np.arange(29973,30000))
b = functools.reduce(lambda acc,cur: acc*cur, np.arange(1,30))
print(1/(a*b))
