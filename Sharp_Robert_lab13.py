# Sharp, Robert zoom meeting, video

def main():
    songs_added = ['Capo', 'Irregular', 'The Yard']
    try:
        #Using 'a' to append p.291
        outfile = open("songs.txt", 'a')
        for song in songs_added:
            outfile.write(song + "\n")
#using except and IOerror clause p.327-329
    except IOError:
        return False
    except Exception:
        return True

    results = songs_added
    #printing results with the if/else
    if results:
        print("These songs were added to the file:", songs_added)
    else:
        print("Songs were not added to the file.")

main()

