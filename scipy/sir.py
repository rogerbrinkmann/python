import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


def sir(x, t, transm, recov):

    s, i, _ = x

    dsdt = -transm * s * i
    didt = transm * s * i - recov * i
    drdt = recov * i

    return [dsdt, didt, drdt]


transm = 2.4
recov = 1
x0 = [1, 0.01, 0]
t = np.linspace(0, 12, 1000)
x = odeint(sir, x0, t, args=(transm, recov))

s = x[:, 0]
i = x[:, 1]
r = x[:, 2]

plt.plot(t, s, "b", label="susceptible")
plt.plot(t, i, "r", label="infected")
plt.plot(t, r, "g", label="removed")
plt.legend(loc="best")
plt.title("S-I-R model")
plt.xlabel("t")
plt.show()
