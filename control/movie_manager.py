import os


def list_movies(location):
    mylocations = []
    for file_location in os.listdir(location):
        if is_movie_type(file_location):
            mylocations += [file_location]
    return mylocations


def is_movie_type(location):
    potential_files = os.listdir(location)
    if not potential_files:
        return False
    return True