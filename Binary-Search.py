# Uses python3
code sorted list first, breaks the list in half to search for item

import sys


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0] #number of items in array
    m = data[n + 1]
    unsorted_list = data[1 : n + 1]
    low=0
    high=n-1
    
    sorted_list = sorted(unsorted_list)
    
    
    
    for item in data[n + 2:]: # list contains items to be searched for in sorted_list
       

        def BinarySearch(sorted_list,low,high,item):
            
            while low <= high:
            
            
                mid=(low + ((high-low)//2))
                
                if item ==sorted_list[mid]:
                    return mid + 1  # returns position of the item in the list like in normal counting, ie starts counting positions from 1
                
                elif item < sorted_list[mid]:
                    high=mid-1
                
                    
                
                else:
                    low= mid + 1
            
            #returns -1 if item not array
            return -1
         
        
        print (BinarySearch(sorted_list,low,high,item), end=" ")
