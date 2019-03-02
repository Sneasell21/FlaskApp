FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

ENV REDIS_URL redis
ENV REDIS_PORT 6379
EXPOSE 8098
CMD ["python", "/code/app.py"]
