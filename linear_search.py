
def linear_search(arr, target):
    for id,i in  enumerate(arr):
        if i == target:
            return id
    return -1


if __name__ == "__main__":

    arr = list(map(int, input("Array:\t").split()))
    target = int(input("Target:\t"))
    print(linear_search(arr, target))
