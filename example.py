#!/usr/bin/python

import logging
from control import movie_manager

logging.basicConfig(level=logging.INFO)

for movie in movie_manager.list_movies('/share/MD0_DATA/Multimedia/Films/Films/'):
    print movie
