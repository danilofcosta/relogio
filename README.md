# Relógio Digital e Analógico com Python

Este projeto implementa um aplicativo de Relógio Digital e Analógico utilizando as bibliotecas `customtkinter` e `pygame`. O aplicativo exibe um relógio digital atualizado a cada segundo e um relógio analógico que desenha os ponteiros das horas, minutos e segundos em tempo real.

## Tecnologias Utilizadas
- Python 3
- `customtkinter` para a interface gráfica
- `pygame` para reproduzir o som de tic-tac
- `math` e `time` para cálculos relacionados ao relógio analógico

## Funcionalidades
- Relógio digital com formato `HH:MM:SS AM/PM`.
- Relógio analógico com atualização automática dos ponteiros.
- Reprodução de som de tic-tac a cada segundo.
- Suporte para modo claro e escuro.

## Como Executar o Projeto
1. Certifique-se de ter o Python instalado (versão 3.7 ou superior).
2. Instale as dependências necessárias executando:
   ```sh
   pip install customtkinter pygame
   ```
3. Execute o script Python:
   ```sh
   python nome_do_arquivo.py
   ```

## Estrutura do Código
O código está estruturado dentro da classe `RelogioDigital`, que herda de `CTkFrame`. Os principais métodos incluem:
- `__init__`: Inicializa a interface do relógio.
- `atualizar_relogio`: Atualiza a exibição do relógio digital a cada segundo.
- `tocar_som`: Reproduz o som de "tic-tac".
- `RelogioAnalogico`: Desenha o relógio analógico e seus ponteiros.



