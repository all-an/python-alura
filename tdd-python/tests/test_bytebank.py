from bytebank import Funcionario
import pytest

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

    def test_quando_decrescimo_salario_recebe100000_deve_retornar_90000(self):
        entrada_nome = 'Paulo Bragança'
        entrada_salario = 100000
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_se_salario_maior_ou_igual100000_e_sobrenome_gerentes_retornaTrue(self):
        entrada_nome = 'Sergio Bragança'
        entrada_salario = 101000

        funcionario = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        eh_socio = funcionario._eh_socio()

        assert eh_socio == True
    
    def test_quando_calcular_bonus_recebe_salario_1000_deve_retornar_100(self):
        entrada_nome = 'Sergio Bragança'
        entrada_salario = 1000
        esperado = 100

        funcionario = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        bonus = funcionario.calcular_bonus()

        assert bonus == esperado

    def test_quando_calcular_bonus_recebe_salario_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_nome = 'Sergio Bragança'
            entrada_salario = 1000000

            funcionario = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
            resultado = funcionario.calcular_bonus()

            assert resultado