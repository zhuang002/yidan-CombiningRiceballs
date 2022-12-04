cache = {}


def tryCombine(seq:list[int], start:int, end:int) -> tuple[bool, int]:
    # exit point
    if start == end:
        return True, seq[start]
    key = (start, end)
    if key in cache:
        return cache[key]

    maxBall = 0
    # try combine 2
    for i in range(start, end, 1):
        canCombine1, maxCombined1 = tryCombine(seq, start, i)
        if maxBall < maxCombined1:
            maxBall = maxCombined1
        canCombine2, maxCombined2 = tryCombine(seq, i+1, end)
        if maxBall < maxCombined2:
            maxBall = maxCombined2
        if canCombine1 and canCombine2 and maxCombined1 == maxCombined2:
            result = (True, maxCombined1+maxCombined2)
            cache[key] = result
            return result

    if start == end-1:
        result = (False, maxBall)
        cache[key] = result
        return result

    # try combine 3

    for i in range(start, end-1, 1):
        for j in range(i+1, end, 1):
            canCombine1, maxCombined1 = tryCombine(seq, start, i)
            if maxBall < maxCombined1:
                maxBall = maxCombined
            canCombine2, maxCombined2 = tryCombine(seq, i+1, j)
            if maxBall < maxCombined2:
                maxBall = maxCombined
            canCombine3, maxCombined3 = tryCombine(seq, j+1, end)
            if maxBall < maxCombined3:
                maxBall = maxCombined
            if canCombine1 and canCombine2 and canCombine3 and maxCombined1 == maxCombined3:
                result = (True, maxCombined1 + maxCombined2 + maxCombined3)
                cache[key] = result
                return result
    result = (False, maxBall)
    cache[key] = result
    return result


input()
seq = list(map(int, input().split(' ')))
(canCombine, maxCombined) = tryCombine(seq, 0, len(seq)-1)
print(maxCombined)
