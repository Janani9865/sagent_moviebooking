from datetime import datetime

class usersdata:
    users=[]
    def __init__(self,user_id:int,user_name:str,mail_id:str,phn_no:str,password:str):
        self.user_id = user_id
        self.user_name = user_name
        self.mail_id = mail_id
        self.phn_no = phn_no
        self.password = password

class usersfunctionality:
    def validate_login(self,mail_id,password= None):
        registered_mailid = [user.mail_id for user in usersdata.users if user.mail_id == mail_id]
        if not registered_mailid and password == None:
            return True
        else:
            verified_password = [user.password for user in usersdata.users if user.password == password]
            if registered_mailid and password:
                return mail_id
            
    def signup(self):
        user_id = (usersdata.users[-1].user_id)+1
        user_name = input("Enter the user name :\n").lower()
        mail_id = input("Enter the mail_id: \n").lower()
        phn_no = input("Enter the phn_no :\n")
        password = input("Enter the password : \n").lower()
        if self.validate_login(mail_id):
            new_user = usersdata(user_id,user_name,mail_id,phn_no,password)
            usersdata.users.append(new_user)
            return mail_id
        
        
    def login(self):
        input_id = input("\nEnter the mail_id: \n").lower()
        password = input("\nEnter the password: \n").lower()
        if self.validate_login(input_id,password):
            return input_id

class moviesdata:
    movies=[]
    def __init__(self,movie_id:int,movie_name:str,duration:str,rating:float):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.duration = duration
        self.rating = rating
        
class moviesfunctionality:
    def display_info(self):
        print("                 MOVIES LISTS                  \n")
        print("-------------------------------------------------------\n")
        for movie in moviesdata.movies:
            print(movie.movie_id, '\t', movie.movie_name , '\t', movie.duration, '\t', movie.rating)
    
    def select_movie(self):  
        print("-------------------------------------------------------\n")
        movie_id = int(input("Enter the movie id :\n"))
        for movie in moviesdata.movies:
            if movie.movie_id == movie_id:
                return movie.movie_name

class theatresdata:
    theatres=[]
    def __init__(self,theatre_id:int,theatre_name:str,location:str,rating:float,movies:list,show_time):
        self.theatre_id = theatre_id
        self.theatre_name = theatre_name
        self.location = location
        self.rating = rating
        self.movies = movies
        self.show_time = show_time

class theatresfunctionality:
    def display_info(self, selected_movie):
        # Display information about available theatres showing a specific movie
        print("---------------------------------------------------------\n")
        for theatre in theatresdata.theatres:
            if selected_movie in theatre.movies:
                print(theatre.theatre_id, '\t', theatre.theatre_name, '\t', theatre.location, '\t', theatre.rating)
    
    def select_theatre(self,selected_movie):
        print("---------------------------------------------------------\n")
        theatre_id = int(input("Enter the theatre id : \n"))
        for theatre in theatresdata.theatres:
            if selected_movie in theatre.movies:
                return theatre.theatre_name
    
    def display_showtime(self, selected_theatre):
        print("--------------------------------------------------------\n")
        for theatre in theatresdata.theatres:
            if theatre.theatre_name == selected_theatre:
                [print(key, value) for key, value in theatre.show_time.items()]
        return [theatre.show_time for theatre in theatresdata.theatres if theatre.theatre_name == selected_theatre]

    def select_showtime(self, selected_theatre):
        show_time = self.display_showtime(selected_theatre)
        print("--------------------------------------------------------\n")
        show_id = int(input("\nEnter the Show_id:\n"))
        print("--------------------------------------------------------\n")
        if show_id > 0 and show_id <= 4: 
            return show_time[0][show_id]

class seatsdata:
    seats=[]
    def __init__(self,theatre_name,show_time):
        self.theatre_name = theatre_name
        self.show_time = show_time
        self.seats = [["A1","A2","A3","A4","A5"],
                      ["B1","B2","B3","B4","B5"],
                      ["C1","C2","C3","C4","C5"],
                      ["D1","D2","D3","D4","D5"]]

class seatsfunctionality:
    def display_seats(self,theatre_name,show_time):
        required_seats =[seat_details.seats for seat_details in seatsdata.seats if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time]
        if required_seats == []:
            new_seats = seatsdata(theatre_name,show_time)
            seatsdata.seats.append(new_seats)
            self.display_seats(theatre_name,show_time)
        
        else:
            for seat_details in seatsdata.seats:
                if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time:
                    for rows in seat_details.seats:
                        print(*rows)
                        
    def select_seats(self,theatre_name,show_time):
        self.display_seats(theatre_name,show_time)
        required_seats = [seat_details.seats for seat_details in seatsdata.seats if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time]
        requested_seats = input("\nEnter the seats as space separated (A1.A2,B1):\n").upper().split(' ')
        selected_seats=[]
        for rows in required_seats[0]:
            for seat in rows:
                if seat in requested_seats:
                    selected_seats.append(seat)
    
        
        if len(selected_seats) == len(requested_seats):
            for rows in required_seats[0]:
                for i in range(len(rows)):
                    if rows[i] in selected_seats:
                        rows[i]= '0 '
            return selected_seats

class bookingsdata:
    bookings=[]
    def __init__(self,mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price,payment_mode,booked_time):
        self.mail_id = mail_id
        self.movie = selected_movie
        self.theatre = selected_theatre
        self.show_time = selected_show_time
        self.seats = selected_seats
        self.price = total_price
        self.payment_mode = payment_mode
        self.booked_time = booked_time

class bookingfunctionality:
    def booking_preview(self,mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price):
        print("---------------------------------------------------\n")
        print("Booking Preview \n")
        print(f'Movie Details: {selected_movie}')
        print(f'Theatre details : {selected_theatre}')
        print(f'Show details : {selected_show_time}')
        print(f'Seats details : {selected_seats}')
        print(f'Price details : {total_price}')
        print("----------------------------------------------------\n")
        print("Payment option \n1.card\n2.UPI")
        payment_choice = int(input("\nEnter the input(card / UPI) :\n"))
        print("----------------------------------------------------\n")
        if payment_choice!=1 and payment_choice!=2:
            print("Invalid payment choie")
            return False
        else:
            if payment_choice ==1:
                payment_mode = 'card'
                print("Booked Successfully")
            elif payment_choice ==2:
                payment_mode = 'UPI'
                print('Booked Successfully')
            booked_time = datetime.now().strftime("%y/%m/%d:%H:%M:%S")
            new_booking = bookingsdata(mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price,payment_mode,booked_time)
            bookingsdata.bookings.append(new_booking)
            return True
            
    def display_history(self):
        if len(bookingsdata.bookings) == 0:
            print("Booking history is empty")
        else:
            print("---------------------------------------------------\n")
            for booking in bookingsdata.bookings:
                print(booking.movie,booking.theatre,booking.show_time,booking.seats,booking.price,booking.booked_time,sep=' -- ')
        
    def delete_history(self):
        if len(bookingsdata.bookings) == 0:
            print("Booking history is empty")
        else:
            del(bookingsdata.bookings[-1])
            print("YOUR LAST HISTORY HAS BEEN DELETED")
            choice = input("\nDo you have to clear all the history (yes/no):\n").lower()
            if choice == 'yes':
                bookingsdata.bookings.clear()
                print("\nBooking history has been deleted")
            else:
                print("Invalid input")
                                    
class moviebookingsystem:
    def __init__(self):
        self.user = usersfunctionality()
        self.movie = moviesfunctionality()
        self.theatre= theatresfunctionality()
        self.seats = seatsfunctionality()
        self.booking = bookingfunctionality()
        self.stay_in = True
        self.mail_id = None
    
    def signup_or_login(self):
        choice = input("Enter the choice(Login/Signup): \n").title()
        if choice == 'Login':
            self.mail_id= self.user.login()
            if not self.mail_id:
                print("Invalid mailid or password")
                self.stay_in = False
        
        elif choice == 'Signup':
            self.mail_id = self.user.signup()
            if not self.mail_id:
                print("User already exists")
                self.stay_in = False
    
    def run(self):
        while self.stay_in:
            print("\n---------------------------------------------------\n")
            print("                 MENU                 \n")
            print("1. Book movie ")
            print("2. Display Booking history ")
            print("3. Delete Book history ")
            print("4. Logout\n")
            print("-------------------------------------------------------\n")
            choices = int(input("Enter the choice:\n"))
            if choices == 1:
                self.book_movie()
            elif choices == 2:
                self.display_booking_history()
            elif choices == 3:
                self.delete_booking_history()
            elif choices == 4:
                self.logout()
            else:
                print("Invalid Choice")
        
    def book_movie (self):
        self.movie.display_info()
        selected_movie = self.movie.select_movie()
        if not selected_movie:
            print("Invalid movie id\n")
            return
        
        self.theatre.display_info(selected_movie)
        selected_theatre = self.theatre.select_theatre(selected_movie)
        if not selected_theatre:
            print("Invalid Theatre id")
            return
        
        selected_show_time = self.theatre.select_showtime(selected_theatre)
        if not selected_show_time:
            print("Invalid show time")
            return
        
        selected_seats = self.seats.select_seats(selected_theatre,selected_show_time)
        if not selected_seats:
            print("Invalid seat selection")
            return
        
        total_price = len(selected_seats)*200
        if not self.booking.booking_preview(self.mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price):
            self.stay_in = False
    
    def display_booking_history(self):
        self.booking.display_history()
        
    def delete_booking_history(self):
        self.booking.delete_history()
        
    def logout(self):
        print("Logout Successfully")
        self.stay_in = False
           
user1 = usersdata(1,'Janani','jananihari98@gmail.com','9865214328','janz9865')
user2 = usersdata(2,'Hari','hari12@gmail.com','9698578016','hari9698')
usersdata.users.append(user1)
usersdata.users.append(user2)

movie1 = moviesdata(1,"Ayalaan       ","2hr 30 mins",9.1)
movie2 = moviesdata(2,"Captain Miller","3hr 10 mins",8.4)
moviesdata.movies.append(movie1)
moviesdata.movies.append(movie2)

theatre1 = theatresdata(1,"Thangam cinemas","pollachi  ",9.1,['Captain Miller'],{1:'10:00am',2:'2:00pm',3:'6:00pm'})
theatre2 = theatresdata(2,"Durais cinemas ","coimbatore",8.4,['Ayalaan       '],{1:'10:30am',2:'2:30pm',3:'6:30pm'})
theatresdata.theatres.append(theatre1)
theatresdata.theatres.append(theatre2)

booking_system = moviebookingsystem()
booking_system.signup_or_login()
booking_system.run()
