def quartiles(arr): #Avoid using recursive function to save memory
    length = len(arr)
    arr=sorted(arr)
    Q1=length//4
    Q2=length//2
    Q3=int(length*0.75)
    
    # in case the Length is Odd number
    if length%2!=0:
        print((arr[Q1]+arr[(Q1)-1])//2)    #Q1                
        print(arr[Q2])                     #Q2        
        print((arr[Q3]+arr[Q3+1])//2)      #Q3 
    
    # in case the length is even number 
    # let's check if the length would be even in the three parts or not 
    
    else:
        if (length % 4 == 0 ):
            print((arr[Q1]+arr[Q1-1])//2)  #Q1
            print((arr[Q2]+arr[Q2-1])//2)  #Q2
            print((arr[Q3]+arr[Q3-1])//2)  #Q3
        else:
            print(arr[Q1])                 #Q1
            print((arr[Q2]+arr[Q2-1])//2)  #Q2
            print(arr[Q3])  
            
n = int(input().strip())

data = list(map(int, input().rstrip().split()))

quartiles(data)
        