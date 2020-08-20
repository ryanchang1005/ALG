"""
找出購票方式最便宜的組合
days : 要去旅遊的日子 : [1, 4, 6, 7, 8, 20] : 第1, 4, 6, 7, 8, 20天要去旅遊
costs : [2, 7, 15] : 一日票$2, 七日票$7, 三十日票$15(固定三個元素)
return : 11
第1天買一日票$2 1
第4天買七日票$7 4~10 
第20天買一日票$2 20

思路
需用dp存第i天所需花費金額
如那天不用旅遊, 如[1,4,5,20]中, 2,3,6~19都不旅遊那麼這些天所需花費金額公式如下
dp[i] = dp[i - 1]
如果那天需要旅遊, 到那天總花費為 "昨天花費+買一日票花費", "七天前花費+買七日票花費", "三十天前花費+買三十日票花費", 當中取最小作為當天總累積花費
dp[i] = min(dp[i - 1] + cost[0], dp[i - 7] + cost[1], dp[i - 30] + cost[2])
"""


def solve(days, costs):
    # 第i天累積最小花費dp[i]
    dp = [-1 for i in range(366)]
    dp[0] = 0  # 第0天設0花費, 因day1需計算

    # 初始化
    # 值為-1=不旅遊的日子, 值為0=旅遊的日子
    for d in days:
        dp[d] = 0
    for i in range(1, 366):
        if dp[i] == -1:
            # 不旅遊
            dp[i] = dp[i-1]
        else:
            # 旅遊
            # 將三種方案算出, 並找出最小值
            d1 = dp[i-1] + costs[0]
            d7 = dp[i-7] + costs[1]
            d30 = dp[i-30] + costs[2]
            dp[i] = min(d1, d7, d30)
    return dp[days[len(days)-1]]


if __name__ == "__main__":
    costs = [2, 7, 15]
    print(solve([1, 4, 6, 7, 8, 20], costs))  # 11
    print(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs))  # 17