# DOCUMENTAÇÃO PROJETO FINAL - SMARTLIBRARY
---
## 1. INTRODUÇÃO
### 1.1 PROPÓSITO
#### Este Documento especifica os Requisitos de Software para a Biblioteca CLI digital da SmartLibrary. O Sistema Será Utilizado por um Único Usuário que fará a Administração e Controle de Estoque e de Empréstimos da Biblioteca
### 1.2 Escopo 
#### O Sistema controlará:
- O Estoque de Livros;
- Período de Empréstimo;
- Registro de Livros;
- Cadastro de Alunos;
- Consulta de Pendências;
### 1.3 Definições, Abreviações
-  **SCL**: Sistema de Controle de Livros;
- **RF**: Requisito Funcional;
- **RN**: Regra de Negócio;
- **RNF**: Requisito Não Funcional;
- **CLI**: Comand Line Interface;
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
|Administrador/Bibliotecária(o)|Básico a Média|Operação Total do Sistema Via Teminal|
|------------------------------|--------------|-------------------------------------|
### 2.4 Restrições 
- Interface deve ser baseada em CLI
-O sistema não deve gerenciar Múltiplos acessoas ao banco de dados Local

## 3. Resquisitos Específicos
### 3.1 Requisitos Funcionais(RF)
**Descrição:** O que o Sistema deve Fazer
- RF001- Cadastro de Livros 
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:

- RF002- Busca no Acervo 
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:
- RF003- Registro de Emprestimo
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:
- RF004- Restrição de Idade 
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:
- RF005- Criação de Contas para Usuários
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:
- RF006- Consulta de Pendências 
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:
### 3.2 Regras de Negócio(RN)
**Descrição**: Critérios de excelência exigidos pelo cliente ou mercado para o sistema.
- Limite de Itens por Usuário
**Descrição**:ayua
**Prioridade**:
**Versão**:
**Data**:
- Exclusividade de Cópia
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:
- Quadro de Multas
**Descrição**:
**Prioridade**:
**Versão**:
**Data**:
### 3.3 Regras Não-Funcionais(RNF)
**Descrição:** Como o Sistema deve Funcionar  
- RNF001- Persistência de Dados Local 
**Descrição**:
**Prioridade**:
**Versão**:1.0
**Data**:
- RNF002- Arquitetura Monousuário
**Descrição**:
**Prioridade**:
**Versão**:1.0
**Data**:

## 4. Controle de Versões
### Histórico de Versões
| Versão | Data | Autor | Modificações |
|--------|------|-------|--------------|
| 1.0    | 2026-05-27| Rafael & Sophia | Versão Inicial do Projeto|
| 1.1    | 2026-06-05| Rafael & Sophia | Depuração do Código |
| 1.2    | 2026-06-12| Rafael          | Depuração do Código e correção de Lógica |
