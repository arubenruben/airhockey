FROM python:3-alpine

WORKDIR /usr/airhockey

COPY ./src .

CMD [ "python3", "game.py" ]