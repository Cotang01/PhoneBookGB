import text_fields as txt


def main_menu() -> int:
    print('''Главное меню:\n
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n''')
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Введите число от 1 до 8')


def print_info(message: str):
    print('\n' + '-'*len(message))
    print(message)
    print('-' * len(message) + '\n')


def show_contacts(book: list[dict], message: str):
    if book:  # Пустой список = False, не пустой список = True
        print('\n' + '-' * 83)
        for num, user in enumerate(book, 1):  # Enumerate с 1
            print(f'{num:>3}. {user.get("name"):<30}'
                  f'{user.get("phone"):<25}'
                  f'{user.get("info"):<25}')
        print('-' * 83 + '\n')
    else:
        print(message)


def new_user() -> dict:
    new_name = input(txt.new_name)
    new_phone = input(txt.new_phone)
    new_info = input(txt.new_info)
    return {'name': new_name, 'phone': new_phone, 'info': new_info}


def find_contact() -> str:
    cont_search = input(txt.user_find)
    return cont_search


def found_contact(i: tuple):
    string1 = f'\nНомер данного пользователя: {i[0]}\n'
    string2 = f'Доп. инфо данного пользователя: {i[1]}\n'
    print("\n"f'{"-" * len(string1)}'
          f'{string1}'
          f'{string2}'
          f'{"-" * len(string1)}')


def confirm(message: str) -> bool:
    answer = input(message + '(Да/Нет): ')
    if answer.lower() == 'да':
        return True
    if answer.lower() == 'нет':
        return False


def change_contact() -> str:
    change_user = input(txt.change_user)
    return change_user


def additional_change_info() -> tuple:
    changeable_data = input('\n' + txt.info_to_change)
    if changeable_data.upper() == 'ФИО':
        change_fio = input('\n' + txt.change_name)
        changeable_data = (change_fio, 'fio')
        return changeable_data
    if changeable_data.upper() == 'НОМЕР':
        change_phone = input('\n' + txt.change_phone)
        changeable_data = (change_phone, 'phone')
        return changeable_data
    if changeable_data.upper() == 'ИНФО':
        change_info = input('\n' + txt.change_info)
        changeable_data = (change_info, 'info')
        return changeable_data


def user_to_delete() -> str:
    del_user = input('\n' + txt.delete_user)
    return del_user
