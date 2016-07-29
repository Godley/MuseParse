import unittest

from MuseParse.classes.ObjectHierarchy.TreeClasses.PieceTree import PieceTree


class TestClass(unittest.TestCase):

    def setUp(self):
        self.tags = []
        self.attrs = {}
        self.chars = {}
        self.piece = PieceTree()
