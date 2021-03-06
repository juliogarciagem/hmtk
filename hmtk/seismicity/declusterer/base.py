"""
Module :mod:`hmtk.parsers.catalogue.base` defines an abstract base class
for :class:`CatalogueParser <BaseCatalogueDecluster>`.
"""
import abc

class BaseCatalogueDecluster(object):
    """
    Abstract base class for implementation of declustering algorithms
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def decluster(self, catalogue, config):
        """
        Implements declustering algorithms
        :param catalogue: 
            Catalogue of earthquakes
        :type catalogue: 
        :param config: 
            Declustering configuration dictionary
        :type config: Dictionary
        
        Returns two vectors 
        """
        return
