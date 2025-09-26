movie_list = ["No country for old men", "Underworld", "Alien"]

while True:
    new_movie = input("Add a movie to the list (or type 'Stop' to finish): ")

    if new_movie.lower() == "stop":
        break

    movie_list.append(new_movie)


print("\nFinal movie list:")
for index, movie in enumerate(movie_list):
    print(index, movie)


