def binary_search(arr, left, right, key):
    if right >= left:
        mid = int(left + (right - left) // 2)

        if arr[mid] < key:
            return binary_search(arr, mid + 1,right,key)

        elif arr[mid] > key:
            return binary_search(arr, left, mid - 1, key)
        else:
            return mid
    
    else:
        return -1


arr = [2,3,7,9,11]

key = 2

result = binary_search(arr,0,len(arr) - 1,key)

print(result)
