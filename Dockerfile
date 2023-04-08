FROM python:3.8 

RUN mkdir /app
WORKDIR /app
RUN pip install Flask
ADD . /app
EXPOSE 8080
CMD python main.py