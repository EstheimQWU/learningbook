def recursion(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursion(arr[1:])

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]  # 基准值
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    print(recursion([3, 4, 5, 6, 7]))
    print(quicksort([10, 2, 5, 16, 33, 12, 1, 21]))