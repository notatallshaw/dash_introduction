# Dash Introduction

Dash is a tool for creating interactive data visualization web sites, in particular it works natively with Plotly graphs. See the official websites:

 * https://dash.plot.ly/
 * https://plot.ly/python/


# Prerequisites 

To follow this introduction you will need to install Python 3 and the following third party modules:

 * requests
 * pandas
 * plotly
 * dash
 * dash-html-components
 * dash-core-components

## Install Python

If you have not installed Python already you can install from either Python.org or Anaconda.com:

 * https://www.anaconda.com/download (recommend, especially for Windows users)
 * https://www.python.org/downloads
 
Remember to select the "include in PATH" option when installing, it will be much easier to run from command line

## Install the modules

If you installed Anaconda it is easier to the "conda" package manager to install modules. Simply type the following in the command line:

    conda install requests pandas plotly
    conda install dash dash-html-components dash-core-components -c conda-forge
    
 If you installed Python from Python.org or are using your system Python install then one of the following commands should work:
 
    python3 -m pip install --user --upgrade requests pandas plotly dash dash-html-components dash-core-components
    
 Or:
 
    python -m pip install --user --upgrade requests pandas plotly dash dash-html-components dash-core-components
    
## Install and IDE (optional)

I would recommend installing an IDE or advanced Text Editor and getting used to it. Here are a list of a few (I personally use Pycharm):

 * https://www.jetbrains.com/pycharm/download
 * https://code.visualstudio.com
 * https://www.sublimetext.com
 * Or whatever works for you!

