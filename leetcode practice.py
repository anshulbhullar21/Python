#TWO SUM:
# nums=[2,7,11,15]
# target=9

# i=0

# while i<len(nums):
#     j=i+1

#     while j<len(nums):
#         if nums[i] + nums[j] == target:
#             print(i,j)

#         j=j+1

#     i=i+1   

#CONTAINS DUPLICATE
# nums=[1,2,3,1]

# i=0
# found=False

# while i<len(nums):
#     j=i+1

#     while j<len(nums):
#         if nums[i]==nums[j]:
#             found=True

#         j=j+1

#     i=i+1        

# print(found)

#Best Time to Buy and Sell Stock
prices=[7,4,2,8]

max_profit=0
i=0

while i<len(prices):
    j=i+1

    while j<len(prices):
        profit=prices[j]-prices[i]

        if profit>max_profit:
            max_profit=profit

        j=j+1

    i=i+1

print(max_profit)        
