from seat import Seat

class Theater:

    def __init__(self,name,location):
        self.name = name
        self.shows = {
            '9:00 am' : None,
            '2:00 pm' : None,
            '6:00 pm' : None
        }
        self.seats = {
            '9:00 am' : [[ Seat(f'{y}{x}',self.name) for x in range(1,10)] for y in range(0,10)],
            '2:00 pm' : [[ Seat(f'{y}{x}',self.name) for x in range(1,10)] for y in range(0,10)],
            '6:00 pm' : [[ Seat(f'{y}{x}',self.name) for x in range(1,10)] for y in range(0,10)], 
            }
        self.location = location 

        
    def set_movies(self,movie_name):
        self.shows.update(dict.fromkeys(['9:00 am','2:00 pm','6:00 pm'] , movie_name))
    
    def set_movies_time(self,shows_list,movie_name):
        for show in shows_list:
            self.shows[show] = movie_name


    def __str__(self) -> str:
        return (f'theater Name : {self.name} \nlocation : {self.location} \n{self.get_shows()}') 

    
    def get_shows(self) -> str:
            shows = ""
            for time,movie in self.shows.items():
                shows += f'{time} : {movie} \n'
            return shows

    def print_seats(self,time):
        print(f'\n"NOTE" : "BD" represents Booked\n')
        if time in self.seats:
            seats = self.seats[time]
            for row in seats:
                for seat in row:
                    print(seat,end="|")
                print()

    def clear_seats(self):
        self.seats = {
            '9:00 am' : [[ Seat(f'{y}{x}',self.name) for x in range(1,10)] for y in range(0,10)],
            '2:00 pm' : [[ Seat(f'{y}{x}',self.name) for x in range(1,10)] for y in range(0,10)],
            '6:00 pm' : [[ Seat(f'{y}{x}',self.name) for x in range(1,10)] for y in range(0,10)], 
            }