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
        show_id = int(input("\nEnter the Show_id:\n"))
        print("--------------------------------------------------------\n")
        if show_id > 0 and show_id <= 4: 
            return show_time[0][show_id]

class moviebookingsystem:
    def __init__(self):
        self.user = usersfunctionality()
        self.movie = moviesfunctionality()
        self.theatre= theatresfunctionality()
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
            print("---------------------------------------------------\n")
            print("1. Book movie ")
            print("2. Display Booking history ")
            print("3. Delete Book history ")
            print("4. Logout\n")
            choices = int(input("Enter the choice:\n"))
            if choices == 1:
                self.book_movie()
            elif choices == 2:
                self.display_booking_history
            elif choices == 3:
                self.delete_booking_history
            elif choices == 4:
                self.logout
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



