FROM node:boron
RUN mkdir -p /app
WORKDIR /app
COPY . .
ADD VERSION .

EXPOSE 8545
CMD node index.js
