# Documento de Modelos

## Modelo Conceitual

### Diagrama de Classes usando Mermaid

```mermaid
classDiagram
    class Modelo {
        -int id_modelo
        -String nome
        -id_marca marca
        +cadastrarModelo(nome, marca) void
        +visualizarVeiculo(id_modelo) Veiculo
        +editarVeiculo(id_modelo) void
        +excluirVeiculo(id_modelo) void
    }

    class Marca {
        -int id_marca
        -String marca
        +cadastrarMarca() void
        +visualizarMarca() Veiculo
        +editarMarca() void
        +excluirMarca() void
    }

    class Veiculo {
        -int id_veiculo
        -Modelo id_modelo
        -String categoria
        -String cor
        -String placa
        -Cliente id_cliente
        +cadastrarVeiculo(marca, modelo, tipo, cor, placa, id_cliente) void
        +visualizarVeiculo(id_veiculo) Veiculo
        +editarVeiculo(id_veiculo) void
        +excluirVeiculo(id_veiculo) void
    }

    class Cliente {
        -int id_pessoa
        -String nome
        -String cpf
        -Endereco endereco
        +cadastrarPessoa(nome, cpf, endereco) void
        +visualizarPessoa(id_pessoa) Pessoa
        +editarPessoa(id_pessoa) void
        +excluirPessoa(id_pessoa) void
    }

    class Enderecos {
        -int id_endereco
        -String rua
        -Bairro id_bairro
        -String numero
        +cadastrarEndereco(rua, bairro, numero) void
        +visualizarEndereco() Endereco
        +editarEndereco() void
        +deletarEndereco() void
    }

    class Bairro {
        -int id_bairro
        -String nomeBairro
        -Cidade id_cidade
    }

    class Cidade {
        -int id_cidade
        -String nomeCidade
    }

    class Ordem_de_Servico {
        -int id_ordem_servico
        -Procedimento id_procedimento
        -Veiculo id_veiculo
        -Date data
        +cadastrarProcedimento() void
        +visualizarProcedimento() Procedimento
        +editarProcedimento() void
        +excluirProcedimento() void
        +relatorio_ordem_servico(periodo) servicos_periodo
        +calcular_valor_total() valor_final
    }

    class Cobranca {
        -int id_cobranca
        -Ordem_de_Servico id_ordem_servico
        -float valor_total
        -Date data_emissao
        +calcular_valor_restante() float
        +pagamento_pendente() ordens_servico
    }

    class Pagamento {
        -int id_pagamento
        -Cobranca id_cobranca
        -float valor_pago
        -Date data
        -String metodo_pagamento
    }

    class Insumos_do_Servico {
        -int id_insumos_serv
        -Ordem_serv id_ordem_serv
        -Insumo id_insumo
        -int qtd_usada
    }

    class Insumo {
        -int id_insumo
        -String nome
        -String descricao
        -int quantidade
        +cadastrarInsumo() void
        +visualizarInsumo() Insumo
        +editarInsumo() void
        +excluirInsumo() void
        +relatorio_estoque() insumo_faltando
    }

    class Procedimento {
        -int id_procedimento
        -String nome
        -float valor
        -dateTime tempoEstimado
        -String descricao
        -int id_insumo
        +cadastrarProcedimento() void
        +visualizarProcedimento() Procedimento
        +editarProcedimento() void
        +excluirProcedimento() void
    }

    %% Relacionamentos e Multiplicidades
    Marca "1..1" -- "1..*" Modelo
    Modelo "1..1" -- "1..*" Veiculo
    Cliente "1..1" -- "1..*" Veiculo
    Cliente "1..1" -- "1..1" Enderecos
    Bairro "1..1" -- "1..*" Enderecos
    Cidade "1..1" -- "1..*" Bairro
    Veiculo "1..1" -- "1..*" Ordem_de_Servico
    Procedimento "1..1" -- "1..*" Ordem_de_Servico
    Ordem_de_Servico "1..1" -- "1..1" Cobranca
    Cobranca "1..1" -- "1..*" Pagamento
    Ordem_de_Servico "1..1" -- "1..*" Insumos_do_Servico
    Insumo "1..1" -- "1..*" Insumos_do_Servico
```

### Descrição das Entidades

Descrição sucinta das entidades presentes no sistema.

| Entidade | Descrição   |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cliente   | Entidade para representar os clientes da loja tendo as informações de: nome, telefone e *endereco*.                                                  |
| Veiculo   | Entidade que representa um veiculo de determinado cliente tem as informações: *Modelo*, categoria, cor, placa, *cliente*. |
| Procedimentos   | Entidade que representa um Procedimento/Serviço que a oficina com as informações: nome, valor, tempoEstimado, descrição. |
| Ordem de Serviços | Entidade que representa uma Ordem de serviço onde se relacionam um veiculo de um cliente a um procedimento que foi realizado nele com as informações: *procedimento*, *veiculo*, data. |
| Insumo | Entidade que representa um Insumo presente no estoque da Oficina com as informações: nome, descricao, quantidade.  |

## Modelo de Dados (Entidade-Relacionamento)

Para criar modelos ER é possível usar o BrModelo e gerar uma imagem. Contudo, atualmente é possível criar modelos ER usando a ferramenta **Mermaid**, escrevendo o modelo diretamente em markdown. Acesse a documentação para escrever modelos [ER Diagram Mermaid](https://mermaid-js.github.io/mermaid/#/entityRelationshipDiagram).

```mermaid
erDiagram
    MARCA ||--|{ MODELO : "possui"
    MODELO ||--|{ VEICULO : "tem"
    CLIENTE ||--|{ VEICULO : "possui"
    ENDERECO ||--|| CLIENTE : "pertence_a"
    BAIRRO ||--|{ ENDERECO : "contem"
    CIDADE ||--|{ BAIRRO : "contem"
    VEICULO ||--|{ ORDEM_SERVICO : "registra"
    PROCEDIMENTO ||--|{ ORDEM_SERVICO : "realizado_em"
    ORDEM_SERVICO ||--|| COBRANCA : "gera"
    COBRANCA ||--|{ PAGAMENTO : "recebe"
    ORDEM_SERVICO ||--|{ INSUMOS_SERVICO : "utiliza"
    INSUMO ||--|{ INSUMOS_SERVICO : "usado_como"
```

### Dicionário de Dados

| Tabela     | Cliente |
| ---------- | ------- |
| Descrição  | Armazena as informações pessoais e de contato dos clientes da oficina. |
| Observação | Cada cliente pode possuir um ou mais veículos associados a ele. |

| Nome          | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_pessoa     | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| nome          | nome completo do cliente         | VARCHAR      | 150     | Not Null |
| cpf           | documento de identificação       | VARCHAR      | 14      | Unique / Not Null |
| id_endereco   | referência ao endereço do cliente| SERIAL       | ---     | FK / Not Null |

| Tabela     | Veiculo |
| ---------- | ------- |
| Descrição  | Armazena os dados dos veículos cadastrados para manutenção na oficina. |
| Observação | O veículo obrigatoriamente pertence a um cliente e é de um modelo específico. |

| Nome          | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_veiculo    | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| categoria     | categoria do veículo (ex: SUV)   | VARCHAR      | 50      | Not Null |
| cor           | cor predominante do veículo      | VARCHAR      | 30      | Not Null |
| placa         | placa de identificação           | VARCHAR      | 10      | Unique / Not Null |
| id_modelo     | referência ao modelo do veículo  | SERIAL       | ---     | FK / Not Null |
| id_cliente    | referência ao dono do veículo    | SERIAL       | ---     | FK / Not Null |

| Tabela     | Ordem_Servico |
| ---------- | ------------- |
| Descrição  | Registra os serviços que estão sendo ou foram realizados na oficina. |
| Observação | Entidade central que conecta o veículo aos procedimentos e peças (insumos). |

| Nome              | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ----------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_ordem_servico  | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| data              | data de abertura do serviço      | DATE         | ---     | Not Null |
| id_procedimento   | referência ao procedimento       | SERIAL       | ---     | FK / Not Null |
| id_veiculo        | referência ao veículo consertado | SERIAL       | ---     | FK / Not Null |

| Tabela     | Procedimento |
| ---------- | ------------ |
| Descrição  | Catálogo de serviços e mão de obra oferecidos pela oficina. |
| Observação | Define o que é feito, tempo estimado e quanto custa a mão de obra. |

| Nome              | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ----------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_procedimento   | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| nome              | nome do serviço oferecido        | VARCHAR      | 100     | Not Null |
| valor             | valor cobrado pela mão de obra   | NUMERIC      | 10,2    | Not Null |
| tempoEstimado     | tempo estimado para conclusão    | TIMESTAMP    | ---     | Not Null |
| descricao         | detalhamento técnico do serviço  | VARCHAR      | 250     | --- |
| id_insumo         | referência a um insumo padrão    | SERIAL       | ---     | FK |

| Tabela     | Insumo |
| ---------- | ------ |
| Descrição  | Estoque de peças e materiais utilizados nos serviços da oficina. |
| Observação | Pode representar desde peças grandes até consumíveis (óleo, estopa). |

| Nome              | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ----------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_insumo         | identificador gerado pelo SGBD   | SERIAL       | ---     | PK / Identity |
| nome              | nome da peça ou material         | VARCHAR      | 100     | Not Null |
| descricao         | especificações técnicas e marca  | VARCHAR      | 250     | --- |
| quantidade        | quantidade atual em estoque      | INTEGER      | ---     | Not Null |
