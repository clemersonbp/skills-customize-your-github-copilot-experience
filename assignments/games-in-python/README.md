
# 📘 Assignment: Games in Python

## 🎯 Objetivo

Praticar a criação de jogos simples em Python para reforçar conceitos de variáveis, listas, controle de fluxo (condicionais e loops) e manipulação de strings, desenvolvendo lógica de programação aplicada de forma divertida.

## 📝 Tarefas

### 🛠️	Hangman (Jogo da Forca)

#### Description
Implemente o clássico jogo da forca. O programa escolhe uma palavra secreta e o jogador tenta adivinhar letra por letra antes de esgotar o número máximo de tentativas.

#### Requirements
Completed program should:

- Selecionar aleatoriamente uma palavra de uma lista pré-definida
- Exibir o progresso com sublinhados para letras não descobertas (ex: `_ _ a _ o`)
- Aceitar palpites de uma única letra por tentativa
- Impedir repetição de palpites já feitos e informar ao usuário
- Informar quantidade de tentativas incorretas restantes
- Encerrar com mensagem de vitória (todas as letras descobertas) ou derrota (tentativas esgotadas) mostrando a palavra
- Usar apenas a biblioteca padrão (permitido: `random`)

Exemplo de execução (parcial):

```
Palavra: _ _ _ _ _
Tentativas restantes: 6
Letras usadas: 
Digite uma letra: a
Boa! Palavra: a _ _ a _
Tentativas restantes: 6
Letras usadas: a
```

### 🛠️	Number Guessing (Adivinhe o Número)

#### Description
Crie um jogo onde o computador escolhe um número secreto dentro de um intervalo e o jogador tenta adivinhar. Após cada palpite, o programa informa se o número é maior ou menor até que o acerto aconteça.

#### Requirements
Completed program should:

- Solicitar do usuário o intervalo máximo (ex: até 100) ou usar um padrão (1–100)
- Gerar um número aleatório dentro do intervalo definido
- Ler palpites numéricos e validar entrada (tratar valores não inteiros)
- Informar “maior” ou “menor” após cada tentativa incorreta
- Contar o número de tentativas até o acerto
- Exibir mensagem final parabenizando e mostrando total de palpites
- Permitir jogar novamente sem reiniciar o script (perguntar “Deseja jogar de novo? (s/n)”)

Exemplo de execução (parcial):

```
Adivinhe o número (1–100)
Seu palpite: 50
O número é maior.
Seu palpite: 75
O número é menor.
Seu palpite: 63
Acertou! Tentativas: 3
Jogar novamente? (s/n): n
```

---

Boa sorte! Foque em código limpo, nomes de variáveis descritivos e feedback claro ao jogador. Depois que ambos os jogos funcionarem, experimente adicionar melhorias (dicas, níveis de dificuldade, placar). 
