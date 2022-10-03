from cgitb import reset


def search(arr, N, x):
    
    for i in range(N):
        if arr[i] == x:
            return i
    return -1 

if __name__ == '__main__':
    arr = [1,2,3,4,5]   
    N = len(arr)
    x = int(input('search number: '))

    result = search(arr,N,x)
    if result == -1:
        print("Element is not present in array")
    else:
        print('Element is present at index',result)

