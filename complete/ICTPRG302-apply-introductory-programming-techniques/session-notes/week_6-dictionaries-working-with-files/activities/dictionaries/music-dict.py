# ### Activity 2: Music Dictionary
# **Objective:** Create a dictionary of artists and their popular songs and write a program to interact with this dictionary.

# **Instructions:**
# 1. Start by creating a dictionary.
# 2. Add five musicians and their popular songs.
# 3. Write a function that takes an artist's name as input and prints their popular song.
# 4. Write a function to add a new artist and their song to the dictionary.
# 5. Write a function to remove an artist from the dictionary.
# 6. Write a function to print ALL the artists in the dictionary.

# **Include:**
# * {}
# * []
# * print()
# * def
# * if
# * else

# **Task:**  
# Run the code to see the output and test the program by adding and removing different items to see how it behaves. Happy coding! 😊

def inital_dict():
    music_dict = {
        'Taylor Swift': 'Shake it Off',
        'Ed Sheeran': 'Gallway Grill',
        'Adele': 'Rollin\' in the deep',
        'Billie Eilish': 'Bellyache',
        'Drake': 'Crew Love'
        }
    return music_dict

def print_popular_song(music_dict):
        artist = input("Please enter the name of an artist to See their song: ").title().strip()
        while True:
            if artist in music_dict:                        
                print(f"A popular song from {artist} is {music_dict[artist]}")
                break
            else:
                artist = input("That artist isn't included, please choose another: ").title().strip()

def print_music_dict(music_dict):
    print_style = input("Would you like to see a list of artists, songs or both (artists / songs / both)? ").lower()
    while True:
        if print_style == 'both':
            print("Music Dictionary:")
            for key, value in music_dict.items():
                print(f"Artist: {key.strip()}, Song: {value}")
            break
        elif print_style == 'artists':
            print("\n\nArtists:")
            for key, value in music_dict.items():
                print(key.strip())  
            break
        elif print_style == 'songs':
            print("\n\nPopular Songs:")
            for key, value in music_dict.items():
                print(value)  
            break
        else:
            print_style = input("Please enter 'artists', 'songs' or 'both': ").lower()


def add_artist_song(music_dict):
    while True:
        artist = input("Please enter the name of an artist to add or edit: ").title().strip()
        if artist == '':
            break
        elif artist in music_dict:
            print(f"{artist} is already in the dictionary, most popular song is {music_dict[artist].strip()}")
            song = input("What would you like their new popular song to be? ").title().strip()
            music_dict[artist] = song
            print(f"{artist}'s new most popular song is {music_dict[artist].strip()}")
            break
        else:
            print(f"{artist} is new to the dictionary", end=', ') 
            song = input(" What is their most popular song? ")
            music_dict[artist] = song
            print(f"{artist}'s new most popular song is {music_dict[artist].strip()}")
            break

def remove_artist_song(music_dict):
    artist = input("Please choose an artist to remove a song from: ").title().strip()
    while True:
        if artist == '':
            break
        elif artist in music_dict:
            del(music_dict[artist])
            print(f"{artist.title()} has been removed from the dictionry.")
            break
        else:
            artist = input("That artist does not exist in the dictionary, please cheeose another: ").title().strip()


### Main
music_dict = inital_dict()

print_music_dict(music_dict)

print_popular_song(music_dict)

add_artist_song(music_dict)

print_music_dict(music_dict)

remove_artist_song(music_dict)

print_music_dict(music_dict)

# **Output:**
# ```
# A popular song by Taylor Swift is: Shake it Off
# Bruno Mars has been added to the dictionary with the song: Uptown Funk
# Drake has beem removed from the dictionary.
# Artists in the Dictionary:
# Taylor Swift
# Ed Sheeran
# Adele
# Billie Eilish
# Bruno Mars
# ```

# **Discussion question:**  
# How would you modify the program to handle multiple popular songs for each artist?
# Make the value for each artist a list instead of a string.

