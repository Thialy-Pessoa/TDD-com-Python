from unittest import TestCase
from dominio import Usuario, Lance, Leilao


# Aprender mais bibliotecas
# Construção de um cenario para reduzir possibilidades de erros

class TestLeilao(TestCase):

    def setUp(self):
        self.user1 = Usuario('Marcos')
        self.user2 = Usuario('Pedro')
        self.lance_user1 = Lance(self.user1, 100.0)
        self.lance_user2 = Lance(self.user2, 150.0)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_menor_valor_de_um_lance_quando_adicionados_em_orem_crescente(self):
        self.leilao.propoe(self.lance_user1)
        self.leilao.propoe(self.lance_user2)

        menor_valor_esoerado = 100
        maior_valor_esperado = 150

        #Usamos o assertequal quando queremos comparar valores
        #o primeiro é o valor esperado, o segundo o valor retornado
        self.assertEqual(menor_valor_esoerado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(ValueError):

            self.leilao.propoe(self.lance_user2)
            self.leilao.propoe(self.lance_user1)


    def test_quando_apenas_1_lance_eh_recebido(self):
        # Deve retornar o mesmo valor para o menor e o maior lance.

        self.leilao.propoe(self.lance_user1)

        self.assertEqual(100, self.leilao.menor_lance)
        self.assertEqual(100, self.leilao.maior_lance)

    def test_quando_apenas_varios_lance_recebido(self):
        # Com essa estrututa foi possivel passar
        # Aprenda a deixar a estrutura de condição melhor

        user3 = Usuario('Agar')

        lance_user3 = Lance(user3, 220.0)

        self.leilao.propoe(self.lance_user1)
        self.leilao.propoe(self.lance_user2)
        self.leilao.propoe(lance_user3)

        maior_valor_esperado = 220
        menor_valor_esoerado = 100

        self.assertEqual(menor_valor_esoerado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # Se o leilao não tiver lances deve permitir porpor um lace
    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_user1)

        quantidade_lances_receidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_lances_receidos)

    # Se o usuario seguinte for diferente deve permitir propor o lance
    def teste_deve_permitir_lance_quando_os_ultimos_usuarios_sao_diferentes(self):
        self.leilao.propoe(self.lance_user1)
        self.leilao.propoe(self.lance_user2)

        quantidade_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances_recebidos)

    # Se o ultimo usuario for igual ao antecessor não deve permitir lances
    def teste_se_o_ultimo_e_penultimo_forem_iguais_nao_permitir_lances(self):
        novo_lance_user2 = Lance(self.user2,230)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_user2)
            self.leilao.propoe(novo_lance_user2)


    #Os lances só podem ser crescentes.
#    def tests_lances_crescentes(self):
