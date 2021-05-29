from dominio import Usuario, Lance, Leilao, Avaliador

user1 = Usuario('Marcos')
user2 = Usuario('Pedro')

lance_user1 = Lance(user1,100.0)
lance_user2 = Lance(user2,150.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_user1)
leilao.lances.append(lance_user2)

for lance in leilao.lances:
    print(f"O {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')



