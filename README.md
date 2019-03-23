
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