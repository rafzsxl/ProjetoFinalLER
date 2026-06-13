# DOCUMENTAÇÃO PROJETO FINAL - SMARTLIBRARY
---
## 1. INTRODUÇÃO
### 1.1 PROPÓSITO
#### Este Documento especifica os Requisitos de Software para a Biblioteca CLI digital da SmartLibrary. O Sistema Será Utilizado por um Único Usuário que fará a Administração e O Controle de Estoque e de Empréstimos da Biblioteca

### 1.2 Escopo
#### O Sistema controlará:
- O Estoque de Livros;
- Período de Empréstimo;
- Registro de Livros;
- Cadastro de Alunos;
- Consulta de Pendências;

### 1.3 Definições/Abreviações
-  **SCL**: Sistema de Controle de Livros;
- **RF**: Requisito Funcional;
- **RN**: Regra de Negócio;
- **RNF**: Requisito Não Funcional;
- **CLI**: Command Line Interface;

### 1.4 Referências
    - IEEE 29148:2018 - Systems and software engineering;
    - CMMI for Development, Version 2.0 ;
---

## 2. Descrição Geral
### 2.1 Perspectiva do Produto
#### O SCL é Um standalone de Operador Único(monouser), desenvolvido para rodar Localmente via CLI. Operando 100% offline e persistindo seus dados de forma estruturada em arquivos locais.

### 2.2 Funções do Produto
- Controle de Estoque;
- Validação de Limites de Emprestimo;
- Gerenciamento de Alunos e Livros;
- Validação de Limites de Empréstimo por Estudante;
- Bloqueio de Transações para Itens já Alocados;

### 2.3 Características dos Usuários
|       Tipo de Usuário        | Nível Técnico|        Funções Principais           |
|------------------------------|--------------|-------------------------------------|
|Administrador/Bibliotecária(o)|Básico a Média|Operação Total do Sistema Via Terminal|

### 2.4 Restrições
- Interface deve ser baseada em CLI;
- O sistema não deve gerenciar Múltiplos acessos ao banco de dados Local;

---
## 3. Resquisitos Específicos
### 3.1 Requisitos Funcionais(RF)
**Descrição:** O que o Sistema deve Fazer

### - RF001- Cadastro de Livros
**Descrição:** O sistema deve permitir o cadastro de um livro, armazenando obrigatoriamente: Título, Autor, Ano de Publicação e Classificação Indicativa (Idade).

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

### - RF002- Busca no Acervo
**Descrição:** O sistema deve disponibilizar uma função de busca que permita filtrar o acervo por Título ou Autor do Livro.

**Prioridade:** Importante (Média)

**Versão:** 1.0

**Data:** 12/06/2026

### - RF003- Registro de Emprestimo
**Descrição:** O sistema deve registrar a operação de empréstimo relacionando o CPF do Aluno ao Título do Livro

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

### - RF004- Criação de Contas para Usuários
**Descrição:** O sistema deve permitir o cadastro de alunos, registrando de forma estruturada: CPF do Aluno, Nome Completo e Idade

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

### - RF005- Consulta de Pendências
**Descrição:** O sistema deve emitir um relatório em formato de texto no terminal contendo todos os empréstimos em atraso quando solicitado pelo operador.

**Prioridade:** Importante (Média)

**Versão:** 1.0

**Data:** 2026-05-27

### 3.2 Regras de Negócio(RN)
**Descrição:** Critérios de excelência exigidos pelo cliente ou mercado para o sistema.
### - RN001 - Limite de Itens por Usuário
**Descrição:** O sistema deve impedir a conclusão de um novo empréstimo caso o aluno selecionado já possua 3 (três) livros sob empréstimo ativo simultaneamente.

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

### - RN002 - Exclusividade de Cópia
**Descrição:** O sistema deve garantir que cada cópia física de um livro cadastrado seja tratada de forma exclusiva, impedindo que um mesmo exemplar seja associado a mais de um empréstimo ativo simultaneamente.

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

### - RN003 - Quadro de Multas
**Descrição:** O sistema deve aplicar uma penalidade financeira teórica ou suspensão temporal ao cadastro do aluno sempre que o prazo de devolução de um empréstimo for ultrapassado.

**Prioridade:** Importante (Média)

**Versão:** 1.0

**Data:** 2026-05-27

### - RN004- Restrição de Idade
**Descrição:** O sistema deve bloquear o empréstimo se a idade do aluno for inferior à Classificação Indicativa cadastrada no livro.

**Prioridade:** Importante (Média)

**Versão:** 1.0

**Data:** 2026-05-27
   
### 3.3 Requisitos Não-Funcionais(RNF)
#### Descrição: Como o Sistema deve Funcionar  
### - RNF001 - Persistência de Dados Local
**Descrição:** O sistema deve persistir o estado dos dados em arquivos locais (JSON) imediatamente após o término de cada operação de escrita, garantindo a integridade contra fechamentos inesperados do terminal.

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

### - RNF002 - Arquitetura Monousuário
**Descrição:** O sistema deve ser projetado para operar estritamente em ambiente local e centralizado, suportando a execução de apenas uma instância ativa por vez.

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

### - RNF003- Portabilidade e Restrição de Arquitetura
**Descrição:** O sistema deve ser executável nativamente em ambiente de console (Terminal Linux/macOS ou Prompt de Comando Windows) sem dependência de servidores web.

**Prioridade:** Essencial (Alta)

**Versão:** 1.0

**Data:** 2026-05-27

---

## 4. Controle de Versões
### Histórico de Versões
| Versão | Data | Autor | Modificações |
|--------|------|-------|--------------|
| 1.0    | 2026-05-27| Rafael & Sophia | Versão Inicial do Projeto|
| 1.1    | 2026-06-05| Rafael & Sophia | Depuração do Código |
| 1.2    | 2026-06-12| Rafael          | Depuração do Código e correção de Lógica | 
| 1.3    | 2026-06-13| Rafael          | Implementação da RN004|
