import json
import re
#strings
i = 1
def escape_json(unescaped_json: str) -> str:
    return (
        re.sub(r'(?<!:)(?<!,)(?<!{)(?<!\[)"(?!:)(?!,)(?!})(?!\])' ," кавычка ",unescaped_json).replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )

raw_json = input("Введите значение JSON: ")
tasks = json.loads(escape_json(raw_json))
for task in tasks:
    print('')
    answer_type = task["answer"]["type"]
    if answer_type == "answer/single":
        right_answer = (task["answer"]["options"][0]["text"])
        print('Задание№', str(i) + ')', right_answer)
        i += 1


    elif answer_type == "answer/multiple":
        print('!!!Сколько написано правильных в задании столько нужно и выбирать начиная с первого!!!\n Обычно 3 правильных ответа\n Относиться только к заданию --->', i)
        for b in range(len((task["answer"]["options"]))): # находит длинну
            right_answer = (task["answer"]["options"][b]["text"]) # проходит с 0 до конца и выводит ответы
            print('Задание№', str(i) + ')', right_answer)
        i += 1


    elif answer_type in ["answer/match", "answer/match/timeline"]:
        for b in range(len((task["answer"]["options"]))):  # находит длинну
            right_answer = (task["answer"]["options"][b]["text"])  # проходит с 0 до конца и выводит ответы
            print('Задание№', str(i) + ')', right_answer)
        i += 1


    elif answer_type in ["answer/number", "answer/string"]:
        print('Мы знаем что номер', i ,'не работает и делаем фикс всем городом')
        i += 1

    elif answer_type == "answer/groups":
        for b in range(len((task["answer"]["options"]))):  # находит длинну
            right_answer = (task["answer"]["options"][b]["text"])  # проходит с 0 до конца и выводит ответы
            print('Задание№', str(i) + ')', right_answer)
        i += 1


    elif answer_type == "answer/table":
        print('Мы знаем что номер', i ,'не работает и делаем фикс всем городом')
        i += 1

    elif answer_type == "answer/order":
        for b in range(len((task["answer"]["options"]))):  # находит длинну
            right_answer = (task["answer"]["options"][b]["text"])  # проходит с 0 до конца и выводит ответы
            print('Задание№', str(i) + ')', right_answer)
        i += 1


    elif answer_type == "answer/inline/choice/single":
        print('Мы знаем что номер', i ,'не работает и делаем фикс всем городом')
        i += 1

    elif answer_type == "answer/gap/match/text":
        print('Мы знаем что номер', i ,'не работает и делаем фикс всем городом')
        i += 1
    else:
        print('Ebat sho za huitu ti vstavil')
        print('Отпраь модеру свой тест:', 'https://vk.com/sklenov97')
