def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/len(arr)
    var = sum(pow(i-mean,2) for i in arr) / len(arr)
    std = math.sqrt(var)
    print(round(std, 1))
       