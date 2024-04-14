FROM python:3.10-slim

RUN pip install pipenv

COPY Pipfile Pipfile.lock /app/

WORKDIR /app
RUN pipenv install --deploy --ignore-pipfile

COPY . /app/

CMD ["pipenv", "run", "python", "__main__.py"]
