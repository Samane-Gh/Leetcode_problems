num1 =[1]
num2 =[]
m=1
n=0
i=0
j=0
def mergeSort(num1,num2,m,n):
    if m==0:
            num1 = num2
    elif n==0:
        return(num1)
    else:
        while i<n or j<m:
            if num1[i] < num2[j] and num1[i] !=0:
                i+=1
                
            elif num1[i] == num2[j]:
                num1[i+2] = num1[i+1]
                num1[i+1] = num2[j]
                i+=1
                j+=1
            elif num1[i] == 0:
                num1[i] =num2[j]
                i+=1
                j+=1
    return(num1)

print(mergeSort(num1,num2,m,n))