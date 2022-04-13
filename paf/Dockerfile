FROM python:3.9

WORKDIR /app
COPY /app/requirements.txt /app
RUN python3 -m pip install -r /app/requirements.txt

# Definindo variáveis de ambiente que serão usadas pela aplicação flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=True

ENV FLASK_SQLALCHEMY_TRACK_MODIFICATIONS=True

ENV FLASK_SQLALCHEMY_BINDS_ws=mysql+pymysql://dafws:7rVQW48ph2@db:3306/daf-ws
ENV FLASK_SQLALCHEMY_BINDS_paf=mysql+pymysql://dafpaf:E37vEB3dnm@db:3306/daf-paf
ENV FLASK_REDIS_HOST=redis
ENV FLASK_REDIS_PORT=6379
ENV FLASK_ENDERECO_SEF=sef:8080

EXPOSE 5000
CMD ["flask", "run"]