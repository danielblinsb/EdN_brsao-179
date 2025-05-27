# Define the album name and year
album_name = "The Queen is dead, 1986"

# Define the tracklist
tracklist = [
    "The Queen Is Dead",
    "Frankly, Mr. Shankly",
    "I Know It's Over",
    "Never Had No One Ever",
    "Cemetry Gates",
    "Bigmouth Strikes Again",
    "The Boy with the Thorn in His Side",
    "Vicar in a Tutu",
    "There Is a Light That Never Goes Out",
    "Some Girls Are Bigger Than Others",
]

# Define the function to get the message based on the track name
def get_favorite_song_message(track_name):
    if track_name == "Bigmouth Strikes Again" or track_name == tracklist[5]:
        return "I love this one"
    elif track_name == "Some Girls Are Bigger Than Others" or track_name == tracklist[-1]:
        return "this is your favorite"
    else:
        return "it's good but listen to the album from the beginning"

# Example usage
track_name = "Bigmouth Strikes Again"  # Change this to test with different track names
message = get_favorite_song_message(track_name)

# Print the album name and the message
print(f"The name of the album is {album_name} and her favorite song is:")
print(message)

