FROM node:20.12.0-alpine3.18

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm config set fetch-retry-maxtimeout 1000000 && npm install
COPY . /app

EXPOSE 3000

CMD ["npm", "start"]