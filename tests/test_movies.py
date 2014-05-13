from unittest import TestCase
import mock
from control import movie_manager


class BaseTestCase(TestCase):
    def setUp(self):
        self.active_patchers = []

    def tearDown(self):
        for patcher in self.active_patchers:
            patcher.stop()

    def setup_patch(self, to_patch):
        patcher = mock.patch(to_patch)
        self.active_patchers.append(patcher)
        return patcher.start()


class TestListAllMovies(BaseTestCase):
    def setUp(self):
        super(TestListAllMovies, self).setUp()
        self.mock_listdir = self.setup_patch('os.listdir')
        self.mock_listdir.return_value = []

    def test_that_list_all_movies_returns_all_valid_movies(self):
        self.mock_listdir.return_value = ['location1', 'location2']
        movie_locations = movie_manager.list_movies('somelocation')
        self.assertEqual(movie_locations, ['somelocation/location1', 'somelocation/location2'])

    def test_that_list_all_movies_returns_empty_list_when_no_movies_found(self):
        self.mock_listdir.return_value = []
        movie_locations = movie_manager.list_movies('somelocation')
        self.assertEqual(movie_locations, [])

    def test_that_list_all_movies_strips_movies_which_are_not_validated_as_movie(self):
        mock_movietype = self.setup_patch('control.movie_manager.is_movie_type')
        mock_movietype.side_effect = [True, False, True]

        self.mock_listdir.return_value = ['location1', 'notmovie', 'location2']
        movie_locations = movie_manager.list_movies('somelocation')
        self.assertEqual(movie_locations, ['somelocation/location1', 'somelocation/location2'])


class TestValidateMovie(BaseTestCase):
    def setUp(self):
        super(TestValidateMovie, self).setUp()
        self.mock_listdir = self.setup_patch('os.listdir')
        self.mock_listdir.return_value = []

    def test_that_is_movie_type_returns_true_when_is_a_valid_movie_director(self):
        self.mock_listdir.return_value = ['myawesomemovie']
        self.assertTrue(movie_manager.is_movie_type('somelocation'))

    def test_that_is_movie_type_returns_false_when_directory_is_empty(self):
        self.mock_listdir.return_value = []
        self.assertFalse(movie_manager.is_movie_type('somelocation'))

    def test_that_is_movie_type_returns_false_when_location_is_a_file(self):
        self.mock_listdir.side_effect = OSError

        self.assertFalse(movie_manager.is_movie_type('somelocation'))
