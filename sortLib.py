import matplotlib.pyplot as plt
import logging
import numpy as np
# import random
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

	def selectionCompare(x, y, order):
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
		if(order not in [1, -1]):
			logging.warning("Order value not valid (1, -1)")

		for loop in range(1, len(array)):
			for iterator in range(0, len(array) - loop):
				if(sorter.boubleCompare(array[iterator], array[iterator + 1], order)):
					sorter.swapElements(array, iterator, iterator + 1)
					if(plot):
						self.ax.clear()
						self.ax.bar([i for i in range(1, len(array) + 1)], array, self.width)
						plt.pause(0.01 / len(array))

		logging.info("Sorted array:")
		logging.info(array)
		return array

	def insertion(self, array, order = 1, plot = False):
		logging.info("given array:")
		logging.info(array)
		if(order not in [1, -1]):
			logging.warning("Order value not valid (1, -1)")

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
		logging.info("Sorted array:")
		logging.info(array)
		return array

	def selection(self, array, order = 1, plot = False):
		# for i in range(len(array)):
		for j in range(len(array)):
			sorter.swapElements(
				array, 
				j, 
				array[j:].index(min(array[j:])) + j
			) 

			if(plot):
					self.ax.clear()
					self.ax.bar([i for i in range(1, len(array) + 1)], array, self.width)
					plt.pause(0.01 / len(array))

		return array

	def quickSort(self, array, order = 1, plot = False):
		result = []
		# print(array)
		if len(array) > 1:
			pivot = array.pop(len(array) - 1)
			print("pivot", pivot)
			partition = [[], []]
			for element in array:
				if(element < pivot):
					partition[0].append(element)
				else:
					partition[1].append(element)
			print("partition", partition)
			result = [sorter.quickSort(self, partition[0]) + result]
			result = result + sorter.quickSort(self, partition[1])
			print("result", result)
			return [pivot]
		else:
			return [array]

	def mergeSort(self, array, order = 1, plot = False):
		if (len(array) <= 1):
			return array

		left = []
		right = []

		for index, element in enumerate(array):
			if (index < (len(array) / 2)):
				left.append(element)
			else:
				right.append(element)

		left = sorter.mergeSort(self, left)
		right = sorter.mergeSort(self, right)

		return sorter.merge(left, right)

	def merge(left, right):
		result = []
		while(left and right):
			if (left[0] <= right[0]):
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		while(left):
			result.append(left.pop(0))
		while(right):
			result.append(right.pop(0))

		return result


sort = sorter()

randomArray = list(np.random.randint(100, size= 20))
print("Random array:")
print(randomArray)
print("----------------")

boubleArray = randomArray.copy()
insertionArray = randomArray.copy()
selectionArray = randomArray.copy()
MergeSortArray = randomArray.copy()

print("Bouble:")
print(sort.bouble(boubleArray, order = -1, plot = False))

print("Insertion:")
print(sort.insertion(randomArray, order = 1, plot = False))

print("Selection:")
print(sort.selection(selectionArray, order = 1, plot = False))

print("Merge:")
print(sort.mergeSort(MergeSortArray, order = 1, plot = False))


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
