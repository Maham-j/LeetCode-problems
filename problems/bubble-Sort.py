if __name__ == '__main__':
    # Read the total number of elements in the array
    n = int(input().strip())
    
    # Read the array elements and store them in a list 'a'
    a = list(map(int, input().rstrip().split()))
    
    # Initialize a counter to keep track of the number of swaps
    swap = 0

    # Iterate through each element to perform bubble sort
    for i in range(n):
        # Iterate through the array from the first element to the second-to-last element
        for j in range(n - 1):
            # Check if the current element is greater than the next element
            if a[j] > a[j+1]:
                # Swap the elements using tuple unpacking
                a[j], a[j+1] = a[j+1], a[j]
                # Increment the swap counter
                swap += 1

    # Print the result after sorting
    print(f"Array is sorted in {swap} swaps.")
  
    # Print the first element
    print("First Element:", a[0])  

    # Print the last element
    print("Last Element:", a[n - 1])  
