class Seat:
    def __init__(self,seat_no,theater_name):
        self.seat_no = seat_no
        self.theater = theater_name
        self.movie = None
        self.booked_by = None

    
    def __str__(self):
        if self.booked_by == None:
            return self.seat_no
        else :
            return 'BD'

    def book_seat(self,user,movie_name):
        if self.booked_by == None:
            self.booked_by = user
            self.movie = movie_name
            return self
        else:
            print(f"{self.seat_no} seat is already booked , already booked") 

    def breif(self):
        return (f'name : {self.theater} ; movie : {self.movie} ; booked by : {self.booked_by}')
