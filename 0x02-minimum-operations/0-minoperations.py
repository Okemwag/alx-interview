#!/usr/bin/python3

def minOperations(n):
    if n <= 0:
        return 0

    result = 0
    i = 2
    while i * i <= n:
        while n % i == 0:
            result += i
            n /= i
        i += 1

    if n > 1:
        result += n

    return result

