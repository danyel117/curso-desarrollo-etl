import pandas as pd
import pandasql as ps

pd.set_option('display.float_format', '{:.2f}'.format)

dataset = {}


def pysqldf(q):
    globals().update(dataset)
    return ps.sqldf(q, globals())


def execute_sql(file_name):
    path = f'./queries/{file_name}.sql'
    with open(path, 'r') as file:
        query = file.read()
    return pysqldf(query)



def extract():
    print('Extrayendo datos...')
    dataset['clientes'] = pd.read_csv('./inputs/cliente.csv', sep=';')
    dataset['facturas'] = pd.read_csv('./inputs/factura.csv', sep=';')
    dataset['despachos'] = pd.read_csv('./inputs/despacho.csv', sep=';')
    dataset['recogidas'] = pd.read_csv('./inputs/recogida.csv', sep=';')
    dataset['lotes'] = pd.read_csv('./inputs/lote.csv', sep=';')
    dataset['fincas'] = pd.read_csv('./inputs/finca.csv', sep=';')
    dataset['cultivos'] = pd.read_csv('./inputs/cultivo.csv', sep=';')
    dataset['precios'] = pd.read_csv('./inputs/precio.csv', sep=';')
    dataset['usuarios'] = pd.read_csv('./inputs/usuario.csv', sep=';')

def transform():
    print('Transformando datos...')
    # calcular el precio por mes por cultivo
    dataset['precios_por_mes'] = execute_sql('precios_por_mes')
    # calcular el total recogido por cultivo, finca y mes
    dataset['total_recogido'] = execute_sql('total_recogido')
    # calcular el ingreso por mes por cultivo por finca
    dataset['ingreso_mes_cultivo_finca'] = execute_sql('ingreso_mes_cultivo_finca')
    # calcular el ingreso por mes por finca
    dataset['ingreso_por_finca'] = execute_sql('ingreso_por_finca')
    # calcular el ingreso por mes por cultivo
    dataset['ingreso_por_cultivo'] = execute_sql('ingreso_por_cultivo')
    # calcular el ingreso por mes por mes
    dataset['ingreso_por_mes'] = execute_sql('ingreso_por_mes')
    # calcular el total de hectareas por finca
    dataset['hectareas_por_finca'] = execute_sql('hectareas_por_finca')
    # calcular el ingreso por hectarea por finca
    dataset['ingreso_por_hectarea'] = execute_sql('ingreso_por_hectarea')


def load():
    print('Cargando datos...')
    dataset['ingreso_por_finca'].to_csv('./outputs/ingreso_por_finca.csv', index=False)
    dataset['ingreso_por_cultivo'].to_csv('./outputs/ingreso_por_cultivo.csv', index=False)
    dataset['ingreso_por_mes'].to_csv('./outputs/ingreso_por_mes.csv', index=False)
    dataset['ingreso_por_hectarea'].to_csv('./outputs/ingreso_por_hectarea.csv', index=False)


def execute_etl():
    print('Ejecutando ETL...')
    extract()
    transform()
    load()



if __name__ == '__main__':
    execute_etl()