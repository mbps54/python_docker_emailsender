## App for automatic e-mail generation (for MS Exchange)
### Description
Docker container can send a letter(s) to a comma separated list of email addresses (from system environments)
```POST_SCHEDULE``` - OPTIONAL variable, if it is ommited, email is send once.
Crontab style is used, but use "X" instead of "*"

### This git direcory contains:
1. Python and bash codes
2. Dockerfile to make a Docker container
3. Kubernetes Deployment manifest to run the app

Docker image is also available on [Docker Hub](https://hub.docker.com/r/mbps54/app-email)

### Make Docker image
1. Build an image from code
```
docker build . -t mbps54/app-email-sender:latest
```

2. Push container to hub (optional)
```
docker push mbps54/app-email-sender:latest
```
### Usage options
1. Run Docker container with a schedule (17:00 at Wednesdays)
```
docker run -it \
-e POST_SERVER='mail.hogwarts.com' \
-e POST_DOMAIN='GRYFFINDOR' \
-e POST_USERNAME='harry.potter' \
-e POST_PASSWORD='Caput.Draconis' \
-e POST_FROM_ADDRESS='harry.potter@hogwarts.com' \
-e POST_TO_ADDRESS_LIST='hermione.granger@hogwarts.com' \
-e POST_SUBJECT='Philosopher's Stone' \
-e POST_MESSAGE='Dear Hermione, ...' \
-e POST_SCHEDULE='00 17 X X 3' \
mbps54/app-email-sender:latest
```

2. Run Docker container once
```
docker run -it \
-e POST_SERVER='mail.hogwarts.com' \
-e POST_DOMAIN='GRYFFINDOR' \
-e POST_USERNAME='harry.potter' \
-e POST_PASSWORD='Caput.Draconis' \
-e POST_FROM_ADDRESS='harry.potter@hogwarts.com' \
-e POST_TO_ADDRESS_LIST='hermione.granger@hogwarts.com' \
-e POST_SUBJECT='Philosopher's Stone' \
-e POST_MESSAGE='Dear Hermione, ...' \
mbps54/app-email-sender:latest
```

3. Run app locally (no Docker container)
```
export POST_SERVER='mail.hogwarts.com'
export POST_DOMAIN='GRYFFINDOR'
export POST_USERNAME='harry.potter'
export POST_PASSWORD='Caput.Draconis'
export POST_FROM_ADDRESS='harry.potter@hogwarts.com'
export POST_TO_ADDRESS_LIST='hermione.granger@hogwarts.com'
export POST_SUBJECT='Philosopher's Stone'
export POST_MESSAGE='Dear Hermione, ...'
```
Then add app to /etc/crontab or start it once

### Info
```
tree -a -I ".git"
.
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── post_owl.py
├── requirements.txt
└── start.sh

0 directories, 7 files
```
