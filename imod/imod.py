import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)



m = 2
c = 1
y_linear = m * x + c


y_sine = np.sin(x)
y_cosine = np.cos(x)
y_tan = np.tan(x)
noise = np.random.normal(0, 0.5, size=len(x))
y_noisy = 2 * x + 1 + noise


plt.figure(figsize=(10, 6))
plt.plot(x, y_linear, label = "Linear: y = mx + c", linewidth=2)
plt.plot(x, y_sine, label="Sine wave: sin(x)", linewidth = 2.0)

plt.scatter(x, y_noisy, label= "Noisy data(stats)", alpha = 0.5, s = 20)

plt.legend()
plt.title("Linear vs Sine vs Statistical data")
plt.grid(True)

plt.show()
