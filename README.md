nbtutor
-------

A small utility for teaching with IPython notebooks: generate a student
version of the notebook with the exercises cleared, while keeping
your master version with the solutions.

To install this, git clone the repo and then do:

    git clone https://github.com/jorisvandenbossche/nbtutor.git
    cd nbtutor
    python setup.py develop

Further, you need to copy the nbextension to your IPython folder:

    cp nbextensions/* $(ipython locate)/nbextensions/

To ensure the the extension is loaded automatically, edit your your `custom.js`
(found in `$(ipython locate profile)/static/custom/custom.js`) to include the
following:

    $([IPython.events]).on("app_initialized.NotebookApp", function () {
        IPython.load_extensions("excluder");
    });

And for converting, add to your `ipython_nbconvert_config.py` file (inside
your profile folder):

    c = get_config()
    c.Exporter.preprocessors = ['nbtutor.ClearExcercisePreprocessor']


and then run the following `nbconvert` command to convert a notebook:

    ipython nbconvert notebook.ipynb --to-notebook


Copyright (c) 2015, Joris Van den Bossche

BSD 2-Clause licensed, feel free to use or adapt!
