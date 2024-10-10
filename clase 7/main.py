# from nombre_del_archivo import nombre_de_la_clase
from ETL import ETL


if __name__ == '__main__':
    # etl para el calculo de las recogidas por hectarea
    etl = ETL(name='recogidas_por_hectarea',queries_path='./etl1.sql')
    etl.execute()

    # etl para el calculo de recogidas por cultivo
    etl2 = ETL(name='top5_cultivos',queries_path='./etl2.sql')
    etl2.execute()

    # etl para calcular el top 5 de usuarios que mas recogidas han hecho
    etl3 = ETL(name='top5_usuarios',queries_path='./etl3.sql')
    etl3.execute()
