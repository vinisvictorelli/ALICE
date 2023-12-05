# ALICE
ALICE - Assistente de Linguagem e Interação Computadorizada Eficiente

# DEPENDÊNCIAS
Para utilizar este projeto, por favor, certifique-se que o `Python`, `pip` e o `pipenv` estejam instalados em seu computador. O pip e o pipenv foram utilizados para gerenciar as dependências do projeto. Por este motivo, toda vez que for executar este projeto pela linha de comando, devemos entrar no ambiente provisionado pelo pipenv e dentro dele executar os arquivos que desejamos:

Para entrar no ambiente provisionado pelo pipenv, use o seguinte comando:

```bash
pipenv shell
```

Este comando criará e entrará em um ambiente isolado (virtualenv) para as dependências do projeto no seu computador, evitando conflitos com as dependências já existentes. A partir deste momento, toda utilização do comando pip será subsituída pelo comando pipenv, pois estaremos gerenciando as dependências no virtualenv (o ambiente isolado criado para este projeto).

Para instalar as dependências deste projeto, execute o seguinte comando:

```bash
pipenv install
```

Para instalar um pacote específico para este projeto, use o seguinte comando:

```bash
pipenv install <dependência>
```

Use o comando acima no lugar de:

```bash
pip install <dependência>
```

Caso deseje sair do virtualenv em execução pelo pipenv, basta digitar `Ctrl+D` no teclado.

## LINUX UBUNTU
Caso você esteja executando este projeto no Linux Ubuntu, fique atento pois há alguns pacotes que devem ser instalados pelo gerenciador de pacotes do sistema operacional.
Listei alguns comandos aqui, pois serão úteis e pouparão o seu tempo, evitando algumas pesquisas na internet:

```bash

sudo apt-get install portaudio19-dev
sudo apt-get install ffmpeg libavcodec-extra
sudo apt-get install -y python3-dev libasound2-dev

```

# EXECUÇÃO
Para executar este projeto, entre no virtualenv fornecido pelo pipenv, conforme as instruções anteriores, e execute o seguinte comando:

```bash
python3 main.py
```

Caso deseje executar, separadamente, qualquer uma das funções de alguns arquivos do projeto, execute o seguinte comando:

```bash
python -c 'from <nome_arquivo> import <função_arquivo>; <função_arquivo>()'
```

Por exemplo:

```bash
cd voice_generate
python -c 'from app import voice; voice("Olá! Tudo bem?", "saudacao.mp3")'
```
> [!IMPORTANT]
> Certifique-se de que esteja no diretório que contém os arquivos que você deseja executar (assim como foi feito no exemplo acima).

# ESTRUTURA DO PROJETO
Esse projeto está dividido em várias pastas e subpastas:
* A pasta [_api\_alice\_online_](api_alice_online/) possui códigos para que o projeto utilize uma IA conversacional;
* A pasta [_audios_](audios/) possui, principalmente, os arquivos de áudios padrões que a ALICE diz. Além disso contém alguns arquivos .py para a geração destes áudios;
* A pasta [_face\_recognition_](face_recognition/) contém os arquivos que são importantes para a realização do reconhecimento facial;
  * A pasta [_known_](face_recognition/known/) contém as imagens que serão utilizadas como base para a IA realizar o reconhecimento facial das pessoas.
* A pasta [_others_](others/) contém outros arquivos foram úteis durante o desenvolvimento do projeto, seja para o simples entendimento das funções ou para a realização de testes;
* A pasta [_voice\_generate_](voice_generate/) possui arquivos que são importantes para a geração de arquivos de voz que são utilizados no projeto;
* A pasta [_voice\_recognition_](voice_recognition/) possui arquivos que são importantes para o reconhecimento da fala do usuário;

# BARD_API TOKEN
Verifique os [tokens que você deseja utilizar](https://medium.com/@marc.bolle/access-google-bard-with-python-package-bard-api-6000251d1aa8) para autenticação com o Bard e faça as alterações no arquivo [_googlebardapi.py_](api_alice_online/googlebardapi.py) presente na pasta [_api\_alice\_online_](api_alice_online/).