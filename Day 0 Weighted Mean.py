def weightedMean(X, W):
    # Write your code here
    numerator = sum([X[i]*W[i] for i in range(len(X))])
    denominator = sum(W)
    
    print(round(numerator/denominator,1))