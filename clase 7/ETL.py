import pandasql as ps
import pandas as pd
import os


class ETL:
    def __init__(self, 
                 name: str,
                 input_path: str = './inputs', 
                 output_path: str = './outputs', 
                 queries_path: str = './queries.sql'
                ):
        self.name = name
        self.input_path = input_path
        self.output_path = output_path
        self.queries_path = queries_path
        self.dataset = {}


    def pysqldf(self, query: str):
        print("Ejecutando query...")

        if 'create table' in query.lower():
            nombre_tabla = query.split(' ')[2]
            print(f"Creando tabla {nombre_tabla}")

            query_select = query.replace(f'create table {nombre_tabla} as', '')
            
            result = ps.sqldf(query_select, self.dataset)
            self.dataset[nombre_tabla] = result
            return result

        return ps.sqldf(query, self.dataset)
    
    def parse_queries(self) -> list[str]:
        with open(self.queries_path, 'r') as file:
            queries = file.read()
        return queries.split(';')

    def extract(self):
        print("Extrayendo datos...")

        for file in os.listdir(self.input_path):
            print('Extrayendo datos del archivo ', file)
            # nombre_tabla = file.split('.')[0]
            nombre_tabla = file.replace('.csv', '')
            self.dataset[nombre_tabla] = pd.read_csv(f'{self.input_path}/{file}', sep=';')

    def transform(self):
        print("Transformando datos...")
        queries = self.parse_queries()

        for query in queries:
            self.pysqldf(query)

    
    def load(self):
        print("Cargando datos...")
        for table in self.dataset.keys():
            if 'out' in table.lower():
                file_name = table.replace('out_', '')
                print("Cargando tabla: ", file_name)
                self.dataset[table].to_csv(f'{self.output_path}/{file_name}.csv', index=False)

    def execute(self):
        print(f"--------------- Ejecutando ETL: {self.name} ---------------")
        self.extract()
        self.transform()
        self.load()
        print(f"--------------- ETL {self.name} ejecutada correctamente ---------------")