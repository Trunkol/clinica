# clinica

## Instalação:

Este projeto necessita do Python 3 e o Docker instalado na máquina principal. Para instalar as dependencia do Python, deve-se entrar no diretório principal do projeto é executar o seguinte comando:

`pip install -r requirements.txt`

E para subir o banco no redis temos que rodar um container desta forma:

`sudo docker run -d -p 6379:6379 redis`

Depois, para rodar um banco do sqlite fazemos:

`python ./manage.py migrate`

Por fim, rodamos o servidor na porta 8000 com o seguinte comando:

`python ./manage.py runserver`
