#import statements to use random number generator
import random
import time

import sys 
sys.setrecursionlimit(10**6) 
  
#max random number
MAX = 20000

#genenrate random list
def generateRandomList(listSize):
	return random.sample(range(MAX), listSize)

#genenrate sorted list
def generateSortedList(listSize):
	arr = []
	for i in range(listSize):
		arr.append(i+1)
	return arr
	
	
def insertionSort(unsortedList):
	for i in range(1, len(unsortedList)):
		key = unsortedList[i]
		j = i -1
		
		while j >= 0  and unsortedList[j] > key:
			unsortedList[j + 1] = unsortedList[j]
			j = j - 1
		
		unsortedList[j+1] = key
		
	return unsortedList
	
def quickSort(unsortedList,left = None,right = None):
	if left is None and right is None:
		return quickSort(unsortedList,0,len(unsortedList)-1)
		
		
	pivot = 0
	if (left < right):
		i = 0
	#splits the array in two  
		i = left - 1 

		j = left
		
		while j <= right- 1 :
			if unsortedList[j] <= unsortedList[right]:
				i = i + 1	
				unsortedList[i], unsortedList[j] = unsortedList[j], unsortedList[i]
			j = j +1
	#swap
		unsortedList[i + 1], unsortedList[right] = unsortedList[right], unsortedList[i + 1] 
		pivot = i+1;
		
	#sort left side
		quickSort(unsortedList, left, pivot - 1)
	#sort right side
		quickSort(unsortedList, pivot + 1, right)
		
	else:
		arr = unsortedList
		
	return unsortedList

def mergeSort(unsortedList): 
    if len(unsortedList) >1:
        mid = int(len(unsortedList)/2)
        left = unsortedList[:mid]
        right = unsortedList[mid:]
  
        mergeSort(left)
        mergeSort(right)
  
        i = j = k = 0
          
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                unsortedList[k] = left[i] 
                i+=1
            else: 
                unsortedList[k] = right[j] 
                j+=1
            k+=1
           
        while i < len(left): 
            unsortedList[k] = left[i] 
            i = i + 1
            k = k + 1
          
        while j < len(right): 
            unsortedList[k] = right[j] 
            j = j + 1
            k = k + 1
			
        return unsortedList

def heapify(unsortedList, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2 
  
    if l < n and unsortedList[i] < unsortedList[l]: 
        largest = l 
  
    if r < n and unsortedList[largest] < unsortedList[r]: 
        largest = r 
  
    if largest != i: 
        unsortedList[i],unsortedList[largest] = unsortedList[largest],unsortedList[i] #swap 
  
        heapify(unsortedList, n, largest) 
  
def heapSort(unsortedList):
	n = len(unsortedList)
   
	for i in range(n//2 - 1, -1, -1):
		heapify(unsortedList, n, i)
  
	for i in range(n-1, 0, -1):
		unsortedList[i], unsortedList[0] = unsortedList[0], unsortedList[i]
		heapify(unsortedList, i, 0)
		
	return unsortedList


#sorts a list
#param[1] sort alogrithm
#param[2] list to be sorted
#return soted Array
def sort(sortFucntion, unsortedList):
	sortedArray = sortFucntion(unsortedList)
	return sortedArray
	
#gets execution time for sorting algorithm
#param[1] list to be sorted
#param[2] sort alogrithm
#return execution time
def getExecutionTime(list,algorithm):
	startTime = time.time()
	sort(algorithm,list)
	endTime = time.time()
	
	elaspedTime = endTime - startTime;
	return elaspedTime
	
def main():
	n = [100,500,1000,2000,5000,8000,10000]
	algorithms = [insertionSort,heapSort,mergeSort,quickSort]
	algorithmStr = ['insertion','heapSort','mergeSort','quickSort']
	
	for i in range(len(algorithms)):
		for size in n:
			unsorted = generateRandomList(size)
			sorted = generateSortedList(size)
			
			print("algorithm:",algorithmStr[i],"\tsize: ",size,"\ttype: unsorted\texecutionTime:",getExecutionTime(unsorted,algorithms[i]))
			print("algorithm:",algorithmStr[i],"\tsize: ",size,"\ttype: sorted\texecutionTime:",getExecutionTime(sorted,algorithms[i]))
		print()

if __name__ == "__main__":
	main()
	
	
	
