with open('dicionario.txt', 'r+') as dic:
    dicionario = dic.read().split()
#    dicionario = dicionario.replace("\r", "").replace("\n", "")
    
with open('documento.txt', 'r+') as docin:
    documento = []
    ignorado = []
    documento = (docin.read().split())
    docfinal = list((set(documento) - set(dicionario)) - set(ignorado))
    
for item in docfinal:
    print(item + 'é uma palavra desconhecida o que fazer?')
    ctrl_2 = [1 , 2 , 3]
    while(True):
        print('(1) Aceitar\n(2) Ignorar\n(3) Substituir\nInsira um codigo: ',end='')
        ctrl_1 = int(input())
        try:
            ctrl_2.index(ctrl_1)
            break
        except ValueError:
            print('Codigo invalido, insira um valido!')
    if ctrl_1 == 1:   #aceite
        print('aceito')
        dicionario.append(item)
    elif ctrl_1 == 2: #ignore
        print('ignorado')
        ignorado.append(item)
    elif ctrl_1 == 3: #substitua
        print('substituido')
        print('Por qual palavra?')
        substituta = input()
        i = documento.index(item)
        documento[i] = substituta
        
char = []
str = ['hello','world!','(HELLO)','!WORLD']
pal = str[0]
print (pal[0])
for word in str:
        for ch in word:
            print (ch)
            if ch == '(' or ch == ')' or ch == '.' or ch == ',' or ch == '':
                
        
dic.close()
docin.close()
#docout.close()
with open('dicionario.txt', 'w') as dic:
    dic.write(dicionario)
with open('documento.txt', 'w') as doc:
    doc.write(documento)