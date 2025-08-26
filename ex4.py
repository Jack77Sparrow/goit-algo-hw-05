from colorama import Fore


def input_error(func):
    def inner(*args, **kwargs):
        try:

            return func(*args, **kwargs)
        
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return f"{Fore.YELLOW}Contact not found{Fore.RESET}"
        except IndexError:
            return f"{Fore.RED}Usage: phone <name>{Fore.RESET}"
        

    return inner





def parse_input(user_input):
    """
    Parse user input into command and arguments.

    Args:
        user_input (str): рядок, введений користувачем.

    Returns:
        tuple: (command, args), де command (str) — команда, 
            args (list[str]) — список аргументів.
    """
    # Розбиваємо введений рядок на частини
    command, *args = user_input.split()
    # Видаляємо зайві пробіли і приводимо команду до нижнього регістру
    command = command.strip().lower()
    return command, args

@input_error
def add_contact(person, user_info):
    """
    Add a new contact to the phone book.

    Args:
        person (list): [ім'я, телефон].
        user_info (dict): словник з контактами.

    Returns:
        None
    """
    
    # Розпаковуємо ім'я і номер
    name, phone = person
    # Додаємо у словник
    user_info[name] = phone
    return f'{Fore.GREEN}Contact added{Fore.RESET}'

    
    
    
        
@input_error
def show_phone(contact, user_info):
    """
    Show phone number by contact name.

    Args:
        contact (list): [ім'я].
        user_info (dict): словник з контактами.

    Returns:
        str | None: номер телефону або None.
    """
    # Якщо не передали аргумент (ім’я)
    
    name = contact[0]
    
    return user_info[name]
    

    
@input_error
def change_contact(contact, user_info):
    """
    Change existing contact’s phone number.

    Args:
        contact (list): [ім'я, новий телефон].
        user_info (dict): словник з контактами.

    Returns:
        None
    """
    
    # Розпаковуємо ім’я і новий телефон
    name, phone = contact
    if name in user_info:
        user_info[name] = phone
        return 'Contact updated'
    else:
        return f"{Fore.RED}Name is not found{Fore.RESET}"



@input_error
def show_all(user_info):
    """
    Show all contacts in the phone book.

    Args:
        user_info (dict): словник з контактами.

    Returns:
        None
    """
    # Якщо контактів ще немає
    if not user_info:
        return f"{Fore.YELLOW}No contacts yet{Fore.RESET}"
        
    result = ''
    # Виводимо всі контакти
    for name, phone in user_info.items():
        result += f"{Fore.BLUE}Name: {Fore.RESET}{name}\n{Fore.BLUE}Phone: {Fore.RESET}{phone}\n"
    return result


def main():
    """
    Main function that runs the assistant bot.
    """
    # Створюємо словник для контактів
    contacts = {}
    
    print(f"{Fore.RED}Welcome to the assistant bot{Fore.RESET}")
    while True:
        # Отримуємо команду від користувача
        user_input = input("Enter a command: ").strip().lower()
        command, data = parse_input(user_input)

        # Виконуємо дію в залежності від команди
        if command in ['exit', 'close']:
            print("Good bye!")
            break
        elif command in ['hello', 'hi']:
            print('How can I help you')
        elif command == 'add':
            print(add_contact(data, contacts))
        elif command == 'phone':
            print(show_phone(data, contacts))
        elif command == 'change':
            print(change_contact(data, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('invalid command')


if __name__ == '__main__':
    main()
