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
        return False 
    
    def admin_login(self,name,password) -> bool:
        if name in self.admins:
            if self.admins[name].password == password:
                self.current_user = self.customers[name]
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
        self.theater_list[theaterName] = Theater(theaterName,location)
    
    def set_movie_group(self,movie_name,show_time_list,theater_list):
        for theater in theater_list:
            for show_time in show_time_list:
                self.theater_list[theater].shows[show_time] = movie_name

    def set_movie_specific(self,theater,movie_name,show_time,):
        self.theaters_list[theater].shows[show_time] = movie_name

    def __str__(self) -> str:
        string = ""
        for theater in self.theater_list:
            string += f'git  {theater}\n'
            for show in self.theater_list[theater].shows:
                string += f'{show} : {self.theater_list[theater].shows[show]} \n'
        return string
    

bookshow = app()
bookshow.add_theater('luxe','velachery')
bookshow.add_theater('luxa','velachery')
bookshow.add_theater('luxi','velachery')
bookshow.add_theater('luxo','velachery')

bookshow.set_movie_group("rrr",['9:00 am','6:00 pm'],['luxe','luxa','luxi','luxo'])

print(bookshow)

