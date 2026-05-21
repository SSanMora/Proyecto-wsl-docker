FROM node:current-alpine
WORKDIR /usr/src/app

# Instalar express directamente antes de ejecutar el código
RUN npm install express

COPY index.js .
EXPOSE 3000
CMD ["node", "index.js"]
