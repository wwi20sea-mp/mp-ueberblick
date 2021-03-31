def fib(n):
  # fib (0) = 1
  # fib (1) = 1
  # fib (n) = fib(n-1) + fib(n-2)
  if n == 0 or n == 1:
    return 1
  return fib(n-1) + fib(n-2)



for n in range(10):
  print(fib(n))

fib = lambda n: 1 if n <= 1 else (fib(n-1) + fib(n-2))

for n in range(10):
  print(fib(n))
