import matplotlib.pyplot as plt
import logging
import numpy as np
# import timeit


logging.basicConfig(level=logging.WARNING)


class sorter():
	def __init__(self):
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)
		self.width = 1 / 1.5

	def boubleCompare(x, y, order):
		if(order == -1):
			return x > y
		else:
			return x < y

	def swapElements(array, index1, index2):
		aux = array[index1]
		array[index1] = array[index2]
		array[index2] = aux

	def bouble(self, array, order = 1, plot = False):
		logging.info("given array:")
		logging.info(array)
		logging.info("generated array:")
		logging.info([i for i in range(1, len(array) + 1)])

		for loop in range(1, len(array)):
			for iterator in range(0, len(array) - loop):
				if(sorter.boubleCompare(array[iterator], array[iterator + 1], order)):
					sorter.swapElements(array, iterator, iterator + 1)
					if(plot):
						self.ax.clear()
						self.ax.bar([i for i in range(1, len(array) + 1)], array, self.width)
						plt.pause(0.01 / len(array))

		return array

	def insertion(self, array, order = 1, plot = True):
		elementIndex = 1
		while(elementIndex < len(array)):
			insertedElemntIndex = elementIndex
			while(insertedElemntIndex > 0 and array[insertedElemntIndex - 1] > array[insertedElemntIndex]):
				sorter.swapElements(array, insertedElemntIndex, insertedElemntIndex - 1)
				insertedElemntIndex = insertedElemntIndex - 1
				if(plot):
					self.ax.clear()
					self.ax.bar([i for i in range(1, len(array) + 1)], array, self.width)
					plt.pause(0.01 / len(array))
			elementIndex = elementIndex + 1
		return array


sort = sorter()

randomArray = list(np.random.randint(100, size= 20))

boubleArray = randomArray.copy()
print("Bouble:")
print(sort.bouble(boubleArray, order = -1, plot = True))

insertionArray = randomArray.copy()

print("Insertion:")
print(sort.insertion(randomArray))

# -------------------
# timeit experiments:
# -------------------
s = '''
sort = sorter()

randomArray = list(np.random.randint(100, size= 10))

print("Bouble:")
sort.bouble(randomArray, order = -1, plot = False)
'''

# print(timeit.timeit(stmt=s, globals=globals(), number = 1))
