# Dash Introduction

Dash is a tool for creating interactive data visualization web sites, in particular it works natively with Plotly graphs. See the official websites:

 * https://dash.plot.ly/
 * https://plot.ly/python/
 * https://plot.ly/python/reference/


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

If you installed Anaconda it is easier to the "conda" package manager to install modules. Simply add the conda-forge channel if not already done:

    conda config --append channels conda-forge
    
And then install the modules (the specific cryptography and zeromq packages are due to problems I was having installing on Windows):

    conda create -n dash python dash dash-core-components dash-html-components
    
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
 
# FAQ

 1. Do I need to pay for Plotly or Dash?
 
 No! Most features for both Plotly and Dash are free, and this introduction will only cover how to set-up your own website that does not use any of the paid for features that Plotly provides.
 
 2. Do I need to understand JavaScript?
 
 No! Dash is specifically created for Python developers to code purely in Python. More advanced features like building your own Dash Components will require an understanding of JavaScript and React.js this is not needed for building even complex interactive sites.
 
 3. Do I need to understand HTML or CSS?
 
 A little bit helps. A very basic understanding of HTML is required and the more CSS you understand the prettier you will be able to make your sites.
 
 4. Could I build a complex web application using Dash?
 
 Yes... Dash is designed to make very easy to build single web pages. Building large complex web applications using just Dash is possible but will require some effort by you!
