
# How to use GPU

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

# Installation of dependencies

### Windows
* Install git bash for windows and run it as administrator after installation https://git-scm.com/download/win. Execute every following command with this shell.
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
* Download anaconda with python 3.7 https://www.anaconda.com/distribution/
* Execute file from terminal and install into default location
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
