def recursive_binerySearch(list, target):
    if len(list) == 0:
        return False
    else: 
        middle = len(list) //2
        if list[middle] == target:
            return True
        else: 
            if list[middle] < target:
                return recursive_binerySearch(list[middle+1:], target)
            else: 
                return recursive_binerySearch(list[:middle],target) 

numbers = [1,2,3,4,5,6,7,8,9,10]
print(recursive_binerySearch(numbers, 8))
