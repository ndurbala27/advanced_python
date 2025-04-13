# Durbala, Nate CPT
# Exercise 3
# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.

def make_album(artist_name, album_title):
    """Take in artist name and album title,
    build a dictionary describing a music album containing the two values"""
    # the value of artist_name is stored with the key 'artist',
    # the value of album_title is stored with the key 'title'
    album = {'artist': artist_name,
             'title' : album_title}

    # the entire dictionary representing an album is returned
    return  album

album1 = make_album('five finger death punch', 'got your six')
album2 = make_album('five finger death punch', 'war is the answer')
album3 = make_album('five finger death punch', 'american capitalist')

# the return value is printed with the two pieces of textual information
print(album1)
print(album2)
print(album3)
