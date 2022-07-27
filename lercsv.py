import csv

with open('testecsv.csv', 'r', encoding='utf-8') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=",")
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print(f'\033[1;4m{linha}\033[m')
        else:
            print(linha)