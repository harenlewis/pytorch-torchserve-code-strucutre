FROM pytorch/torchserve:latest-gpu

COPY mnist.py mnist_cnn.pt mnist_handler.py /home/model-server/

USER root
# RUN printf "\nservice_envelope=json" >> /home/model-server/config.properties
USER model-server

RUN torch-model-archiver \
  --model-name=mnist \
  --version=1.0 \
  --model-file=/home/model-server/model.py \
  --serialized-file=/home/model-server/resnext_nn.pt \
  --handler=/home/model-server/handler.py \
  --export-path=/home/model-server/model-store

CMD ["torchserve", \
     "--start", \
     "--ts-config=/home/model-server/config.properties", \
     "--models", \
     "mnist=mnist.mar"]
