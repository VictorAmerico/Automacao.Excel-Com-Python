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
