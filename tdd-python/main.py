from bytebank import Funcionario

#allan = Funcionario('Allan Test', '13/03/2000', 1000)

#print(allan.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()