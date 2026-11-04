
# 📘 Atividade: Jogo da Forca em Python

## 🎯 Objetivo

Construa um jogo da Forca para praticar manipulação de strings, loops, condicionais, entrada de dados e seleção aleatória em Python.

## 📝 Tarefas

### 🛠️ Implementar uma partida de Forca

#### Descrição
Escreva um programa que escolha uma palavra secreta e permita que o jogador tente adivinhá-la, uma letra por vez.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra de uma lista predefinida.
- Mostrar cada letra ainda não descoberta como um sublinhado, separado das demais letras.
- Solicitar palpites de letras e revelar todas as ocorrências de cada letra correta.
- Permitir no máximo seis palpites incorretos.
- Encerrar a partida quando a palavra for descoberta ou quando o limite de palpites incorretos for atingido.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra secreta.

### 🛠️ Validar palpites e permitir outra partida

#### Descrição
Melhore a interação do jogo para tratar palpites inválidos ou repetidos e permitir que o jogador inicie uma nova partida.

#### Requisitos
O programa concluído deve:

- Aceitar apenas um caractere alfabético por palpite e ignorar diferenças entre letras maiúsculas e minúsculas.
- Informar quando o jogador repetir uma letra, sem descontar uma tentativa incorreta.
- Não descontar tentativas por entradas inválidas.
- Perguntar ao jogador se deseja iniciar outra partida depois que uma terminar.