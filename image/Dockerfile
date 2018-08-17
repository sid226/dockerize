FROM node:boron
RUN mkdir -p /workspace
WORKDIR /workspace
COPY . .
ADD VERSION .

EXPOSE 8545
CMD node app/index.js
