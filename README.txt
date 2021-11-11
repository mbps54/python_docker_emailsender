It is a Python code and Dockerfile to make a ready container to send emails via MS Exchange server.
Image can send a letter(s) to a comma separated list of email addresses (from system environments)
POST_SCHEDULE - OPTIONAL variable, it it is ommited, email is send right now. Crontab style is used, but use "X" instead of "*"

1. Build an image:
docker build . -t email

2a. Run a locally generated container with a schedule (17:00 at Wednesdays)
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
email

2b. Run a locally generated container only once
docker run -it \
-e POST_SERVER='mail.hogwarts.com' \
-e POST_DOMAIN='GRYFFINDOR' \
-e POST_USERNAME='harry.potter' \
-e POST_PASSWORD='Caput.Draconis' \
-e POST_FROM_ADDRESS='harry.potter@hogwarts.com' \
-e POST_TO_ADDRESS_LIST='hermione.granger@hogwarts.com' \
-e POST_SUBJECT='Philosopher's Stone' \
-e POST_MESSAGE='Dear Hermione, ...' \
email

3a. Run a container from hub.docker.com with a schedule (17:00 at Wednesdays)
docker run -it
-e POST_SERVER='mail.hogwarts.com'
-e POST_DOMAIN='GRYFFINDOR'
-e POST_USERNAME='harry.potter'
-e POST_PASSWORD='Caput.Draconis'
-e POST_FROM_ADDRESS='harry.potter@hogwarts.com'
-e POST_TO_ADDRESS_LIST='hermione.granger@hogwarts.com'
-e POST_SUBJECT='Philosopher's Stone'
-e POST_MESSAGE='Dear Hermione, ...'
-e POST_SCHEDULE='00 17 X X 3'
mbps54/email:2.0

3b. Run a container from hub.docker.com once
docker run -it
-e POST_SERVER='mail.hogwarts.com'
-e POST_DOMAIN='GRYFFINDOR'
-e POST_USERNAME='harry.potter'
-e POST_PASSWORD='Caput.Draconis'
-e POST_FROM_ADDRESS='harry.potter@hogwarts.com'
-e POST_TO_ADDRESS_LIST='hermione.granger@hogwarts.com'
-e POST_SUBJECT='Philosopher's Stone'
-e POST_MESSAGE='Dear Hermione, ...'
-e POST_SCHEDULE='00 17 X X 3'
mbps54/email:2.0
