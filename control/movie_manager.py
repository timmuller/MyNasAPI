import os
import logging


def list_movies(location):
    mylocations = []
    for file_location in os.listdir(location):
        full_file_location = os.path.join(location, file_location)
        if is_movie_type(full_file_location):
            logging.debug("%s is a movie, save for future process" % full_file_location)
            mylocations += [full_file_location]
    return mylocations


def is_movie_type(location):
    try:
        potential_files = os.listdir(location)
    except OSError:
        potential_files = []

    if not potential_files:
        return False
    return True