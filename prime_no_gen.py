import time

primes = [2]
N = int(input('Please enter the integer upto which you require primes: '))
is_prime = False
start_time = time.time()

for number in range(3,N+1):
    for prime in primes:
        if number % prime == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        primes.append(number)

end_time = time.time()
length = len(primes)
print(f'The primes are {primes}')
print(f'Number of primes: {length}')
print(f'Approximate time of execution: {end_time - start_time}')