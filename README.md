🏦 MiniBank – Sistema Bancário em Python

Bem-vindo ao **MiniBank**, um sistema simples e funcional de gerenciamento bancário desenvolvido em Python.  
Com ele, é possível **cadastrar usuários**, **criar contas**, **realizar transações** e **consultar extratos** de forma prática e organizada.

---

## 🎯 Objetivo

O MiniBank tem como objetivo permitir que um mini banco simule as principais operações financeiras do dia a dia, proporcionando **uma experiência de POO (Programação Orientada a Objetos)** completa em Python.

---

## ⚙️ Funcionalidades

### ✅ Gerenciamento de Usuários
- Criar novos clientes com dados básicos: nome, CPF, data de nascimento e endereço.
- Cada cliente pode possuir **uma ou mais contas**.

### 🏦 Gerenciamento de Contas
- Criar contas correntes associadas a clientes existentes.
- Listar todas as contas cadastradas.
- Limite de saques e controle de saldo implementados na conta corrente.

### 💵 Operações Bancárias
- **Depósito**: adiciona valor ao saldo da conta.
- **Saque**: remove valor do saldo, respeitando saldo e limite.
- **Extrato**: exibe todas as transações realizadas (depósitos e saques) e saldo atual.

### 📋 Relatórios
- Visualizar todas as contas criadas e seus respectivos titulares.

---

## 🧠 Conceitos de Programação Utilizados

- **Programação Orientada a Objetos (POO)**
- **Herança e Abstração**
- **Métodos Abstratos** (`@abstractmethod`)
- **Encapsulamento de dados**
- Uso de **`@classmethod`** e **`@property`**
- Integração de classes (`Cliente`, `PessoaFisica`, `Conta`, `ContaCorrente`, `Historico`, `Transacao`, `Deposito`, `Saque`)

---

## 🚀 Como Executar

### 1️⃣ Pré-requisitos
- Python **3.10 ou superior** instalado na máquina.

### 2️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/minibank.git
cd minibank

3️⃣ Estrutura de arquivos

minibank/
│
├─ minibank.py          # Arquivo principal
├─ historico.py
├─ conta.py
├─ contacorrente.py
├─ cliente.py
├─ pessoafisica.py
├─ deposito.py
├─ saque.py
└─ transacao.py

4️⃣ Executar o programa

python minibank.py

🧪 Como usar

    Execute o programa.

    Use o menu para:

        Criar clientes (Novo usuário)

        Criar contas (Nova conta)

        Depositar (Depositar)

        Sacar (Sacar)

        Consultar extrato (Extrato)

        Listar todas as contas (Listar contas)

    Escolha as opções digitando o número correspondente.

🧭 Futuras Melhorias

    Adicionar persistência de dados (JSON ou banco de dados).

    Implementar interface gráfica (Tkinter ou web).

    Criar testes automatizados com pytest.

    Adicionar ContaPoupança e juros automáticos.

    Permitir transferência entre contas.

💻 Exemplo de uso

# Criando um cliente
cliente = PessoaFisica("Bruno", "01/01/1990", "12345678900", "Rua das Palmeiras, 100")

# Criando uma conta corrente
conta = ContaCorrente.nova_conta(cliente, numero=1)
cliente.adicionar_conta(conta)

# Realizando depósito
dep = Deposito(500)
cliente.realizar_transacao(conta, dep)

# Realizando saque
saq = Saque(200)
cliente.realizar_transacao(conta, saq)

# Consultando extrato
conta.historico.imprimir_extrato()
