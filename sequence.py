def fibonacci_sequence(n):
    if n <= 0:
        return []
    
    fib_seq = [0, 1]  

    while fib_seq[-1] + fib_seq[-2] <= n:
        next_number = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_number)
    
    return fib_seq


n = int(input("Enter a value for 'n': "))


fib_seq = fibonacci_sequence(n)
print("Fibonacci sequence up to", n, ":")
print(fib_seq)
