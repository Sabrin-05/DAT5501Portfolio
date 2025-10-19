'''Using an old project to implement unit testing techniques learnt at the start of DAT5501 module

What is this project:
A Movies/TVShows collection manager that has the ability to view collection items, both individually and in bulk.
This project gives the user the ability to add additional items, remove them, and edit information about the item.'''



class Watch_list:
    def __init__(self,movies_list=[],shows_list=[]):
        self.movies_list = movies_list
        self.shows_list = shows_list 
        self.genre = ["Action", "Comedy", "Horror", "Thriller"]
        self.watch_status = ["Complete", "Incomplete"]
    
    def add_movie(self, name,length, genre, actors, ratings, watch_status):
        #method adds a movie to the list when user enters all attributes
        movie = Movies(name,length, genre, actors, ratings, watch_status)
        self.movies_list.append(movie) #.append() adds movie to the end of the list
        
    def add_show(self, name, genre, no_seasons, no_episodes, actors, ratings,watch_status):
        #method adds a show to the list when user enters all attributes
        show = Series(name, genre, no_seasons, no_episodes, actors, ratings,watch_status)
        self.shows_list.append(show) #.append() adds show to the end of the list
        
    def remove_movie(self, name):
        #method removes a movie from the movie list once user enters name
        found = False
        for movie in self.movies_list:
            if movie.getName().lower() == name.lower():       #case insensitive
                #loops through names within the list to find a match
                self.movies_list.remove(movie)
                found = True
                print(f"{movie.getName()} has been removed from watchlist")
                break
            if not found:    
                print(f"{movie.getName()} has not been found in watchlist")
        
        
    def remove_show(self, name):
        #method removes a show from the show list once user enters name
        found = False
        for show in self.shows_list:
            if show.getName().lower() == name.lower():       #case insensitive
                #loops through names within the list to find a match
                self.shows_list.remove(show)
                found = True
                print(f"{show.getName()} has been removed from watchlist")
                break
        if not found:
            print(f"{show.getName()} has not been found in watchlist")
                
            
        
    def edit_movie(self):
        #method finds and edits an attribute of the users choice in the movies_list
        for index, movie in enumerate(self.movies_list):
            #loop through list and gives all the movies a number
            print(f"{index}. {movie.getName()}")

        movie_selected = int(input("Enter the number of the movie you'd like to edit"))    #allows user to select a specific movie to edit
        if movie_selected < 0 or movie_selected > len(self.movies_list) - 1:
            #stops user from selecting a number that's not in the list
            print("Invalid choice. Please choice from the numbers above:")
        else:
            print("Selecting movie to edit now")

        edit_mode = input("Select field to edit: name, genre, watch status, ratings, length")
        if edit_mode == "name":
            edit_name = input(f"Please enter new name for {movie.getName()}")
            self.movies_list[movie_selected].updateName(edit_name)     #updates with a new name given by the user 
            print("Name of movie has been updated")
            
        elif edit_mode == "genre":
            edit_genre = input(f"Please enter new genre for {movie.getGenre()}")
            self.movies_list[movie_selected].updateGenre(edit_genre)   #updates with a new genre given by the user 
            print("Genre of movie has been updated")
            
        elif edit_mode == "watch status":
            edit_watch_status = input(f"Please enter new watch status for {movie.getWatch_status()}")
            self.movies_list[movie_selected].updateWatch_status(edit_watch_status)   #updates with a new watch_status given by the user
            print("Watch status of movie has been updated")

        elif edit_mode == "ratings":
            edit_ratings = input(f"Please enter new rating for {movie.getRatings()}")
            self.movies_list[movie_selected].updateRatings(edit_ratings)   #updates with a new rating given by the user
            print("Ratings of movie has been updated")
        
        elif edit_mode == "length":
            edit_length = input(f"Please enter new length for {movie.getLength()}")
            self.movies_list[movie_selected].updateLength(edit_length)   #updates with a new length given by the user
            print("Length of movie has been updated") 
        
        else:
            print("Please select one of the above choices")

         

        
    def edit_show(self):
        #method finds and edits an attribute of the users choice in the shows_list
        for index, show in enumerate(self.shows_list):
            #loop through list and gives all the shows a number
            print(f"{index}. {show.getName()}")

        show_selected = int(input("Enter the number of the show you'd like to edit"))   #allows user to select a specific show to edit
        if show_selected < 0 or show_selected > len(self.shows_list) - 1:
            #stops user from selecting a number that's not in the list
            print("Invalid choice. Please choice from the numbers above:")
        else:
            print("Selecting show to edit now")

        edit_mode = input("Select field to edit: name, genre, watch status, ratings, no.seasons, no.episodes")
        if edit_mode == "name":
            edit_name = input(f"Please enter new name for {show.getName()}")
            self.shows_list[show_selected].updateName(edit_name)   #updates with a new name given by the user 
            print("Name of show has been updated")
            
        elif edit_mode == "genre":
            edit_genre = input(f"Please enter new genre for {show.getGenre()}")
            self.shows_list[show_selected].updateGenre(edit_genre)   #updates with a new genre given by the user 
            print("Genre of show has been updated")
            
        elif edit_mode == "watch status":
            edit_watch_status = input(f"Please enter new watch status for {show.getWatch_status()}")
            self.shows_list[show_selected].updateWatch_status(edit_watch_status)   #updates with a new watch_status given by the user
            print("Watch status of show has been updated")

        elif edit_mode == "ratings":
            edit_ratings = input(f"Please enter new rating for {show.getRatings()}")
            self.shows_list[show_selected].updateRatings(edit_ratings)   #updates with a new rating given by the user
            print("Ratings of show has been updated")
        
        elif edit_mode == "no.seasons":
            edit_no_seasons = input(f"Please enter new no.seasons for {show.getNo_seasons()}")
            self.shows_list[show_selected].updateNo_seasons(edit_no_seasons)   #updates with a new no.seasons given by the user
            print("No.seasons of show has been updated") 
        
        elif edit_mode == "no.episodes":
            edit_no_episodes = input(f"Please enter new no.episodes for {show.getNo_episodes()}")
            self.shows_list[show_selected].updateNo_episodes(edit_no_episodes)   #updates with a new no.episodes given by the user
            print("No.episodes of show has been updated")
        
        else:
            print("Please select one of the above choices")
        
        
    def search_movie(self):
        #method searches for the features that the user selects and returns the movies with matching feature
        search_mode = input("What feature would you like to search by: name, genre, watch status")
        
        if search_mode == "name":
            search_name = input("Enter name to search for:")
            found = False
            for movie in self.movies_list:      #loops through list of movies to find a matching name
                if movie.getName().lower() == search_name.lower():
                    print(f"Movie found: {movie.getName()}")
                    found = True
            if not found:
                    print("There is no movie by that name")
        
        if search_mode == "genre":
            search_genre = input("Enter genre to search for:")
            found = False
            for movie in self.movies_list:    #loops through list of movies to find a matching genre
                if movie.getGenre().lower() == search_genre.lower():
                    print(f"Movie found: {movie.getGenre()}")
                    found = True
            if not found:
                    print("There is no show with that genre:")
        
        if search_mode == "watch_status":
            search_watch_status = input("Enter a status to search for:")
            found = False
            for movie in self.movies_list:     #loops through list of movies to find a matching watch_status
                if movie.getWatch_status().lower() == search_watch_status.lower():
                    print(f"Movie found {movie.getWatch_status()}")
                    found = True
            if not found:
                    print("There is no movie with that status")
        
        if search_mode == "length":
            search_length = input("Enter a length to search for:")
            found = False
            for movie in self.movies_list:    #loops through list of movies to find a matching length
                if movie.getLength.lower() == search_length.lower():
                    print(f"Movie found: {movie.getLength()}")
                    found = True
            if not found:
                    print("There is no movie with that length")
                    

    def display_movies(self):
        #method displays all the movies within the list with all its attributes
        if not self.movies_list:
            print("No movies in the watch list")
        else:
            for movie in self.movies_list:     #loops through list and display name,genre etc.
                print(f"Name: {movie.getName()}")
                print(f"Genre: {movie.getGenre()}")
                print(f"Actors: {movie.getActors()}")
                print(f"Rating: {movie.getRatings()}")
                print(f"Watch Status: {movie.getWatch_status()}")
                print(f"Length: {movie.getLength()}")
        
            
    def display_shows(self):
        #method displays all the shows within the list with all its attributes
        if not self.shows_list:
            print("No shows in the watch list")
        else:
            for show in self.shows_list:        #loops through list and display name,genre etc.
                print(f"Name: {show.getName()}")
                print(f"Genre: {show.getGenre()}")
                print(f"Actors: {show.getActors()}")
                print(f"Rating: {show.getRatings()}")
                print(f"Watch Status: {show.getWatch_status()}")
                print(f"No. seasons: {show.getNo_seasons()}")
                print(f"No. episodes: {show.getNo_episodes()}")
        

    def display_all(self):
        #method displays both the movies and shows in the list by calling two previous methods
        self.display_movies()
        self.display_shows()
    
    def summary_statistics(self):
        #method finds all movies and shows with the same feature and adds them up
        genres = {}
        watch_status ={}
        ratings = {}
        
        
        for movie in self.movies_list:
            #loops through the movies to add up same movies with genres,watch_status,rating
            genre = movie.getGenre
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
            

            watch_status = movie.getWatch_status
            if status in watch_status:
                watch_status[status] += 1
            else:
                watch_status[status] = 1
            
            ratings = movie.getRatings
            if rating in ratings:
                watch_status[status] += 1
            else:
                watch_status[status] = 1
        
        for show in self.shows_list:
            #loops through the shows to add up same shows with genres,watch_status,rating
            genre = show.getGenre
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
            

            watch_status = show.getWatch_status
            if status in watch_status:
                watch_status[status] += 1
            else:
                watch_status[status] = 1
            
            ratings = show.getRatings
            if rating in ratings:
                watch_status[status] += 1
            else:
                watch_status[status] = 1
        
        print("Summary count for genres (Movies and Shows):")
        for genre, count in genres.items():
            print(f"Genres: {count}")
        
        print("Summary count for ratings (Movies and Shows):")
        for rating, count in ratings.items():
            print(f"Ratings: {count}")    
        
        print("Summary count for genres (Movies and Shows):")
        for status, count in watch_status.items():
            print(f"Watch Status: {count}")



            

class Media:
    def __init__(self, name, genre, actors, ratings, watch_status):
        self.name = name
        self.genre = genre
        self.actors = actors
        self.ratings = ratings
        self.watch_status = watch_status

    def getName(self):
        return self.name

    def updateName(self,new_name):
        self.name = new_name

    def getGenre(self):
        return self.genre

    def updateGenre(self,new_genre):
        self.genre = new_genre

    def getActors(self):
        return self.actors

    def updateActors(self,new_actors):
        self.actors = new_actors

    def getRatings(self):
        return self.ratings

    def updateRatings(self,new_ratings):
        self.genre = new_ratings

    def getWatch_status(self):
        return self.watch_status
    
    def updateWatch_status(self,new_watch_status):
        self.watch_status = new_watch_status
        
class Movies(Media):
    def __init__(self, name, length, genre, actors, ratings, watch_status):
        super().__init__(name, genre, actors, ratings, watch_status)
        self.length = length

    def getLength(self):
        return self.length

    def updateLength(self,new_length):
        self.length = new_length

class Series(Media):
    def __init__(self, name, genre, no_seasons, no_episodes, actors, ratings,watch_status):
        super().__init__(name, genre, actors, ratings, watch_status)
        self.no_seasons = no_seasons
        self.no_episodes = no_episodes

    def getNo_seasons(self):
        return self.no_seasons

    def updateNo_seasons(self,new_no_seasons):
        self.no_seasons = new_no_seasons

    def getNo_episodes(self):
        return self.no_episodes

    def updateNo_episodes(self,new_no_episodes):
        self.no_episodes = new_no_episodes



import csv

def load_data(watch_list, data_path):
    #loads csv containing a users current watchlist
    filename = data_path
    with open(filename, mode='r', newline ='', encoding= 'utf-8') as my_csvfile:
        watchlist_data = csv.DictReader(my_csvfile)
        for row in watchlist_data:
            if row['Media(Type)'].lower() == 'Movie'.lower():
                name = row['Name'].lower()
                genre = row['Genre'].lower()
                actors = row['Actors'].split(',').lower()
                watch_status = row['Watch Status'].lower()
                ratings = row['Ratings']
                length = row['Length']

                watch_list.add_movie(name,genre,actors,watch_status,ratings,length)       #adds the movies in the csv to the watchlist
            
            elif row['Media(Type)'].lower() == 'Show'.lower():
                name = row['Name'].lower()
                genre = row['Genre'].lower()
                actors = row['Actors'].split(',').lower()
                watch_status = row['Watch Status'].lower()
                ratings = row['Ratings']
                no_seasons = row['No. Seasons']
                no_episodes = row['No. Episodes']
                
                watch_list.add_show(name,genre,actors,watch_status,no_seasons,no_episodes)      #add the shows in the csv to the watchlist
                
    print("Your data has successfully been updated")

def log_in(username,password):
    #takes in a cuurent users username and password 
    #returns the pathfile with current watchlist
    #if both username and password matches
    try:
        password = password +"\n"
        
        with open("login.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                fields = line.split(",")
                if fields[0] == username and fields[1].strip() == password:
                    return fields[2]
    except Exception:
        #returns a print statement to show that something went wrong
        print(Exception)
    
    return False


def main_menu():
    watch_list = Watch_list() 
    choice = -1
    username= input("Enter your username to login")
    password = input("Enter your password to login")
    data_path = log_in(username,password)
    while choice != "9":
        print("1. Add a movie to the watchlist:")
        print("2. Add a show to the watchlist:")
        print("3. Remove movie/show in watchlist")
        print("4. Display current watchlist:")
        print("5. Edit movie/show in watclist")
        print("6. Search for movie/show in watchlist:")
        print("7. Load existing watchlist ")
        print("8. Show summary statitics")
        print("9. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Please enter name of film:")
            print("Existing genres")
            
            for genre in watch_list.genre:
                print(genre)
            genre = input("Please enter the genre from the above list")
            #to make it possible to add a genre i want to have an add option 
            # that adds genre to the watch_list.genre using append
            while genre not in watch_list.genre:
                add_genre = input("Genre not found. Would you like to add a new genre? (yes/no)")
                if add_genre.lower() == "yes":
                    watch_list.genre.append(genre)
                    print(f" New genre: {genre} has been added")
                    break
                else:
                    input("Please enter the genre from the above list")

            actors = []
            while True:
                name_actors = input(f"Enter name of actors in '{name}' (Or enter nothing to stop:)")
                if name_actors == '':
                    break
                actors.append(name_actors)   # add name of actors to the end of the list 
                print('The actors names are:')
                for name_actors in actors:
                    print('  ' + name_actors)
                    
            
            watch_status = input("Have you completed this movie? (yes/no)")
            if watch_status.lower() == "yes":
                ratings = input("Enter your rating of the movie 1-10:")
            else:
                ratings = "Not rated"    
            
            length = int(input("Enter the length of this movie"))

            watch_list.add_movie(name, length, genre, actors, ratings, watch_status)
            print(f"{name} successfully added to watch list")
                                       
            
        elif choice == "2":
            name = input("Please enter name of show:")
            print("Existing genres:")
            
            for genre in watch_list.genre:
                print(genre)
            genre = input("Please enter the genre from the above list")
            #to make it possible to add a genre i want to have an add option 
            # that adds genre to the watch_list.genre using append
            while genre not in watch_list.genre:
                add_genre = input("Genre not found. Would you like to add a new genre? (yes/no)")
                if add_genre.lower() == "yes":
                    watch_list.genre.append(genre)
                    print(f" New genre: {genre} has been added")
                else:
                    input("Please enter the genre from the above list")

            actors = []
            while True:
                name_actors = input(f"Enter name of actors in '{name}' (Or enter nothing to stop:)")
                if name_actors == '':
                    break
                actors.append(name_actors)   # list concatenation
                print("The actors names are:")
                for name_actors in actors:
                    print('  ' + name_actors)
                    
            
            watch_status = input("Have you completed this show? (yes/no)")
            if watch_status.lower() == "yes":
                ratings = input("Enter your rating of the movie 1-10:")
            else:
                ratings = "Not rated"
            
            no_seasons = int(input("Enter number of seasons:"))
            no_episodes = int(input("Enter number of seasons"))

            watch_list.add_show(name, genre, actors, ratings, watch_status, no_seasons, no_episodes)
            print(f"{name} successfully added to watch list")
        
        elif choice == "3":
            remove_option = input("1. Remove a movie \n2. Remove a show")
            if remove_option == "1":
                movie_name = input("Enter name of movie to remove")
                print(f"Removing {movie_name}:")
                watch_list.remove_movie(movie_name)
            elif remove_option == "2":
                show_name = input("Enter name of show to remove")
                print(f"Removing {show_name}:")
                watch_list.remove_show(show_name)
                break
            else:
                print("Please choose one of the above:")
            
        
        elif choice == "4":
            option = input("1. View all \n 2.View movies \n3. View shows ")
            if option == "1":
                print("Displaying all:")
                watch_list.display_all()
            elif option == "2":
                print("Displaying all movies in watch_list:")
                watch_list.display_movies()
            elif option == "3":
                print("Displaying all shows in list:")
                watch_list.display_shows()
                break
            else:
                print("Please choose one of the above:")
        
        elif choice == "5":
            edit_option = input("1. Edit a movie \n2. Edit a show ")
            if edit_option == "1":
                print("Editing a movie:")
                watch_list.edit_movie()
            elif edit_option == "2":
                print("Editing a show:")
                watch_list.edit_show()
                break
            else:
                print("Please choose one of the above options")
            
                
            
        elif choice == "6":
            option = input("1. Search for a movie \n2. Search for a show")
            if option == "1":
                print("Searching for a movie:")
                watch_list.search_movie()
            elif option == "2":
                print("Searching for a show:")
                watch_list.search_show()
                break
            else:
                print("Please choose one of the above:")
            
        elif choice == "7":
            filename = input("What would you like to call your watchlist")
            load_data(watch_list,data_path)
        
        elif choice == "8":
            watch_list.summary_statistics(genre,ratings,watch_status)
            
        elif choice == "9":
            print("Exiting the watch list....")
            break
        else:
            print("Please choose one of the above:")

main_menu()

# import pandas as pd 
# this section attempts to create an empty csv for new users to build their collection
# def create_account(username,password):
#     try:
        
#         data = []
#         username = input("Make a username to create a new account")
#         password = input("Make a password to create a new account")
    