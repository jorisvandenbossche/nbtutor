nbtutor
-------

A small utility for teaching with IPython notebooks: generate a student
version of the notebook with the exercises cleared, while keeping
your master version with the solutions.

To install this, git clone the repo and then do:

    git clone https://github.com/jorisvandenbossche/nbtutor.git
    cd nbtutor
    pip install .

Further, you need to install the nbextension:

    jupyter nbextension install nbextension/

To ensure the the extension is loaded automatically, you also have to
enable the extension:

    jupyter nbextension enable nbtutor

And for converting, make a file that is eg called 'nbtutor_config.py' with
the following content:

    c.Exporter.preprocessors = ['nbtutor.ClearExercisePreprocessor']

and then run the following `nbconvert` command to convert a notebook:

    jupyter nbconvert notebook.ipynb --to notebook --config nbtutor_config.py


Copyright (c) 2015, Joris Van den Bossche

BSD 2-Clause licensed, feel free to use or adapt!
