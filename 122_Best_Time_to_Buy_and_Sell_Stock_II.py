from types import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) == 1:
        #     return 0

        # max_profit = 0
        # min_price = prices[0]
        # for i in prices:
        #     if i < min_price:
        #         min_price = i
        #     elif i - min_price > max_profit:
        #         max_profit =  i - min_price
        # print(max_profit)
        
        # temp_profit = 0
        # index = 0
        # while index < len(prices):
        #     if index + 1 < len(prices) and prices[index] < prices[index + 1] :
        #         temp_profit += prices[index + 1] - prices[index]
        #         index += 2
        #     else:
        #         index += 1
        # print(temp_profit)
        # return max_profit if max_profit > temp_profit else temp_profit

        # 1st I will iterate through the list and will take the min element and max element wich can produce the profit
        # not the min max randomly rather they should produce the max profit as like previous method
        # replace that with max_profit then from the element of which the next elemnt is a bigger element than the
        # current element substract that current element from the next element then store that profit in a different
        # variable and do that sequentially till you get to a situation where may be the current element is the last
        # element and now compare both the 1st max_profit with current sum profit the one that is bigger return that

        [6,1,3,2,4,7]
        if len(prices) == 1:
            return 0

        max_profit = 0
        curr = prices[0]

        for i in range(len(prices)):
            if prices[i] > curr:
                max_profit += prices[i] - curr
            curr = prices[i]
        
        return max_profit
        # The main part that is missing in the 1st approach for which the 1st approch is wrong is we can buy the stock and sell it on the same day which means it is also possible that we sell
        # it the same day and then buy it. For example we have bought it yesterday and today we will sell it and then we
        # will again but that today and sell it tomorrow if tomorrow is greater than today and so does today is greater
        # than yesterday.
