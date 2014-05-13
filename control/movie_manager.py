import os
import logging


def list_movies(location):
    my_movies = []
    for file_location in os.listdir(location):
        full_file_location = os.path.join(location, file_location)
        if is_movie_type(full_file_location):
            logging.debug("%s is a movie, save for future process" % full_file_location)
            my_movies += [Movie(full_file_location)]
    return my_movies


def is_movie_type(location):
    try:
        potential_files = os.listdir(location)
    except OSError:
        potential_files = []

    if not potential_files:
        return False
    return True

class Movie(object):
    def __init__(self, location):
        self.absolute_location = location

    def foldername(self):
        return os.path.basename(self.absolute_location)

    def __repr__(self):
        return self.foldername()
    
    def __str__(self):
        return self.foldername()