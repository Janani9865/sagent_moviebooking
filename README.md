from datetime import datetime
#user data class
class usersdata:
    #emptylist 
    users=[]
    #constructor for initializing the userdata
    def __init__(self, user_id:int, user_name:str, mail_id:str, phn_no:str, password:str):
        self.user_id = user_id
        self.user_name = user_name
        self.mail_id = mail_id
        self.phn_no = phn_no
        self.password = password
        
        
#user functionality class
class userfunctionality:
    # method overloading because the validate function only doing both the function of signup and login
    def validate_user(self,mail_id,password=None):
        registered_mail_id = [user.mail_id for user in usersdata.users if user.mail_id == mail_id]
        
        if not registered_mail_id and password == None:
            #if not registered mail_id and no password provided return true
            return True
        else:
            verified_password = [user.password for user in usersdata.users if user.password==password]
            if registered_mail_id and verified_password:
                return True
            
    #user signup function
    def signup(self):
        #user signup function
        user_id= (usersdata.users[-1].user_id)+1
        user_name = input("Enter the user name: \n").lower()
        mail_id = input("Enter the mail_id : \n").lower()
        phn_no = input("Enter the phn_no :\n")
        password = input("Enter the password :\n")
        
        if self.validate_user(mail_id):
            new_data=usersdata(user_id,user_name,mail_id,phn_no,password)
            usersdata.users.append(new_data)
            return mail_id
    
        
    def login(self):
        #user login function
        input_id = input("Enter the registered mail_id : \n").lower()
        input_password = input("\nEnter the input_password : \n")
        
        if self.validate_user(input_id,input_password):
            return input_id
    
#movie data class
class moviesdata:
    movies=[]
    def __init__(self, movie_id:int, movie_name:str, duration:str, rating:float):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.duration = duration
        self.rating = rating
        
#movie functionaloity class
class moviefunctionality:
    def display_info(self):
        #display the available movies
        print("----------------------------------------------------\n")
        for movie in moviesdata.movies:
            print(movie.movie_id,'\t',movie.movie_name,'\t',movie.duration,'\t',movie.rating)
        
    def select_movie(self):
        #select a movie based on input
        print("-----------------------------------------------------\n")
        movie_id = int(input("Enter the movie id : \n"))
        for movie in moviesdata.movies:
            if movie.movie_id==movie_id:
                return movie.movie_name
            
#theatres data class
class theatresdata():
    theatres=[]
    def __init__(self, theatre_id:int, theatre_name:str, location:str, rating:float, movies:list, show_time):
        self.theatre_id = theatre_id
        self.theatre_name = theatre_name
        self.location = location
        self.rating = rating
        self.movies = movies
        self.show_time = show_time
        
#theatres functionality class
class theatresfunctionality():
    def display_info(self,movie):
        print("-----------------------------------------------------\n")
        for theatre in theatresdata.theatres:
            if movie in theatre.movies:
                print(theatre.theatre_id,'\t',theatre.theatre_name,'\t',theatre.location,'\t',theatre.rating)
    
    def select_theatre(self,selected_movie):
        theatre_id = int(input("Enter the theatre id :\n"))
        for theatre in theatresdata.theatres:
            if theatre.theatre_id == theatre_id and selected_movie in theatre.movies:
                return theatre.theatre_name
            
    def display_showtime(self,selected_theatre):
        print("-----------------------------------------------------\n")
        for theatre in theatresdata.theatres:
            if theatre.theatre_name == selected_theatre:
                [print(key,value)for key,value in theatre.show_time.items()]
            return[theatre.show_id for theatre in theatresdata.theatres if theatre.theatre_name==selected_theatre]
        
    def select_showtime(self,selected_theatre):
        print("-------------------------------------------------------\n")
        show_time = self.display_show_time(selected_theatre)
        show_id = int(input("Enter the show id : \n"))
        if show_id>0 and show_id<=4:
            return show_time[0][show_id]
        
class seatsdata(): 
    seats_datas=[]
    def __init__(self,theatre_name,show_time):
        self.theatre_name = theatre_name
        self.show_time = show_time
        self.seats = [["A1" "A2" "A3" "A4" "A5"
                      "B1" "B2" "B3" "B4" "B5"
                      "C1" "C2" "C3" "C4" "C5"
                      "D1" "D2" "D3" "D4" "D5"]]
        
class seatfunctionality():
    def display_seats(self,theatre_name,show_time):
        required_seats = [seat_details.seats for seat_details in seatsdata.seats_datas if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time]
        if required_seats==[]:
            new_seat = seatsdata(theatre_name,show_time)
            seatsdata.seats_datas.append(new_seat)
            self.display_seats(theatre_name,show_time)
        
        else:
            for seat_details in seatsdata.seats_datas:
                if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time:
                    for rows in seat_details.seats:
                        print(*rows)
    def select_seats(self,theatre_name,show_time):
        selected_seats=[]
        required_seats = [seat_details.seats for seat_details in seatsdata.seats_datas if seat_details.theatre_name == theatre_name and seat_details.show_time == show_time]
        requested_seats=input("Enter the seats as space separated (Ex: A1 A2): \n").upper().split(' ')
        for rows in required_seats[0]:
            for seats in rows:
                if seats in requested_seats:
                    selected_seats.append(seats)
    
        if len(selected_seats)==len(required_seats):
            for row in selected_seats:
                for i in range(len(row)):
                    if row[i] in selected_seats:
                        row[i]='0 '
            return selected_seats
                               
class bookingsdata():
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
        
class bookingfunctionality():
    def booking_preview(self,mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price):
        print("------------------------------------------------------\n")
        print("Booking preview")
        print("------------------------------------------------- ----\n")
        print(f'movie details: {selected_movie}')
        print(f'theatre details: {selected_theatre}')
        print(f'show_details: {selected_show_time}')
        print(f'seat details: {selected_seats}')
        print(f'price_details : {total_price}')
        print("        ----------------------------------------------\n")
        payment_choice = int(input("Enter a payment choice:\n1.Card \n2.UPI"))
        if payment_choice!=1 and payment_choice!=2:
            print("Invalid choice")
            return False
        
        if payment_choice==1:
            payment_mode = "card"
            print("Booked Successfully")
        elif payment_choice ==2:
            payment_mode = "UPI"
            print("Booked Successfully")
        booked_time = datetime.now().strftime("%d/%m/%y,%h:%m:%s")
        new_booking = bookingsdata(mail_id,selected_movie,selected_theatre,selected_show_time,selected_seats,total_price,payment_mode,booked_time)
        bookingsdata.bookings.append(new_booking)
        return True
    
    def display_history(self):
        if len(bookingsdata.bookings)==0:
            print("Booking history is Empty")
        
        else:
            print("----------------------------------------\n")
            for booking in bookingsdata.bookings:
                print(booking.movie,booking.theatre,booking.show_time,booking.seats,booking.price,booking.payment_mode,booking.booked_time, sep=' -- ')
                      
    def delete_history(self):
        if len(bookingsdata.bookings)==0:
            print("Booking history is Empty")       
        else:
            del(bookingsdata.bookings[-1])
            print("The lastbooking history has been deleted")
            choice = input("Do you want to clear all (yes/no: \n)").lower()
            if choice=='y':
                bookingsdata.bookings.clear()
                print("The booking history has been deleted")
            else:
                print("Invalid Input")
                
                
class moviebookingsystem():
    def __init__(self):
        self.user = userfunctionality()
        self.movie = moviefunctionality()
        self.theatre = theatresfunctionality()
        self.seats = seatfunctionality()
        self.booking = bookingfunctionality()
        self.stay_in = True
        self.mail_id = None
    
    def signup_or_login(self):
        choice= input("Enter your choice(Login/Signup): \n").title()
        
        if choice == 'Signup':
            self.mail_id = self.user.signup()
            if not self.mail_id:
                print("User already exists")  
                self.stay_in = False
        
        elif choice == 'Login':
            self.mail_id = self.user.login()
            if not self.mail_id :
                print("Invalid mail_id or password!\n")
                self.stay_in = False      
       
    def run(self):
        #mail loop for movie booking system
        while self.stay_in:
            print("----------------------------------------------------")
            print("Menu : ")
            print("1. Book Movie")
            print("2. Display Booking history")
            print("3. Delete Booking history")
            print("4. Logout")
            choice = int(input("\nEnter your choice: \n"))
            
            if choice == 1:
                self.book_movie()
            elif choice == 2:
                self.display_booking_history()
            elif choice == 3:
                self.delete_booking_history()
            elif choice == 4:
                self.logout()
            else:
                print("INVALID CHOICE")
    
    def book_movie(self):
        self.movie.display_info()
        selected_movie = self.movie.select_movie()
        if not selected_movie:
            print("Invalid movie id")
            return
        
        self.theatre.display_info(selected_movie)
        selected_theatre = self.theatre.select_theatre(selected_movie)
        if not selected_theatre:
            print("Invalid theatre id")
            return
        
        select_show_time = self.theatre.select_showtime(selected_theatre)
        if not select_show_time:
            print("Invalid show id")
            return
        
        selected_seat = self.seats.select_seat(selected_theatre,select_show_time)
        if not selected_seat:
            print("Invalid seat selection")
            return
        
        total_price =len(selected_seat)*600
        if not self.booking.booking_preview(self.mail_id,selected_movie,selected_theatre,select_show_time,selected_seat,total_price):
            self.stay_in = False
    
    def display_booking_history(self):
        self.booking.display_history()
    
    def delete_booking_history(self):
        self.booking.delete_history()
        
    def logout(self):
        print("Logout Succesffully")
        self.stay_in = False
         
#Initializing the sample data
if __name__ == "__main__":
    user1=usersdata(1, 'janz','jananihari98@gmail.com','9865214328','janz9865')
    user2=usersdata(2,'kavz','kaviya79@gmail.com','7904203106','kavz7904')
    user3=usersdata(3,'hari','hari96@gmail.com','9698578016','hari9698')
    usersdata.users.append(user1)
    usersdata.users.append(user2)
    usersdata.users.append(user3)
    
    movie1=moviesdata(1,'Joe           ','2h 27mins',9.5)
    movie2=moviesdata(2,'Captain miller','3h 15mins',8.3)
    movie3=moviesdata(3,'Ayalan        ','3h 5mins ',9.3)
    moviesdata.movies.append(movie1)
    moviesdata.movies.append(movie2)
    moviesdata.movies.append(movie3)
    
    theatre1=theatresdata(1,'Thangam cinemas','pollachi',9.0,['Ayalan','Joe'],{1:'10:00am',2:'2:00pm',3:'4:30pm',4:'7:00pm'})
    theatre2=theatresdata(2,'Durais','pollachi',8.5,['Ayalan','Captain miller'],{1:'10:00am',2:'2:00pm',3:'4:30pm',4:'7:00pm'})
    theatre3=theatresdata(3,'Nallappa','pollachi',7.0,['Captain miller','Joe'],{1:'10:00am',2:'2:00pm',3:'4:30pm',4:'7:00pm'})
    theatresdata.theatres.append(theatre1)
    theatresdata.theatres.append(theatre2)
    theatresdata.theatres.append(theatre3)
    
    booking_system=moviebookingsystem()
    booking_system.signup_or_login()
    booking_system.run()
