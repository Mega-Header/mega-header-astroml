FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3
COPY mega-header-astroml/serving /app/mega-header-astroml/serving
WORKDIR /app
CMD ["python3", "-m", "mega-header-astroml.serving.grpc_server"]
