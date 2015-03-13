# -*- coding: utf-8 -*-
"""
nbtutor - a small utility to indicate which cells should be cleared (exercises).
"""

from IPython.nbconvert.preprocessors.base import Preprocessor

class ClearExcercisePreprocessor(Preprocessor):

    def preprocess_cell(self, cell, resources, index):

        if 'clear_cell' in cell.metadata and cell.metadata.clear_cell:
            cell['source'] = []
            cell['execution_count'] = None
            cell['outputs'] = []

        return cell, resources
