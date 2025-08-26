from typing import Generator, Callable
import re

def generator_numbers(text: str) -> Generator[float, None, None]:
    """Генератор чисел з тексту"""
    # використовуємо регулярні вирази для знаходження всіх чисел з плаваючою точкою та без
    digits = re.findall(r"\s(\d+\.\d+)\s", text)
    # генеруємо числа
    for num in digits:
        yield float(num)
    
def sum_profit(text: str, func: Callable) -> float:
    """Сумуєм числа із тексту"""
    # Виводимо загальний дохід використовуючи функцію sum
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

func = generator_numbers
print(sum_profit(text, func))
