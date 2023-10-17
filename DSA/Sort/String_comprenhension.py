# String Compression
# def compress(chars):
#     lis = []
#     for i in chars:
        
    
    
# chars = ["a","a","b","b","c","c","c"]
# compress(chars)

def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
        
    return max_profit
prices = [7,1,5,3,6,4]
print(maxProfit(prices))


# def maxProfit(prices):
# 	if not prices:
# 		return 0

# 	maxProfit = 0
# 	minPurchase = prices[0]
# 	for i in range(1, len(prices)):		
# 		maxProfit = max(maxProfit, prices[i] - minPurchase)
# 		minPurchase = min(minPurchase, prices[i])
# 	return maxProfit
    