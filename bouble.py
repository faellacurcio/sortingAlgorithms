import matplotlib.pyplot as plt
import logging
import numpy as np


logging.basicConfig(level=logging.WARNING)


class sorter():
	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)

	def bouble(self, array, order = 1, plot = False):
		logging.info("given array:")
		logging.info(array)
		logging.info("generated array:")
		logging.info([i for i in range(1, len(array) + 1)])

		width = 1 / 1.5

		if(plot):
			self.ax.bar([i for i in range(1, len(array) + 1)], array, width)
			plt.pause(0.5)

		for loop in range(1, len(array)):
			for iterator in range(0, len(array) - loop):
				if(array[iterator] < array[iterator + 1]):
					aux = array[iterator]
					array[iterator] = array[iterator + 1]
					array[iterator + 1] = aux
					if(plot):
						self.ax.clear()
						self.ax.bar([i for i in range(1, len(array) + 1)], array, width)
						plt.pause(0.001 / len(array))
			if(plot):
				plt.pause(1)

		return array


sort = sorter()
randomArray = list(np.random.randint(100, size= 10))
# print(sort.bouble(randomArray, plot = True))
print(sort.bouble(randomArray, plot = True))
