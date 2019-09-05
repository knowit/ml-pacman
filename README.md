
In this workshop you will be programming in Python.
For the most part of the workshop, you will be doing this through a Jupyter Notebook,
an interface for working with Python and the corresponding environment in the cloud.
Through this interface,  which will be connected to a GPU,
you will train your reinforcement learning model.

Unfortunately, to run the game itself, and watch your trained model in action,
you will need to setup a Python environment locally.
If you have the time, it is preferable that you get this up and running beforehand,
so that we can spend more time on the fun stuff during the workshop.

If you know your way around Python and Python environments, all you have to do is:
 * Clone this repository: ```git clone https://github.com/knowit/ml-pacman.git```
 * Install the required packages for the project: `pip install -r requirements.txt`
 * Head into the jupyter package and run jupyter_main.py.
 A graphical interface with our version of Pac-Man should show on the screen if the setup is right.

Otherwise, please follow the instructions corresponding to your OS
to setup a working Python environment on your local machine.

**Note:** Setting up a working Python environment can at times be a troublesome affair.
If you have any problems during the setup, please contact us at manu.gopinathan@knowit.no
and malte.loller-andersen@knowit.no, and we will try to assist you the best we can.
If it does not work, do not worry. We will help you on the day of the workshop.

# Project setup

#### IDE
We recommend using PyCharm by JetBrains: https://www.jetbrains.com/pycharm/

The following steps are OS-dependent and after installing the dependecies you should be able to run the code in this project.

### Windows 10

#### Git
* Install git bash for windows and run it as administrator after installation https://git-scm.com/download/win. Execute every following command with this shell.
* Clone this repository with ```git clone https://github.com/knowit/ml-pacman.git```


#### Python

* Install python 3.7 from https://www.python.org/downloads/windows/. Follow the install guide, but make sure that the `install pip` checkbox is checked, and that `add python to path` is checked. That makes it a lot easier. You should now be able to write `python` in the command prompt to start python.
* You can either install Python packages globally or in a virtual environment.
It is advisable to create a separate virtual environment for all your Python projects,
so that they do not interfere with each other.
Run these commands in Terminal.
    - Install virtualenv: Run `pip3 install virtualenv`
    - Create a virtualenv for the project: Run `virtualenv PATH_TO_ENVIRONMENT_DIRECTORY/[INSERT_ENV_NAME]`,
    e.g `virtualenv ml-pacman` will create the environment in the current directory.
    - **Note:** There is an extension to `virtualenv` called `virtualenvwrapper`,
    which has extended functionality. You can check it out if you want to, but it is not critical:
    https://virtualenvwrapper.readthedocs.io/en/latest/
* Activate the new virtual environment. Run: `source PATH_TO_ENVIRONMENT_DIRECTORY/[ENV_NAME]/bin/activate`,
e.g. `source PATH_TO_ENVIRONMENT_DIRECTORY/ml-pacman/bin/activate`
* Your command line should now display something like: `(ml-pacman)`,
which means you're inside the virtual environment. Now you can install the required packages. Run:
`pip install -r requirements.txt`
* Head into the jupyter package and run jupyter_main.py.
 A graphical interface with our version of Pac-Man should show on the screen if the setup is right.


#### Anaconda

If you want to use anaconda you are welcome to do so, but we don't have much knowledge about it, and therefore can't help you much if you can't figure it out yourself.

### MacOS

#### Git
* Install git: https://git-scm.com/download/mac
* Clone this repository: ```git clone https://github.com/knowit/ml-pacman.git```

#### Python
* Download Python 3.7: https://www.python.org/downloads/
* You can either install Python packages globally or in a virtual environment.
It is advisable to create a separate virtual environment for all your Python projects,
so that they do not interfere with each other.
Run these commands in Terminal.
    - Install virtualenv: Run `pip3 install virtualenv`
    - Create a virtualenv for the project: Run `virtualenv PATH_TO_ENVIRONMENT_DIRECTORY/[INSERT_ENV_NAME]`,
    e.g `virtualenv ml-pacman` will create the environment in the current directory.
    - **Note:** There is an extension to `virtualenv` called `virtualenvwrapper`,
    which has extended functionality. You can check it out if you want to, but it is not critical:
    https://virtualenvwrapper.readthedocs.io/en/latest/
* Activate the new virtual environment. Run: `source PATH_TO_ENVIRONMENT_DIRECTORY/[ENV_NAME]/bin/activate`,
e.g. `source PATH_TO_ENVIRONMENT_DIRECTORY/ml-pacman/bin/activate`
* Your command line should now display something like: `(ml-pacman)`,
which means you're inside the virtual environment. Now you can install the required packages. Run:
`pip install -r requirements.txt`
* Head into the jupyter package and run jupyter_main.py.
 A graphical interface with our version of Pac-Man should show on the screen if the setup is right.

### Ubuntu
#### Git
* Install git with ```sudo apt-get install git```. (https://git-scm.com/download/linux)
* Clone this repository with ```git clone https://github.com/knowit/ml-pacman.git```

#### Python
* Install Python:
```
sudo apt-get update
sudo apt-get install python3.7
```
* If this doesn't work execute this: `sudo add-apt-repository ppa:deadsnakes/ppa` and try the previous commands again
* You can either install Python packages globally or in a virtual environment.
It is advisable to create a separate virtual environment for all your Python projects,
so that they do not interfere with each other.
Run these commands in Terminal.
    - Install virtualenv: Run `pip3 install virtualenv`
    - Create a virtualenv for the project: Run `virtualenv PATH_TO_ENVIRONMENT_DIRECTORY/[INSERT_ENV_NAME]`,
    e.g `virtualenv ml-pacman` will create the environment in the current directory.
    - **Note:** There is an extension to `virtualenv` called `virtualenvwrapper`,
    which has extended functionality. You can check it out if you want to, but it is not critical:
    https://virtualenvwrapper.readthedocs.io/en/latest/
* Activate the new virtual environment. Run: `source PATH_TO_ENVIRONMENT_DIRECTORY/[ENV_NAME]/bin/activate`,
e.g. `source PATH_TO_ENVIRONMENT_DIRECTORY/ml-pacman/bin/activate`
* Your command line should now display something like: `(ml-pacman)`,
which means you're inside the virtual environment. Now you can install the required packages. Run:
`pip install -r requirements.txt`
* Head into the jupyter package and run jupyter_main.py.
 A graphical interface with our version of Pac-Man should show on the screen if the setup is right.

