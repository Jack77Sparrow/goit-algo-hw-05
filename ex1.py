def caching_fibonacci():
    # Створюємо словник для кешу, де ключ = n, значення = число Фібоначчі
    cache = {}

    def fibonacci(n):
        # Перевірка, що n — ціле число
        if not isinstance(n, int):
            raise TypeError("n має бути цілим числом")
        
        # Перевірка, що n — невід'ємне число
        if n < 0:
            raise ValueError("n має бути невід'ємним числом")

        # Якщо значення вже є в кеші — повертаємо його
        if n in cache:
            return cache[n]

        # Базові випадки Фібоначчі
        if n == 0:
            cache[0] = 0
            return 0
        elif n == 1:
            cache[1] = 1
            return 1

        # Рекурсивно рахуємо і зберігаємо в кеш
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    # Повертаємо функцію fibonacci, яка "пам’ятає" про cache
    return fibonacci


# Використання:
fib = caching_fibonacci()

print(fib(10))   # -> 55
print(fib(15))   # -> 610
print(fib(13))   # -> 233