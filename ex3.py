import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    '''парсить данні з списку та створює словник з данними '''
    data = line.split()
    return {
        "date": data[0],
        'time': data[1],
        'level': data[2],
        'message': ' '.join(data[3:])
            }


def load_logs(file_path: str) -> list:
    '''Читає файл та повертає список з усіма даними
    
    Вхідні дані:
    file_path: str - шлях до файлу
    
    Вивід:
    list - список з усіма даними
    '''
    result = []
    # зчитуємо файл
    with open(file_path, 'r', encoding='utf-8') as file:
        # проходимось по файлу та використовуючи функцію parse_log_line додаємо дані до списку
        for line in file:
            result.append(parse_log_line(line.strip()))
        # перевіряємо чи є якісь дані в файлі якщо ні то повертаємо None
        if not result:
            print(f"File {file_path} is empty")
            return None
    return result


def filter_logs_by_level(logs: list, level: str) -> list:
    '''Повертає дані для певного рівня
    
    Вхідні дані:
    logs: list - логи в вигляді списку
    level: str - рівень
    
    Повертає:
    list: - список логів

    '''
    # додає в список елементи для конкретного рівня
    result = [log for log in logs if log['level'].upper() == level.upper()]
    
    return result
    
    


def count_logs_by_level(logs: list) -> dict:
    '''підраховує кількість логів для кожного рівня
    
    Вхідні дані:
    logs: list - логи в вигляді списку

    Повертає:
    dict - словник який приймаж рівень та кількість логів цього рівня


    '''

    count = defaultdict(int)
    # Перебираємо логи та додаємо в словник 1 якщо цей рівень зустрічається в словнику
    for log in logs:
        level = log['level']  
        count[level] += 1


    return count

def display_log_counts(count: dict):
    """Виводить дані в зрозумілому форматі
    
    вхідні дані:
    count: dict - словник з кількістю логів для кожного рівня
    """

    # виводимо дані в зрозумілому форматі
    print(f"|{'Рівень логування':<18}|{'Кількість':^15}|")
    print(f"|{'-'*18}|{'-'*15}|")
    for level, i in count.items():
        print(f"|{level:<18}|{i:^15}|")
    print(f"|{'-'*18}-{'-'*15}|")

    


        

def main():
    '''головна функція для запуску програми'''
    args = sys.argv
    file_path = args[1]
    try:
        
        logs = load_logs(file_path)
        if logs is None:
            return
        
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено")
        return 

    count = count_logs_by_level(logs)
    display_log_counts(count)

    if len(args) > 2:
        level = args[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()