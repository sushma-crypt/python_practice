current_movies = {'Caption Of America':'11.00am',
                  'FRIENDS':'1.00pam',
                  'Center of earth':'3.00pm',
                  'spider man':'5.00pm'}

print("We are showing the following movies:")
for key in current_movies:
    print(key)                  

movie = input('What movie would you like the showtime for?\n')                  

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, 'is playing at', showtime)    