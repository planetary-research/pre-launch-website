# Planetary Research
This is the pre-launch website of the Planetary Research diamond open access journal.

Click [here](https://planetary-research-journal) to access the website.

The website content and configure files are located in the `docs` folder. These need to be compiled into a static website using the following command in the top level directory:

```
sphinx-build -b html docs docs_html
```

This website makes uses of the theme `furo`, as well as the sphinx plugins `sphinxcontrib.youtube`, `sphinx-copybutton` and `sphinx-toolbox`. Before compiling the static website, these dependencies will need to be installed using either pip

```
pip install furo
pip install sphinx-copybutton
pip install sphinx-toolbox
pip install sphinxcontrib.youtube
```

or conda

```
conda install furo
conda install sphinx-copybutton
conda install sphinx-toolbox
pip install sphinxcontrib.youtube  # no conda package available
```
