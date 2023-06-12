<h1 align="center"> Beat Run </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-green?style=flat-square" alt="Status">
</p>

<p align="center"> 
  Este é o projeto do Beat Run em Python. O jogo permite que um professor crie uma partida, adicione perguntas com respostas e os alunos possam participar da partida respondendo às perguntas.
</p>

## :hammer: Requisitos

- Python 3.x
- Terminal ou Console
- Bibliotecas Python (não requer instalação adicional)

## Instruções de Uso

1. Clone o repositório ou faça o download dos arquivos do projeto.
2. Certifique-se de ter o Python 3.x instalado em seu sistema.
3. Abra um terminal ou console e navegue até o diretório do projeto.
4. Execute o seguinte comando para iniciar o jogo:

```bash
python main.py
```

5. Siga as instruções fornecidas pelo jogo para criar uma conta como professor ou fazer login como aluno.
6. Se for um professor, você poderá criar uma nova partida e adicionar perguntas ao jogo.
7. Se for um aluno, insira o PIN da partida fornecido pelo professor para participar.
8. O jogo exibirá as perguntas e alternativas de resposta. Digite o número da resposta desejada.
9. Ao final da partida, será exibida a pontuação obtida.

## Funcionalidades
- Login como professor ou aluno.
- Criação de partida pelo professor.
- Adição de perguntas com respostas pelo professor.
- Participação dos alunos na partida com base no PIN fornecido.
- Exibição das perguntas e alternativas de resposta aos alunos.
- Cálculo da pontuação obtida pelos alunos.

## Arquivos
- `main.py`: Arquivo principal que contém a lógica do jogo.
- `users_prof.csv`: Arquivo CSV que armazena as contas dos professores.
- `PIN-game.csv`: Arquivo CSV que armazena as perguntas e respostas de uma partida.
- `dev/games/`: Diretório onde são armazenados os arquivos de dados do jogo.

## Limitações e Possíveis Melhorias
- O jogo atualmente possui apenas perguntas de múltipla escolha com alternativas.
- Não há um sistema de pontuação global ou ranking.
- As perguntas e respostas são armazenadas localmente em arquivos CSV.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para sugerir melhorias, correções de bugs ou novas funcionalidades.

## Licença
<img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="Status">

Divirta-se jogando o Jogo de Perguntas e Respostas! Se tiver alguma dúvida ou problema, entre em contato.
