movies = [
    ["Harry Potter and The Philosopher's Stone", "Adventure", 152, 2001],
    ["Dune: Part Two", "Science Fiction", 167, 2024],
    ["Black Panther", "Action", 135, 2018],
    ["Oppenheimer", "Drama", 181, 2023],
    ["Avengers: End Game", "Adventure", 181, 2019],
    ["Interstellar", "Science Fiction", 169, 2014],
    ["The Dark Knight", "Action", 152, 2008]
]

# Hàm lọc phim theo thể loại và năm
def recommend_movies(genre, year):
    return [movie for movie in movies if movie[1].lower() == genre.lower() and movie[3] == year]

# Khởi động chatbot
print("Hi! I'm your AI chatbot.")
print("How are you today?")
mood = input()

if mood.lower() in ["fine", "good", "great", "okay"]:
    print("That's great! Which type of genres do you want to watch?")
    genre = input()
    
    print("Do you have a specific year in mind? If yes, please enter the year (e.g., 2018), or type 'any' for any year.")
    year_input = input()
    
    if year_input.lower() == "any":
        recommended_movies = [movie for movie in movies if movie[1].lower() == genre.lower()]
    else:
        try:
            year = int(year_input)
            recommended_movies = recommend_movies(genre, year)
        except ValueError:
            print("Invalid year input. Please enter a valid year.")
            recommended_movies = []

    if recommended_movies:
        print(f"Here are some {genre} movies you might like:")
        for movie in recommended_movies:
            print(f"- {movie[0]} ({movie[3]})")
    else:
        print(f"Sorry, I don't have any {genre} movies for the year {year_input} to recommend right now.")
else:
    print("I hope you feel better soon! If you want to talk about movies, I'm here.")