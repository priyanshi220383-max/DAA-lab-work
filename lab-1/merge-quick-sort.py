def compare_merge_quick_tasks(tasks):
    def comes_before(task1, task2):
        if task1[1] != task2[1]:
            return task1[1] > task2[1]
        return task1[0] < task2[0]

    merge_comparisons = 0
    
    def merge_sort(arr):
        nonlocal merge_comparisons
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        sorted_arr = []
        i = j = 0
        while i < len(left) and j < len(right):
            merge_comparisons += 1
            if comes_before(left[i], right[j]):
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
                
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        return sorted_arr

    quick_comparisons = 0
    
    def quick_sort(arr, low, high):
        if low < high:
            p_idx = partition(arr, low, high)
            quick_sort(arr, low, p_idx - 1)
            quick_sort(arr, p_idx + 1, high)

    def partition(arr, low, high):
        nonlocal quick_comparisons
        pivot = arr[high]  # Use the last element as pivot
        i = low - 1
        for j in range(low, high):
            quick_comparisons += 1
            if comes_before(arr[j], pivot):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    merge_sorted = merge_sort(tasks.copy())
    
    quick_sorted = tasks.copy()
    quick_sort(quick_sorted, 0, len(quick_sorted) - 1)

    if merge_comparisons < quick_comparisons:
        better_algo = "Merge Sort"
    elif quick_comparisons < merge_comparisons:
        better_algo = "Quick Sort"
    else:
        better_algo = "Both Equal"

    report = []
    report.append("Task Prioritization Report")
    
    report.append("Merge Sort Result")
    for task in merge_sorted:
        report.append(f"{task[0]} {task[1]}")
    report.append(f"Merge Comparisons: {merge_comparisons}")
    
    report.append("Quick Sort Result")
    for task in quick_sorted:
        report.append(f"{task[0]} {task[1]}")
    report.append(f"Quick Comparisons: {quick_comparisons}")
    
    report.append(f"Better Algorithm: {better_algo}")
    
    return report