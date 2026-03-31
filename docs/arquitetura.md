# Arquitetura do software

[ USUÁRIO ]
| CAMADA FRONTEND  |
| ------------- |
| Interface     |
| Estilização   |
| Interação     |
     │
     │ Requisição HTTP (JSON/REST/GraphQL)
     │ ◄──────────────────────────────────►
     │ Resposta de Dados (Status 200, 404)
     │
| CAMADA BACKEND  |
| ------------- |
| Regras de Negócio|
| APIs   |
| Segurança     |

     │
     ▼
| CAMADA DE DADOS |
| ------------- |
| Banco de dados|
| Cache   |
| Storage     |