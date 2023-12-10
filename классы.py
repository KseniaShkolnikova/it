import sqlite3
import bd
porols = sqlite3.connect('poroli')
porol = porols.cursor()
bd.bd.bd(self=1)
class obche:
    def izmenFio(name):
        name2 = input(("\n Введите имя, которое вы себе хотите: "))
        try:
            porol.execute("UPDATE porol SET name =? WHERE  name = ?", (name2, name))
            porols.commit()
            print("\n---------------------------------------\n Новое имя удачно записано\n-----------------------------------\n")
        except:
            print("\n---------------------------------------\n Не удалось. Попробуйте еще раз\n-----------------------------------\n")
        return

    def prosmotr(self):
        try:
            porol.execute("SELECT * FROM tovar ")
            rows = porol.fetchall()
            print("\n--------------------------------------- Список товаров -----------------------------------\n")
            for row in rows:
                print(row)
            print()
        except:
            print("\n---------------------------------------\n Нет товаров\n-----------------------------------\n")
        return 
class adminicotrud (obche):
    pass
    def ydalittovar(self):
        while True:
            try:
                __id = int (input("\n Введите ID книги, которую необходимо удалить: "))
                __idv = str (__id)
                porol.execute("SELECT * FROM tovar WHERE id =?",(__idv))
                prover = porol.fetchall()
                kpp = prover[0]
                porol.execute("DELETE FROM tovar WHERE id=?",(__idv))
                porols.commit()
                print("\n---------------------------------------\n Книга была удачно удалена\n-----------------------------------\n")
                break
            except:
                print("\n---------------------------------------\n Неверный id. Попробуйте еще раз\n-----------------------------------\n")
        return
    def dobavtovar (self):
        __nazvanie = str (input("\n Введите название книги: "))
        __avtor = str(input(" Введите автора книги: "))
        while True:
            try:
                __colvo = int(input(" Введите колличество книг: "))
                break
            except:
                print("\n---------------------------------------\n Нужно вводить число\n---------------------------------------\n")
        while True:
                try:
                    __cena = int(input(" Введите цену книги: "))
                    break
                except:
                    print("\n---------------------------------------\n Нужно вводить число\n---------------------------------------\n")
        porol.execute("INSERT INTO tovar (nazvania,avtor,colvo,cena) VALUES (?,?,?,?)",(__nazvanie,__avtor,__colvo,__cena))
        print("\n---------------------------------------\n Книга была удачно добавлена\n---------------------------------------\n")
        porols.commit()
        return
    def izmentovar (self):
        while True:
            try:
                __id = int (input("\n Введите id книги, которую необходимо изменить: "))
                __idv = str(__id)
                porol.execute("SELECT * FROM tovar WHERE id =?", (__idv))
                prover = porol.fetchall()
                kpp = prover[0]
                __vibor4 = str(input("\n Что вы хотите изменить?\n  1. Название\n  2. Автор\n  3. Колличество книг\n  4. Цена\n"))
                break
            except:
                print("\n---------------------------------------\n Неверный id. Попробуйте еще раз\n-----------------------------------\n")
        match __vibor4:
            case '1':
                __name2 = input(("\n Введите новое название книги: "))
                porol.execute("UPDATE tovar SET nazvania =? WHERE id = ?", (__name2, __idv))
                porols.commit()
            case '2':
                __avtor2 = input((" Введите нового автора книги: "))
                porol.execute("UPDATE tovar SET avtor =? WHERE id = ?", (__avtor2, __idv))
                porols.commit()
            case '3':
                while True:
                    try:
                        __colvo2 = input((" Введите новое количество книг: "))
                        porol.execute("UPDATE tovar SET colvo =? WHERE id = ?", (int(__colvo2), __idv))
                        porols.commit()
                        break
                    except:
                        print("\n---------------------------------------\n Нужно вводить число\n---------------------------------------\n")
            case '4':
                while True:
                    try:
                        __cena2 = input((" Введите новую цену книги: "))
                        porol.execute("UPDATE tovar SET cena =? WHERE id = ?", (int(__cena2), __idv))
                        porols.commit()
                        break
                    except:
                        print("\n---------------------------------------\n Нужно вводить число\n---------------------------------------\n")
        print("\n---------------------------------------\n Товар успешно изменен\n---------------------------------------\n")
        return
class admin(adminicotrud):
    pass
    def ydalsotrud (self):
        porol.execute("SELECT * FROM porol WHERE dolznost_id = ?",(str(3)))
        rows = porol.fetchall()
        for row in rows:
            print(row)
        while True:
            try:
                __id = (input("\n Введите ID сотрудника, которого необходимо удалить: "))
                __idv = str(__id)
                porol.execute("DELETE FROM porol WHERE id=? AND  dolznost_id =?", (int(__idv), int(3)))
                porols.commit()
                print("\n---------------------------------------\n Сотрудник был успешно удвлен\n---------------------------------------\n")
                break
            except:
                print("\n---------------------------------------\n Неверный id. Попробуйте еще раз\n-----------------------------------\n")
        return
    def dobavsotrud (self):
        __logina = str(input("\n Введите логин для нового сотрудника: "))
        __porola = str(input(" Введите пороль для нового сотрудника: "))
        __name = str(input(" Введите имя нового сотрудника: "))
        __rabota = str(input(" Введите работу, которую будет выполнять новый сотрудник: "))
        porol.execute("INSERT INTO porol (logina,porola,name,rabota,dolznost_id) VALUES (?,?,?,?,?)", (__logina, __porola, __name, __rabota,3))
        porols.commit()
        print("\n---------------------------------------\n Новый сотрудник успешно добавлен\n---------------------------------------\n")
        return
    def izmensotrud (self):
        while True:
            try:
                porol.execute("SELECT * FROM porol WHERE dolznost_id = ?", (str(3)))
                rows = porol.fetchall()
                for row in rows:
                    print(row)
                __id = int(input("\n Введите id сотрудника: "))
                porol.execute("SELECT * FROM porol WHERE dolznost_id=?", (str(3)))
                __rabot2 = input((" Введите новую работу для сотрудника: "))
                porol.execute("UPDATE porol SET rabota =? WHERE  id = ? AND dolznost_id =?", (str(__rabot2), int(__id),int (3)))
                porols.commit()
                print("\n---------------------------------------\n Работа была усешно выдана\n---------------------------------------\n")
                break
            except:
                print("\n---------------------------------------\n Неверный id. Попробуйте еще раз\n-----------------------------------\n")
        return
class pokup(obche):
    pass
    def zakaz(name,logina):
        while True:
            porol.execute("SELECT * FROM tovar")
            rows = porol.fetchall()
            for row in rows:
                print(row)
            while True:
                try:
                    __id = int(input("\n Введите id книги, которую вы хотите купить: "))
                    __idv =str(__id)
                    porol.execute("SELECT colvo FROM tovar WHERE id=?",(__idv))
                    __colvo1 = porol.fetchone()
                    __colvo=__colvo1[0]
                    colvo2 = __colvo-1
                    porol.execute("UPDATE tovar SET colvo =? WHERE  id = ?", (colvo2, __idv))
                    porols.commit()
                    porol.execute("SELECT nazvania FROM tovar WHERE id=?",(__idv))
                    __nazv1 = porol.fetchone()
                    nazv = __nazv1[0]
                    porol.execute("SELECT cena FROM tovar WHERE id=?", (__idv))
                    __cena1 = porol.fetchone()
                    cena = __cena1[0]
                    porol.execute("SELECT id FROM porol WHERE logina=?", (logina))
                    __id1 = porol.fetchone()
                    __id = str(__id1[0])
                    porol.execute("INSERT INTO zakaz(nazvanie,cena,name,porol_id) VALUES (?,?,?,?)", (nazv,cena,name,__id))
                    porols.commit()
                    break
                except:
                    print("\n--------------------------------\n Неверный id. Попробуйте еще раз\n--------------------------------\n")
            vibor7 = str(input("\n Хотите купить еще ?: \n"))
            if vibor7== "Да" or vibor7== "да":
                print("\n------------------------ Повторный заказ ------------------------")
            elif vibor7 == "Нет" or vibor7 == "нет":
                break
            else:
                print("\n--------------------------------\n Нужно вводить да или нет. Попробуйте еще раз\n--------------------------------\n")
        return
    def posmotzakaz(logina):
        while True:
            try:
                porol.execute("SELECT id FROM porol WHERE logina=?", (logina))
                id1 = porol.fetchall()
                id = int
                id = (id1[0])
                porol.execute("SELECT * FROM zakaz WHERE porol_id =?",(id))
                rows = porol.fetchall()
                print("\n--------------------------------------- Ваши заказы ---------------------------------------")
                for row in rows:
                    print(row)
                print()
                break
            except:
                print("\n--------------------------------\n У вас нет заказов\n--------------------------------\n")
