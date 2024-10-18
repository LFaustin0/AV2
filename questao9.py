import re

def palavras (string):
    
    total = re.findall('[ ]', string)

    print(f"Total de palavras: {len(total) + 1}")

string = 'essa frase contém 10 palavras'
palavras(string)
