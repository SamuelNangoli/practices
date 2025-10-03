class Movie:
    def __init__(self, title, seats):
        self.title = title
        self.seats = seats

    def  book_seat(self):
        if self.seats > 0: 
            self.seats -= 1 #reducing the seats by 1 coz of booking
            print('Taken')
        print('Available')

    def cancel_seat(self):
        self.seats += 1 #adding the seats by 1 coz cancel

        def __str__(self):
            return f"{self.title} (Seats left: {self.seats})"

class BookSystem:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie):
        self.movies[movie.title] = movie

    def book_seat(self, title):
        if title in self.movies:
            if self.movies[title].book_seat():
                print(f"Booked a seat for {title}.")
            else:
                print(f"Sorry, {title} is fully booked.")
        else:
            print(f'Movie {title} is not found.')
    
    def cancel_booking(self, title):
        if title in self.movies:
            self.movies[title].cancel_seat()
            print(f'Cancelled 1 booking for  {title}. Seat restored.')
        else:
            print(f"Movie {title} is not found.")
    
    def available_movies(self):
        print("\nAvailable movies with seats left:")
        for movie in self.movies.values():
            if movie.seats > 0:
                print(movie)


system = BookSystem()

#adding the movies
system.add_movie(Movie('Avengers', 1))
system.add_movie(Movie('Justice League', 2))
system.add_movie(Movie('New Avengers', 3))
system.add_movie(Movie('Batman', 4))

#booking seats for different movies
system.book_seat('Avengers')
system.book_seat('New Avengers')
system.book_seat('Justice League')
system.book_seat('New Avengers')
system.book_seat('Batman')

#cancels booking for movie New Avengers
system.cancel_booking('New Avengers')

#shows the available movie
system.available_movies()