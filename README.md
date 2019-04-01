
# Installation of dependencies

The following steps are OS-dependent and after installing the dependecies you should be able to run the code in this project.

### Windows
#### Git
* Install git bash for windows and run it as administrator after installation https://git-scm.com/download/win. Execute every following command with this shell.
* Clone this repository with ```git clone https://github.com/knowit/ml-pacman.git```

#### Anaconda / Python
* Install anaconda with python 3.7 https://www.anaconda.com/distribution/
* Run command ```echo ". C:\\Users\\<username>\\Anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc``` and replace <username> with your username
* Run command ```source ~/.bashrc```
* Run command in project folder: ```conda create -n ml-pacman python=3.6.5```
* Run command ```conda activate ml-pacman```
* Run command ```pip install pygame```
* Run command ```conda install numpy```
* Run command ```conda install matplotlib```
* Run command ```conda install keras```

### MacOS
#### Git
* Git should already be installed on OSX so no need to do anything else with git installation
* Clone this repository with ```git clone https://github.com/knowit/ml-pacman.git```

#### Anaconda / Python
* Install anaconda with python 3.7 https://www.anaconda.com/distribution/
* Run command ```export PATH="/Users/<username>/anaconda3/bin:$PATH"``` and replace <username> with your username
* Run command ```echo ". /Users/<username>/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc``` and replace <username> with your username
* Run command ```source ~/.bashrc```
* Run command in project folder: ```conda create -n ml-pacman python=3.6.5```
* Run command ```conda activate ml-pacman```
* Run command ```pip install pygame```
* Run command ```conda install numpy```
* Run command ```conda install matplotlib```
* Run command ```conda install keras```

### Ubuntu/Linux
#### Git
* install git with ```sudo apt install git-all```
* Clone this repository with ```git clone https://github.com/knowit/ml-pacman.git```

#### Anaconda / Python
* Download anaconda with python 3.7 https://www.anaconda.com/distribution/
* Make downloaded file an executable with ```chmod +x <anaconda file>``` when in same folder as downloaded file
* Execute file with ```./<anaconda file>``` and install into default location
* Copy and paste into ~/.bashrc file and replace <username> with your username
```
__conda_setup="$(CONDA_REPORT_ERRORS=false '/home/<username>/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/home/<username>/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/<username>/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/home/<username>/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
```
* Run command ```source ~/.bashrc```
* Run command in project folder: ```conda create -n ml-pacman python=3.6.5```
* Run command ```conda activate ml-pacman```
* Run command ```pip install pygame```
* Run command ```conda install numpy```
* Run command ```conda install matplotlib```
* Run command ```conda install keras```


# How to use GPU (Hopefully won't be needed)

### How to upload files
1. From your local file system:
`scp -r [ml-pacman folder path] 10.198.204.4:~/[insert personal folder name]/`
    - If you have trouble connecting, try pinging the IP until it responds:
    `ping 10.198.204.4`


### How to connect to GPU instance
1. SSH into instance from your shell: `ssh workshop@10.198.204.4`
    - If you have trouble connecting, try pinging the IP until it responds:
    `ping 10.198.204.4`

### How to run your code on the GPU
1. Create a personal folder where you can upload your files:
`mkdir [insert personal folder name]`
2. Launch a new shell instance: `screen`
3. Navigate to your folder and run
