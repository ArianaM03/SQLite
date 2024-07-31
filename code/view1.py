from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from data1 import Admin, User

Builder.load_file("ui1.kv")


class MenuScreen(Screen):
    pass


class AdminScreen(Screen):
    pass


class UserScreen(Screen):
    pass


class OfficeScreen(Screen):
    def current_data(self):
        self.data = Admin.show_off()
        self.idd, self.name_of_office, self.address, self.phone, self.person = 'id\n', 'Название офиса\n', 'Адрес\n', 'Телефон\n', 'ФИО\n'
        for i in self.data:
            self.idd += f"{i[0]}\n"
            self.name_of_office += f"{i[1]}\n"
            self.address += f"{i[2]}\n"
            self.phone += f"{i[3]}\n"
            self.person += f"{i[4]}\n"

    def show_off(self):
        self.current_data()
        self.ids['id_idd_label'].text = self.idd
        self.ids['id_name_label'].text = self.name_of_office
        self.ids['id_address_label'].text = self.address
        self.ids['id_phone_label'].text = self.phone
        self.ids['id_person_label'].text = self.person


class AddOfficeScreen(Screen):
    def add_of(self, *args):
        Admin.add_off(*args)


class DelOfficeScreen(Screen):
    def del_of(self, category, key):
        Admin.del_off(category, key)


class UpdateOfficeScreen(Screen):
    def upd_of(self, key, name_of_col, new_inf):
        Admin.update_off(key, name_of_col, new_inf)


class TourScreen(Screen):
    def current_data(self):
        self.data = Admin.show()
        self.id, self.name_of_office, self.name_of_tour, self.type, self.dates, self.duration_days, self.type_of_tr, self.point_of_dep = \
            'id\n', 'Название офиса\n', 'Название тура\n', 'Тип\n', 'Даты\n', 'Продолжительность\n', 'Тип транспорта\n', 'Точка отправления\n'
        for i in self.data:
            self.id += f"{i[0]}\n"
            self.name_of_office += f"{i[1]}\n"
            self.name_of_tour += f"{i[2]}\n"
            self.type += f"{i[3]}\n"
            self.dates += f"{i[4]}\n"
            self.duration_days += f"{i[5]}\n"
            self.type_of_tr += f"{i[6]}\n"
            self.point_of_dep += f"{i[7]}\n"

    def show_tour(self):
        self.current_data()
        self.ids['id_id_label'].text = self.id
        self.ids['id_office_label'].text = self.name_of_office
        self.ids['id_tour_label'].text = self.name_of_tour
        self.ids['id_type_label'].text = self.type
        self.ids['id_dates_label'].text = self.dates
        self.ids['id_days_label'].text = self.duration_days
        self.ids['id_transport_label'].text = self.type_of_tr
        self.ids['id_point_label'].text = self.point_of_dep


class AddTourScreen(Screen):
    def addTour(self, *args):
        Admin.add_tour(*args)


class DeleteTourScreen(Screen):
    def delTour(self, category, key):
        Admin.del_tour(category, key)


class UpdateTourScreen(Screen):
    def updTour(self, key, name_of_col, new_inf):
        Admin.update_tour(key, name_of_col, new_inf)


class HotelScreen(Screen):
    def current_data(self):
        self.data = Admin.show_hotel()
        self.id, self.locality, self.hotel_name, self.amount_of_stars = \
            'id\n', 'Название города\n', 'Название отеля\n', 'Количество звезд\n'
        for i in self.data:
            self.id += f"{i[0]}\n"
            self.locality += f"{i[1]}\n"
            self.hotel_name += f"{i[2]}\n"
            self.amount_of_stars += f"{i[3]}\n"

    def show_hotel(self):
        self.current_data()
        self.ids['id_id_label'].text = self.id
        self.ids['id_locality_label'].text = self.locality
        self.ids['id_hotel_name_label'].text = self.hotel_name
        self.ids['id_stars_label'].text = self.amount_of_stars


class AddHotelScreen(Screen):
    def add_hotel(self, *args):
        Admin.add_hotel(*args)


class UpdHotelScreen(Screen):
    def upd_hotel(self,key, name_of_col, new_inf):
        Admin.update_hotel(key, name_of_col, new_inf)


class DelHotelScreen(Screen):
    def del_hotel(self, category, key):
        Admin.del_tour(category, key)


class InfAboutTourScreen(Screen):
    def current_data(self, key):
        self.data = User.show_full_tour(key)
        self.id, self.name_of_office, self.name_of_tour, self.type, self.dates, self.duration_days, self.locality, self.hotel, self.amount_of_stars, self.price, self.type_of_tr, self.point_of_dep, self.address, self.phone, self.person = \
            'id\n', 'Название офиса\n', 'Название тура\n', 'Тип\n', 'Даты\n', 'Продолжительность\n', 'Место расположение\n', 'Отель\n', 'Количество звезд\n', 'Стоимость\n', 'Тип транспорта\n', 'Точка отправления\n', 'Адрес\n', 'Телефон\n', 'ФИО\n'
        for i in self.data:
            self.id += f"{i[0]}\n"
            self.name_of_office += f"{i[1]}\n"
            self.name_of_tour += f"{i[2]}\n"
            self.type += f"{i[3]}\n"
            self.dates += f"{i[4]}\n"
            self.duration_days += f"{i[5]}\n"
            self.locality += f"{i[6]}\n"
            self.hotel += f"{i[7]}\n"
            self.amount_of_stars += f"{i[8]}\n"
            self.price += f"{i[9]}\n"
            self.type_of_tr += f"{i[10]}\n"
            self.point_of_dep += f"{i[11]}\n"
            self.address += f"{i[12]}\n"
            self.phone += f"{i[13]}\n"
            self.person += f"{i[14]}\n"

    def show_info(self, key):
        self.current_data(key)
        self.ids['id_id_label'].text = self.id
        self.ids['id_office_label'].text = self.name_of_office
        self.ids['id_tour_label'].text = self.name_of_tour
        self.ids['id_type_label'].text = self.type
        self.ids['id_dates_label'].text = self.dates
        self.ids['id_days_label'].text = self.duration_days
        self.ids['id_locality_label'].text = self.locality
        self.ids['id_hotel_label'].text = self.hotel
        self.ids['id_stars_label'].text = self.amount_of_stars
        self.ids['id_price_label'].text = self.price
        self.ids['id_transport_label'].text = self.type_of_tr
        self.ids['id_point_label'].text = self.point_of_dep
        self.ids['id_address_label'].text = self.address
        self.ids['id_phone_label'].text = self.phone
        self.ids['id_person_label'].text = self.person


class InfStarsScreen(Screen):
    def current_data(self):
        self.data = User.show_hotels5()
        self.hotel = 'Отель\n'
        for i in self.data:
            self.hotel += f"{i[0]}\n"

    def show_info(self):
        self.current_data()
        self.ids['id_hotel_label'].text = self.hotel


class PriceListScreen(Screen):
    def current_data(self, key):
        self.data = User.show_price_list(key)
        self.dates, self.name_of_tour, self.price, self.name_of_office, self.address, self.phone, self.person,  = 'Даты\n', 'Название тура\n', 'Цена\n', 'Название офиса\n', 'Адрес\n', 'Телефон\n', 'ФИО\n'
        for i in self.data:
            self.dates = f"{i[0]}\n"
            self.name_of_tour += f"{i[1]}\n"
            self.price = f"{i[2]}\n"
            self.name_of_office += f"{i[3]}\n"
            self.address += f"{i[4]}\n"
            self.phone += f"{i[5]}\n"
            self.person += f"{i[6]}\n"

    def show_info(self, key):
        self.current_data(key)
        self.ids['id_dates_label'].text = self.dates
        self.ids['id_tour_label'].text = self.name_of_tour
        self.ids['id_price_label'].text = self.price
        self.ids['id_name_label'].text = self.name_of_office
        self.ids['id_address_label'].text = self.address
        self.ids['id_phone_label'].text = self.phone
        self.ids['id_person_label'].text = self.person



class TestApp(App):
    Window.clearcolor = (.67, .73, .89, 1)

    def build(self):
        self.title = "Travel Agency"
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(AdminScreen(name='admin'))
        sm.add_widget(UserScreen(name='user'))
        sm.add_widget(OfficeScreen(name='office'))
        sm.add_widget(AddOfficeScreen(name='addoffice'))
        sm.add_widget(DelOfficeScreen(name='deloffice'))
        sm.add_widget(UpdateOfficeScreen(name='updoffice'))
        sm.add_widget(TourScreen(name='tour'))
        sm.add_widget(AddTourScreen(name='addtour'))
        sm.add_widget(DeleteTourScreen(name='deltour'))
        sm.add_widget(AddTourScreen(name='addtour'))
        sm.add_widget(UpdateTourScreen(name='updtour'))
        sm.add_widget(HotelScreen(name='hotel'))
        sm.add_widget(AddHotelScreen(name='addhotel'))
        sm.add_widget(UpdHotelScreen(name='updhotel'))
        sm.add_widget(DelHotelScreen(name='delhotel'))
        sm.add_widget(InfAboutTourScreen(name='infotour'))
        sm.add_widget(InfStarsScreen(name='star'))
        sm.add_widget(PriceListScreen(name='list'))
        return sm


if __name__ == '__main__':
    TestApp().run()