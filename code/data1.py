import sqlite3

DB = 'tour1.db'


class DataBase():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def __enter__(self):
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()


class Admin:
    @staticmethod
    def create_table_of_tour():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS  tour1(
            tourID INT PRIMARY KEY,
            name_of_office TEXT,
            name_of_tour TEXT,
            type TEXT,
            dates TEXT,
            duration_days INT,
            locality TEXT,
            price_list INT,
            type_of_tr TEXT,
            point_of_dep TEXT);""")

    @staticmethod
    def filling():
        tours = [
            ('1', 'АльтусТурБай', 'Албания', 'Экскурсия', '14.07.2022 - 20.07.2022',  '7', 'Албания', '1', 'Самолет', 'ул. Октябрьская 5'),
            ('2', 'ТурАгенство "А"', 'Г-Ч', 'Автобусный тур', '01.05.2022 - 14.05.2022', '14', 'Грузия, Черногория', '2', 'Автобус', 'ст.м. Первомайская'),
            ('3', 'УмноТуры', 'Снег', 'Горнолыжный', '30.12.2022 - 02.01.2023', '3', 'Буковель', '3', 'Поезд', 'Вокзал')
        ]
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.executemany("""INSERT INTO tour1 VALUES(?,?,?,?,?,?,?,?,?,?);""", tours)
            print("done2")

    @staticmethod
    def create_office():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS  office(
                officeID TEXT PRIMARY KEY,
                name_of_office TEXT,
                address TEXT,
                phone TEXT,
                person TEXT);""")

    @staticmethod
    def fill_office():
        offices = [
            ('001', 'АльтусТурБай', 'ул. Октябрьская 5', '+375291012237', 'Войшнис Майя Александровна'),
            ('002', 'ТурАгенство "А"', 'ул. Гикало 30', '+375291442489', 'Свиридова Мария Олеговна'),
            ('003', 'УмноТуры', 'ул. Платонова 1', '+375443567622', 'Платонов Александр Владимирович')
        ]
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.executemany("""INSERT INTO office VALUES(?,?,?,?,?);""", offices)
        print("done2")

    @staticmethod
    def create_price_list():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS  price_list(
            priceID TEXT PRIMARY KEY,
            tourID INT,
            price INT);""")

    @staticmethod
    def fill_price_list():
        price_list = [
            ('1', '1', '1700'),
            ('2', '2', '3000'),
            ('3', '3', '5000')
        ]
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.executemany("""INSERT INTO price_list VALUES(?,?,?);""", price_list)
        print("done3")

    @staticmethod
    def show_price():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT * FROM price_list""")
            return cur.fetchall()

    @staticmethod
    def show_tour():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT * FROM tour1""")
            # cur.execute(f"SELECT id, name_of_tour, type, duration_days, locality, hotel, amount_of_stars, price, type_of_tr, point_of_dep FROM tour1;")
                        # f"WHERE name_of_office = '{office}';")
            # cur.execute("SELECT * FROM tour1")
            return cur.fetchall()


    # --------------------------------------TOUR---------------------------------------------------

    @staticmethod
    def show():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"SELECT tourID, name_of_office, name_of_tour,type,dates,duration_days,type_of_tr,point_of_dep FROM tour1;")
            return cur.fetchall()

    @staticmethod
    def add_tour(*args):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""INSERT INTO tour1(tourID, name_of_office, name_of_tour, type, dates, duration_days, type_of_tr, point_of_dep) VALUES(?,?,?,?,?,?,?,?)""", tuple(args))
        print('Тур успешно добавлен!')

    @staticmethod
    def del_tour(category, key):
        categories = ['id', 'name_of_tour']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM tour1 WHERE {categories[category]} = '{key}'")
        print('Тур успешно удалён!')

    @staticmethod
    def update_tour(key, name_of_col, new_inf):
        categories = ['id', 'name_of_office', 'name_of_tour', 'type', 'dates', 'duration_days', 'type_of_tr', 'point_of_dep']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""UPDATE tour1 SET {categories[name_of_col]} = '{new_inf}'
                        WHERE id = '{key}'""")

    @staticmethod
    def update_hotel(key, hotel, locality):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""UPDATE tour1 SET locality = '{locality}', hotel = '{hotel}' WHERE id = '{key}'""")

    @staticmethod
    def del_table():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""DROP TABLE hotel""")
            print('done')
    # -----------------------------------OFFICE---------------------------------------------
    @staticmethod
    def show_off():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"SELECT * FROM office;")
            return cur.fetchall()

    @staticmethod
    def add_off(*args):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""INSERT INTO office VALUES(?,?,?,?,?)""", tuple(args))
        print('Офис успешно добавлен!')

    @staticmethod
    def del_off(category, key):
        categories = ['officeID', 'name_of_office', 'address', 'phone', 'person']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM office WHERE {categories[category]} = '{key}'")
        print('Тур успешно удалён!')

    @staticmethod
    def update_off(key, name_of_col, new_inf):
        categories = ['officeID', 'name_of_office', 'address', 'phone', 'person']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""UPDATE office SET {categories[name_of_col]} = '{new_inf}'
                        WHERE officeID = '{key}'""")

# -----------------------------------------------HOTEL-----------------------------------------
    @staticmethod
    def create_locality():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS  locality(
            localityID TEXT PRIMARY KEY);""")

    @staticmethod
    def fill_locality():
        localitys = [
            # ('Албания')
            # ('Грузия, Черногория')
            ('Буковель')
        ]
        print(len(localitys))
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""INSERT INTO locality VALUES(?);""", localitys)

    @staticmethod
    def create_hotel():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS  hotel(
            hotelID TEXT PRIMARY KEY,
            locality TEXT,
            hotel_name TEXT,
            amount_of_stars INT);""")

    @staticmethod
    def fill_hotel():
        hotels = [
            ('01', 'Албания', 'King', '5'),
            ('02', 'Грузия, Черногория', 'Hotel_A', '4'),
            ('03', 'Буковель', 'HHH', '4')
        ]
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.executemany("""INSERT INTO hotel VALUES(?,?,?,?);""", hotels)

    @staticmethod
    def show_loc():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT * FROM locality""")
            return cur.fetchall()

    @staticmethod
    def show_hotel():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT * FROM hotel""")
            return cur.fetchall()

    @staticmethod
    def add_hotel(*args):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""INSERT INTO hotel VALUES(?,?,?,?)""", tuple(args))
    #     Admin.add_loc()
    #
    # @staticmethod
    # def add_loc():
    #     with DataBase(DB) as connection:
    #         cur = connection.cursor()
    #         cur.execute("""INSERT INTO locality (locality) SELECT locality FROM hotel
    #                        WHERE locality != hotel.locality""")
    #         print('asdf')

    @staticmethod
    def del_hotel(category, key):
        categories = ['hotelID', 'locality', 'hotel_name', 'amount_of_stars']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"DELETE FROM hotel WHERE {categories[category]} = '{key}'")
        print('Тур успешно удалён!')

    @staticmethod
    def update_hotel(key, name_of_col, new_inf):
        categories = ['hotelID', 'locality', 'hotel_name', 'amount_of_stars']
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""UPDATE hotel SET {categories[name_of_col]} = '{new_inf}'
                        WHERE hotelID = '{key}'""")

# ----------------------------------------------USER-----------------------------------------
class User:
    @staticmethod
    def show_full_tour(key):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""SELECT tour1.tourID, tour1.name_of_office, tour1.name_of_tour, tour1.type, tour1.dates, 
                           tour1.duration_days, locality, hotel.hotel_name, hotel.amount_of_stars, price_list.price, tour1.type_of_tr, 
                            tour1.point_of_dep, office.address, office.phone, office.person FROM tour1 
                           INNER JOIN office USING(name_of_office)
                           INNER JOIN hotel USING(locality)
                           INNER JOIN price_list USING(tourID)
                           WHERE tour1.tourID = '{key}'""")
            return cur.fetchall()

    @staticmethod
    def show_hotels5():
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute("""SELECT hotel_name FROM hotel 
                           WHERE amount_of_stars = 5""")
            return cur.fetchall()

    @staticmethod
    def show_price_list(date):
        with DataBase(DB) as connection:
            cur = connection.cursor()
            cur.execute(f"""SELECT tour1.dates, tour1.name_of_tour, price_list.price, name_of_office, address, phone, person FROM office
                           INNER JOIN tour1 USING(name_of_office)
                           INNER JOIN price_list USING(tourID)
                           WHERE dates = '{date}'""")
            return cur.fetchall()


if __name__ == '__main__':
    i = Admin()

    a = User()
    print(a.show_price_list('30.12.2022 - 02.01.2023'))


