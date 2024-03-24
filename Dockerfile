FROM nginx:alpine
COPY ./nginx.cfg etc/nginx/sites-available/nginx.conf

EXPOSE 80
EXPOSE 443