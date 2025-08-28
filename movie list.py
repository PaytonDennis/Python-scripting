movie_list = ["No country for old me","Underworld","Alien"]

for index, movie in enumerate(movie_list):
    print(enumerate(movie_list))


for index, movie in range(3):
  new_movie = input("Add a movie to the list")
  movie_list.append(new_movie)
  print(enumerate(movie_list))
