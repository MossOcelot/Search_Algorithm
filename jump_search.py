import math

def jump_search(arr, val):
    jump = int(math.sqrt(len(arr)))

    left,right = 0,0

    while left <= len(arr) and arr[left] <= val:
        right = min(len(arr) - 1,left + jump)
        if arr[left] <= val and arr[right] >= val: # val ต้องอยู่ระหว่าง left right
            break
        left += jump

        if left >= len(arr):
            return -1
    
    for i in range(left,right + 1):
        if arr[i] == val:
            return i
    return -1

        


arr = [0,1,1,2,3,5,8,13,21,34,55,77,89,91,95,110]

for i in range(17):
    val = int(input())

    result = jump_search(arr, val)

    print('index:',result)


    