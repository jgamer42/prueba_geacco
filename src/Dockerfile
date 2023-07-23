FROM python:3.9
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ /app/
COPY .env /app/
RUN cd src
#RUN python manage.py migrate
EXPOSE 8000
