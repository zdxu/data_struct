

def method(arr, element):
    length = len(arr)
    left = 0
    right = length-1
    if arr[left] > element < arr[right]:
        return -1
    if arr[left] == element:
        print 1
        return left
    if arr[right] == element:
        print 2
        return right
    count = 2
    while right - left > 1:
        count = count + 1
        mid = left + int(0.618 * (right - left))
        print mid
        if arr[mid] == element:
            print count
            return mid
        elif arr[mid] > element:
            right = mid
        else:
            left = mid
    print count
    return -1


if __name__ == '__main__':
    arr = []
    for i in range(100):
        arr.append(i)
    print(method(arr, 48.6))

# n * 0.618^? = 1  =>       git test     hhh  。。。。     (1/0.618)^? = n => log (1.618) (n)
