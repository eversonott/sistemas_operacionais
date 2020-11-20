# Software, scripts e comandos Unix 
Scripts são utilizados para executar diversas funções, até mesmo automatizar processos. Eles são feitos em arquivos texto com a extensão ".sh".

Programar em Shell Script proporciona maior flexibilidade e maior controle sobre o sistema operacional.

## Scripts
Exemplo de script em Python que usamos para criar um diretório:
O makedirs cria o diretório recursivamente, ou seja, vai ser criado primeiro a pasta relatorio, depois a pasta audienceMatters e por último a pasta com o nome do gênero escolhido.
<pre><code>import os

try:
    dir = './relatorio/audienceMatters/{genre}'    #a variavel genre vem do input do usuario   
    os.makedirs(dir)
except Exception:
    print "Algo deu errado :( "</code></pre>

Equivalente dele em shell script:

<pre><code>#!/bin/bash
SHELL=/bin/sh
PATH=/sbin:/usr/sbin:/usr/bin:/bin

echo "Escreva um genero de filme: "
read genre

if [ -e "./relatorio/audienceMatters/$genre" ]
then
echo " o diretorio existe"
else
echo " o diretorio não existe vamos criar o diretorio"
mkdir ./relatorio/audienceMatters/$genre
fi
exit</code></pre>

## Comandos Unix que utilizamos para criar essa documentação :)
* `mkdocs new [dir-name]` - Cria um novo projeto
* `mkdocs serve` - Inicia o servidor
* `mkdocs build` - Faz o build da documentação



