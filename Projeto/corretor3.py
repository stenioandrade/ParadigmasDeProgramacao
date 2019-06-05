import os
ignorado = []
documentofinal = []
dicionario = []
book = 'main-dict.txt'
text = 'documento.txt'
ignored = 'ignocred.txt'


def aceita(word):
    global book
    global ignorado
    ignorado.append(word)
    dicionario.append(word)
    add_to_dict(word)
    add_to_ignored(word)
#    with open(book, 'w') as dic:
#        dic.write(word + '\n')
#        dic.close()


def load_dict():
    global book
    global dicionario
    flag = True
    while(flag):
        try:
            with open(book, 'r') as dic:
                dicionario = dic.read().split()
                dic.close()
            flag = False
        except IOError:
            os.system('clear')
            print('                Falha ao abrir '+book)
            input()
    return


def save_dict():
    global book
    global dicionario
    flag = True
    while(flag):
        try:
            with open(book, 'w') as dic:
                for line in dicionario:
                    dic.write(str(line) + '\n')
        #        dic.write(word + '\n')
                dic.close()
            flag = False
        except IOError:
            os.system('clear')
            print('                Falha ao abrir '+book)


def add_to_dict(word):
    global book
    flag = True
    while(flag):
        try:
            with open(book, 'a') as dic:
                dic.write(word + '\n')
                dic.close()
            flag = False
        except IOError:
            os.system('clear')
            print('                Falha ao abrir '+book)
            input()


def get_word():
    global text
#    print('Qual o nome do seu documento?')
#    text = str(input())
#    if text[-4:] != '.txt':
#        text = book + '.txt'
#    os.system('clear')
    flag = True
    while(flag):
        try:
            with open(text, 'r') as doc:
                texto = doc.readlines()
                temp = [line[:-1] for line in texto]
                texto = temp
                doc.close()
            flag = False
        except IOError:
            os.system('clear')
            print('                Falha ao abrir '+text)
            input()
    return texto


def put_word():
    global text
    global documentofinal
    flag = True
    while(flag):
        try:
            with open(text, 'w') as doc:
                for line in documentofinal:
                    doc.write(str(line))
                doc.close()
            flag = False
        except IOError:
            os.system('clear')
            print('                Falha ao abrir '+text)
            input()


def add_to_ignored(word):
    global ignorado
    ignorado.append(word)
    flag = True
    while flag:
        try:
            with open(ignored, 'a') as ig:
                ig.write(word + '\n')
                ig.close()
            flag = False
        except IOError:
            os.system('clear')
            print('                Falha ao abrir '+ignored)
            input()


def clear_ignored():
    global ignorado
    flag = True
    while flag:
        try:
            with open(ignored, 'w') as ig:
                ig.close()
            ignorado[:] = []
            flag = False
        except IOError:
            os.system('clear')
            print('                Falha ao abrir '+ignored)
            input()


def consult_user(word):
    global book
    valido = True
    ctrl_2 = [1, 2, 3]
    while True:
        print('              ###################################################')
        print('              #             CORRETOR ORTOGRÁFICO                #')
        print('              ###################################################')
        print('              #           ________________________              #')
        print('              #           | Código |    Ação     |              #')
        print('              #           |________|_____________|              #')
        print('              #           |__(1)___|___Aceitar___|              #')
        print('              #           |__(2)___|___Ignorar___|              #')
        print('              #           |__(3)___|__Substituir_|              #')
        print('              #           |________|_____________|              #')
        print('              #                                                 #')
        print('              ###################################################')
        print('              "' + word + '" é uma palavra desconhecida o que fazer?')
        if valido:
            print('              Insira um codigo: ', end='')
        else:
            print('              Codigo inválido!')
            print('              Insira um válido por favor: ', end='')
        try:
            ctrl_1 = int(input())
            ctrl_2.index(ctrl_1)
            break
        except ValueError:
            os.system('clear')
            valido = False
    if ctrl_1 == 1:   #aceite
        aceita(word)
#        print('aceito')
        return word
    elif ctrl_1 == 2: #ignore
#        print('ignorado')
        add_to_ignored(word)
        return word
    elif ctrl_1 == 3: #substitua
        print('              Por qual palavra: ', end='')
        substituta = input()
#        print('substituido')
        return substituta
#        i = documento.index(word)
#        documento[i] = substituta

def is_known(word):
    global ignorado
    global dicionario
    try:
        dicionario.index(word)
    except ValueError:
        try:
            ignorado.index(word)
        except ValueError:
            raise ValueError
        
def process_document():
    global documentofinal
    texto = get_word()
    for line in texto:
        linha = line.split()
        for word in linha:
            try:
                is_known(word)
#                dicionario.index(word)
                documentofinal.append(word)
            except ValueError:
#                print(word)
                fst = word[1:]
                chfst = word[0]
                lst = word[:-1]
                chlst = word[-1]
                mid = word[1:-1]
                try:
                    is_known(fst)
#                    dicionario.index(fst)
                    documentofinal.append(chfst+fst)
                except ValueError:
#                    print(fst)
                    try:
                        is_known(lst)
#                        dicionario.index(lst)
                        documentofinal.append(lst+chlst)
                    except ValueError:
#                        print(lst)
                        try:
                            is_known(mid)
#                            dicionario.index(mid)
                            documentofinal.append(chfst+mid+chlst)
                        except ValueError:
#                            print(mid)
                            documentofinal.append(consult_user(word))
                            os.system('clear')
            documentofinal.append(' ')
        documentofinal.append('\n')
    put_word()
    print('              ###################################################')
    print('              #             CORRETOR ORTOGRÁFICO                #')
    print('              ###################################################')
    print('              #                                                 #')
    print('              #         Correção finalizada com sucesso!        #')
    print('              #                                                 #')
    print('              #         Vale 10 né professor?                   #')
    print('              #                                                 #')
    print('              ###################################################',end='')
    input()

def main():
    clear_ignored()
    load_dict()
    process_document()
    save_dict()
    clear_ignored()

if __name__ == "__main__":
    main()







































