FROM python:3.6

RUN mkdir /var/www
WORKDIR /var/www/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod 777 -R /tmp
RUN chmod 777 -R ./
CMD ["uwsgi", "--ini", "/var/www/uwsgi.ini"]
