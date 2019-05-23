import pandas as pd
import os

#http://sistemas.cvm.gov.br/?cadgeral
file_name = 'SPW_FI.txt'

file_path = os.path.join(file_name)

df = pd.read_csv(file_path, encoding='iso-8859-1', sep='\t')

df.to_excel('fundos_ativos.xls')