# Desafios Analytical

## Introdução

Em nossos serviços, muitas vezes precisamos manipular imagens para que a
leitura da mesma seja feita de forma correta. Uma dessas manipulações
requer a imagem com perspectiva corrigida e o mínimo de espaço em branco
o possível, para nossos motores poderem trabalhar diretamente no
documento, com o mínimo de ruído possível.

O problema é que, muitas das imagens que recebemos, além de virem
rotacionadas, são, por exemplo, escaneadas, logo, temos de tratar isso
internamente. Outro problema é que, muitas das vezes, aparecem artefatos
na área branca da imagem, dificultando o foco no documento em si.

## Desafio

Visando melhorar a qualidade das imagens lidas, o foco deste desafio
será criar uma aplicação que reduz ao máximo o espaço branco ao redor de
imagens de documentos. É importante notar que a rotação do documento
também influencia no resultado, visto que retângulos alinhados com um
dos eixos geram imagens mais compactas.

Tal desafio terá duas etapas obrigatórias:

1.  Implementação da aplicação indicada em
    [*Python*](http://python.org/) (versão 3.9 ou superior) utilizando,
    primariamente, do pacote do *OpenCV* para *Python*, disponível no
    [*PyPI*](https://pypi.org/project/opencv-python/). Além disso, tal
    aplicação deverá fazer uso do pacote *Flask*, também disponível no
    [*PyPI*](https://pypi.org/project/Flask/), para prover uma rota
    *http* que receberá a imagem e parâmetros a serem definidos pelo
    desenvolvedor, e retornará o binário da imagem de saída. Para
    utilização da rota *http*, também deverá ser criada uma coleção do
    [*PostMan*](https://www.postman.com/).
2.  Implementação de uma aplicação similar em *C++* que também faça uso
    do *OpenCV*, mas que seja chamada apenas por parâmetros de linha de
    comando, com argumentos também a ser definidos pelo desenvolvedor.
    Tal implementação deverá acompanhar um arquivo *Makefile* para
    compilação.

Além destas, existem 2 etapas bônus, opcionais:

1.  Criação de *bindings* das funções em *C++* como chamadas em *Python*
    utilizando do módulo *ctypes*. Nesse caso, também será necessária
    uma regra no *Makefile* para compilação da *library*.
2.  Implementação de extensões do desafio, seja em *Python* ou *C++*
    (linguagem de escolha do desenvolvedor) que inclua alguma nova
    funcionalidade relacionada ao problema que o desenvolvedor julgue
    interessante.

Tanto os pacotes utilizados quanto as versões dos mesmos e de
compiladores, interpretadores, etc, ficam a cargo do desenvolvedor. Não
será permitido usar um pacote de alto nível que faça as funcionalidades
requisitadas, nem copiar código do mesmo. Todo o histórico do
desenvolvimento deverá ser mantido, através de *commits* em um
repositório privado do *git* que será criado pelo desenvolvedor e
disponibilizado para os avaliadores antes do início do desafio.

É importante que o desenvolvedor descreva o processo criativo que o
levou até a solução.

## O que será avaliado

Em ordem de importância:

-   Criatividade nas soluções e na(s) ideia(s) de extensão;
-   Processo criativo;
-   Utilização de algoritmos e estruturas de dados;
-   Complexidade assintótica, otimizações e tempo de execução do código;
-   Qualidade dos resultados;
-   Afinidade com as linguagens e tecnologias requisitadas;
-   Parametrização dos componentes;
-   Afinidade com o uso / aprendizado de novas tecnologias e soluções;
-   Capacidade de pesquisar e implementar soluções para os problemas que
    poderão aparecer;
-   Organização do código e *commits*.

## O que será disponibilizado

-   [Imagens para teste](/files/img-desafio.tar.xz);
-   Acesso *ssh* com permissão de administrador para uma máquina recém
    formatada onde a solução deverá ser implementada e testada.

Se for da vontade do desenvolvedor, poderão ser usadas outras imagens
para teste, que também poderão ser disponibilizadas (a cargo do
desenvolvedor) para os avaliadores.

Os prazos podem ser estendidos a pedido do desenvolvedor.

## mostQI

Acesse nosso [linkedin](https://www.linkedin.com/company/mobile-solution-technology/posts/?feedView=all) para mais informações sobre vagas e novidades.
