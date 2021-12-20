#Primeiro passo do algoritmo é inputar as variaveis de nome e idade para manipular durante o programa
nome=input('Digite o nome da criança: ')
idade=int(input('Agora a sua idade: '))

while True:
#Segundo,Cria um laço de repetição para colocar o usuário em loop até que digite "N" para sair do programa:
    if idade >=1:
        if idade <=5:
            #Entra em uma dupla checagem de condições para definir Faixa etaria do ensino:
            print('{} está na educação infantil.'.format(nome))
            cont = input('Deseja continuar? ,por favor digite "S" para sim e "N" para não:  ')
            #Atribui a variavel "cont" de continuar um valor que equivale a Sim ou Não, qualquer outro mostra opção invalida
            #se a opção for "S" de sim o usuario entra em loop de nomes idades através do continue, se "N" o programa encerra
            if cont == 'S':
                nome = input('Digite o nome da criança: ')
                idade = int(input('Agora a sua idade: '))
                continue
            elif cont == 'N':
                print('Encerrando o programa...')
                break
            else:
                print('Opção invalida')
                continue
    if idade>=6:
        if idade<=10:
            print('{} está no ensino fundamental I' .format(nome))
            cont = input('Deseja continuar? ,por favor digite "S" para sim e "N" para não:  ')
            if cont == 'S':
                nome = input('Digite o nome da criança: ')
                idade = int(input('Agora a sua idade: '))
                continue
            elif cont == 'N':
                print('Encerrando o programa...')
                break
            else:
                print('Opção invalida')
                continue

    if idade>=11:
        if idade<=14:
            print('{} está no Ensino Fundamental II' .format(nome))
            cont = input('Deseja continuar? ,por favor digite "S" para sim e "N" para não:  ')
            if cont == 'S':
                nome = input('Digite o nome da criança: ')
                idade = int(input('Agora a sua idade: '))
                continue
            elif cont == 'N':
                print('Encerrando o programa...')
                break
            else:
                print('Opção invalida')
                continue
        else:
            print('{} está no Ensino Medio.'.format(nome))
            cont = input('Deseja continuar? ,por favor digite "S" para sim e "N" para não:  ')
            if cont == 'S':
                nome = input('Digite o nome da criança: ')
                idade = int(input('Agora a sua idade: '))
                continue
            elif cont == 'N':
                print('Encerrando o programa...')
                break
            else:
                print('Opção invalida')
                continue






