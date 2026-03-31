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


## Tabela de tecnologias

| Mecanismo de Análise | Tecnologia de Implementação | Justificativa/Responsabilidade |
| ------------- |:-------------:|:--------------:
| Frontend      | React.js      | Interface responsiva e dinâmica, consumo da api e boa perfomance         |
| Backend       | Django     | Facilidade de implementação, segurança e velocidade         |
| Persistência      | PostgreSQL     | Armazenamento relacional, escalabilidade e open source         |