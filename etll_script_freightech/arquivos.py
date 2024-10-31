
with open('load/armazem', 'r') as arquivo:
    linhas = arquivo.readlines()
    colunas = linhas[0].strip().split(',')
    for linha in linhas[1:]:
        if linha == linhas[1]: # se for a primeira linha
            indices = [i for i, coluna in enumerate(colunas) if coluna.strip()]
        else:
            valores = [valor.strip() for valor in linha.split(',')]
            # insert into tab(indices[0],indices[1],indices[2]) values (valores[0],valores[1],valores[2])
            # insert into tab("Vigencia","Unidade - CNPJ",	"Unidade - Nome") values (""ARMAZEM_1_10_2024","56228356017107","CDD BARREIRAS")
            

            # #    
        
        valores = linha.strip().split(',')
        # Aqui você pode inserir os valores no banco de dados
        print(f"Valores a serem inseridos: {valores}")
        
    
