import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def space_linear(timeline):
	x = range(len(timeline))
	y = timeline

	plt.xlabel("Iteration")
	plt.ylabel("Occupied space")


	plt.plot(x, y)
	plt.show()