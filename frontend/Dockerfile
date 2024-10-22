FROM node:20.18-alpine

WORKDIR /app

EXPOSE 3000

COPY package.json package-lock.json ./

COPY config_images_gallery.json /etc/config_images_gallery.json

RUN npm install --silent

COPY . ./

CMD ["npm", "start"]