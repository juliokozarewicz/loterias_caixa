from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import warnings
from pandas import DataFrame


warnings.filterwarnings("ignore")

def lotomania_pesquisa_resultado(concurso):
    """
    Pesquisa o resultado da Lotomania pelo número do concurso.
    """

    try:
        
        options = Options() 
        options.add_argument('--headless') # não abre a janela.
        
        navegador = webdriver.Firefox(
            
            executable_path='C:/webdriver/geckodriver.exe',
            options=options
            
        )
        
        navegador.get(
            
            'https://loterias.caixa.gov.br/Paginas/Lotomania.aspx'
            
        )
        
        pesquisa_concurso = navegador.find_element(
            
            By.XPATH,
            '//*[@id="buscaConcurso"]'
            
        )
        
        pesquisa_concurso.send_keys(str(concurso))
        
        pesquisa_concurso.send_keys(Keys.ENTER)
        
        sleep(1)
        
        result_lotomania = {
            
            'n1': 0,
            'n2': 0,
            'n3': 0,
            'n4': 0,
            'n5': 0,
            'n6': 0,
            'n7': 0,
            'n8': 0,
            'n9': 0,
            'n10': 0,
            'n11': 0,
            'n12': 0,
            'n13': 0,
            'n14': 0,
            'n15': 0,
            'n16': 0,
            'n17': 0,
            'n18': 0,
            'n19': 0,
            'n20': 0,
            'produto': '',
            'concurso': 0
            
        }
        
        for num in range(1,21):
            
            result_lotomania[f'n{num}'] = pesquisa_concurso.find_element(
                
                By.XPATH,
                f'//*[@id="wp_resultados"]/div[2]/div/div/div[1]/ul/li[{num}]'
                
            ).text
            
            result_lotomania[f'n{num}'] = int(result_lotomania[f'n{num}'])
        
        result_lotomania['produto'] = 'lotomania'
        
        result_lotomania['concurso'] = concurso
        
        df_lotomania_resultado = DataFrame([result_lotomania])
        
        navegador.close()
    
    except Exception as error:
        print(error)
    
    return df_lotomania_resultado
