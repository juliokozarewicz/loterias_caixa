from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import warnings
from pandas import DataFrame


warnings.filterwarnings("ignore")

def lotofacil_pesquisa_resultado(concurso):
    """
    Pesquisa o resultado da Lotofácil pelo número do concurso.
    """

    try:
        
        options = Options() 
        options.add_argument("--incognito")
        options.add_argument("--disable-logging")
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        navegador = webdriver.Chrome(
            
            executable_path='C:/Users/cadastro/anaconda3/chromedriver.exe',
            options=options
            
        )
        
        navegador.get(
            
            'https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx'
            
        )
        
        pesquisa_concurso = navegador.find_element(
            
            By.XPATH,
            '//*[@id="buscaConcurso"]'
            
        )
        
        pesquisa_concurso.send_keys(str(concurso))
        
        pesquisa_concurso.send_keys(Keys.ENTER)
        
        sleep(1)
        
        result_lotofacil = {
            
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
            'produto': '',
            'concurso': 0
            
        }
        
        for num in range(1,16):
            
            result_lotofacil[f'n{num}'] = pesquisa_concurso.find_element(
                
                By.XPATH,
                f'//*[@id="wp_resultados"]/div[2]/div/div/div[1]/ul/li[{num}]'
                
            ).text
            
            result_lotofacil[f'n{num}'] = int(result_lotofacil[f'n{num}'])
        
        result_lotofacil['produto'] = 'lotofacil'
        
        result_lotofacil['concurso'] = concurso
        
        df_lotofacil_resultado = DataFrame([result_lotofacil])
        
        navegador.close()
    
    except Exception as error:
        print(error)
    
    return df_lotofacil_resultado
