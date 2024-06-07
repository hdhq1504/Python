import pandas as pd

movies = {
    'Name' : ['Harry Potter and The Philosopher\'s Stone', 'Dune: Part Two', 'Black Panther', 'Oppenheimer', 'Avengers: End Game', 'Interstellar', 'The Dark Knight'],
    'Genre' : ['Adventure', 'Science Fiction', 'Action', 'Drama', 'Adventure', 'Science Fiction', 'Action'],
    'Length': [152, 167, 135, 181, 181, 169, 152],
    'Year' : [2001, 2024, 2018, 2023, 2019, 2014, 2008]
}

df = pd.DataFrame(movies)

# Hàm lọc phim theo thể loại và năm
def recommend_movies(genre, year = None):
    if year:
        movie = df[(df['Genre'].str.lower() == genre.lower()) & (df['Year'] == year)]
    else:
        movie = df[df['Genre'].str.lower() == genre.lower()]
    return movie

# Khởi động chatbot
print("Hi! How are you today?")
mood = input()

if mood.lower() in ["fine", "good", "great", "okay"]:
    print("That's great! Which type of genres do you want to watch?")
    genre = input()
    
    print("Do you have a specific year in mind? If yes, please enter the year (e.g., 2018), or type 'any' for any year.")
    year_input = input()
    
    if year_input.lower() == "any":
        recommended_movies = recommend_movies(genre)
    else:
        try:
            year = int(year_input)
            recommended_movies = recommend_movies(genre, year)
        except ValueError:
            print("Invalid year input. Please enter a valid year.")
            recommended_movies = pd.DataFrame()

    if not recommended_movies.empty:
        print(f"Here are some {genre} movies you might like:")
        for _, movie in recommended_movies.iterrows():
            print(f"- {movie['Name']} ({movie['Year']})")
    else:
        print(f"Sorry, I don't have any {genre} movies for the year {year_input} to recommend right now.")
else:
    print("I hope you feel better soon! If you want to talk about movies, I'm here.")