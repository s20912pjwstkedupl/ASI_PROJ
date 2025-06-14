#FROM python:3.12-bookworm AS base
#
#WORKDIR /app
#
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    curl \
#    software-properties-common \
#    git \
#    && rm -rf /var/lib/apt/lists/*
#COPY requirements.txt .
#RUN pip3 install -r requirements.txt
#RUN pip3 install kedro==0.19.12

FROM python:3.12-slim
WORKDIR /app
RUN pip3 install streamlit==1.44.1 autogluon==1.2 pandas==2.2.3
COPY ./data/07_model_output/autogluon_model/models/LightGBMXT/model.pkl models/ModelOut/predictor.pkl
COPY ./data/07_model_output/autogluon_model/models/LightGBMXT/model.pkl datasets/freelancer_earnings_bd.csv
COPY ./app.py app.py
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]