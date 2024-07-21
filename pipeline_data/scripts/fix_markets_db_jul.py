from data_processing import Data

path_json = '../data_raw/data_companyA.json'
path_csv = '../data_raw/data_companyB.csv'

# extract data
data_companyA = Data(path_json, 'json')
data_companyB = Data(path_csv, 'csv')

# data transformation
# mapping the new default DB naming
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

data_companyB.rename_columns(key_mapping)

# data join
combined_data = Data.join(data_companyA.data, data_companyB.data)

# load data
path_total = '../data_processed/combined_data.csv'
combined_data.save(path_total)