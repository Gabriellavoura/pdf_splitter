import pdf_splitter as splitter
import time

start = time.time()

# passa o endereço da pasta input como parametro, retorna o pdf e o nome do mesmo como uma lista [pdf,name]
pdf_info = splitter.pdf_input();

# Atribui os itens da lista a variaveis para melhorar a semantica
pdf = pdf_info[0]
name = pdf_info[1]

# Atribui o numero de paginas a uma variavel
num_pages = splitter.get_numPages(pdf)

# Passar como argumento pdf, nome, numero de paginas e o endereco para salvar,
#  Caso o numero de paginas e path não forem definidos os mesmos são setados como default configurado no pdf_splitter.py
splitter.pdf_splitter (pdf,name,num_pages)

end = time.time()

print("Arquivos separados em: " + str(end - start) + " Segundos.");