import sys
import json
import jsonschema
def error1():
    """"
    функция для неопознанных команд
    """
    print(f"Неизвестная команда")

def help1():
    """"
    Функция для вывода списка команд
    """
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список тудентов имеющих 2ки, иначе вывести информацию, что таких студентоыв нет;")
    print("save (file_name) - сохранить информацию в файл с именем file_name;")
    print("load (file_name) - загрузить информацию из файла с именем file_name;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

def add1():
    """"
        Функция для добавления информации о новых студентах
    """
    #вводим имя т номре группы
    fullname=input('введите фамилию , имя и отчества студента: ')
    group=int(input('введите номер группы '))

    #создать список оценок и список предметов, а также словарь пустой
    marks=[]
    lessons=['математика', 'информатика','экономика','программирование','философия']
    res={}
    #кладем введеные значения в слоыарь
    res['fullname']=fullname
    res['group']=group

    #создать пустой словарь
    d={}

    #кладем в список в оценок в словарь
    for i in range(0,5):
        d[lessons[i]]=int(input(f'оценка по {lessons[i]}: '))
    marks.append(d)
    res['marks']=marks
    return res

def list1(students):
    """"
    Функция для вывода списка добавленных рейсов
    """
    res=[]
    # Вывести данные о всех студентах.
    for idx, i in enumerate(students, 1):
        #проитерировать список с оценками
        for j in i['marks'][0]:
            if i['marks'][0][j]==2:
                s=f"имя: {i['fullname']}    ||||группа: {i['group']}   ||||оценки: {i['marks']}"
                #положить информацию о студенте в список
                res.append(s)
                break
    if len(res)==0:
        print('двоечников нет')
    else:
        for k in res:
            print(k,'\n')

def save_students(file_name, students):
    """
    Сохранить всех работников в файл JSON.
    """
    # Открыть файл с заданным именем для записи.
    with open(file_name, "w", encoding="utf-8") as f:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кирилицы установим ensure_ascii=False
        json.dump(students, f, ensure_ascii=False, indent=4)
def load_students(file_name):
    """
    Загрузить всех работников из файла JSON.
    """
    # Открыть файл с заданным именем для чтения.
    with open(file_name, "r", encoding="utf-8") as fin:
        n = json.load(fin)
        if validate_json_data(n):
            return n
        else:
            return False

def validate_json_data(data):
    """
    Проверка вводимых данных
    """
    schema = {
    "title": "students",
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "fullname": {"type": "string"},
            "group": {"type": "integer"},
            "marks": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                    "математика": {"type":"integer"},
                    "информатика": {"type":"integer"},
                    "экономика": {"type":"integer"},
                    "программирование": {"type":"integer"},
                    "философия": {"type": "integer"}
                    }
                }
            }
        },
        "additionalProperties": False,
        "required": ["fullname", "group", "marks"]
    }
}

    try:
        jsonschema.validate(data, schema)
        print("Данные прошли валидацию.")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print("Ошибка валидации данных:", e)
        return False
def main():
    """"
    Главная функция программы.
    """
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список тудентов имеющих 2ки, иначе вывести информацию, что таких студентоыв нет;")
    print("save (file_name) - сохранить информацию в файл с именем file_name;")
    print("load (file_name) - загрузить информацию из файла с именем file_name;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    # Список работников.
    students = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        if command=='exit':
            break

        elif command == 'add':
            # Добавить словарь в список.
            i = add1()
            students.append(i)
            # Отсортировать список в случае необходимости.
            if len(students) > 1:
                students.sort(key=lambda item: item.get('fullname', ''))

        elif command == 'list':
            list1(students)

        elif command == 'help':
            help1()

        elif command.startswith("save "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            save_students(file_name, students)
        elif command.startswith("load "):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Получить имя файла.
            file_name = parts[1]
            # Сохранить данные в файл с заданным именем.
            students = load_students(file_name)
        elif command=='exit':
            exit(1)
        else:
            error1()



if __name__ == '__main__':
    main()

