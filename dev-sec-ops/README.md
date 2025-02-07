# Kali Linux

## Change the source.list
`sudo nvim /etc/apt/sources.list`
And change the **first** *http* to **https**.

## Virtual Manager
After install kali linux please install this package
`apt install spice-vdagent` - This will allow you to copy from the host machine to the guest machine.
In addition this will allow to use to **resize based on window**.
If you want to resize your window, it does not work with VGA for some reason.

## Install Docker

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  bookworm stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

## Run Gitlab

Pull docker image
`sudo docker pull gitlab/gitlab-ce:latest`

Run the container
```bash
export GITLAB_HOME=/srv/gitlab

docker run -d \
	--hostname gitlab.cve.com \
	-p 433:433 -p 80:80 -p 22:22 \
	--name gitlab \
	--restart always \
	--volume $GITLAB_HOME/config:/etc/gitlab \
	--volume $GITLAB_HOME/logs:/var/log/gitlab \
	--volume $GITLAB_HOME/data:/var/opt/gitlab \
	--shm-size 2gb \
	gitlab/gitlab-ce:latest
```
## Extract the initial password from gitlab

The command we use is: `grep 'Password:' /etc/gitlab/initial_root_password` but we do it in conjuction with the `exec`.
`sudo docker exec -it gitlab grep 'Password:' /etc/gitlab/initial_root_password`

## Clone WebGoat

`git clone https://github.com/WebGoat/WebGoat.git`

## Create an SSH key

Create a SSH key and add it to gitlab
`ssh-keygen -t ed25519 -C "your_email@example.com"`

## Pushing the repository
To print the public key we'll use this command.
`cat ~/.ssh/id_ed25519.pub`

Afterwards please add the SSH public key to gitlab.

Remove the `.git` folder and initiate a new git repo.
```bash
git init --initial-branch=main
git remote add origin git@gitlab.cve.com:root/webgoat.git
git add .
git commit -m "Initial commit"
git push --set-upstream origin main
```


## Creating a runner

Now go to the admin panel and create a new runner.

This will install the gitlab-runner cli.

```bash
# Download the binary for your system
sudo curl -L --output /usr/local/bin/gitlab-runner https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64

# Give it permission to execute
sudo chmod +x /usr/local/bin/gitlab-runner

# Create a GitLab Runner user
sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash

# Install and run as a service
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner start
```

If you use the docker version please pull the docker image using this `docker pull gitlab/gitlab-runner:latest`, and then do the other commands.
If you're using docker please be sure to add a mapping between the host IP and the hostname of the gitlab.
For example if the host IP is 182.168.124.20 and the git lab hostname is `gitlab.code.com` make sure to add it in the `/etc/hosts` files and in the config file
of the gitlab runner `extra_hosts = ["gitlab.code.com:192.168.124.20"]`.

## Defect Dojo

Clone the project
`git clone https://github.com/DefectDojo/django-DefectDojo.git`

Get the credentials
`docker logs django-defectdojo-initializer-1 | grep Admin`

## API Requests

```bash
curl -X GET "http://localhost:8080/api/v2/" \
-H "Content-Type: application/json" \
-H "Authorization: Token 1355f2f547e05ac9e6ad273e4f750152adb8daf3" \
-k
```

