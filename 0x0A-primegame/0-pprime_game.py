#!/usr/bin/python3
"""
Python script to solve prime game algorithm question
"""
def isWinner(x, nums):
    """   
    Define the play_game function, which takes an integer n and simulates the game described 
    """
     def sieve(n):
        primes = [True] * (n+1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
               for j in range(i*i, n+1,i):
                   prime[j] = False

        return primes

    def play_game(n):
        primes = sieve(n)
        player = 1
        while True:
           valid_moves = [i for i in range(2, n+1) if primes[i]]
           if not valid_moves:
              break

           move = max(valid_moves)
           for i in range(move, n+1, move):
               primes[i] = False
           player = 3 - player

        return player
