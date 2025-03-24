import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1,1,1000)

a = 0.085 # [m]
z = 0.289
w_m = 17.32 # [rad/s]
w_d = 16.58 # [rad/s]
phi = 76.53 # [degrees]
big_x = 0.295 # [m]
w = 6*np.pi # [rad/s]
theta = 73.65 # [degrees]

x = a*np.exp(-z*w_m*t)*np.sin(w_d*t + phi) + big_x*np.cos(w*t-theta)

plt.figure(figsize=(10,5))
plt.plot(t,x, label='x(t)')
plt.xlabel('Time (t)')
plt.ylabel('x(t)')
plt.title(f"Plot of x(t) = {a} exp(-{z}*{w_m}*t) sin({w_d}*t+{phi}) + {big_x} cos({w:.2f}*t-{theta})")
plt.legend()
plt.grid(True)
plt.show()