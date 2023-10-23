print("please enter the  Target number :")
target = int(input())
print("Please enter the range of  array :")
n = int(input())
nums =[]
def get_array(sizeOfArray):
    for i in range(0,sizeOfArray):
        temp = int(input())
        nums.append(temp)
get_array(n)     
visited_numbers = dict()  
 
for index, num in enumerate(nums):  
               
    number_to_be_search = target - num  
               
    if number_to_be_search in visited_numbers:  
        print ([index, visited_numbers[number_to_be_search]] )   
    else:  
        visited_numbers[num] = index  
    

     
        

        
    