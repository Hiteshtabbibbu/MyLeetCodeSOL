'''
Given a coins of array we need to find minimum number of coins for a given target
Example 11 = 1 + 5 + 5
'''

cost = [1,2,5]
tar = 11
dp = [float('inf')]*(tar+1)
dp[0] = 0
for i in range(tar+1):
    for j in range(len(cost)):
        if cost[j] > i or dp[i-cost[j]]==float('inf'):
            continue
        else:
            dp[i] = min(dp[i],1+dp[i-cost[j]])
print(dp)
if dp[tar]!=float('inf'):
    print(dp[tar])
