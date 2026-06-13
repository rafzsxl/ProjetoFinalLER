import json
import os
from datetime import datetime, timedelta

ARQUIVO_ALUNOS = "alunos.json"
ARQUIVO_LIVROS = "livros.json"
ARQUIVO_EMPRESTIMOS = "emprestimos.json"

def carregar_dados():
    alunos = {}
    livros = {}
    emprestimos = []

    if os.path.exists(ARQUIVO_ALUNOS):
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
            alunos = json.load(f)
    if os.path.exists(ARQUIVO_LIVROS):
        with open(ARQUIVO_LIVROS, "r", encoding="utf-8") as f:
            livros = json.load(f)
            for titulo, dados in livros.items():
                if "classificação" in dados:
                    dados["classificacao"] = dados.pop("classificação")
    if os.path.exists(ARQUIVO_EMPRESTIMOS):
        with open(ARQUIVO_EMPRESTIMOS, "r", encoding="utf-8") as f:
            emprestimos = json.load(f)

    return alunos, livros, emprestimos

def salvar_dados(alunos, livros, emprestimos):
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
    with open(ARQUIVO_LIVROS, "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)
    with open(ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8") as f:
        json.dump(emprestimos, f, indent=4, ensure_ascii=False)

def cadastrar_aluno(alunos):
    print("\n--- CADASTRO DE ALUNO ---")
    
    while True:
        cpf = input("CPF (Apenas números): ").strip()
        if not cpf:
            print("Erro: O CPF não pode ser vazio.")
        elif not cpf.isdigit():
            print("⚠️ ERRO: O CPF deve conter apenas números!")
        elif cpf in alunos:
            print("Erro: Este CPF já está cadastrado.")
            return
        else:
            break

    while True:
        nome = input("Nome completo: ").strip().lower()
        if nome:
            break
        print("Erro: O nome não pode ser vazio.")

    while True:
        idade_input = input("Idade: ").strip()
        if not idade_input:
            print("Erro: A idade não pode ser vazia.")
        elif not idade_input.isdigit():
            print("⚠️ ERRO: A idade deve conter apenas números!")
        else:
            idade = int(idade_input)
            break

    alunos[cpf] = {"nome": nome, "idade": idade}
    print(f"Aluno {nome.title()} cadastrado com sucesso!")

def cadastrar_livro(livros):
    print("\n--- CADASTRO DE LIVRO ---")
    
    while True:
        titulo = input("Título do livro: ").strip().lower()
        if not titulo:
            print("Erro: O título não pode ser vazio.")
        elif titulo in livros:
            print("Erro: Este livro já está cadastrado.")
            return
        else:
            break
            
    while True:
        autor = input("Autor: ").strip().lower()
        if autor:
            break
        print("Erro: O autor não pode ser vazio.")

    classificacoes_validas = ["livre", "10", "12", "14", "16", "18"]
    
    while True:
        classificacao = input("Classificação etária (Livre, 10, 12, 14, 16, 18): ").strip().lower()
        if classificacao in classificacoes_validas:
            classificacao_formatada = "Livre" if classificacao == "livre" else classificacao
            break
        print("⚠️ ERRO: Opção inválida! Digite exatamente: Livre, 10, 12, 14, 16 ou 18.")

    livros[titulo] = {"autor": autor, "classificacao": classificacao_formatada, "disponivel": True}
    print(f"Livro '{titulo.title()}' cadastrado com sucesso!")

def buscar_livro(livros):
    print("\n--- BUSCA NO ACERVO ---")
    termo = input("Digite o título ou autor para buscar: ").lower().strip()
    encontrados = False

    for titulo, dados in livros.items():
        if termo in titulo or termo in dados["autor"]:
            status = "Disponível" if dados["disponivel"] else "Emprestado"
            faixa = dados.get("classificacao", "Não informada")
            print(f"- Título: {titulo.title()} | Autor: {dados['autor'].title()} | Classificação: {faixa} | Status: {status}")
            encontrados = True

    if not encontrados:
        print("Nenhum livro encontrado com esse termo.")

def registrar_emprestimo(alunos, livros, emprestimos):
    print("\n--- REGISTRO DE EMPRÉSTIMO ---")
    cpf = input("CPF do aluno: ").strip()
    if cpf not in alunos:
        print("Erro: Aluno não cadastrado.")
        return

    livros_com_aluno = sum(1 for e in emprestimos if e["cpf_aluno"] == cpf and not e["devolvido"])
    if livros_com_aluno >= 3:
        print("Erro: O aluno já atingiu o limite de 3 livros emprestados!")
        return

    titulo = input("Título do livro: ").strip().lower()
    if titulo not in livros:
        print("Erro: Livro não encontrado no acervo.")
        return

    if not livros[titulo]["disponivel"]:
        print("Erro: Este livro já está emprestado para outra pessoa.")
        return

    classificacao_livro = livros[titulo]["classificacao"]
    idade_aluno = alunos[cpf]["idade"]

    if classificacao_livro.isdigit():
        if idade_aluno < int(classificacao_livro):
            print(f"\n❌ ERRO DE CLASSIFICAÇÃO ETÁRIA!")
            print(f"O aluno {alunos[cpf]['nome'].title()} tem apenas {idade_aluno} ano(s).")
            print(f"Este livro possui classificação indicativa de +{classificacao_livro} anos. Empréstimo negado!")
            return

    while True:
        dias_input = input("Simular empréstimo há quantos dias? (0 para hoje): ").strip()
        if not dias_input:
            dias_atraso_simulado = 0
            break
        elif dias_input.isdigit():
            dias_atraso_simulado = int(dias_input)
            break
        print("Erro: Digite um número inteiro de dias.")

    data_emprestimo = datetime.now() - timedelta(days=dias_atraso_simulado)

    emprestimos.append({
        "cpf_aluno": cpf,
        "titulo_livro": titulo,
        "data_emprestimo": data_emprestimo.strftime("%Y-%m-%d %H:%M:%S"),
        "devolvido": False
    })

    livros[titulo]["disponivel"] = False
    print(f"Empréstimo do livro '{titulo.title()}' registrado com sucesso para {alunos[cpf]['nome'].title()}!")

def calcular_multa(data_emprestimo_str):
    data_emp = datetime.strptime(data_emprestimo_str, "%Y-%m-%d %H:%M:%S")
    data_atual = datetime.now()
    dias_passados = (data_atual - data_emp).days

    if dias_passados > 7:
        dias_atraso = dias_passados - 7
        return dias_atraso, dias_atraso * 1.50
    return 0, 0.0

def consultar_pendencias(alunos, emprestimos):
    print("\n--- PENDÊNCIAS E MULTAS ---")
    pendentes = [e for e in emprestimos if not e["devolvido"]]

    if not pendentes:
        print("Não há empréstimos pendentes no momento.")
        return

    for e in pendentes:
        nome_aluno = alunos[e['cpf_aluno']]['nome']
        dias_atraso, multa = calcular_multa(e["data_emprestimo"])
        status_prazo = f"EM ATRASO ({dias_atraso} dias) - Multa: R$ {multa:.2f}" if dias_atraso > 0 else "No prazo"
        print(f"Livro: '{e['titulo_livro'].title()}' | Aluno: {nome_aluno.title()} | Status: {status_prazo}")

def registrar_devolucao(livros, emprestimos):
    print("\n--- REGISTRO DE DEVOLUÇÃO ---")
    titulo = input("Título do livro que está sendo devolvido: ").strip().lower()

    emprestimo_ativo = None
    for e in emprestimos:
        if e["titulo_livro"] == titulo and not e["devolvido"]:
            emprestimo_ativo = e
            break

    if not emprestimo_ativo:
        print("Erro: Este livro não consta como emprestado ou não existe.")
        return

    dias_atraso, multa = calcular_multa(emprestimo_ativo["data_emprestimo"])

    emprestimo_ativo["devolvido"] = True
    emprestimo_ativo["data_devolucao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    livros[titulo]["disponivel"] = True

    print("\nDevolução concluída com sucesso!")
    if multa > 0:
        print(f"⚠️ ATENÇÃO: Livro entregue com {dias_atraso} dias de atraso. VALOR DA MULTA: R$ {multa:.2f}")
    else:
        print("Livro entregue dentro do prazo. Sem multas.")

def main():
    alunos, livros, emprestimos = carregar_dados()

    while True:
        print("\n=================================")
        print("  SISTEMA DE CONTROLE DE LIVROS  ")
        print("=================================")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Livro")
        print("3. Buscar Livro no Acervo")
        print("4. Registrar Empréstimo")
        print("5. Registrar Devolução")
        print("6. Consultar Pendências / Multas")
        print("0. Salvar e Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno(alunos)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "2":
            cadastrar_livro(livros)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "3":
            buscar_livro(livros)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "4":
            registrar_emprestimo(alunos, livros, emprestimos)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "5":
            registrar_devolucao(livros, emprestimos)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "6":
            consultar_pendencias(alunos, emprestimos)
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "0":
            salvar_dados(alunos, livros, emprestimos)
            print("Dados salvos com segurança. Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()