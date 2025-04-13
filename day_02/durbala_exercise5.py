# Durbala, Nate CPT
# Exercise 5
# Start with your program from Exercise 4.
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input and
# print the dictionary that’s created.
# Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, num_tracks=''):
    """Take in artist name and album title, and an optional number of tracks
    build a dictionary describing a music album containing the three values"""
    # the value of artist_name is stored with the key 'artist',
    # the value of album_title is stored with the key 'title',
    # if num_tracks is provided, then store value with the key 'number of tracks'
    if num_tracks:
        album = {'artist': artist_name,
                 'title' : album_title,
                 'number of tracks' : num_tracks}
    else:
        album = {'artist': artist_name,
                 'title': album_title }

    # the entire dictionary representing an album is returned
    return  album


while True:
    print("\nEnter an album’s artist and title.")
    print("It's okay if you don't know the number of tracks on the album.")
    print("(enter 'q' at any time to quit)")

    artist_name = input("\nAtrist name: ")
    if artist_name == 'q':
        break

    album_title = input("\nAlbum title: ")
    if album_title == 'q':
        break

    num_tracks = input("\nNumber of tracks (optional): ")
    if num_tracks == 'q':
        break

    album_made = make_album(artist_name, album_title, num_tracks)
    print(f"\n{album_made}")