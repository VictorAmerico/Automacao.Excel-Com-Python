# Automacao.Excel-Com-Python
Automação De Excel Com Python

# Inicio do projeto

~~~python
from asyncio.windows_events import NULL


def converter_de_horas_minutos(num_horas):
    minutos = num_horas * 60
    return minutos

def convert__de_horas_para_segundos(num_horas):
    minutes = converter_de_horas_minutos(num_horas)
    segundos = minutes * 60
    return segundos

def converter_de_minutos_horas(num_nim):
    mhoras = num_nim/ 60
    return mhoras

def convert__de_minutos_para_segundos(num_nim):
    ssegundos = num_nim * 60
    return ssegundos



def converter_de_segundos_horas(num_segundos):
    segundos_horas = num_segundos/3600
    return segundos_horas

def convert__de_segundos_para_minutos(num_segundos):
    h_minutes = converter_de_segundos_horas(num_segundos)
    m_segundos = h_minutes * 60
    return m_segundos


escolha=True
while escolha:
    print("""
    =============HORAS===============
    1.Um unico poço trabalhando
    2.Dois poços trabalhando juntos
    3.Três poços trabalhando juntos
    4.Mostrar todos os tempos
    5.Exit/Quit/Saída
    =================================
    """)
    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        print('\n')
        hora = float(input('Número de horas que '
                           'um unico poço trabalhou: '))
    
        if hora <= 24:  
            print('\n')
            minuto = converter_de_horas_minutos(hora)
            #segundos = convert__de_horas_para_segundos(hora)
            print(str(hora) + ' horas são '+ str(minuto)+' minutos.')   
        else :
            print('\n')
            print("Não permitido") 
    elif escolha =="2":
        print('\n')
        hora2 = float(input('Número de horas que '
                           'dois poços trabalhabalharam juntos: '))

        if hora2 <= 24-hora:  
            print('\n')
            minuto2 = converter_de_horas_minutos(hora2)
            #segundos = convert__de_horas_para_segundos(hora2)
            print(str(hora2) + ' horas são '+ str(minuto2)+' minutos.')
        else :
            print('\n')
            print("Não permitido") 
    elif escolha == "3":
        print('\n')
        hora3 = float(input('Número de horas que '
                           'dois poços trabalhabalharam juntos: '))
        if hora3 <= 24-(hora + hora2):  
            print('\n')
            minuto3 = converter_de_horas_minutos(hora3)
            #segundos = convert__de_horas_para_segundos(hora2)
            print(str(hora3) + ' horas são '+ str(minuto3)+' minutos.')
        else :
            print('\n')
            print("Não permitido") 
            
          elif escolha=="4":
        if str(minuto)  == 'undefined':
            print("Nenhum tempo foi definido")
        else:
            print(str(minuto))
            print(str(minuto2))
            print(str(minuto3))
            
    elif escolha=="5":
      print("\n Adeus")
      escolha = None
    else:
       print("\n Escolha não válida.\n Tente outra vez.")
        
 ~~~
 
 # Segunda Etapa
 Aprendendo a integrar python com Execel com Openpyxl
 
 Créditos: <https://www.youtube.com/watch?v=rCRyCM4JC3E&ab_channel=DevAprender>
 
 #Primeiro contato com a integração Python-Excel (1/2)
 ~~~~python
 import openpyxl

#criar uma planilha(book)

book = openpyxl.Workbook();

#Como visualizar páginas existentes

print(book.sheetnames)

#Como criar uma página

book.create_sheet('Frutas')

#Como selecionar uma página

frutas_page = book['Frutas']
frutas_page.append(['Produto','Quantidade','Preço'])
frutas_page.append(['Banana','5','R$3,90'])
frutas_page.append(['Fruta 2','2','R$3,90'])
frutas_page.append(['Fruta 3','10','R$3,90'])
frutas_page.append(['Fruta 4','4','R$3,90'])

#Sakvar a planilha

book.save('Planilha de compras.xlsx')
 ~~~~
#Primeiro contato com a integração Python-Excel (2/2)

~~~python
import openpyxl

#Carregando arquivo
book = openpyxl.load_workbook('Planilha de compras.xlsx')
#Selecionando uma página
frutas_page = book['Frutas']
#Imprimindo os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2,max_row=5):
    for cell in rows:
        #print(f'{rows[0].value},{rows[1].value},{rows[2].value}')
        if cell.value == 'Banana':
            cell.value = 'Fruta 1'

#Salvar Alterações
book.save('Planilha de Compras v2.xlsx')

~~~
