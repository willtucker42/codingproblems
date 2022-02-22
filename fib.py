# return the nth number in the fibonacci sequence
def fib(n):
    memo = {}
    return fibHelper(n, memo)


def fibHelper(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibHelper(n - 1, memo) + fibHelper(n - 2, memo)
    # print(memo[n])
    return memo[n]

