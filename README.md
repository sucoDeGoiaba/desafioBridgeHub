# Desafio - BridgeHub

## Instalando aplicação:
Abra o terminal/Powershell e rode os comandos abaixo:

Clonando o repositório:

Via HTTPS:
```
git clone https://github.com/sucoDeGoiaba/desafioBridgeHub.git
```

Via SSH:
```
git clone https://github.com/sucoDeGoiaba/desafioBridgeHub.git
```

Entrando na pasta:
```
cd desafioBridgeHub
```

Instalando dependências:
```
pip install -r requirements.txt
```

Criando tabelas no banco de dados:
```
python db_setup.py
```


Iniciando o servidor:
```
python app.py
```


## Rotas implementadas:

### Usuário

* **GET /users/**
 
    Schema da resposta
    ```
    {
        "usuarios": [
            {   
                "id" : <Integer>,
                "nome" : <String>,
                "email": <String>,
                "telefone" : <String>,
            }
        ]
    }
    ```

* **GET /users/<id>**
 
    Schema da resposta
    ```
    {
        "usuario": [
            {   
                "id" : <Integer>,
                "nome" : <String>,
                "email": <String>,
                "telefone" : <String>
            }
        ]
    }
    ```

* **POST /add_user/**
 
    Schema da requisição
    ```
    {
        "nome" : <String>,
        "email": <String>,
        "telefone" : <Integer>
    }
    ```
 
    Schema da resposta
    ```
    {
        "resposta": "Usuário adicionado!"
    }
    ```

* **PUT /edit_user/<id>**
 
    Schema da requisição
    ```
    {
        "nome" : <String>,
        "email": <String>,
        "telefone" : <Integer>
    }
    ```
 
    Schema da resposta
    ```
    {
        "resposta": "Usuário editado!"
    }
    ```

* **DELETE /delete_user/**

    Schema da requisição
    ```
    {
        "id" : <Integer>,
    }
    ```
 
    Schema da resposta
    ```
    {
        "resposta": "Usuário deletado!"
    }
    ```