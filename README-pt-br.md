[Leia isto em Inglês / Read this in English](README.md)

# 🃏 Jogo de Blackjack (Vinte e Um) em Python
... (resto do conteúdo em português)

# 🃏 Jogo de Blackjack (Vinte e Um) em Python

Este projeto é uma implementação completa do clássico jogo de cartas Blackjack (Vinte e Um), desenvolvido em Python puro. O jogo roda inteiramente no terminal e foi criado com foco em código limpo, modularização e na aplicação correta das regras do jogo.

## ✨ Funcionalidades

* **Lógica Completa de Jogo:** Implementa as regras essenciais do Blackjack, incluindo:
    * Turno do jogador com opções de "Hit" (pegar carta) e "Stand" (parar).
    * Turno automático do dealer, que é obrigado a pegar cartas até atingir 17 pontos.
    * Detecção de "Bust" (pontuação acima de 21).
* **Simulação de Baralho Real:** O programa cria um baralho finito de 52 cartas, que é embaralhado no início de cada partida. As cartas distribuídas são removidas do baralho, tornando o jogo mais realista.
* **Cálculo Inteligente do Ás:** A pontuação da mão calcula dinamicamente o valor do Ás como 11 ou 1, sempre buscando a melhor pontuação possível para o jogador sem "estourar".
* **Interface de Terminal Clara:** O jogo apresenta as informações de forma organizada, mostrando as mãos e pontuações do jogador e do dealer a cada etapa.

## 🚀 Como Executar

1.  **Pré-requisitos:** Certifique-se de que você tem o Python 3 instalado em sua máquina.
2.  **Download:** Baixe ou clone este repositório.
3.  **Execução:** Navegue até a pasta do projeto no seu terminal e execute o seguinte comando:
    ```bash
    python main.py
    ```
4.  **Jogar:** Siga as instruções no console para jogar.

## 🧠 Conceitos de Programação Aplicados

Este projeto foi um exercício prático para solidificar diversos conceitos importantes de software:

* **Modularização e Funções:** O código é organizado em funções com responsabilidades únicas, seguindo o **Princípio da Responsabilidade Única (SRP)**. Temos funções dedicadas para criar o baralho, distribuir cartas, calcular pontuações, gerenciar os turnos de cada jogador e determinar o vencedor.
* **Estrutura de Dados:** Utiliza uma **lista de dicionários** para representar o baralho, onde cada carta é um objeto com propriedades (`rank`, `suit`, `value`). Esta abordagem torna o acesso aos dados explícito e o código mais legível.
* **Gerenciamento de Estado:** As variáveis `deck`, `player_hand` e `dealer_hand` são gerenciadas e passadas entre as funções, controlando o estado do jogo a cada rodada.
* **Lógica Condicional:** Uso intensivo de estruturas `if/elif/else` e loops `while` para controlar o fluxo do jogo e aplicar as regras complexas do Blackjack.

## 🔮 Melhorias Futuras

Este projeto tem uma base sólida que permite várias expansões interessantes, como:

* Implementar um sistema de apostas com um saldo fictício para o jogador.
* Adicionar um loop principal para permitir que o usuário jogue várias partidas seguidas.
* Permitir a escolha de jogar com múltiplos baralhos.
* Melhorar a experiência do usuário com pausas (`time.sleep`) e limpeza de tela (`os.system`).
