# User Story US04 - Manter Procedimentos
## Manter procedimentos

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema conter informações gerais a respeito do procedimento. Um procedimento tem os atributos nome, valor, tempo_medio e descrição. O administrador (adm) do sistema será responsável por cadastrar o procedimento. Também poderá consultar dados sobre o procedimento no sistema. O administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os usuários comuns do sistema. |

## Regras de negócios

| Regras de negócio| Descrição|
| ------------- | :-----------------:|
| RN01 - Atributos Obrigatórios         | Para que um procedimento seja cadastrado, é indispensável o preenchimento dos campos: Nome, Valor, Tempo Médio e Descrição.    |
| RN02 - Restrição de Acesso (Perfil)        | Apenas o usuário com perfil de Administrador (ADM) tem permissão para realizar as operações de adicionar, alterar, consultar ou remover procedimentos.  |
| RN03 - Validação de Dados        | O sistema deve validar todos os dados informados antes de persistir as informações no banco de dados.    |
| RN04 - Precedência de Consulta        | Para realizar qualquer alteração ou exclusão de um procedimento, o sistema deve obrigatoriamente realizar uma consulta prévia para garantir a existência do registro. |
| RN05 - Integridade de Exclusão (Suspensão)      | O processo de remoção deve seguir a lógica de suspensão (exclusão lógica), garantindo que os dados não sejam perdidos caso haja vínculo com históricos de serviço.    |
| RN06 - Unicidade de Procedimento       | O sistema deve garantir que não existam procedimentos duplicados com o mesmo nome para evitar inconsistências nos valores cobrados.   |

## Mensagens do Manter Procedimentos

* Mensagem de sucesso
  * MS01 - Sucesso no Cadastro: "Procedimento cadastrado com sucesso!"
  * MS02 - Sucesso na Edição: "Dados do veículo procedimento com sucesso!" 
  * MS03 - Sucesso na Exclusão: "O procedimento foi desativado com sucesso!"
* Mensagens de Erro
  * MS04 - Dados Inválidos: "Erro: Informações inválidas detectadas. Por favor, insira os dados novamente."
  * MS05 - Procedimento Inexistente:"Erro: O procedimento informado não está cadastrado no sistema ou encontra-se suspenso."
  * MS06 - Falha na Exclusão: "Erro: O sistema apresentou instabilidade e não registrou a desativação do procedimento. Tente novamente."
* Mensagens de Alerta e Confirmação
    * MS07 - Confirmação de Exclusão: "Deseja realmente suspender o cadastro deste procedimento no sistema?"
    * MS08 - Alerta de Campos Obrigatórios: "Atenção: Os campos Nome, Valor e Tempo Médio devem ser preenchidos corretamente."


## Tabelas impactadas

1. Tabela Procedimento (Principal)
  1. Atributos manipulados: id_procedimento, nome, valor, tempo_estimado e descrição.
2. Tabela Ordem_Servico (Impacto de Relacionamento)
  1. Relação: Cada registro de Ordem de Serviço possui uma chave estrangeira id_procedimento.
  2. Regra: Não é possível cadastrar um serviço sem que o procedimento executado já esteja registrado.
3. Tabela Insumo (Impacto de Associação)
    1. Relação: Ao manter um procedimento, o sistema pode precisar consultar quais materiais (insumos) são necessários para que esse serviço seja concluído.

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Manter procedimento |
| RF01.1        | Cadastrar procedimento  |
| RF01.2        | Alterar procedimento  |
| RF01.3        | Consultar procedimento       |
| RF01.5        | Excluir procedimento |

| Código | Descrição |
|--------|----------------------------------------------------|
| TA01.01| Verificar se todos os dados informados são válidos. |
| TA01.02| Verificar se está salvando os dados do proceidmento. |
| TA01.03| Verificar se está consultando dados do proceidmento corretamente. |
| TA01.04| Verificar se está atualizando dados do proceidmento corretamente. |
| TA01.05| Verificar se está suspendendo dados do proceidmento corretamente. |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 2 h                                 | 
| **Tempo Gasto (real):**   | 30m                                 | 
| **Tamanho Funcional**     |                                     | 
| **Analista**              | Riam                                | 
| **Desenvolvedor**         | José                                | 
| **Revisor**               | Ariadny                             | 
| **Testador**              | Ariadny                             | 

### User Story US02 - Manter Projeto

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US04</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Cadastrar, atualizar, visualizar e deletar dados do procedimento.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US04 - Manter procedimento</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em> o administrador </em>, quero <em> adicionar, visualizar, atualizar e remover</em> procedimento para <em>conseguir manter o sistema</em>.
    </td>
  </tr>
  <!-- <tr>
    <td style="padding:6px;"><strong>Requisitos Relacionados</strong></td>
    <td style="padding:6px;">RF01, RF02...</td>
  </tr> -->
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve exibir mensagem de erro caso os dados estejam inválidos.</li>
        <li>O sistema deve exibir mensagem de procedimento inexistente caso ele tente pesquisar um procedimento não cadastrado.</li>
        <li>O sistema deve exibir mensagem de erro caso não consiga deletar procedimento.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>TA01 - Cadastro bem-sucedido com todos os dados preenchidos.</li>
        <li>TA02 - Para cadastrar, atualizar e visualizar válidar os dados.</li>
        <li>TA03 - Tentativa de deletar sem sucesso retorna erro.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">2h</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;">30m</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tamanho Funcional</strong></td>
    <td style="padding:6px;"></td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Prioridade</strong></td>
    <td style="padding:6px;">Essencial</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Responsáveis</strong></td>
    <td style="padding:6px;">
      <ul>
        <li><strong>Analista:</strong> Riam</li>
        <li><strong>Desenvolvedor:</strong> José</li>
        <li><strong>Revisor:</strong> Ariadny</li>
        <li><strong>Testador:</strong> Ariadny</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>
