# desafioBridgeHub

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