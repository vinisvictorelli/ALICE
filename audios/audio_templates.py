def audio_templates():
    return {
        'welcome': {
            'text': 'Olá! Sou a ALICE, a Assistente de Linguagem e Interação Computadorizada Eficiente. Estou aqui para facilitar a sua vida. Apenas permito que pessoas autorizadas me façam perguntas. Para isso faço o reconhecimento facial do usuário que está interagindo comigo.',
            'audio_name': 'welcome.mp3'
        },
        'face_recognition_instructions': {
            'text': 'Vou iniciar o reconhecimento facial. Caso você queira parar o reconhecimento, digite a tecla q do seu teclado.',
            'audio_name': 'face_recognition_instructions.mp3'
        },
        'searching': {
            'text': 'Aguarde um momento enquanto penso em sua resposta...',
            'audio_name': 'searching.mp3'
        }
    }