# Planetary Research
The pre-launch website of the planetary science diamond open access journal.

Click [here](https://doaj-planetary-research-initiative.readthedocs.io/en/latest/index.html) to open.

In the docs folder of this repository are the .rst (reStructured Text) files and the configuration file for the content. Compile with the Python sphinx module when in the main repository directory using:

```
sphinx-build -b html docs docs_html
```

The theme is **furo**, which needs to be installed along with  **sphinxcontrib.youtube**, **sphinx-copybutton** and **sphinx-toolbox** before compiling:

```
pip install furo  # or conda install furo
pip install sphinx-copybutton  # or conda install sphinx-copybutton
pip install sphinx-toolbox  # or conda install sphinx-toolbox
pip install sphinxcontrib.youtube
```
