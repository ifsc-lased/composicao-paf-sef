FROM mysql:8

COPY ./ddl-dml/*.sql /docker-entrypoint-initdb.d/

RUN mkdir -p /init-script
COPY ./init-script/* /init-script/
RUN bash /init-script/dados-contribuinte.sh /init-script/contribuinte.properties /docker-entrypoint-initdb.d/2-contribuinte.sql