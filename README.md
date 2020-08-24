# Api Task List

![](ERD.png)

Steps to run this project:

1. You should run the containers and build the images
```shell
    docker-compose up --build
```

2. Then create db connection
- DRIVER: PostgreSQL
- HOST: db
- PORT: 5432
- DATABASE: tasklist
- USERNAME: postgres
- PASSWORD: secretpassword

3. To run project you must access
http://127.0.0.1:80/


## Endpoint:

### Status da API
| Methods  | Actions                   | Url                                         |
|:--------:|:--------------------------|:--------------------------------------------|
| GET      | status da api             | {{url}/                                     |

### Task List
| Methods  | Actions                                    | Url                            |
|:--------:|:-------------------------------------------|:-------------------------------|
| GET      | retorna todas as lista cadastradas         | {{url}}/taskList               |
| POST     | permite criar uma nova lista               | {{url}}/taskList               |
| PUT      | permite a edição de uma lista específica   | {{url}}/taskList/{{id}}        |
| DELETE   | permite a remoção de uma lista específica  | {{url}}/taskList/{{id}}        |

### Task
| Methods  | Actions                                    | Url                            |
|:--------:|:-------------------------------------------|:-------------------------------|
| GET      | retorna todas as tarefas de uma lista      | {{url}}/tasks                  |
| POST     | permite criar uma nova tarefa              | {{url}}/tasks                  |
| PUT      | permite a edição de uma tarefa específica  | {{url}}/tasks/{{id}}           |
| DELETE   | permite a remoção de uma tarefa específica | {{url}}/tasks/{{id}}           |

### Tag
| Methods  | Actions                                    | Url                            |
|:--------:|:-------------------------------------------|:-------------------------------|
| GET      | retorna todas as tags cadastradas          | {{url}}/tags                   |
| POST     | permite criar uma ou mais tags             | {{url}}/tags                   |
| PUT      | permite a edição de uma tag específica     | {{url}}/tags/{{id}}            |
| DELETE   | permite a remoção de uma tag específica    | {{url}}/tags/{{id}}            |
