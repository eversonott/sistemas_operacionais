# Sistemas de arquivos e E/S
Após a execução do programa é gerado um arquivo lista_filmes.csv contendo os nomes dos filmes e nota da audiência. O arquivo é gerado no diretório do projeto.
E ordenado por ordem crescente pelo comando:
<pre><code>sort -t"," -k2 lista_filmes.csv</code></pre>
o comando "-k2" ordena por coluna, no caso do nosso projeto, ele está ordenando a 2 coluna do arquivo .csv, ou seja, pela nota da audiência.


