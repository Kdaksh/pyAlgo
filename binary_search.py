
def binary_search(arr, target):
    lower_bound = 0
    upper_bound = len(arr) - 1
    while lower_bound <= upper_bound:

        mid = (lower_bound+upper_bound)//2
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                lower_bound = mid+1

            else:
                upper_bound = mid-1

    return -1


if __name__ == "__main__":

    arr = list(map(int, input("Array:\t").split()))
    target = int(input("Target:\t"))
    print(binary_search(arr, target))
