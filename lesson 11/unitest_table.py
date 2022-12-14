from unittest import TestCase
from table_exceptions import *
from table_sys_val import *
import unittest

class TableTest(TestCase):

    def setUp(self) -> None:
        self.japanikaa = TableReservationSystem([3, 5, 2, 2, 6, 4, 3, 6], 'Japanika')

    def test_release_check(self):
        #japanika = TableReservationSystem([3, 5, 2, 2, 6, 4, 3, 6], 'Japanika')
        self.japanikaa.reserve(1,2)

        with self.assertRaises(Exception):
            self.japanikaa.reserve(1, 2)


if __name__ == '__main__':
    unittest.main()