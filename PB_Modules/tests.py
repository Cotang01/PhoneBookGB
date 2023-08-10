import text_fields as txt

phone_book = [{'name': 'Тихонов Константин Павлович',
               'phone': '+7 (922) ''603-57-84',
               'info': 'Сосед'},
              {'name': 'Ткачёва Людмила Викторовна',
               'phone': '+7 (909) 811-62-72',
               'info': 'Учительница'},
              {'name': 'Ласман Афанасий Денисович',
               'phone': '+7 (978) 673-76-58',
               'info': 'Друг семьи'},
              {'name': 'Смагин Трофим Ефимович',
               'phone': '+7 (910) 353-78-55',
               'info': 'Плитка'},
              {'name': 'Мирзoяна Юлиана Ефремовна',
               'phone': '+7 (973) 127-85-87',
               'info': 'Мамина подруга'},
              {'name': 'Мирзоянов Даниил Романович',
               'phone': '+7 (973) 164-39-41',
               'info': 'Сын маминой подруги'}]
print(phone_book)

# Перевод списка с вложенными словарями в строку
# data = []
# for i in phone_book:
#     data.append(';'.join([v for v in i.values()]))
# data = '\n'.join(data)
# print(data)


# view
def user_to_delete() -> str:
    del_user = input('\n' + txt.delete_user)
    return del_user


# controller
user_delete = user_to_delete()


# model
def deleting_user(user_delete: str):
    global phone_book
    for i in phone_book:
        if user_delete.upper() in i.get('name').upper():
            phone_book.pop(phone_book.index(i))
