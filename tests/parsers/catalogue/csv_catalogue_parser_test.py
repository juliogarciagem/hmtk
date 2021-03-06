import unittest
import os

from hmtk.parsers.catalogue.csv_catalogue_parser import CsvCatalogueParser

class CsvCatalogueParserTestCase(unittest.TestCase):
    """ 
    Unit tests for the csv Catalogue Parser Class
    """
    
    BASE_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
    
    def setUp(self):
        """
        Read a sample catalogue containing 8 events after instantiating
        the CsvCatalogueParser object.
        """
        filename = os.path.join(self.BASE_DATA_PATH, 'test_catalogue.csv') 
        parser = CsvCatalogueParser(filename)
        self.cat = parser.read_file()

    def test_read_catalogue(self):
        """
        Check that the some fields in the first row of the catalogue are read
        correctly
        """
        self.assertEqual(self.cat.data['eventID'][0], 54)
        self.assertEqual(self.cat.data['Agency'][0], 'sheec')
        self.assertEqual(self.cat.data['year'][0], 1011)
        
    def test_read_catalogue_num_events(self):
        """
        Check that the number of earthquakes read form the catalogue is 
        correct
        """
        self.assertEqual(self.cat.get_number_events(),8)