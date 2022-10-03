def binary_search(arr,low, high, tofind):
    if high >= low:
        mid = int(low + (high - low) // 2)

        if arr[mid] < tofind:
            return binary_search(arr,mid + 1,high,tofind)
        elif arr[mid] > tofind:
            return binary_search(arr,low, mid - 1,tofind)
        else:
            return mid
    else:
        return -1

def exponential_search(arr, tofind):
    n = len(arr)

    if arr[0] == tofind:
        return 0

    i = 1
    while i < n and arr[i] <= tofind:
        i = i * 2
    return binary_search(arr,i/2,min(i,n),tofind)
    
arr = [1,3,5,6,7,8,9,10,34,56]
tofind = 10

result = exponential_search(arr, tofind)

print("index:",result)
