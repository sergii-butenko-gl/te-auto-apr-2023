FROM python:3.11.3-slim-buster

# COPY THE FRAMEWORK
WORKDIR /test_auto
COPY . .

# install requirements
RUN pip install -r requirements.txt

# create instruction on how to run tests
ENTRYPOINT [ "pytest" ]