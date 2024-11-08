# Projeto Reconhecedor de Voz e Digitação

Este projeto utiliza o reconhecimento de voz para transcrever o que você fala e digitar automaticamente no teclado. Ele pode ser útil para automatizar tarefas, como enviar mensagens no Discord ou realizar ações em jogos e aplicativos, tudo com comandos de voz.

## Funcionalidades

- **Digitação por Voz**: O usuário pode ditar textos, que são automaticamente digitados no teclado.
- **Envio de Mensagens**: Ao dizer "enviar", o programa simula o pressionamento da tecla Enter, facilitando o envio de mensagens.

---

## Requisitos

Antes de rodar o projeto, você precisa instalar as dependências necessárias:

- **Python 3.x**: O projeto foi desenvolvido utilizando Python 3.
- **Bibliotecas**:
  - `speechrecognition`: Para reconhecimento de voz.
  - `pyautogui`: Para simular a digitação e pressionamento de teclas.

Você pode instalar as dependências utilizando o `pip`:

```bash
pip install SpeechRecognition pyautogui
```

---

## Como Usar

1. **Clone este repositório** para sua máquina:

   ```bash
   git clone https://github.com/PlayDevs/projects.git
   cd projects
   ```

2. **Instale as dependências** (se ainda não fez isso):

   ```bash
   pip install SpeechRecognition pyautogui
   ```

3. **Execute o programa**:

   ```bash
   python init.py
   ```

4. **Fale os comandos**:
   - Para digitar uma mensagem, fale o que deseja escrever e o programa irá digitar automaticamente.
---

## Como Funciona

Este projeto utiliza a biblioteca **SpeechRecognition** para capturar e processar o áudio da sua voz. Com base no que é falado, o programa identifica comandos e executa ações no teclado usando a biblioteca **pyautogui**.

### Exemplo de Comandos

- **"enviar"**: Ele envia a mensagem que digitou pressionando Enter.
- **"Oi, tudo bem?"**: Ele escreve isso no terminal, e no seu teclado.
