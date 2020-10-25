FROM python:3.8-slim-buster

# work within the /code directory of the image
WORKDIR /code

# set tensorflow logging level to Errors only (because tf emits a lot of Info and Warning level logs)
ENV TF_CPP_MIN_LOG_LEVEL 2

# copy over our python library dependencies to the image
COPY requirements.txt .

# install the python dependencies
RUN pip install -r requirements.txt

# download the pretrained model to the image
COPY download-model.py .
RUN [ "python", "download-model.py" ]

# copy over the script itself
COPY index.py .

# fix the entry script to be the index script.
ENTRYPOINT [ "python", "index.py" ]
