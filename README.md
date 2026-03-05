# Prática 2: Sistema Bancário (Ambiente Controlado com CI/CD)

Este repositório contém o código-base para a segunda etapa da prática de versionamento. O objetivo é demonstrar o uso de políticas de proteção de branch, a obrigatoriedade de Pull Requests (PRs) e a validação automatizada de código através de integração contínua (CI) com GitHub Actions.

## 1. Estrutura do Repositório

Diferente do ambiente sem restrições, este repositório possui regras que impedem commits diretos na branch `main`. Ele contém os seguintes arquivos:

* `conta.py`: Contém a regra de negócio do sistema bancário.
* `test_conta.py`: Contém os testes unitários em Python (`unittest`) que garantem que o saldo não fique negativo.
* `.github/workflows/ci.yml`: Arquivo de configuração do pipeline que executa os testes automaticamente a cada Pull Request.

## 2. Preparação do Ambiente Local

Clone o repositório e acesse o diretório do projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DA_PASTA>

```

## 3. Execução das Tarefas via Pull Request

Neste cenário, todas as alterações devem ser feitas em branches isoladas e submetidas a revisão e testes antes da integração.

### Aluno 1: Alterar validação de saque (Issue #1) - Bloqueio pelo CI

**Objetivo:** Introduzir uma falha lógica na validação de saldo para observar a atuação da esteira de testes automatizados bloqueando a integração.

**Passo 1:** Criar uma nova branch a partir da `main`.

```bash
git checkout -b feature/saque-sem-limite

```

**Passo 2:** Alterar o método `sacar` no arquivo `conta.py`, removendo a validação de limite de saldo.

```python
    def sacar(self, valor):
        if valor > 0: 
            self.saldo -= valor
            return True
        return False

```

**Passo 3:** Registrar a alteração e enviar para o repositório remoto.
**Altere o número da issue**.

```bash
git add conta.py
git commit -m "feat: permite saque com saldo negativo. closes #1"
git push origin feature/saque-sem-limite

```

**Passo 4:** Abrir o Pull Request no GitHub.
*Resultado esperado:* O GitHub Actions executará o script `test_conta.py`. O teste falhará, impedindo o clique no botão "Merge pull request".

### Aluno 2: Implementar método de transferência (Issue #2) - Integração Bem-sucedida

**Objetivo:** Adicionar uma nova funcionalidade sem quebrar as regras de negócio existentes.

**Passo 1:** A partir da `main` original, criar uma nova branch.

```bash
git checkout main
git pull origin main
git checkout -b feature/transferencia-contas

```

**Passo 2:** Adicionar o método `transferir` na classe `ContaBancaria` (arquivo `conta.py`).

```python
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        return False

```

**Passo 3:** Registrar e enviar a alteração.

```bash
git add conta.py
git commit -m "feat: adiciona metodo de transferencia entre contas. closes #2"
git push origin feature/transferencia-contas

```

**Passo 4:** Abrir o Pull Request no GitHub.
*Resultado esperado:* O pipeline de CI executará com sucesso e ficará verde. O botão de merge será liberado após a aprovação de um revisor (Code Review).

## 4. O Ciclo de Feedback: Correção de Código (Aluno 1)

O Aluno 1 deve corrigir o código na mesma branch para satisfazer os testes e liberar o merge de seu Pull Request.

**Passo 1:** No ambiente local, garantir que está na branch correta (`feature/saque-sem-limite`) e restaurar a validação do saldo no arquivo `conta.py`.

```python
    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

```

**Passo 2:** Realizar um novo commit com a correção e atualizar a branch remota.

```bash
git add conta.py
git commit -m "fix: restaura validacao de saldo apos falha no pipeline"
git push origin feature/saque-sem-limite

```

*Resultado esperado:* O Pull Request aberto será atualizado automaticamente, os testes rodarão novamente e o status passará de reprovado para aprovado, liberando a integração.
