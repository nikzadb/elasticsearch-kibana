FROM python:3.8
WORKDIR /code
# Use docker cache to speed up the process of package installation
COPY requirements.txt requirements.txt

# install dash_req.txt from the `code` directory in docker (e.g., dashboard)
RUN pip install -U pip && pip install -r requirements.txt

CMD [ "python", "-m", "indexer" ]

