#!/usr/bin/python3
''' Prime Game '''


def isWinner(x, nums):
    '''x is the number of rounds and nums is an array of n
        Returns: name of the player that won the most rounds
        If the winner cannot be determined, return None
        n and x will not be larger than 10000
        Example:
            x = 3, nums = [4, 5, 1]

            First round: 4
            Maria picks 2 and removes 2, 4, leaving 1, 3
            Ben picks 3 and removes 3, leaving 1
            Ben wins because there are no prime numbers left
            for Maria to choose

            Second round: 5
            Maria picks 2 and removes 2, 4, leaving 1, 3, 5
            Ben picks 3 and removes 3, leaving 1, 5
            Maria picks 5 and removes 5, leaving 1
            Maria wins because there are no prime numbers left
            for Ben to choose

            Third round: 1
            Ben wins because there are no prime numbers
            for Maria to choose

            Result: Ben has the most wins
    '''

    if not nums or x < 1 or x != len(nums) or len(nums) == 0:
        return None

    winners = {'Maria': 0, 'Ben': 0}
    maria_turn = True
    flag = False

    for i in nums:
        prime = [i for i in range(2, i+1)]
        p = 2
        if not flag:
            maria_turn = not maria_turn
            flag = True
        while p*p <= i:
            if prime[p] is True:
                for j in range(p*p, i+1, p):
                    prime[j] = False
            p += 1
            maria_turn = not maria_turn
            flag = True

        if maria_turn:
            winners['Maria'] += 1
        else:
            winners['Ben'] += 1

    if winners['Maria'] == winners['Ben']:
        return None
    return max(winners, key=winners.get)
