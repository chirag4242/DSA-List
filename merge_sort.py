def merge_sort(list):
    """
        sort list in ascending order
        returns new sorted list

        Divide: find the mid point in the list and divide into sublists 
        Conquer: Recursively sort the the sublists created in previous step 
        Combine: Merge the sorted sublists in created in the previous step 
    """
    if len(list) <= 1:
      return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

    
def split(list):
    """
        Divide the unsorted list at midpoint into sublists
        Return two sublists - left and right.
    """        
    mid = len(list) //2
    left=  list[:mid]; 
    right = list[mid:]; 
    return left, right
        

def merge(left,right):
    """
        Merges two lists (arrays), sorting them in the process 
       Returns new merge list  
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right [j]:
            l.append(left[i])
            i+=1
        else: 
            l.append(right[j])
            j+=1
    
    while i < len(left):    
        l.append(left[i])
        i+=1
              
    while j < len(right):
        l.append(right[j])
        j+=1
        
    return l

list = [54, 62, 93, 17, 77, 31, 44, 55, 20]
l = merge_sort(list)
print(l)