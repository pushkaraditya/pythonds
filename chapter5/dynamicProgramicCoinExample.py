def getMin(coins, min, lastCoinUsed, val):
    for testVal in range(1, val + 1):
        # print('checking for', testVal)
        for d in [j for j in coins if j <= testVal]:
            # print('testing denomination', d)
            remaining = testVal - d
            numCoins = 1 if remaining == 0 else min[remaining] + 1
            if min[testVal] == 0 or numCoins < min[testVal]:
                min[testVal] = numCoins
                lastCoinUsed[testVal] = d
        # print(min)
            


def main():
    coins = [1, 5, 10, 21, 25]
    n = 63
    min = [0] * (n + 1)
    lastCoinUsed = [0] * (n + 1)
    min[0] = 0
    getMin(coins, min, lastCoinUsed, n)
    print(['{} ({}) => {}'.format(i, lastCoinUsed[i], min[i]) for i in range(1, n + 1)])

main()