## Containerized Machine Translation with HuggingFace T5-base model.
This is a containerized application which uses the python [transformers](https://pypi.org/project/transformers/) package to run machine translation through Google's [T5](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html) model (using the pretrained [t5-base](https://huggingface.co/t5-base) model from HuggingFace).

### Requirements
This project requires [Docker](https://docs.docker.com/get-started/overview/) to run.

### How to Use
Run this project image from docker hub:
```
$ docker run parkernilson/machine-translation-en-to-de "Add a fun sentence to translate here!"
```
NOTE: **`docker run`** will first try to find the image on your computer, and if it can't it will download it from [this project's repo on Docker hub.](https://hub.docker.com/repository/docker/parkernilson/machine-translation-en-to-de)

Also, NOTE: This image is quite large (about 700MB compressed) since it uses Tensorflow, which is a large package, and it also contains files for a pre-trained model which is also very large.