def merge_sort(my_list: list) -> list:
    '''Sorts a list using Merge Sort algorithm'''
    
    if  len(my_list) <= 1: return my_list # check base case where there are no more value in list then return the list
    left = merge_sort(my_list[:len(my_list) // 2]) #cut current list into a left half
    right = merge_sort(my_list[len(my_list) // 2:]) # slice current list into a right half
    return merge(listA=left, listB=right) #return value of merging sorted list

def merge(listA: list, listB: list)-> list:
    '''Merges both list, sorting them'''
    i, j = 0,0 #set values for i and j
    new_list = [] #new accumulator/ new list
    while i < len(listA) and j < len(listB): #loop until one of the variables has reached to the end of its list
        if listA[i] <= listB[j]: #if element at i is less than element at j then append value and increment i
            new_list.append(listA[i])
            i += 1
        elif listB[j] < listA[i]: #if element at j is less than element at i then append value and increment j
            new_list.append(listB[j])
            j += 1
        
        
    #if there are some left over values then add to the list 
    if i < len(listA): new_list.extend(listA[i:]) 
    elif j < len(listB): new_list.extend(listB[j:])
    return new_list #return new list


#testing merge_sort 
from random import randrange
array = [randrange(100) for i in range(45)]
print(merge_sort(array))
new_array = sorted(array)

assert merge_sort(array) == new_array