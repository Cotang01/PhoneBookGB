phone_book = []
start_phone_book = []
PATH = 'phones.txt'


def get_pb():
    global phone_book
    return phone_book


def load_file():
    global phone_book
    global start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data_phones = file.readlines()
    for user in data_phones:
        user = user.strip().split(';')
        phone_book.append({'name': user[0],
                           'phone': user[1],
                           'info': user[2]})
    start_phone_book = phone_book.copy()


def save_pb():
    global phone_book
    data_save = []
    for user in phone_book:
        data_save.append(';'.join([value for value in user.values()]))
        # ';'.join заменяет пробелы на ';' между элементами списка
        # Элементы списка - значения каждого словаря в phone_book
    data_save = '\n'.join(data_save)  # Переводим список в строку
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data_save)


def add_contact(user: dict):
    global phone_book
    phone_book.append(user)


def user_search(user: str) -> tuple:
    global phone_book
    for i in phone_book:
        if user.upper() in i.get('name').upper():
            found_phone = i.get('phone')
            found_info = i.get('info')
            return found_phone, found_info


def data_change(user_change: str, info_change: tuple[str, str]):
    global phone_book
    red_user = {}
    for i in phone_book:
        if user_change.upper() in i.get('name').upper():
            red_user['name'] = i.get('name')
            red_user['phone'] = i.get('phone')
            red_user['info'] = i.get('info')
            i['name'] = 'blank_name'
            i['phone'] = 'blank_phone'
            i['info'] = 'blank_info'
    if info_change[1] == 'fio':
        red_user['name'] = info_change[0]
    if info_change[1] == 'phone':
        red_user['phone'] = info_change[0]
    if info_change[1] == 'info':
        red_user['info'] = info_change[0]
    for i in phone_book:
        if 'blank' in i.get('name'):
            i['name'] = red_user.get('name')
            i['phone'] = red_user.get('phone')
            i['info'] = red_user.get('info')


def deleting_user(user_delete: str):
    global phone_book
    for i in phone_book:
        if user_delete.upper() in i.get('name').upper():
            phone_book.pop(phone_book.index(i))


def exit_pb() -> bool:
    global phone_book
    global start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True
