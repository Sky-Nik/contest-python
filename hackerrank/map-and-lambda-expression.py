# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
import typing as tp
cube = lambda x: x ** 3  # complete the lambda function 

def fibonacci(n: int) -> tp.List[int]:
    # returns a list of fibonacci numbers
    dp = [0, 1]
    for _ in range(n):
        dp.append(dp[-1] + dp[-2])
    return dp[:-2]

if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
