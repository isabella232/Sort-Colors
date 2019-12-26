
def main():
	colors = [2, 1, 0, 1, 2, 0, 2, 2, 1, 0, 2]	# Array of colors8
	SortColors(colors, len(colors))


def SortColors(colors, n):
	# Iterating through all elements of `colors`
	for i in range(n):
		
		# Iterating through remaining elements to check
		for j in range(i+1, n):
			
			# If one element is greater than the next, swap the two elements
			if colors[i] > colors[j]:
				colors[i], colors[j] = colors[j], colors[i]
	
	# Printing the sorted list
	print colors
		
main()
