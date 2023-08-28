def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# 创建生成器
prime_generator = generate_primes()

# 无限生成素数
for _ in range(1000):  # 生成 10 个素数
    prime = next(prime_generator)
    print(prime)
