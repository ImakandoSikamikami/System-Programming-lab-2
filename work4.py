import time

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Factorials of given numbers:\n")

start_time = time.time()

for n in numbers:
    print(f"{n}! = {factorial(n)}")

end_time = time.time()
duration = end_time - start_time

print(f"\n Time taken: {duration:.4f} seconds")