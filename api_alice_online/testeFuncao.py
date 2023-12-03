import time
import matplotlib.pyplot as plt
from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from gtts.tokenizer.tokenizer_cases import tone_marks
from pydub import AudioSegment
from pydub.playback import play

def voice(text):
    tts = gTTS(text=text,lang="pt-br",slow=False)
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3('output.mp3')
 


num_testes = 10
tempos = []
textos = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti. Integer quis feugiat odio.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti. Integer quis feugiat odio. Aenean sagittis odio vel neque efficitur.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti. Integer quis feugiat odio. Aenean sagittis odio vel neque efficitur. Vestibulum dapibus massa ac nulla consectetur.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti. Integer quis feugiat odio. Aenean sagittis odio vel neque efficitur. Vestibulum dapibus massa ac nulla consectetur. Fusce nec nisi eget metus fermentum facilisis.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti. Integer quis feugiat odio. Aenean sagittis odio vel neque efficitur. Vestibulum dapibus massa ac nulla consectetur. Fusce nec nisi eget metus fermentum facilisis. Proin aliquam dapibus turpis, ac congue libero consectetur a.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti. Integer quis feugiat odio. Aenean sagittis odio vel neque efficitur. Vestibulum dapibus massa ac nulla consectetur. Fusce nec nisi eget metus fermentum facilisis. Proin aliquam dapibus turpis, ac congue libero consectetur a. Ut vel est at lacus fermentum gravida.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur vel turpis nec velit elementum consectetur. Suspendisse potenti. Integer quis feugiat odio. Aenean sagittis odio vel neque efficitur. Vestibulum dapibus massa ac nulla consectetur. Fusce nec nisi eget metus fermentum facilisis. Proin aliquam dapibus turpis, ac congue libero consectetur a. Ut vel est at lacus fermentum gravida. Donec tincidunt nisi eu nulla suscipit, eget bibendum orci interdum."
]

for _ in range(num_testes):
    start_time = time.time()
    voice(textos[_])
    end_time = time.time()

    tempo_total = end_time - start_time
    tempos.append(tempo_total)

tempo_medio = sum(tempos) / num_testes
print(f'Tempo médio de execução: {tempo_medio} segundos')

# Criando um gráfico
plt.plot(tempos, marker='o')
plt.xlabel('Tempo para gerar aúdio')
plt.ylabel('Tempo de Execução (s)')
plt.title('Tempo de Execução da Função de geração de aúdio')
plt.show()