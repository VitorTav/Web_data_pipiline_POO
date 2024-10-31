from funcoes import Navegador
import getpass
import time
from funcoes import Validacao
from selenium.webdriver.common.by import By
import pandas as pd


xpath_email_login = "/html/body/app-root/ft-core-login/div/div/div/wac-input/div/div/input"
xpath_senha = "//input[contains(@class,'input is-medium')]"
xpath_entrar = "/html/body/app-root/ft-core-login/div/div/div/wac-button[1]/button"
xpath_exportacao = "/html/body/app-root/ft-home/div/main/aside[1]/ft-menu-lateral/wac-sidebar/div/wac-sidebar-child[2]/div/wac-sidebar-item[5]/div/a"
xpath_modelo_exportacao = "html[1]/body[1]/app-root[1]/ft-home[1]/div[1]/main[1]/div[1]/wac-exportacao-dados[1]/div[1]/div[1]/wac-select[1]/ng-select[1]/div[1]"
xpath_rota_import = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/div[1]/div/wac-select/ng-select/ng-dropdown-panel/div/div[2]/div[2]"
xpath_as_import = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/div[1]/div/wac-select/ng-select/ng-dropdown-panel/div/div[2]/div[3]"
xpath_aramazem_import = "//span[text()='ARMAZÉM']"
xpath_insumos_import = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/div[1]/div/wac-select/ng-select/ng-dropdown-panel/div/div[2]/div[5]"
xpath_empurrada_import = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/div/div/wac-select/ng-select/ng-dropdown-panel/div/div[2]/div[4]"
xpath_zerar_filtro_canal = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[1]/div/ft-segmentos/div/wac-select/ng-select/div/span[1]"
xpath_zerar_filtro_status = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[3]/wac-select/ng-select/div/span[1]"
xpath_filtro_de_exportacoes= "//div[@placement='top']"
xpath_canal_segmento = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[1]/div/ft-segmentos/div/wac-select/ng-select/div"
xpath_filtro_canal_Rota = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[1]/div/ft-segmentos/div/wac-select/ng-select/ng-dropdown-panel/div[1]/div[2]/div[2]"
xpath_click_div_out_filter = "(//div[@class='sm v-space'])[3]"
xpath_status_arquivo = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[3]/wac-select/ng-select/div/div/div[2]/input"
xpath_disponivel_para_donwload = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[3]/wac-select/ng-select/ng-dropdown-panel/div/div[2]/div[4]"
xpath_fechar_filtro = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[1]/div[2]/em"
xpath_atualizar_canais_por_filtro = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[2]/div/wac-flexbar/div/wac-flexbar-child[2]/div/wac-button/button"
xpath_filtro_canal_AS = "(//div[@class='opt-template ng-star-inserted'])[2]"
xpath_filtro_canal_Empurrada = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[1]/div/ft-segmentos/div/wac-select/ng-select/ng-dropdown-panel/div[1]/div[2]/div[7]/div"
xpath_to_scrol_empurrada = "//span[@class='ng-option-label ng-star-inserted']"
xpath_filtro_canal_armazem = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[1]/div/ft-segmentos/div/wac-select/ng-select/ng-dropdown-panel/div[1]/div[2]/div[5]"
xpath_filtro_canal_Insumos = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/ft-acompanhamento-filtros/ft-drawer/div/div/div/div[1]/div[2]/div[1]/div/ft-segmentos/div/wac-select/ng-select/ng-dropdown-panel/div[1]/div[2]/div[8]"


### DATA FRAMES 


xpath_vigencia = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/div[2]/wac-box/div/div/div[2]/ft-escolha-segmento/div/div[2]/div/wac-select/ng-select/div"
xpath_opcoes = "(//div[@role='option']//div)[1]"
xpath_opcoes2 = "(//div[@role='option']//div)[2]"
xpath_dropdown = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/div[2]/wac-box/div/div/div[2]/ft-escolha-segmento/div/div[2]/div/wac-select/ng-select/ng-dropdown-panel"
xpath_fechar_pesquisa = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/div[2]/wac-box/div/div/div[2]/ft-escolha-segmento/div/div[2]/div/wac-select/ng-select/div/span[1]"
xpath_unidades = "//div[@id='unidadeSelect']/div[1]/wac-select[1]/ng-select[1]/div[1]/div[1]/div[2]/input[1]"
xpath_marcar_todos = "(//button[@class='button is-secondary'])[2]"
xpath_touch_for_scrool = "/html/body/app-root/ft-home/div/main/div/wac-exportacao-dados/wac-title/h3"
xpath_exportar_valores = "(//button[@class='button is-secondary'])[3]"
xpath_acompanhamento_exportacoes = "/html/body/app-root/ft-home/div/main/aside[1]/ft-menu-lateral/wac-sidebar/div/wac-sidebar-child[2]/div/wac-sidebar-item[2]/div/a"
xpath_tabela_de_exportação = "//div[contains(@class,'ag-root-wrapper ag-layout-normal')]"
xpath_filtro_tabela_rota = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/div/wac-box/div/div/wac-flexbar/div/wac-flexbar-child[2]/div/div"
xpath_exportar_tabela_Rota = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/div/div/div/div/ft-dinamic-grid/ag-grid-angular/div/div[2]/div[2]/div[3]/div[3]/div[1]/div/div/span[1]/img"
xpath_exportar_tabela_AS = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/div/div/div/div/ft-dinamic-grid/ag-grid-angular/div/div[2]/div[2]/div[3]/div[3]/div[1]/div/div/span[1]/img"
xpath_exorportar_tabela_Empurrada = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/div/div/div/div/ft-dinamic-grid/ag-grid-angular/div/div[2]/div[2]/div[3]/div[3]/div[1]/div/div/span[1]/img"
xpath_exportar_tabela_Armazem = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/div/div/div/div/ft-dinamic-grid/ag-grid-angular/div/div[2]/div[2]/div[3]/div[3]/div[1]/div/div/span[1]/img"
xpath_exportar_tabela_Insumos = "/html/body/app-root/ft-home/div/main/div/ft-acompanhamento-exportacoes/div/div/div/div/div/ft-dinamic-grid/ag-grid-angular/div/div[2]/div[2]/div[3]/div[3]/div[1]/div/div/span[1]/img"
xpath_div_scroll_armazem = "//span[text()='INSUMOS']"
xpath_pesquisa = "(//label[text()=' Funcionalidades ']/following::input)[2]"


'-------------------------------------------------------------------------------------------------------------------------------'

user = 'igor.silva@grupohorizonte.com.br'
key = 'Igor@1407'
armazem = "Armazem"
host_name = "172.16.0.28" 
user_name = "joaotavares" 
user_password = "@joaotavares"
database='dbfreightech'





'-------------------------------------------------------------------------------------------------------------------------------'



usuario = getpass.getuser()
navegador = Navegador(usuario)
validacao = Validacao("C:\\Freightech\\load")
url = 'https://www.google.com'
url_freigtech = 'https://freightech.ambev.com.br/#/login'
navegador.abrir_navegador(url)
time.sleep(5)
print(f"Iniciado")
navegador.change_tab_with_interactions(url_freigtech) 
time.sleep(25)
# navegador.fechar_primeira_janela()
# time.sleep(2)
navegador.click(xpath_email_login)
time.sleep(8)
navegador.escreva_digitando(xpath_email_login,user)
time.sleep(3)
navegador.click(xpath_senha)
time.sleep(3)
navegador.escreva_digitando(xpath_senha,key)
time.sleep(4)
navegador.click(xpath_entrar)
time.sleep(45)
print(f'Autenticado no sistema')

###Canal Rota 


navegador.click(xpath_exportacao)
time.sleep(10) 
navegador.click(xpath_modelo_exportacao)
time.sleep(10)
navegador.click(xpath_rota_import)
time.sleep(10)
print(f"Canal Rota Selecionado")
time.sleep(10)
navegador.click(xpath_fechar_pesquisa)
time.sleep(10) 
navegador.click(xpath_vigencia)
time.sleep(10)
navegador.click(xpath_opcoes)
time.sleep(3)
navegador.click(xpath_opcoes2)
time.sleep(10)
navegador.click(xpath_unidades)
time.sleep(10)
navegador.click(xpath_marcar_todos)
time.sleep(10)
navegador.click(xpath_touch_for_scrool)
time.sleep(2)
navegador.scroll_down()
time.sleep(2)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.click(xpath_exportar_valores)
time.sleep(240)
navegador.refresh_pagina()
time.sleep(10)
navegador.click(xpath_acompanhamento_exportacoes)
time.sleep(10)
navegador.click(xpath_filtro_de_exportacoes)
time.sleep(25)
try:
    elemento = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_canal)
    if elemento.is_displayed() and elemento.is_enabled():
        elemento.click()
    else:
        print("Elemento para zerar filtro do canal não está visível ou habilitado.")
except Exception as rota:
    print(f"Erro ao zerar o filtro do canal: {rota}")  

time.sleep(5)    
navegador.click(xpath_canal_segmento)
time.sleep(5)
navegador.click(xpath_to_scrol_empurrada)
time.sleep(5)
navegador.click(xpath_filtro_canal_Rota)
time.sleep(5)
navegador.click(xpath_click_div_out_filter)
time.sleep(5)
try:
    elemento_status = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_status)
    if elemento_status.is_displayed() and elemento_status.is_enabled():
        elemento_status.click()
    else:
        print("Elemento para zerar filtro de status não está visível ou habilitado.")
except Exception as status:
    print(f"Erro ao zerar o filtro de status: {status}")
navegador.click(xpath_status_arquivo)
time.sleep(5)
navegador.click(xpath_disponivel_para_donwload)
time.sleep(5)
navegador.click(xpath_atualizar_canais_por_filtro)
time.sleep(5)
navegador.click(xpath_exportar_tabela_Rota)
time.sleep(60)
# navegador.change_tab_with_interactions(url_freigtech)
# time.sleep(35)
nome_rota = navegador.mover_arquivo('rota')
time.sleep(15)
# resultado = validacao.verificar_integridade_xlsx("C:\\Freightech\\load\\ROTA")
# print(f"A integridade do CSV é: {resultado}")
time.sleep(40)




###CANAL AS

navegador.click(xpath_exportacao)
time.sleep(10) 
navegador.click(xpath_modelo_exportacao)
time.sleep(10) 
navegador.click(xpath_as_import)
time.sleep(10)
print(f"AS Selecionado")
navegador.click(xpath_fechar_pesquisa)
time.sleep(10) 
navegador.click(xpath_vigencia)
time.sleep(10)
navegador.click(xpath_opcoes)
time.sleep(3)
navegador.click(xpath_opcoes2)
time.sleep(10)
navegador.click(xpath_unidades)
time.sleep(10)
navegador.click(xpath_marcar_todos)
time.sleep(10)
navegador.click(xpath_touch_for_scrool)
time.sleep(2)
navegador.scroll_down()
time.sleep(2)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.click(xpath_exportar_valores)
time.sleep(180)
navegador.refresh_pagina()
time.sleep(15)
navegador.click(xpath_acompanhamento_exportacoes)
time.sleep(10)
navegador.click(xpath_filtro_de_exportacoes)
time.sleep(25)
try:
    elemento = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_canal)
    if elemento.is_displayed() and elemento.is_enabled():
        elemento.click()
    else:
        print("Elemento para zerar filtro do canal não está visível ou habilitado.")
except Exception as As:
    print(f"Erro ao zerar o filtro do canal: {As}")  

time.sleep(5)    
navegador.click(xpath_canal_segmento)
time.sleep(5)
navegador.click(xpath_filtro_canal_AS)
time.sleep(5)
navegador.click(xpath_click_div_out_filter)
time.sleep(5)
try:
    elemento_status = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_status)
    if elemento_status.is_displayed() and elemento_status.is_enabled():
        elemento_status.click()
    else:
        print("Elemento para zerar filtro de status não está visível ou habilitado.")
except Exception as status:
    print(f"Erro ao zerar o filtro de status: {status}")
navegador.click(xpath_status_arquivo)
time.sleep(5)
navegador.click(xpath_disponivel_para_donwload)
time.sleep(5)
navegador.click(xpath_atualizar_canais_por_filtro)
time.sleep(5)
navegador.click(xpath_exorportar_tabela_Empurrada)
time.sleep(60)
# navegador.change_tab_with_interactions(url_freigtech)
# time.sleep(35)
nome_as = navegador.mover_arquivo('as')
# resultado = validacao.verificar_integridade_xlsx("C:\\Freightech\\load\\AS")
# print(f"A integridade do CSV é: {resultado}")
time.sleep(40)


###CANAL EMPURRADA 

navegador.click(xpath_exportacao)
time.sleep(10)
navegador.click(xpath_modelo_exportacao)
time.sleep(10)
navegador.click(xpath_empurrada_import)
time.sleep(10)
print(f"Empurrada Selecionado")
navegador.click(xpath_fechar_pesquisa)
time.sleep(10) 
navegador.click(xpath_vigencia)
time.sleep(10)
navegador.click(xpath_opcoes)
time.sleep(10)
navegador.click(xpath_opcoes2)
time.sleep(3)
navegador.click(xpath_unidades)
time.sleep(10)
navegador.click(xpath_marcar_todos)
time.sleep(10)
navegador.click(xpath_touch_for_scrool)
time.sleep(2)
navegador.scroll_down()
time.sleep(2)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.click(xpath_exportar_valores)
time.sleep(120)
navegador.refresh_pagina()
time.sleep(15)
navegador.click(xpath_acompanhamento_exportacoes)
time.sleep(10)
navegador.click(xpath_filtro_de_exportacoes)
time.sleep(25)
try:
    elemento = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_canal)
    if elemento.is_displayed() and elemento.is_enabled():
        elemento.click()
    else:
        print("Elemento para zerar filtro do canal não está visível ou habilitado.")
except Exception as empurrada:
    print(f"Erro ao zerar o filtro do canal: {empurrada}")  

time.sleep(5)    
navegador.click(xpath_canal_segmento)
time.sleep(5)
navegador.click(xpath_filtro_canal_Empurrada)
time.sleep(5)
navegador.click(xpath_click_div_out_filter)
time.sleep(5)
try:
    elemento_status = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_status)
    if elemento_status.is_displayed() and elemento_status.is_enabled():
        elemento_status.click()
    else:
        print("Elemento para zerar filtro de status não está visível ou habilitado.")
except Exception as status:
    print(f"Erro ao zerar o filtro de status: {status}")
navegador.click(xpath_status_arquivo)
time.sleep(5)
navegador.click(xpath_disponivel_para_donwload)
time.sleep(5)
navegador.click(xpath_atualizar_canais_por_filtro)
time.sleep(5)
navegador.click(xpath_exorportar_tabela_Empurrada)
time.sleep(60)
# navegador.change_tab_with_interactions(url_freigtech)
# time.sleep(35)
nome_empurrada = navegador.mover_arquivo('empurrada')

# resultado = validacao.verificar_integridade_xlsx("C:\\Freightech\\load\\EMPURRADA")
# print(f"A integridade do CSV é: {resultado}")
time.sleep(40)


##  CANAL DE ARMAZEM 


navegador.click(xpath_exportacao)
time.sleep(10)
navegador.click(xpath_modelo_exportacao)
time.sleep(10)
navegador.escreva_digitando(xpath_pesquisa,armazem)
time.sleep(3)
navegador.click(xpath_aramazem_import)
time.sleep(10)
print(f"Armazém Selecionado")
navegador.click(xpath_fechar_pesquisa)
time.sleep(10) 
navegador.click(xpath_vigencia)
time.sleep(10)
navegador.click(xpath_opcoes)
time.sleep(3)
navegador.click(xpath_opcoes2)
time.sleep(10)
navegador.click(xpath_unidades)
time.sleep(10)
navegador.click(xpath_marcar_todos)
time.sleep(10)
navegador.click(xpath_touch_for_scrool)
time.sleep(2)
navegador.scroll_down()
time.sleep(2)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.click(xpath_exportar_valores)
time.sleep(180)
navegador.refresh_pagina()
time.sleep(15)
navegador.click(xpath_acompanhamento_exportacoes)
time.sleep(10)
navegador.click(xpath_filtro_de_exportacoes)
time.sleep(25)
try:
    elemento = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_canal)
    if elemento.is_displayed() and elemento.is_enabled():
        elemento.click()
    else:
        print("Elemento para zerar filtro do canal não está visível ou habilitado.")
except Exception as armazem:
    print(f"Erro ao zerar o filtro do canal: {armazem}")  

time.sleep(5)    
navegador.click(xpath_canal_segmento)
time.sleep(5)
navegador.click(xpath_filtro_canal_armazem)
time.sleep(5)
navegador.click(xpath_click_div_out_filter)
time.sleep(5)
try:
    elemento_status = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_status)
    if elemento_status.is_displayed() and elemento_status.is_enabled():
        elemento_status.click()
    else:
        print("Elemento para zerar filtro de status não está visível ou habilitado.")
except Exception as status:
    print(f"Erro ao zerar o filtro de status: {status}")
navegador.click(xpath_status_arquivo)
time.sleep(5)
navegador.click(xpath_disponivel_para_donwload)
time.sleep(5)
navegador.click(xpath_atualizar_canais_por_filtro)
time.sleep(5)
navegador.click(xpath_exportar_tabela_Armazem)
time.sleep(60)
# navegador.change_tab_with_interactions(url_freigtech)
# time.sleep(35)
nome_armazem = navegador.mover_arquivo('armazem')
time.sleep(1)
# resultado = validacao.verificar_integridade_xlsx("C:\\Freightech\\load\\ARMAZEM")
# print(f"A integridade do CSV é: {resultado}")
time.sleep(40)


###CANAL DE INSUMOS 

navegador.click(xpath_exportacao)
time.sleep(10)
navegador.click(xpath_modelo_exportacao)
time.sleep(10)
navegador.click(xpath_insumos_import)
time.sleep(10)
print(f"Insumos Selecionado")
navegador.click(xpath_fechar_pesquisa)
time.sleep(10) 
navegador.click(xpath_vigencia)
time.sleep(10)
navegador.click(xpath_opcoes)
time.sleep(3)
navegador.click(xpath_opcoes2)
time.sleep(10)
navegador.click(xpath_unidades)
time.sleep(10)
navegador.click(xpath_marcar_todos)
time.sleep(10)
navegador.click(xpath_touch_for_scrool)
time.sleep(2)
navegador.scroll_down()
time.sleep(2)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.scroll_down()
time.sleep(1)
navegador.click(xpath_exportar_valores)
time.sleep(180)
navegador.refresh_pagina()
time.sleep(10)
navegador.click(xpath_acompanhamento_exportacoes)
time.sleep(10)
navegador.click(xpath_filtro_de_exportacoes)
time.sleep(25)
try:
    elemento = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_canal)
    if elemento.is_displayed() and elemento.is_enabled():
        elemento.click()
    else:
        print("Elemento para zerar filtro do canal não está visível ou habilitado.")
except Exception as insumos:
    print(f"Erro ao zerar o filtro do canal: {insumos}")  

time.sleep(5)    
navegador.click(xpath_canal_segmento)
time.sleep(5)
navegador.click(xpath_filtro_canal_Insumos)
time.sleep(5)
navegador.click(xpath_click_div_out_filter)
time.sleep(5)
try:
    elemento_status = navegador.navegador.find_element(By.XPATH, xpath_zerar_filtro_status)
    if elemento_status.is_displayed() and elemento_status.is_enabled():
        elemento_status.click()
    else:
        print("Elemento para zerar filtro de status não está visível ou habilitado.")
except Exception as status:
    print(f"Erro ao zerar o filtro de status: {status}")
navegador.click(xpath_status_arquivo)
time.sleep(5)
navegador.click(xpath_disponivel_para_donwload)
time.sleep(5)
navegador.click(xpath_atualizar_canais_por_filtro)
time.sleep(5)
navegador.click(xpath_exportar_tabela_AS)
time.sleep(60)
# navegador.change_tab_with_interactions(url_freigtech)
# time.sleep(35)
nome_insumos = navegador.mover_arquivo('insumos')

# resultado = validacao.verificar_integridade_xlsx("C:\\Freightech\\load\\INSUMOS")
# print(f"A integridade do CSV é: {resultado}")
time.sleep(40)

conexao = validacao.conectar_banco(host_name,user_name,user_password,database)

nomes_arquivo = [nome_rota,nome_as,nome_empurrada,nome_armazem,nome_insumos]
for nome_arquivo in nomes_arquivo:
    #nome_arquivo = 'C:\\Users\\admin.joao\\Documents\\ARMAZEM\\ARMAZÉM_2024-09-30_10-31-09.xlsx'
    arquivo_excel = pd.ExcelFile(nome_arquivo)
    nomes_abas = arquivo_excel.sheet_names

    for nome_aba in nomes_abas:
        arquivo = pd.read_excel(nome_arquivo, sheet_name=nome_aba)
        colunas = arquivo.columns.tolist()
        todosValores = "";
        for index, linha in arquivo.iterrows():
            if index == 0: # se for a primeira linha
                tabela = 'Armazem'
                indices = [coluna.strip() for coluna in colunas if coluna.strip()]
                indices = ','.join(['"'+indice+'"' for indice in indices])
                #print(indices)
            else:
                valores = linha.tolist()
                valores_string = ','.join(['"'+str(valor)+'"' for valor in valores])  # Converte cada valor para string, coloca entre aspas e junta com ","
                valores_string = "(" + valores_string + "),"
                todosValores = todosValores+ valores_string

        todosValores = todosValores.rstrip(',')
        sql = "insert into "+nome_aba+"("+indices+") values " 
        sql = sql+todosValores


try:
    cursor = conexao.cursor()
    cursor.execute(sql)
except Exception as e:
    print(f"Erro ao executar insert: {e}")


        


    

        # with open('C:\\Users\\admin.joao\\Documents\\ARMAZEM\\sql_query_' + nome_aba + '.txt', 'w') as arquivo_sql:
        #     arquivo_sql.write(sql)










