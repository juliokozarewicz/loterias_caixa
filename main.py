from pandas import read_excel, DataFrame, read_csv
from lotofacil_resultado import lotofacil_pesquisa_resultado
from megasena_resultado import megasena_pesquisa_resultado
import warnings


# I'm sorry for this =(
warnings.filterwarnings("ignore")

# conferência
data_input = read_excel(

    '1_data/raw/jogos_apostados.xlsx',
    sheet_name = 'jogos',
    header = 2,
    index_col = 'id'

    )

data_input = DataFrame(data_input)

lista_produtos = data_input['produto'].unique()

df_conferencia_final = DataFrame()

for produto in lista_produtos:

    df_produto = data_input[data_input['produto'] == produto]

    if produto == 'lotofacil':
        
        for id_linha in df_produto.index:
            
            df_linha = df_produto[df_produto.index == id_linha]
            
            colunas_df_linha = df_linha.columns
            
            # resultado lotofacil
            lotofacil_resultado = lotofacil_pesquisa_resultado(
                
                df_linha['concurso'].iloc[-1]
                
            )
            
            if (df_linha['concurso'].iloc[-1] == 
               lotofacil_resultado['concurso'].iloc[-1]):
                
                lista_num_acertados = []
                
                for coluna in colunas_df_linha:
                    
                    numero_apostado = df_linha[coluna]
                    
                    if (numero_apostado.values in 
                        lotofacil_resultado.iloc[:,0:15].values):
                        
                        num_apostado = int(numero_apostado.iloc[-1])
                        
                        lista_num_acertados.append(num_apostado)
                        
                        lista_num_acertados.sort()
                
                lista_acertos = [
                    
                    produto,
                    df_linha['concurso'].iloc[-1],
                    lista_num_acertados
                    
                ]
                
                df_conferencia = DataFrame(lista_acertos).T
                
                df_conferencia.columns = [
                    
                    'produto',
                    'concurso',
                    'numeros_acertados'
                    
                ]
                
                soma_acertos = len(lista_num_acertados)
                
                df_conferencia['qtd_acertos'] = soma_acertos
                
                if soma_acertos <= 10:
                    df_conferencia['situacao'] = ''
                
                if soma_acertos >= 11:
                    df_conferencia['situacao'] = f'premiada'
                
                df_conferencia_final = df_conferencia_final.append(
                    
                    df_conferencia
                    
                )

    if produto == 'megasena':
        
        for id_linha in df_produto.index:
            
            df_linha = df_produto[df_produto.index == id_linha]
            
            colunas_df_linha = df_linha.columns
            
            # resultado lotofacil
            megasena_resultado = megasena_pesquisa_resultado(
                
                df_linha['concurso'].iloc[-1]
                
            )
            
            if (df_linha['concurso'].iloc[-1] == 
               megasena_resultado['concurso'].iloc[-1]):
                
                lista_num_acertados = []
                
                for coluna in colunas_df_linha:
                    
                    numero_apostado = df_linha[coluna]
                    
                    if (numero_apostado.values in 
                        megasena_resultado.iloc[:,0:15].values):
                        
                        num_apostado = int(numero_apostado.iloc[-1])
                        
                        lista_num_acertados.append(num_apostado)
                        
                        lista_num_acertados.sort()
                
                lista_acertos = [
                    
                    produto,
                    df_linha['concurso'].iloc[-1],
                    lista_num_acertados
                    
                ]
                
                df_conferencia = DataFrame(lista_acertos).T
                
                df_conferencia.columns = [
                    
                    'produto',
                    'concurso',
                    'numeros_acertados'
                    
                ]
                
                soma_acertos = len(lista_num_acertados)
                
                df_conferencia['qtd_acertos'] = soma_acertos
                
                if soma_acertos <= 3:
                    df_conferencia['situacao'] = ''
                
                if soma_acertos >= 4:
                    df_conferencia['situacao'] = f'premiada'
                
                df_conferencia_final = df_conferencia_final.append(
                    
                    df_conferencia
                    
                )

df_conferencia_final = df_conferencia_final[

    df_conferencia_final['situacao'] == 'premiada'

].reset_index(drop=True)

print(df_conferencia_final)

df_conferencia_final.to_csv(

    '1_data/resultado_conferencia_final.txt',
    index_label='id'

)
