from ETL import ETL


if __name__ == '__main__':
    etl4 = ETL(name='gasto_por_cc', input_path='./data', output_path='./compraventa', queries_path='./etl4.sql')
    etl4.execute()

