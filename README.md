## Containerized Machine Translation with HuggingFace T5-base model.
This is a containerized application which uses the python [transformers](https://pypi.org/project/transformers/) package to run machine translation through Google's [T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) model (using the pretrained [t5-base](https://huggingface.co/t5-base) model from HuggingFace).

### Requirements
This project requires [Docker](https://docs.docker.com/get-started/overview/) to run.

### How to Use
Run this project image from docker hub:
```
$ docker run parkernilson/machine-translation-en-to-de "Add a fun sentence to translate here!"
```
NOTE: This image is quite large, since it requires two large python libraries 'Tensorflow' and HuggingFace's 'Transformers', and it also includes a large (about 1 GB) pretrained model in one of the image layers. Thus, it might take some time to download and spin up.
