#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache={1: 1}):

    if n < 0:
        return 0
    if n <= 1:
        return 1
    if n not in cache:
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')


def eating_cookies2(amount, denominations=[1, 2, 3]):
    if amount < 0:
        return 0
    if amount <= 1:
        return 1
    value = 0
    for denom in denominations:
        value += eating_cookies2(amount - denom)
    return value


for i in range(11):
    print(i, eating_cookies2(i))
