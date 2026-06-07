movies = {
    "Inception": 9,
    "Interstellar": 10,
    "Avatar": 8,
    "The Dark Knight": 10,
    "Titanic": 7
}

average_rating = sum(movies.values()) / len(movies)

highest_rating = max(movies.values())

top_movies = []

for movie, rating in movies.items():
    if rating == highest_rating:
        top_movies.append(movie)

print("Average Rating:", round(average_rating, 2))
print("Highest Rating:", highest_rating)
print("Top Rated Movies:", top_movies)



Average Rating: 8.8
Highest Rating: 10
Top Rated Movies: ['Interstellar', 'The Dark Knight']