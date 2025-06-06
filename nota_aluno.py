gabarito = ['A , B ,C , D , E , E , E , D , C , B , A ']
maior_nota = 0
menor_nota = 0
total_alunos = 0
soma_notas = 0

def corrigir_prova(:)
    acertos = 0
    for i in ranger(10):
        resposta = input(f"Questão (i + 1): ").strip().upper()
        if resposta == gabarito[i]:
           acertos += 1
        return acertos
 
def mostrar_resultados(maior, menor, total, soma):
    if total > 0:
       media = soma / total 
    else: 
        media = 0
    print(f"\nMaior Acerto: (maior)")
    print(f"Menor Acerto : (menor)")
    print(f"Total de Alunos que Utilizaram o sistema: (total)")
    print(F"Media das Notas da Turma: (media:.2f)")

    while True:
        print(f"Aluno {total_alunos + 1}; insira sua resposta: ")      
        