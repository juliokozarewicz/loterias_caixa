from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import warnings
from pandas import DataFrame


warnings.filterwarnings("ignore")

def megasena_pesquisa_resultado(concurso):
    """
    Pesquisa o resultado da Mega-Sena pelo número do concurso.
    """

    try:
        
        options = Options() 
        options.add_argument("--incognito") # modo anônimo.
        options.add_argument("--disable-logging") # desativa 
        options.add_argument('--headless') # não abre a janela.
        options.add_argument('--log-level=3')
        options.add_argument("start-maximized") # caso precise abrir, maximiza.
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        navegador = webdriver.Chrome(
            
            executable_path='C:/Users/cadastro/anaconda3/chromedriver.exe',
            options=options
            
        )
        
        navegador.get(
            
            'https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx'
            
        )
        
        pesquisa_concurso = navegador.find_element(
            
            By.XPATH,
            '//*[@id="buscaConcurso"]'
            
        )
        
        pesquisa_concurso.send_keys(str(concurso))
        
        pesquisa_concurso.send_keys(Keys.ENTER)
        
        sleep(1)
        
        result_megasena = {
            
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
        
        for num in range(1,7):
            
            result_megasena[f'n{num}'] = pesquisa_concurso.find_element(
                
                By.XPATH,
                f'//*[@id="ulDezenas"]/li[{num}]'
                
            ).text
            
            result_megasena[f'n{num}'] = int(result_megasena[f'n{num}'])
        
        result_megasena['produto'] = 'megasena'
        
        result_megasena['concurso'] = concurso
        
        df_megasena_resultado = DataFrame([result_megasena])
        
        navegador.close()
    
    except Exception as error:
        print(error)
    
    return df_megasena_resultado

