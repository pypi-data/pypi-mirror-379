#!/usr/bin/env python3

import unittest
import os
import polars as pl
from ddtig.application import TestPipeline

class TestTestPipeline(unittest.TestCase):
    
    def setUp(self):
        """ Setup:
            Setup test pipeline
        """
        dirpath = os.path.dirname(os.path.abspath(__file__))

        model_file = os.path.join(dirpath, "resources/Iris.fml")        
        dataset = pl.read_csv(os.path.join(dirpath, "resources/Iris.csv"))
        reqs_bva_inverse = os.path.join(dirpath, "resources/reqs_bva_inverse.json")
        reqs_bva_prop = os.path.join(dirpath, "resources/reqs_bva_prop.json")
        reqs_dtc_inverse = os.path.join(dirpath, "resources/reqs_dtc_inverse.json")
        reqs_dtc_prop = os.path.join(dirpath, "resources/reqs_dtc_prop.json")
        
        self.test_pipeline_bva_inverse = TestPipeline(model_file, reqs_bva_inverse, dataset, specs_file=None, classification=True)
        self.test_pipeline_bva_prop = TestPipeline(model_file, reqs_bva_prop, dataset, specs_file=None, classification=True)
        self.test_pipeline_dtc_inverse = TestPipeline(model_file, reqs_dtc_inverse, dataset, specs_file=None, classification=True)
        self.test_pipeline_dtc_prop = TestPipeline(model_file, reqs_dtc_prop, dataset, specs_file=None, classification=True)

        self.test_cases_bva_inverse = self.test_pipeline_bva_inverse.execute()
        self.test_cases_bva_prop = self.test_pipeline_bva_prop.execute()
        self.test_cases_dtc_inverse = self.test_pipeline_dtc_inverse.execute()
        self.test_cases_dtc_prop = self.test_pipeline_dtc_prop.execute()
        
    def test_equivalence_classes(self):
        """ Test:
            1. Number of equivalence classes
        """

        self.assertTrue((len(self.test_pipeline_bva_inverse.eqclasses) == 
                         len(self.test_pipeline_bva_prop.eqclasses) ==
                         len(self.test_pipeline_dtc_inverse.eqclasses) ==
                         len(self.test_pipeline_dtc_prop.eqclasses) == 9), "Number of classes is not correct")
        
    def test_n_test_inputs(self):
        """ Test:
            1. Number of test inputs (Proportional allocation)
            2. Number of test inputs (Inverse allocation)
        """

        self.assertTrue(((self.test_pipeline_bva_inverse.n_testinputs_lst ==                          
                         self.test_pipeline_dtc_inverse.n_testinputs_lst) and
                         (sum(self.test_pipeline_bva_inverse.n_testinputs_lst) ==                          
                         sum(self.test_pipeline_dtc_inverse.n_testinputs_lst) == 150)), "Number of test inputs (Inverse allocation) is not correct.")
        
        self.assertTrue(((self.test_pipeline_bva_prop.n_testinputs_lst ==                          
                         self.test_pipeline_dtc_prop.n_testinputs_lst) and
                         (sum(self.test_pipeline_bva_prop.n_testinputs_lst) ==                          
                         sum(self.test_pipeline_dtc_prop.n_testinputs_lst) == 150)), "Number of test inputs (Proportional allocation) is not correct.")

if __name__ == '__main__':
    unittest.main()