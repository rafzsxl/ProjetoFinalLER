# DOCUMENTAÇÃO PROJETO FINAL - SMARTLIBRARY
---
## 1. INTRODUÇÃO
### 1.1 PROPÓSITO
#### Este Documento especifica os Requisitos de Software para a Biblioteca CLI digital da SmartLibrary. O Sistema Será Utilizado por um Único Usuário que fara a Administração e Controle de Estoque da Biblioteca
### 1.2 Escopo 
#### O Sistema controlará:
- O estoque de Livros;
- Período de Empréstimo;
- Registro de Livros;
- Cadastro de Alunos
- Restrição por Idade
- Consulta de Pendências
### 1.3 Definições, Abreviações
-  **SCL**: Sistema de Controle de Livros
- **RF**: Requisito Funcional
- **RN**: Regra de Negócio
- **RNF**: Requisito Não Funcional
- **CLI**: Comand Line Interface
### 1.4 Referências
---
## 2. Descrição Geral
### 2.1 Perspectiva do Produto
#### O SCL é Um standalone de Operador Único(monouser), desenvolvido para rodar Localmente via CL. Operando 100% offline e persistindo seus dados de forma estruturada em arquivos locais.
### 2.2 Funções do Produto
- Controle de Estoque 
- Validação de Limites de Emprestimo
- Gerenciamento de Alunos e Livros
- Validação de Limites de Empréstimo por Estudante
- Bloqueio de Treansações para Itens já Alocados

### 2.3 Características dos Usuários
|Tipo de Usuário|Nível Técnico|Funções Principais|
|---------------|-------------|------------------|
|Administrador/Bibliotecária(o)|Básico a Média|Operação Total do Sistema Via Teminal|
### 2.4 Restrições 
- Interface deve ser baseada em CLI 

## 3. Resquisitos Específicos
### 3.1 Requisitos Funcionais 
- RF001- Cadastro de Livros 
- RF002- Busca no Acervo 
- RF003- Registro de Emprestimo
- RF004- Restrição de Idade 
- RF005- Criação de Contas para Usuários
- RF006- Consulta de Pendências 
### 3.2 Regras de Negócio
- Limite de Itens por Usuário
- Exclusividade de Cópia
- Quadro de Multas
### 3.3 Regras Não-Funcionais
- RNF001- Persistência de Dados Local 
- RNF002- Arquitetura Monousuário