# 1. User wants to store movies in a list
# 2. User wants to be able to view movie list
# 3. User wants to be able to search for a movie in the list by its title
# Decide where to store movies in code
# Decide what data we want to store for each movie
# SHow the user a menu and let them pick an option
# Implement each requirement in turn, each as a seperate function
# Stop running the program when the type 'qq in the menu
user_selection = ''
movies = []

while user_selection != 'q':
    user_selection = input( f"1. Add movie to list \n2. View movie list \n3. Search for a movie \n'q' to exit" )
    if user_selection == '1':
        movie_name = input("enter the movie name you would like to add")
        movie_director = input("enter the movie director")
        movie_year = input("enter the movie year")
        movies.append({
            'movie_name': movie_name,
            'movie_director': movie_director,
            'movie_year': movie_year,
        })
    elif user_selection == '2':
        for x in movies:
            print(x)
    elif user_selection == '3':
        movie_search = input("enter the name of the movie you want to search")
        for t in movies:
            if t['movie_name'] == movie_search:
                print(t)
            else:
                print("could not find movie in movie list")


