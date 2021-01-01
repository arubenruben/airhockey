FROM python:3

WORKDIR /usr/airhockey

#Install PyGame
RUN python3 -m pip install -U pygame --user

COPY ./src .


CMD [ "python3", "-m", "pygame.examples.aliens" ]
#CMD [ "python3", "game.py" ]