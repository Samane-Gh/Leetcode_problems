def fun(prices, n):
    buy = prices[0]
    profit = 0
    for i in range(1,n):
        if(buy > prices[i]):
            buy = prices[i]
        elif(prices[i] - buy > profit ):
            profit = prices[i] - buy
    return profit

print("Please enter number of prices")
num_prices = int(input())
print("Please enter items of price")
prices = [int(input()) for i in range(num_prices)]
print(fun(prices, num_prices))