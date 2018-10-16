from django.test import TestCase


class BookmarksTestCase(TestCase):
    """Test cases for bookmark events

    This class shall test the transformations of all bookmark related events
    """
    def test_edx_bookmark_listed(self):
        self.assertEqual(1, 0)