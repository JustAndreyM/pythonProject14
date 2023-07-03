import random
print("Добро пожаловать в игру ´Угадайка´")
print ("Выбери режим в котором ты хочешь играть")
print ("Практика: Угадать число от 1 до 3. Попытки:3 (Без возможности проигрыша). Нажать на '0'")
print("Лекго: Угадать число от 1 до 10. Попытки: 3. Нажать на '1'")
print("Нормально: Угадать яисло от 1 до 100. Попытки: 8. Нажать на '2'")
print("Сложно: Угадать число от 1 до 500. Попытки: 10. Нажать на '3'")
print("Экстрим: Угадать число от 1 до 1000. Попытки: 16. Нажать на '4'")
print("САМЫЙ ЭКСТРИМАЛЬНЫЙ ЭКСТРИМ!!! : Угадать число от 1 до 2500. Попытки:20. Нажать на '5'")
print("ЕЩЕ БОЛЕЕ ЭКСТРИМАЛЬНЫЙ ЭКСТРИМ!!! СЛАБОНЕРВНЫМ НЕ ЧИТАТЬ! : Угадать число от 1 до 5000. Попытки: 10. Нажать на '9'")
a = int(input("Введите уровень сложности:"))
if a == 1:
    print("Вы выбрали уровень сложности: Легко")
    SecretNumber = random.randint(0,10)
    print("Я загадал случайное число от 1 до 10.")
    print("Твоя задачь отгадать его.")
    Answer = int(input("Загаданное число это ..."))
    check = 3
    count = 1
    while Answer != SecretNumber and check>0:
        if Answer > SecretNumber:
            check = check - 1
            count = count+1
            print("Загаданное число меньше числа которое ты ввел. Осталось попыток", check)
        elif Answer < SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число больше числа которое ты ввел. осталось попыток", check)
        Answer = int(input("Введите вашь новый выбор"))
    if check == 0:
        print("Ты проиграл. Попробуй еще раз")
        print("Вот число которое ты не смог угадать:", SecretNumber)
    else:
        print("Ура ты угадал! Поздравляю!")
        print("Ты управился за попыток:", count)
elif a == 2:
    print("Вы выбрали уровень сложности: нормально")
    SecretNumber = random.randint(0, 100)
    print("Я загадал случайное число от 1 до 100.")
    print("Твоя задачь отгадать его.")
    Answer = int(input("Загаданное число это ..."))
    check = 8
    count = 1
    while Answer != SecretNumber and check > 0:
        if Answer > SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число меньше числа которое ты ввел. Осталось попыток", check)
        elif Answer < SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число больше числа которое ты ввел. осталось попыток", check)
        Answer = int(input("Введите вашь новый выбор"))
    if check == 0:
        print("Ты проиграл. Попробуй еще раз")
        print("Вот число которое ты не смог угадать:", SecretNumber)
    else:
        print("Ура ты угадал! Поздравляю!")
        print("Ты управился за попыток:", count)
elif a == 3:
    print("Вы выбрали уровень сложности: Сложно")
    SecretNumber = random.randint(0, 500)
    print("Я загадал случайное число от 1 до 1000.")
    print("Твоя задачь отгадать его.")
    Answer = int(input("Загаданное число это ..."))
    check = 16
    count = 1
    while Answer != SecretNumber and check > 0:
        if Answer > SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число меньше числа которое ты ввел. Осталось попыток", check)
        elif Answer < SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число больше числа которое ты ввел. осталось попыток", check)
        Answer = int(input("Введите вашь новый выбор"))
    if check == 0:
        print("Ты проиграл. Попробуй еще раз")
        print("Вот число которое ты не смог угадать:", SecretNumber)
    else:
        print("Ура ты угадал! Поздравляю!")
        print("Ты управился за попыток:", count)
elif a == 4:
    print("Вы выбрали уровень сложности: Экстрим")
    SecretNumber = random.randint(0, 1000)
    print("Я загадал случайное число от 1 до 1000.")
    print("Твоя задачь отгадать его.")
    Answer = int(input("Загаданное число это ..."))
    check = 16
    count = 1
    while Answer != SecretNumber and check > 0:
        if Answer > SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число меньше числа которое ты ввел. Осталось попыток", check)
        elif Answer < SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число больше числа которое ты ввел. осталось попыток", check)
        Answer = int(input("Введите вашь новый выбор"))
    if check == 0:
        print("Ты проиграл. Попробуй еще раз")
        print("Вот число которое ты не смог угадать:", SecretNumber)
    else:
        print("Ура ты угадал! Поздравляю!")
        print("Ты управился за попыток:", count)
elif a == 5:
    print("Вы выбрали уровень сложности: САМЫЙ ЭКСТРИМАЛЬНЫЙ ЭКСТРИМ")
    SecretNumber = random.randint(0, 2500)
    print("Я загадал случайное число от 1 до 2500.")
    print("Твоя задачь отгадать его.")
    Answer = int(input("Загаданное число это ..."))
    check = 20
    count = 1
    while Answer != SecretNumber and check > 0:
        if Answer > SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число меньше числа которое ты ввел. Осталось попыток", check)
        elif Answer < SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число больше числа которое ты ввел. осталось попыток", check)
        Answer = int(input("Введите вашь новый выбор"))
    if check == 0:
        print("Ты проиграл. Попробуй еще раз")
        print("Вот число которое ты не смог угадать:", SecretNumber)
    else:
        print("Ура ты угадал! Поздравляю!")
        print("Ты управился за попыток:", count)
elif a == 9:
    print("Вы выбрали уровень сложности: ЕЩЕ БОЛЕЕ ЭКСТРИМАЛЬНЫЙ ЭКСТРИМ")
    SecretNumber = random.randint(0, 5000)
    print("Я загадал случайное число от 1 до 5000.")
    print("Твоя задачь отгадать его.")
    Answer = int(input("Загаданное число это ..."))
    check = 10
    count = 1
    while Answer != SecretNumber and check > 0:
        if Answer > SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число меньше числа которое ты ввел. Осталось попыток", check)
        elif Answer < SecretNumber:
            check = check - 1
            count = count + 1
            print("Загаданное число больше числа которое ты ввел. осталось попыток", check)
        Answer = int(input("Введите вашь новый выбор"))
    if check == 0:
        print("Ты проиграл. Попробуй еще раз")
        print("Вот число которое ты не смог угадать:", SecretNumber)
    else:
        print("Ура ты угадал! Поздравляю!")
        print("Ты управился за попыток:", count)
if a == 0:
    print("Вы выбрали уровень сложности: Практика")
    SecretNumber = random.randint(0, 3)
    print("Я загадал случайное число от 1 до 3.")
    print("Твоя задачь отгадать его.")
    Answer = int(input("Загаданное число это ..."))
    while Answer != SecretNumber:
        if Answer > SecretNumber:
            print("Загаданное число меньше числа которое ты ввел. Осталось попыток", )
        elif Answer < SecretNumber:
            print("Загаданное число больше числа которое ты ввел. осталось попыток", )
        Answer = int(input("Введите вашь новый выбор"))
    else:
        print("Ура ты угадал! Поздравляю!")