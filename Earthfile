VERSION 0.7
FROM python:3.10.7
WORKDIR /app

deps:
  RUN pip install -r ./requirements.txt
  COPY ./calculator/calc.py .

unit_test:
  FROM +deps
  COPY ./calculator/calc_test.py .
  RUN python -m unittest discover