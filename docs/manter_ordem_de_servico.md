# User Story US06 - Manter Ordem de Serviço
## Manter ordem de serviço

|               |                                                                                                                                                                                                                                                                                                               |
| ------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Descrição** | O sistema deve manter uma Ordem de serviço. O administrador pode cadastrar uma ordem de serviço com os atributos id, id_veiculo, id_procedimento e data. O sistema não terá mecanismo de login, o administrador (adm) do sistema será responsável por cadastrar o usuário. Além disso o adm poderá alterar alguns dados, como o e-mail ou nome. O administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os usuários comuns do sistema. Essa funcionalidade tem algumas dependências de veículos e procedimentos.|

## Regras de negócios

| Regras de negócio                           |                                                                            Descrição                                                                            |
| ------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| RN01 - Vínculo Obrigatório com Veículo      |                                 Toda ordem de serviço deve estar obrigatoriamente vinculada a um veículo cadastrado no sistema.                                 |
| RN02 - Vínculo Obrigatório com Procedimento |                               Toda ordem de serviço deve estar obrigatoriamente vinculada a um procedimento cadastrado no sistema.                              |
| RN03 - Preenchimento Obrigatório            |                          Para cadastrar uma ordem de serviço, é indispensável o preenchimento dos campos: Veículo, Procedimento e Data.                         |
| RN04 - Restrição de Acesso (Perfil):        | Apenas usuários com perfil de "Administrador" (Gerente ou Auxiliar) podem realizar operações de inclusão, alteração, consulta ou exclusão de ordens de serviço. |
| RN05 - Validação de Dados                   |                         O sistema não deve processar o salvamento de informações se houver campos com dados inválidos ou inconsistentes.                        |
| RN06 - Precedência de Consulta              | Para realizar a edição ou a exclusão de uma ordem de serviço, o sistema deve obrigatoriamente realizar uma consulta prévia para garantir que o registro existe. |
| RN07 - Exclusão Lógica (Suspensão)          |   Ao solicitar a exclusão, os dados da ordem de serviço não devem ser apagados definitivamente, mas sim "desativados" ou "suspensos" para manter o histórico.   |
| RN08 - Notificação de Inexistência          |         O sistema deve exibir uma mensagem de erro específica caso a ordem de serviço consultada não esteja cadastrada ou esteja com o status suspenso.         |
| RN09 - Verificação de Dependência           |         O sistema deve garantir que o veículo e o procedimento informados estejam cadastrados e ativos antes de permitir o cadastro da ordem de serviço.        |

## Mensagens do manter ordem de serviço

* Mensagem de sucesso

  * MS01 - Sucesso no Cadastro: "Ordem de serviço cadastrada com sucesso!"
  * MS02 - Sucesso na Edição: "Dados da ordem de serviço atualizados com sucesso!"
  * MS03 - Sucesso na Exclusão: "A ordem de serviço foi desativada com sucesso!"
* Mensagens de Erro

  * MS04 - Dados Inválidos: "Erro: Informações inválidas detectadas. Por favor, corrija os campos destacados e tente novamente."
  * MS05 - Ordem de Serviço Inexistente: "Erro: A ordem de serviço informada não está cadastrada ou encontra-se suspensa."
  * MS06 - Falha na Exclusão: "Erro: Não foi possível excluir a ordem de serviço devido a uma instabilidade no sistema. Tente novamente."
  * MS07 - Erro de Vínculo: "Erro: Não é possível cadastrar a ordem de serviço. É necessário selecionar um veículo e um procedimento válidos."
* Mensagens de Alerta e Confirmação

  * MS08 - Confirmação de Exclusão: "Tem certeza que deseja desativar esta ordem de serviço do sistema?"
  * MS09 - Alerta de Pré-requisito: "Atenção: Para cadastrar uma ordem de serviço, você deve primeiro possuir um veículo e um procedimento previamente registrados."
  * MS10 - Alerta de Campos Obrigatórios: "Atenção: Todos os campos (Veículo, Procedimento e Data) devem ser preenchidos."

## Tabelas impactadas

1. Tabela Ordem_Servico (Principal)
2. Campos principais: id_ordem_servico, data, status.
3. Relacionamentos: Recebe id_veiculo e id_procedimento como referências obrigatórias.
4. Tabela Veiculo
5. Campos envolvidos: id_veiculo, placa.
6. Tabela Procedimento
7. Campos envolvidos: id_procedimento, nome.
8. Tabela Ordem_Servico (Impacto Futuro)

| **Requisitos envolvidos** |                             |
| ------------------------- | :-------------------------- |
| RF01                      | Manter ordem de serviço     |
| RF01.1                    | Cadastrar ordem de serviço  |
| RF01.2                    | Alterar ordem de serviço    |
| RF01.3                    | Consultar ordem de serviços |
| RF01.4                    | Excluir ordem de serviço    |

| Código  | Descrição                                                             |
| ------- | --------------------------------------------------------------------- |
| TA01.01 | Verificar se todos os dados informados são válidos.                   |
| TA01.02 | Verificar se está salvando os dados da ordem de serviço.              |
| TA01.03 | Verificar se está consultando dados da ordem de serviço corretamente. |
| TA01.04 | Verificar se está atualizando dados da ordem de serviço corretamente. |
| TA01.05 | Verificar se está suspendendo dados da ordem de serviço corretamente. |

|                         |           |
| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 15 h      |
| **Tempo Gasto (real):** | 1:30 h    |
| **Tamanho Funcional**   |           |
| **Analista**            | José      |
| **Desenvolvedor**       | Ariadny   |
| **Revisor**             | Riam      |
| **Testador**            | Riam      |

### User Story US02 - Manter Projeto

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US06</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Cadastrar, atualizar, visualizar e deletar dados da ordem de serviço.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US06 - Manter ordem de serviço</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em> o administrador </em>, quero <em> adicionar, visualizar, atualizar e remover</em>, ordens de serviço para <em>conseguir manter o sistema</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve exibir mensagem de erro caso os dados estejam inválidos.</li>
        <li>O sistema deve exibir mensagem de ordem de serviço inexistente caso ele tente pesquisar uma ordem não cadastrada.</li>
        <li>O sistema deve exibir mensagem de erro caso não consiga deletar ordem de serviço.</li>
        <li>Deve haver pelo menos 1 veículo e 1 procedimento cadastrados no sistema.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>TA01 - Cadastro bem-sucedido com todos os dados preenchidos.</li>
        <li>TA02 - Para cadastrar, atualizar e visualizar validar os dados.</li>
        <li>TA03 - Tentativa de deletar sem sucesso retorna erro.</li>
        <li>TA04 - Verificar se o veículo e o procedimento existem.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Estimativa</strong></td>
    <td style="padding:6px;">15h</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Tempo Real Gasto</strong></td>
    <td style="padding:6px;">1:30h</td>
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
        <li><strong>Analista:</strong> José</li>
        <li><strong>Desenvolvedor:</strong> Ariadny</li>
        <li><strong>Revisor:</strong> Riam</li>
        <li><strong>Testador:</strong> Riam</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>
