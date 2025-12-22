def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1 # Why minus 1? 0 index

    while low <= high:

        mid = int (low + (high - low) / 2)

        # check if x is present at mid
        if arr[mid] == x:
            return mid

        # if x is greater, ignore left side
        elif arr[mid] < x:
            low = mid + 1

        # if x is smaller, ignore right half
        else:
            high = mid - 1

    # if we reach here, then the element was not present
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 2 # key

    result = binarySearch(arr, x)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present")
