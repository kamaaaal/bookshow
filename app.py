from locale import currency
from admin import Admin
from customer import Customer
from theater import Theater


class app:
    def __init__(self) -> None:
        self.movies_list = {}
        self.theater_list = {}
        self.customers = {}
        self.admins = {}
        self.current_user = None
    
    # login function returns true on succesfull login 
    def login(self,name,password):
        if name in self.customers:
            if self.customers[name].password == password:
                self.current_user = self.customers[name]
                return True
            else :
                print('wrong password')
        elif name in self.admins:
            if self.admins[name].password == password:
                self.current_user = self.admins[name]
                return True
        return False 
    
    def sign_up(self,name,mail_id,password):
        self.customers[name] = Customer(name,mail_id,password)
        return self.customers[name]
    
    def admin_signup(self,name,mail_id,password,special_key):
        if special_key == "trustMeBroI'mAnAdmin":
            self.admins[name] = Admin(name,mail_id,password)
        return self.admins[name]
    
    def add_theater(self,theaterName,location):
        if self.current_user != None and self.current_user.is_admin:
            self.theater_list[theaterName] = Theater(theaterName,location)
            self.current_user.history.append(
                ("added theater",self.theater_list[theaterName])\
            )
        else : 
            print(f'you are not an admin')
    
    def set_movie_group(self,movie_name,show_time_list,theater_list):
        for theater in theater_list:
            for show_time in show_time_list:
                self.theater_list[theater].shows[show_time] = movie_name

    def set_movie_specific(self,theater,movie_name,show_time,):
        self.theaters_list[theater].shows[show_time] = movie_name
    
    def book_ticket(self,theater_name,show_time,seats_list):
        theater = self.theater_list[theater_name]
        movie = theater.shows[show_time]
        if self.current_user != None:
            for seat in seats_list:
                selected_seat = theater.seats[show_time][int(seat[0])][int(seat[1]) - 1]
                booked_seat = selected_seat.book_seat(self.current_user,movie)
                if booked_seat:
                    self.current_user.history.append(
                        ("booked tiket",booked_seat)
                    )
        else:
            print("your not logged in")
    
    def logout(self):
        self.current_user = None


    def __str__(self) -> str:
        string = ""
        for theater in self.theater_list:
            string += f'git  {theater}\n'
            for show in self.theater_list[theater].shows:
                string += f'{show} : {self.theater_list[theater].shows[show]} \n'
        return string
    

bookshow = app()

bookshow.admin_signup("mhd",'mhd@gmail.com','password',"trustMeBroI'mAnAdmin")
bookshow.login('mhd','password')

bookshow.add_theater('luxe','velachery')
bookshow.add_theater('luxa','velachery')
bookshow.add_theater('luxi','velachery')
bookshow.add_theater('luxo','velachery')

bookshow.set_movie_group("rrr",['9:00 am','6:00 pm'],['luxe','luxa','luxi','luxo'])


print(bookshow.theater_list['luxo'].print_seats('9:00 am'))

bookshow.logout()

bookshow.sign_up("kamal","kamal@kamal.com","thisiskamal")
bookshow.sign_up('natali','dyer@mail.com','ndddd')


bookshow.login("kamal","thisiskamal")

bookshow.book_ticket("luxo",'9:00 am',['01','02','99'])
bookshow.logout()
bookshow.theater_list['luxo'].print_seats('9:00 am')

bookshow.login('natali','ndddd')
bookshow.book_ticket('luxo','9:00 am',['01','22'])
print(bookshow.theater_list['luxo'].print_seats('9:00 am'))

bookshow.admins['mhd'].print_history()

bookshow.customers['kamal'].print_history()

bookshow.customers['natali'].print_history()