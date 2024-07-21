# Projeto: Sistema de Casa Inteligente

- [Objetivo](#Objetivo)
- [Depedências](#Dependências)<br>
- [Executando o Programa](#Executando-o-Programa)<br>
- [Funcionalidades](#Funcionalidades)


## Objetivo
O objetivo deste projeto é projetar e implementar um sistema de casa inteligente abrangente que integra vários conceitos vistos durante a disciplina, como programação orientada a objetos, padrões de projeto, máquinas de estados usando a biblioteca `transitions`, e conceitos de programação funcional, como compreensões de listas e funções como `map`, `filter` e `reduce`, além de argumentos de linha de comando.



## Dependências
- transitions 0.9.1

Certifique-se de ter o Python instalado. Instale as dependências necessárias utilizando o pip:<br>
```pip install -r requirements.txt```

## Executando o Programa
Para executar o programa, siga os seguintes passos:

1 - Clone o repositório para a sua máquina local.<br>
```git clone https://github.com/ClebyFrancisco/projeto-casa-inteligente.git```

2 - Navegue até o diretório do projeto.<br>
```cd .\projeto-casa-inteligente\```

3 - Execute o arquivo <br>```python main.py```

## Funcionalidades
- Buscar o estado dos dispositivos: Lista o estado atual de todos os dispositivos.
- Adicionar dispositivo: Adiciona um novo dispositivo (luz, termostato, sistema de segurança) ao sistema.
- Mudar o estado de um dispositivo: Permite alterar o estado de um dispositivo específico.
- Remover dispositivo: Remove um dispositivo do sistema.
- Mudar o estado de vários dispositivos do mesmo tipo: Permite alterar o estado de todos os dispositivos de um determinado tipo.
- Desligar todas as luzes: Usa a função map para desligar todas as luzes.
- Listar dispositivos ligados: Usa a função filter para listar todos os dispositivos que estão ligados.
- Contar dispositivos ligados: Usa a função reduce para contar quantos dispositivos estão ligados.
