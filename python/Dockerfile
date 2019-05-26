FROM python:3-slim

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libfontconfig1 libxext6

#RUN pip install --no-cache-dir opencv-python

COPY opencv_python-4.1.0.25-cp37-cp37m-manylinux1_x86_64.whl ./
COPY numpy-1.16.3-cp37-cp37m-manylinux1_x86_64.whl ./
RUN pip install numpy-1.16.3-cp37-cp37m-manylinux1_x86_64.whl opencv_python-4.1.0.25-cp37-cp37m-manylinux1_x86_64.whl

COPY psycopg2-2.8.2.tar.gz ./
RUN tar -xzvf psycopg2-2.8.2.tar.gz
RUN python psycopg2-2.8.2/setup.py install

COPY main.py ./
CMD [ "python", "./main.py" ]