with open('dicionario.txt', 'w') as dic:
    dicionario = []
    for line in dic:
        dicionario = (dic.read().splitlines())
    line = line.replace("\r", "").replace("\n", "")
    dicionario.insert(0,line)
    
def check():
    with open('documento.txt', 'r+') as doc:
        documento = []
        ignorado = []
        for linha in doc:
            documento = (doc.read().splitlines())
        linha = linha.replace("\r", "").replace("\n", "")
        documento.insert(0,linha)
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