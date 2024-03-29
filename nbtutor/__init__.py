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

    def __init__(self, **kw):
        if not os.path.exists(self.solutions_dir):
            os.makedirs(self.solutions_dir)

        self.solution_count = 1
        self.exercise_count = 1

        super(Preprocessor, self).__init__(**kw)

    def preprocess_cell(self, cell, resources, index):

        if 'tags' in cell.metadata and 'nbtutor-solution' in cell.metadata.tags:
            fname = os.path.join(
                self.solutions_dir, resources['metadata']['name'] + str(self.solution_count) + '.py')
            with open(fname, 'w') as f:
                f.write(cell['source'])
            cell['source'] = ["# %load {0}".format(fname)]
            cell['outputs'] = []
            # cell['source'] = []

            self.solution_count += 1

        if cell.cell_type == "markdown" and "EXERCISE" in cell.source:
            cell.source = cell.source.replace('EXERCISE', f'EXERCISE {self.exercise_count}')
            self.exercise_count += 1

        return cell, resources

