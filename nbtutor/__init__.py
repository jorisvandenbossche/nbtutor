# -*- coding: utf-8 -*-
"""
nbtutor - a small utility to indicate which cells should be cleared (exercises).
"""

import os

try:
    from nbconvert.preprocessors.base import Preprocessor
except ImportError:
    from IPython.nbconvert.preprocessors.base import Preprocessor

from traitlets import Unicode


class ClearExercisePreprocessor(Preprocessor):

    solutions_dir = Unicode("_solutions").tag(config=True)

    def preprocess_cell(self, cell, resources, index):

        if 'clear_cell' in cell.metadata and cell.metadata.clear_cell:
            fname = os.path.join(
                self.solutions_dir, resources['metadata']['name'] + str(cell['execution_count']) + '.py')
            with open(fname, 'w') as f:
                f.write(cell['source'])
            cell['source'] = ["# %load {0}".format(fname)]
            cell['outputs'] = []
            # cell['source'] = []

        return cell, resources
