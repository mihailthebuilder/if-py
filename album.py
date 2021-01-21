"""Function exercise"""


def make_album(artist, album, tracks_num=0):
    """returns a music album in a dictionary"""
    dict = {"artist": artist.title(), "album": album.title()}

    if tracks_num >= 50:
        print("come on, that's too many albums")
    elif tracks_num >= 1:
        dict["tracks_num"] = tracks_num

    return dict


print(make_album("kenny", "rogers on a bum", 100))
print(make_album("kenny", "boi on a cob", 20))
print(make_album("jonny", "on the spot"))
