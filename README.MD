## Definição de rotas da API

### Listar educandos
TODO:
- Incluir foto do educando

GET /educandos
RESPONSE
```json
[
  {
    "id": 1,
    "nome_completo": "João da Sila",
    "trilha": "Programação",
    "unidade": "SC401"
  },
  ...
]
```

### Listar inisignias
GET / Insignias
RESPONSE
```JSON
[
 {
  "id":1,
  "nome":"Python",
  "trilha":"Programação",
  "niveis": [
    {
      "id":1,
      "requisitos": [
        {
          "id":1,
          "descricao":"conhecer algoritmo"
        },
        {
          "id":2,
          "descricao":"conhecer variáveis"
        },
        {
          "id":3,
          "descricao":"conhecer estruturas de controle"
        }
      ]
    },
    {
      "id":2,
      "requisitos": [
        {
          "id":1,
          "descricao":"conhecer algoritmo"
        },
        {
          "id":2,
          "descricao":"conhecer variáveis"
        },
        {
          "id":3,
          "descricao":"conhecer estruturas de controle"
        }
      ]
    }
  ]
 }
]
```

- insignias de um educando
- Listar níveis de insignias
- Listar os requisitos
- Registar conquista de insignias

### Registrar insignias Novas
POST /insignia/criar
PAYLOAD
```json
{
  "nome":"Python",
  "trilha":"Programação",
  "niveis": [
    {
      "id":1,
      "requisitos": [
        {
          "id":1,
          "descricao":"conhecer algoritmo"
        },
        {
          "id":2,
          "descricao":"conhecer variáveis"
        },
        {
          "id":3,
          "descricao":"conhecer estruturas de controle"
        }
      ]
    },
    {
      "id":2,
      "requisitos": [
        {
          "id":1,
          "descricao":"conhecer algoritmo"
        },
        {
          "id":2,
          "descricao":"conhecer variáveis"
        },
        {
          "id":3,
          "descricao":"conhecer estruturas de controle"
        }
      ]
    }
  ]
}
```

SUCESSO 201
```json
{
  "status": "success",
}
```

ERROR 400
```json
{
  "status": "error",
  "message": "Erro na criação da insígnia",
  "detalhes": "Descrição técnica do erro"
}
```

- Registrar educando Novo



