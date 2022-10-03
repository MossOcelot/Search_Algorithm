# เป็นการ search แบบคาดการณ์ว่าค่าที่ต้องการหานั้นอยู่ตรงไหน ของ arr แล้วค่อย scope ลง

def interpolation_search(arr,low,high,tofind):
    while arr[low] <= tofind and arr[high] >= tofind:
        mid = int(low + (((tofind - arr[low]) * (high - low))/ (arr[high] - arr[low])))

        if arr[mid] < tofind:
            low = mid + 1
        elif arr[mid] > tofind:
            high = mid - 1
        else:
            return mid
    
    if arr[low] == tofind:
        return low
    else:
        return -1

arr = [10,15,19,23,43,78]
tofind = 19

result = interpolation_search(arr,0,len(arr) -1,tofind)
print('Index: ',result)
