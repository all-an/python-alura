from bytebank import Funcionario

class TestBytebank:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24(self):
        # given - contexto
        entrada = '13/03/2000'
        esperado = 24

        funcionario_teste = Funcionario('Test', entrada, 1111)
        
        # when - ação
        resultado = funcionario_teste.idade()

        # then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # given
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        
        # when
        resultado = lucas.sobrenome()

        # then
        assert resultado == esperado