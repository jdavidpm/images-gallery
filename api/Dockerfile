FROM python:3.12

WORKDIR /app

EXPOSE 5050

COPY Pipfile Pipfile.lock ./
COPY config_images_gallery.json /etc/config_images_gallery.json

RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD [ "python", "main.py" ]