# Durbala, Nate CPT
# Exercise 4
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album
# If the calling line includes a value for the number of tracks, add that value to the album’s dictionary.
# Make at least one new function call that includes the number of tracks on an album.

def make_album(artist_name, album_title, num_tracks=0):
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

album1 = make_album('five finger death punch', 'got your six')
album2 = make_album('five finger death punch', 'war is the answer')
album3 = make_album('five finger death punch', 'american capitalist')
album4 = make_album('five finger death punch', 'the wrong side of heaven and the righteous side of hell, volume 1 & 2', '40')


# the return value is printed with the two pieces of textual information
print(album1)
print(album2)
print(album3)
print(album4)