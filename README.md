<h1 align="center"> Desafio de Renderização e de Interação do Flask com o Forms</h1>

# :mag_right: Índice

* [Sobre os Desafios](#sobre)
* [Como Usar](#comoUsar)
* [Ferramentas Utilizadas](#ferramentas)

<span id="sobre"></span>

# Sobre os Desafios

Os desafios a seguir foram baseados no [Repositório](https://github.com/prof-fabriciogmc/html_basico) solicitados na aula de Design Digital, dada pelo profº Fabrício Galende Marques de Carvalho, criador do repositório.

<details>
  <summary><b>Vídeo "Renderização"</b></summary>

 ![print_desafioRenderizacão]()
</details>
<details>
  <summary><b>Vídeo "Forms"</b></summary>
  
 ![print_desafioInteraçãoDoFlaskComOForms]()
</details>


<span id="comoUsar"></span>

# Como Usar

<details>
  <summary><b>O que será necessário:</b></summary>

  <a href="https://git-scm.com/downloads">Git</a> Será necessário o git para fazer uma clonagem do repositório.
</details>

<details>
  <summary><b>Clonando o repositório:</b></summary>
  
  1º Passo: Crie uma pasta vazia.

  2º Passo: Entre na pasta criada e clique no diretório na parte superior e digite cmd:

  ![print_diretório]()

  3º Passo: Dentro do cmd insira o comando:
 
  `git clone "https://github.com/BrunoSerpa/Desafio02_DW1" .`
</details>


<details>
  <summary><b>Rodando Desafio "Renderização":</b></summary>

  Execute o arquivo `imagens.html` em seu navegador padrão. (encontrado em `src/Renderizando Fotos`) 
</details>
<details>
    <summary><b>Rodando Desafio "Forms com Flask":</b></summary>

  1º Passo: Dentro do cmd no qual o repositório foi clonado insira o comando: 
  
  `cd 'src/Interação do Flask com Forms'`

  2º Passo: Crie o Ambiente Virtual com o comando:
  
  `py -m venv venv`
  >Caso os comando não funcionar, troque a palavra <b>py</b> do comando por <b>py3</b>.<br/> 

  3º Passo: Entre no ambiente com o comando:
  
  `.\venv\Scripts\activate`.

  4º Passo: Instale os requerimentos do projeto com o comando:
  
  `pip install -r requirements.txt`.

  5º Passo: Acesse o projeto com o comando:

  `flask run`
  >Isso executará o `app.py` e será possível ver o site funcionando.

  6ºPasso: Após realizar o comando flask run, clique no link que ele te dará no cmd, ou então simplesmente acesse este:
  
  <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a>

  7º Quando finalzar o comando para finalizar o ambiente é:

  `deactivate`
  
</details>

<span id="ferramentas"></span>

# Ferramentas Utilizadas

<a href="https://www.w3schools.com/html/">HTML</a>: Estruturação das páginas.<br/> Foram utilizados: `button`, `footer`, `form`, `img`, `input` e `style`

<a href="https://www.w3schools.com/css/">CSS</a>: Estilização de todas as páginas.<br/>
Foram utilizados tags e classes.

<a href="">Flask</a>: Utilizado para fazer auxilio de manutenções, utilizando do arquivo "controller.py", no qual pega as informações passadas pelo "form.html"