def binerySearch(list, target):
    first = 0
    last = len(list) -1 
    while first <= last:
        middle = first + last //2
        if list[middle] == target: 
            return middle
        elif list[middle] < target:
            first = middle + 1
        else:
            last = middle - 1

    return None

def verify(index):
    if index is not None:
        print ("Target found ar index: ", index)
    else:
        print ("Target not found ar index")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binerySearch(numbers, 12)
verify(result)

result = binerySearch(numbers, 10)
verify(result)
