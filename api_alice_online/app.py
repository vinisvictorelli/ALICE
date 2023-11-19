from gpt4all import GPT4All
model = GPT4All("rift-coder-v0-7b-q4_0.gguf") # device='amd', device='intel'
output = model.generate("Escreva um exemplo de implementação de uma ia com rede neural em python",max_tokens=5000,)
print(output)