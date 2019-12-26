
def main():
	colors = [3, 1, 4, 3 ,2, 2, 5, 1 ,3]	# Array of colors
	k = 4									# Number of colors
	SortColors(colors, len(colors), k)
	
def CheckColor(colors, k):	# Checking if a valid color
	# Iterating through all elements of `colors`
	for i in range(len(colors)):
		
		# Delete element if color is not within the `k` different colors
		if (colors[i] > k or colors[i] < 1):
			del colors[i]
			continue;
		
def SortColors(colors, n, k):
	# Iterating through all elements of `colors`
	for i in range(n):
		
		# Iterating through remaining elements to check
		for j in range(i+1, n):
			
			# If one element is greater than the next, swap the two elements
			if colors[i] > colors[j]:
				colors[i], colors[j] = colors[j], colors[i]
	
	CheckColor(colors, k)
	
	# Printing the sorted list
	print colors

main()
