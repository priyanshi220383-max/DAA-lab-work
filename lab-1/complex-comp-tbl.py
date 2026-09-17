import math

def generate_runtime_complexity_table(n):

    linear_search = n
    binary_search = math.floor(math.log2(n)) + 1
    bubble_sort = n * (n - 1) // 2
    insertion_sort = n * (n - 1) // 2

    result = []

    result.append("Runtime Complexity Comparison")
    result.append("Method ObservedCount ExpectedComplexity Observation")

    result.append(
        f"Linear Search {linear_search} O(n) "
        f"Grows linearly"
    )

    result.append(
        f"Binary Search {binary_search} O(log n) "
        f"Grows logarithmically"
    )

    result.append(
        f"Bubble Sort {bubble_sort} O(n^2) "
        f"Grows quadratically"
    )

    result.append(
        f"Insertion Sort {insertion_sort} O(n^2) "
        f"Grows quadratically"
    )

    return "\n".join(result)