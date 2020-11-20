# Gerenciamento de memória 

O software desenvolvido funciona de maneira local. Será necessário o usuário baixar o projeto no github e rodar o main.py e dar input conforme a apresentação do menu. 
Não possui dependencia com hardware ou software, pois todas as instalações necessárias já estão  na venv (virtual environment) do python, gerenciada.
## Gerencia de memória
O Python disponibiliza um mecanismo de gerência de memória automático que é responsável por alocar e desalocar memória, esse mecanismo é chamado de Garbage Collector.

De tempos em tempos o Garbage Collector do Python percorre a lista de objetos registrados verificando o número de referências para cada um deles. Quando esse número é zero (não existem mais referência para eles) o GC desaloca a memória usada por esse objeto. 

O GC também trabalha de um outro método, mais lento, de coleta de lixo para eliminar objetos que perderam as suas referências externas mas possuem referência circular entre eles.
