## Processing Humanities Multimedia DHSI 2018 | Course Materials

### How to install the Docker images
First, install [Docker CE](https://www.docker.com/community-edition#/download)

 Once you have Docker from anywhere on your machine you can run

`docker pull jromphf/python3-opencv-ffmpeg:0.0.6`

### How to run the Docker containers
Once you have pulled the images, you can run them in an interactive bash session with the following command:

`docker run -ti jromphf/python3-opencv-ffmpeg:0.0.6 bash`


To mount a shared volume, you can run the container with the *-v* flag:

`docker run -ti -v [/path/to/folder/on/host]:[/path/to/folder/on/container] [...]`

Where [path/to/folder/on/host] is the **absolute path** to the folder on the host file system and [/path/to/folder/on/container] is the **absolute path** specifying where the directory will be mounted on the container's file system.

### Cleanup
When you're finished with your containers, you can stop any running containers and / or delete them:

*To stop all containers (active or otherwise):*

`docker stop $(docker ps -a -q)`

*To remove all containers*

`docker rm $(docker ps -a -q)`

If you want to free up space and remove an image, run:

`docker rmi [name-of-repository]/[name-of-image]:[tag]`

To remove all dangling images, run:

`docker rmi $(docker images -f dangling=true -q)`

If you are looking to automate this process, check out
[docker-gc](https://github.com/spotify/docker-gc).

**FOR MAC USERS**

Please note that DockerCE for Mac does not properly release disk space after all of your containers and images have been deleted. It's not uncommon to see disk space balloon to extreme levels (>30GB!) after running Docker for a while. One option is to reset Docker by opening the application, and selecting preferences ---> Reset (the :bomb: icon). **This will remove all containers and images.**

If you're interested, the offending file is:
*~/Library/Containers/com.docker.docker/Data/com.docker.driver.amd64-linux/Docker.qcow2*