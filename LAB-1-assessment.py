def complete_algorithm_performance_assessment(n, arr, target):
  def factorial_rec(x):
    if x <= 1:
      return 1
    return x * factorial_rec(x - 1)

  def factorial_iter(x):
    res = 1
    for i in range(1, x + 1):
      res *= i
      return res

  def fibonacci_rec(x):
    if x <= 0:
      return 0
    if x == 1:
      return 1
    return fibonacci_rec(x - 1) + fibonacci_rec(x - 2)

  def fibonacci_iter(x):
    if x <= 0:
      return 0
    if x == 1:
      return 1
    a = 0
    b = 1
    for _ in range(2, x + 1):
      a, b = b, a + b
    return b

  linear_idx = -1
  linear_comps = 0
  for i in range(n):
    linear_comps += 1
    if arr[i] == target:
      linear_idx = i
      break

  sorted_arr = sorted(arr)
  binary_idx = -1
  binary_comps = 0
  low = 0
  high = n - 1

  while low <= high:
    binary_comps += 1
    mid = (low + high) // 2
    if sorted_arr[mid] == target:
      binary_idx = mid
      break
    elif sorted_arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  if linear_comps < binary_comps:
    search_best = "Linear Search"
  elif binary_comps < linear_comps:
    search_best = "Binary Search"
  else:
    search_best = "Both Equal"

  b_arr = arr.copy()
  bubble_comps = 0
  bubble_swaps = 0
  for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        bubble_comps += 1
        if b_arr[j] > b_arr[j + 1]:
          b_arr[j], b_arr[j + 1] = b_arr[j + 1], b_arr[j]
          bubble_swaps += 1
          swapped = True
    if not swapped:
        break

    i_arr = arr.copy()
    insertion_comps = 0
    insertion_shifts = 0 

    for i in range(1, n):
      key = i_arr[i]
      j = i - 1
      while j >= 0:
        insertion_comps += 1
        if i_arr[j] > key:
          i_arr[j + 1] = i_arr[j]
          insertion_shifts += 1
          j -= 1
        else:
          break

      i_arr[j + 1] = key

    if bubble_comps < insertion_comps:
      sorting_best = "Bubble Sort"
    elif insertion_comps < bubble_comps:
      sorting_best = "Insertion Sort"
    else:
      sorting_best = "Both Equal"

    output = []

    output.append("Algorithm Performace Assessment")
    output.append("Computation Results")
    output.append(f"Factorial Recursive:{factorial_rec(n)}")
    output.append(f"Factorial Iterative:{factorial_iter(n)}")
    output.append(f"Fibonacci Recursive:{fibonacci_rec(n)}")
    output.append(f"Fibonacci Recursive:{fibonacci_iter(n)}")
    output.append("Search Results")
    output.append(f"Linear Index:{linear_idx}")
    output.append(f"Linear Comparisons:{linear_comps}")
    output.append(f"Binary Index:{binary_idx}")
    output.append(f"Binary Comparisons:{binary_comps}")
    output.append(f"Search Best:{search_best}")
    output.append("sorting Results")
    output.append(f"Bubble Sorted:{' '.join(map(str, b_arr))}")
    output.append(f"Bubble Comparisons: {bubble_comps}")
    output.append(f"Bubble Swaps: {bubble_swaps}")
    output.append(f"Insertion Sorted:{' '.join(map(str, i_arr))}")
    output.append(f"Insertion Comparisons: {insertion_comps} ")
    output.append(f"Insertion Shifts: {insertion_shifts}")
    output.append(f"Sorting Best: {sorting_best}")
    output.append("Complexity Summary")
    output.append("Factorial : O(n)")
    output.append("Fibonacci Recursive: O(2^n)")
    output.append("Linear Search: Time O(n)")
    output.append("Binary Search:  O(log n)")
    output.append("Bubble Sort:  O(n^2)")
    output.append("Insertion Sort: Time O(n^2)")

    return output
        
        
            
        


    
      

    