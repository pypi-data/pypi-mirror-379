#!/usr/bin/env python3

import unittest
import os
import pickle
import polars as pl
from ddtig.domain import TestTree
from ddtig.user_interface import SystemSpecsHandler

class TestTestTree(unittest.TestCase):
    
    def setUp(self):
        """ Setup:
            Import Hoeffding Tree
        """
        dirpath = os.path.dirname(os.path.abspath(__file__))
        hoeffding_file = os.path.join(dirpath, f"resources/Appliances_Hoeffding.pkl")
        with open(hoeffding_file, "rb") as f:
            hoeffding_tree = pickle.load(f)

        dataset = pl.read_csv(os.path.join(dirpath, "resources/Appliances.csv"))
        specs = SystemSpecsHandler(dataset, specs_file=None)
        self.testtree = TestTree(hoeffding_tree, specs, logger=None).test_tree
        
    def test_testtree(self):
        """ Test:
            1. Number of nodes
            2. Number of leaves
            3. Sample size
        """

        self.assertTrue((len(self.testtree) == 29), "Number of nodes is not correct.")

        leaves = {leaf: leaf_info for leaf, leaf_info in self.testtree.items() if leaf_info.samples > 0}
        self.assertTrue((len(leaves) == 15), "Number of leaves is not correct.")

        samples = [leaf_info.samples for _, leaf_info in self.testtree.items() if leaf_info.samples > 0]
        self.assertTrue((sum(samples) == 19735), "Sample size is not correct.")
        

if __name__ == '__main__':
    unittest.main()