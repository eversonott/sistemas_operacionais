## Sistemas de arquivos 
O sistema de arquivo é responsável pelo armazenamento e acesso aos dados e programas que pertencem ao sistema operacional e é muito importante para sistemas multiusuários pois controla a proteção dos arquivos.

Os arquivos são manipulados de formas diferentes de acordo com o sistema operacional e em cada sistema de arquivo. Vemos que o Linux, por exemplo, faz distinção de letras minúsculas e maiúsculas e normalmente o nome de um arquivo o nome e a extensão separados por “.”, também é possível ter mais de uma extensão no mesmo arquivo. E nele tudo é visto como arquivo os drivers dos dispositivos, as pastas, no qual cada arquivo é um inode.

É possível utilizar diversos sistemas de arquivo no Linux, cada um desses sistemas de arquivos é montado sobre um diretório e então é criado um ponto de montagem destes sistemas de arquivos. Também pode-se montar vários sistemas de arquivos em vários pontos de montagens, que pode ser até um diretório de máquina remota.

Para que seja possível essa manipulação de sistemas de arquivos o Linux utiliza o Virtual File System (VSF), que faz o gerenciamento destes diversos sistemas e seus respectivos pontos de montagem, fazendo parecer que é apenas um único sistema de arquivo.

## INODE

INODE é uma estrutura que armazena todas as informações e os dados de um arquivo. Ele contém os identificadores dos usuários e grupos ao qual pertencem os arquivos, também informações de gerenciamento como última modificação e último acesso.

Os INODEs possuem ponteiros de blocos de discos, para armazenar os dados do arquivo. Esses blocos são divididos em quatro tipos: blocos diretos, blocos indiretos, blocos indiretos duplos e blocos indiretos triplos.

É possível a identificação de cada INODE através de um número para que o sistema operacional saiba qual ele deve buscar. E o VSF acessa um INODE através de dois parâmetros (partição, número do INODE).

## Como listar os sistemas de arquivos montados

A lista definitiva de sistemas de arquivos montados está em `/proc/mounts`.

Se você tiver qualquer forma de contêiner no seu sistema, `/proc/mountslista` apenas os sistemas de arquivos que estão no seu contêiner atual. Por exemplo, em um chroot , `/proc/mountslista`apenas os sistemas de arquivos cujo ponto de montagem está dentro do chroot.

Há também uma lista de sistemas de arquivos montados no `/etc/mtab`. Esta lista é mantida pelos comandos mounte umount. Isso significa que, se você não usar esses comandos (o que é bastante raro), sua ação (montar ou desmontar) não será registrada.

## Quais são os passos para montar um sistema de arquivos no linux?

Montar um sistema de arquivos no Linux é muito simples. Tudo o que precisamos ter é um diretório específico, o qual chamamos mount point, ao qual o dispositivo será anexado. Exemplos:

<pre><code>mount - t [tipo] [caminho da partição] [ponto de montagem]</code></pre>

## Como desmontar um sistema de arquivo?

Utilize o comando umount para desmontar um sistema de arquivos montado no Linux. A sintaxe é muito simples: basta digitar o comando e declarar o mount point que deseja desmontar. Exemplos:

`umount /dev/sda4`

`umount /arquivos`

`umount /ISSO`

## Virtualização

 A Virtualização é a ideia de construir uma versão virtual de ambientes computadorizados. Ou seja, a criação de máquinas virtuais a partir de um.

## Por que o Docker pode ser útil a segurança e virtualização?

 O Docker é uma ferramenta que permite criar ambientes isolados e portáteis (containers) e através dela os desenvolvedores podem empacotar aplicações com bibliotecas e links necessários trazendo mais eficiência e simplificação.

 Com o Docker não há a necessidade de ter o gerenciamento feito diretamente, ele é instalado em em cada servidor e apresenta comandos simples, facilitanto o dia a dia do desenvolvedor e trazendo segurança.

Para a instalação do Docker seguir os passos do site a seguir: <a href="https://www.hostinger.com.br/tutoriais/install-docker-ubuntu">Docker</a>


## Sistemas de arquivos e E/S no projeto

Após a execução do programa é gerado um arquivo lista_filmes.csv contendo os nomes dos filmes e nota da audiência. O arquivo é gerado no diretório do projeto.
E ordenado por ordem crescente pelo comando:
<pre><code>sort -t"," -k2 lista_filmes.csv</code></pre>
o comando "-k2" ordena por coluna, no caso do nosso projeto, ele está ordenando a 2 coluna do arquivo .csv, ou seja, pela nota da audiência.


