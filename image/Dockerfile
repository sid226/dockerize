FROM node:8
RUN mkdir -p /workspace
WORKDIR /workspace
COPY . .
ADD VERSION .

EXPOSE 8545
CMD node app/index.js
