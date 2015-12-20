# -*- coding: utf-8 -*-
"""
nbtutor - a small utility to indicate which cells should be cleared (exercises).
"""

try:
    from nbconvert.preprocessors.base import Preprocessor
except ImportError:
    from IPython.nbconvert.preprocessors.base import Preprocessor


class ClearExercisePreprocessor(Preprocessor):

    def preprocess_cell(self, cell, resources, index):

        if 'clear_cell' in cell.metadata and cell.metadata.clear_cell:
            cell['source'] = []
            cell['execution_count'] = None
            cell['outputs'] = []

        return cell, resources
