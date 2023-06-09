> Status: Developing 


## Descrição da aplicação:

Uma aplicação do tipo Lista de Tarefas.


## Technologies Used:

* Linux (Ubuntu based)
* Python 3
* HTML
* CSS
* Docker
* Mongo


## How to run the application:

1. Clone o repositório:

    * Clone o repositório: `git clone https://github.com/patrickjcardoso/app_python_o11y.git`

2. Acesse o diretório TaskMaster e liste os arquivos:

        cd app_python_o11y/TaskMaster/
        ls -l

3. Configuração do ambiente:

   * Certifique-se de ter o Python instalado em seu sistema.

        ` sudo apt install python3 python3-pip python3-venv `

   * Configure o ambiente:
        ```
        python3 -m venv .
        source ./bin/activate
        ```
   
   * Instale as dependências executando o comando 
         
         pip install -r requirements.txt
                
4. Inicialize o container do mongo

   `docker run --name mymongo -p 27017:27017 -d mongo`

5. Inicialize o servidor da aplicação:

        `python3 app.py`

5. Acesse a aplicação através do navegador.

        http://localhost:5000
