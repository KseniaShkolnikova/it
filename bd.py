import sqlite3
class bd():
    def bd(self):
        porols = sqlite3.connect('poroli')
        porol = porols.cursor()

        try:
            porol.execute("SELECT * FROM tovar")
            porols.commit()
        except:
            porol.execute('''
                    CREATE TABLE IF NOT EXISTS tovar(
                            id INTEGER PRIMARY KEY UNIQUE,
                            nazvania TEXT NOT NULL UNIQUE,
                            avtor TEXT NOT NULL,
                            colvo INTEGER NOT NULL,
                            cena INTEGER NOT NULL 
                    )
            ''')
            porols.commit()
            scrept2 = '''
                                INSERT INTO tovar (nazvania,avtor,colvo,cena) VALUES ('Зеленая миля', 'Стивен Кинг', 4, 1200);
                                INSERT INTO tovar (nazvania,avtor,colvo,cena) VALUES ('Унесенные ветром', 'Маргарет Митчелл', 9, 1500);
                                INSERT INTO tovar (nazvania,avtor,colvo,cena) VALUES ('Свита короля', 'Нора Сакавич', 53, 600);
                                INSERT INTO tovar (nazvania,avtor,colvo,cena) VALUES ('Прислуга', 'Кэтрин Стокетт', 94, 1201);
                                INSERT INTO tovar (nazvania,avtor,colvo,cena) VALUES ('Новела', 'Школьникова Ксения', 1, 999999);
                            '''
            porols.executescript(scrept2)
        finally:
            try:
                porol.execute("SELECT * FROM dolznost")
            except:
                porol.execute('''
                        CREATE TABLE IF NOT EXISTS dolznost(
                            id INTEGER PRIMARY KEY UNIQUE,
                            dolznost TEXT NOT NULL UNIQUE
                        )
                ''')
                porols.commit()
                scrept ='''
                    INSERT INTO dolznost (dolznost) VALUES ('Админ');
                    INSERT INTO dolznost (dolznost) VALUES ('Покупатель');
                    INSERT INTO dolznost (dolznost) VALUES ('Сотрудник');
                '''
                porols.executescript(scrept)

        porol.execute('''
                  CREATE TABLE IF NOT EXISTS porol(
                        id INTEGER PRIMARY KEY UNIQUE,
                        logina TEXT NOT NULL UNIQUE,
                        porola TEXT NOT NULL,
                        name TEXT NOT NULL,
                        rabota TETX,
                        dolznost_id INTEGER NOT NULL,
                        FOREIGN KEY (dolznost_id) REFERENCES dolznost(id)
                )
        ''')
        porols.commit()

        porol.execute('''
                          CREATE TABLE IF NOT EXISTS zakaz(
                                id INTEGER PRIMARY KEY UNIQUE,
                                nazvanie TEXT NOT NULL,
                                cena TEXT NOT NULL,
                                name TEXT NOT NULL,
                                porol_id INTEGER NOT NULL,
                                FOREIGN KEY (porol_id) REFERENCES porol(id)
                        )
                ''')
        porols.commit()