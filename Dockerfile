FROM python:3.7.6-buster

RUN pip install pytest  \
&& pip install pydantic

