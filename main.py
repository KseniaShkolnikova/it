import sqlite3
import bd
import классы
porols = sqlite3.connect('poroli')
porol = porols.cursor()
bd.bd.bd(self=1)


def sotrudnik(vibor2):
    while True:
        vibor2 = str(input((" Что вы хотите сделать?\n  1. Изменить имя\n  2. Посмотреть товар\n  3. Изменить товар\n  4. Выйти из аакаунта\n")))
        match vibor2:
            case '1':
                классы.adminicotrud.izmenFio(name)
            case '2':
                классы.adminicotrud.prosmotr(self=1)
            case '3':
                vibor3 = str(input("\n Что именно вы хотите сделать?\n  1. Удалить товар\n  2. Добавить товар\n  3. Изменить данные товара\n"))
                match vibor3:
                    case '1':
                        классы.adminicotrud.ydalittovar(self=1)
                    case '2':
                        классы.adminicotrud.dobavtovar(self=1)
                    case '3':
                        классы.adminicotrud.izmentovar(self=1)
            case '4':
                return
def pokupatel(vibor2):
    while True:
        vibor2 =str(input(" Что вы хотите сделать?\n  1. Изменить имя\n  2. Посмотреть товар\n  3. Сделать заказ\n  4. Посмотреть свои заказы\n  5. Выйти из аакаунта\n"))
        match vibor2:
            case '1':
                классы.pokup.izmenFio(name)
            case '2':
                классы.pokup.prosmotr(self=1)
            case '3':
                классы.pokup.zakaz(name, logina)
            case '4':
                классы.pokup.posmotzakaz(logina)
            case '5':
                return

while True:
    print("---------------------------------------------------------------------------")
    vibor1 = str(input(" Книжный магазин 'Питон'.Кто вы? \n  1. Я Админ\n  2. Я Покупатель\n  3. Я Сотрудник\n  4. Я хочу зарегестрироваться\n  5. Я хочу выйти\n"))
    logina = str
    porola = str
    print("---------------------------------------------------------------------------")
    if vibor1 == "4":
        while True:
            vibor5 = str(input(" Вы новый сотрудник или пользователь?\n"))
            if vibor5 =="пользователь" or vibor5=="Пользователь":
                name = input(" Введите свое имя: ")
                while True:
                    logina = input(" Придумайте логин: ")
                    porola = input(" Придумайте пороль: ")
                    try:
                        porol.execute("INSERT INTO porol(logina,porola,name,dolznost_id) VALUES (?,?,?,?)", (logina, porola, name, 2))
                        porols.commit()
                        print(f"\n Здравствуйте, {name}")
                        vibor2=str
                        pokupatel(vibor2)
                    except:
                        print("\n---------------------------------------------------------------------------\n Такой логин уже существует. Придумайте другой логин\n---------------------------------------------------------------------------\n")
            elif vibor5 == "сотрудник" or vibor5=="Сотрудник":
                while True:
                    name = input("Введите свое имя: ")
                    logina = input("Придумайте логин: ")
                    porola = input("Придумайте пороль: ")
                    rabota = str(input("Какая ваша работа: "))
                    try:
                        porol.execute("INSERT INTO porol(logina,porola,name,rabota,dolznost_id) VALUES (?,?,?,?,?)", (logina, porola, name,rabota, 3))
                        porols.commit()
                        print(f"\n Здравствуйте, {name}")
                        vibor2=str
                        sotrudnik(vibor2)
                    except:
                        print("\n---------------------------------------------------------------------------\n Такой логин уже существует. Придумайте другой логин\n---------------------------------------------------------------------------\n")
            else:
                print("\n---------------------------------------------------------------------------\n Нужно ввести свою должность\n---------------------------------------------------------------------------\n")

    elif vibor1 == "2": #Покупатель
        while True:
            logina = input(" Введите логин: ")
            porola = input(" Введите пороль: ")
            porol.execute("SELECT name FROM porol where porola == ? and logina==? and dolznost_id =?", (porola, logina, 2))
            data = porol.fetchone()
            if data is None:
                print("\n---------------------------------------------------------------------------\n Неверный логин или пороль. Попробуйте еще раз\n---------------------------------------------------------------------------\n")
            else:
                for i in data:
                    name = str(i)
                print(f"\n Здравствуйте, {name}")
                vibor2 =str
                pokupatel(vibor2)
                break
    elif vibor1 == "3": #Сотрудник
        while True:
            logina = input(" Введите логин: ")
            porola = input(" Введите пороль: ")
            porol.execute("SELECT name FROM porol where porola == ? and logina==? and dolznost_id=?", (porola, logina, 3))
            data = porol.fetchone()
            if data is None:
                print("\n---------------------------------------------------------------------------\n Неверный логин или пороль. Попробуйте еще раз\n---------------------------------------------------------------------------\n")
            else:
                for i in data:
                    name = str(i)
                print( f"\n Здравствуйте, {name}")
                vibor2=str
                sotrudnik(vibor2)
                break
    elif vibor1 == "1": #Админ
        while True:
            logina = input(" Введите логин: ")
            porola = input(" Введите пороль: ")
            porol.execute("SELECT name FROM porol where porola == ? and logina==? and dolznost_id=?", (porola, logina, 1))
            data = porol.fetchone()
            if data is None:
                print("\n---------------------------------------------------------------------------\n Неверный логин или пороль. Попробуйте еще раз\n---------------------------------------------------------------------------\n")
            else:
                for i in data:
                    name = str(i)
                    print(f"\n Здравствуйте, {name}")
                    break
                while True:
                    vibor2= input((" Что вы хотите сделать?\n  1. Изменить имя\n  2. Посмотреть товар\n  3. Изменить това\n  4. Изменить сотрудников\n  5. Выйти из аакаунта\n"))
                    match vibor2:
                        case '1':
                            классы.admin.izmenFio(name)
                        case '2':
                            классы.admin.prosmotr(self=1)
                        case '3':
                            vibor3 = str(input("\n Что именно вы хотите сделать?\n  1. Удалить товар\n  2. Добавить товар\n  3. Изменить данные товара\n"))
                            match vibor3:
                                case '1':
                                    классы.admin.ydalittovar(self=1)
                                case '2':
                                    классы.admin.dobavtovar(self=1)
                                case '3':
                                    классы.admin.izmentovar (self=1)
                        case '4':
                            vibor6 = str(input("\n Что именно вы хотите сделать\n  1. Удалить сотрудника\n  2. Добавить сотрудника\n  3. Выдать новую работу сотруднику\n"))
                            match vibor6:
                                case '1':
                                    классы.admin.ydalsotrud(self=1)
                                case '2':
                                    классы.admin.dobavsotrud(self=1)
                                case '3':
                                    классы.admin.izmensotrud(self=1)
                        case '5':
                            print("\n----------------------- Пока крутой админ! -----------------------")
                            exit()
    elif vibor1 == '5':
        print("\n                 Досвидания. Приходите еще!             ")
        exit()
    else:
        print(" Нужно ввести номер варианта ответа")
    break
