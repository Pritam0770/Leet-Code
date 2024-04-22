from types import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1st approach
        # final_profit = 0
        # for index,i in enumerate(prices):
        #     max_after_dday =   max(prices[(index+1):]) if index+1 != len(prices) else -1
        #     profit = max_after_dday-i
        #     final_profit = profit if profit > final_profit else final_profit
        # return final_profit if final_profit > 0 else 0

# Here we have taken each element and then again taken the rest ahead list from the element and taken the max from the
# rest ahead list then substracted from that max to the current element and then if the substraction is greater then 0
# then we are updating the value of final_profit else we are keeping the value as it is.
# And at the end we will return the value of final_profit if the value of it is greater than 0 else we will return 0



        # 2nd approach
        max_profit = 0
        min_price = prices[0]

        for i in prices:
            if min_price > i:
                min_price = i
            elif i-min_price > max_profit:
                max_profit = i-min_price
        return max_profit