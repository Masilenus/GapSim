import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def space_linear(data):
	timeline = data[0]
	n_cars = data[1]

	x1 = range(len(timeline))

	y1 = timeline
	y2 = n_cars

	fig = plt.figure(1, figsize=(4, 5))
	ax1 = plt.subplot(211)
	ax1.plot(x1, y1)
	ax1.set_title("Occupied space")


	#plt.ylabel("Occupied space")

	ax2 = plt.subplot(212)
	ax2.plot(x1, y2, 'r')
	plt.xlabel("Iteration")
	ax2.set_title("Cars in street")


	#plt.subplots_adjust(hspace=0.5)
	#plt.gcf().subplots_adjust(bottom=0.15, top=0.85)

	plt.tight_layout()

	plt.show()