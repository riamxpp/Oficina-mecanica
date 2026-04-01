# User Story US05 - Manter Insumo
## Manter Insumo

|---------------| : -----------------------------------------------------------------------------------------------------------|
| **Descrição** | O sistema deve manter o cadastro de insumos. Essa manutenção é feita pelo administrador que pode cadastrar um insumo no sistema inserindo as seguintes informações: nome, marca e descrição. Junto a isso, ele pode visualizar, editar ou excluir um insumo cadastrado. |

## Regras de negócios

| Regras de negócio                   | Descrição                                                                                |
| ------------------------------------| :---------------------------------------------------------------------------------------:|
| RN01 - Preenchimento Obrigatório    | Para cadastrar um insumo, é indispensável o preenchimento dos campos: Nome, Marca e Descrição.|
| RN02 - Validação de Dados           | O sistema não deve processar o salvamento de informações se houver campos com dados inválidos ou inconsistentes.|
| RN03 - Restrição de Acesso (Perfil) | Apenas usuários com perfil de "Administrador" (Gerente ou Auxiliar) podem realizar operações de inclusão, alteração, consulta ou exclusão de insumos.|
| RN04 - Precedência de Consulta      | Para realizar a edição ou a exclusão de um insumo, o sistema deve obrigatoriamente realizar uma consulta prévia para garantir que o registro existe.|
| RN05 - Exclusão Lógica (Suspensão)  | Ao solicitar a exclusão, os dados do insumo não devem ser apagados definitivamente, mas sim "desativados" ou "suspensos".|
| RN06 - Notificação de Inexistência  | O sistema deve exibir uma mensagem de erro específica caso o insumo consultado não esteja cadastrado ou esteja com o status suspenso.|
| RN07 - Controle de Duplicidade      | O sistema não deve permitir o cadastro de insumos com o mesmo nome e marca já existentes.|

## Mensagens do manter insumo

* Mensagem de sucesso
  * MS01 - Sucesso no Cadastro: "Insumo cadastrado com sucesso!"
  * MS02 - Sucesso na Edição: "Dados do insumo atualizados com sucesso!"
  * MS03 - Sucesso na Exclusão: "O insumo foi desativado com sucesso!"

* Mensagens de Erro
  * MS04 - Dados Inválidos: "Erro: Informações inválidas detectadas. Por favor, corrija os campos destacados e tente novamente."
  * MS05 - Insumo Inexistente: "Erro: O insumo informado não está cadastrado ou encontra-se suspenso."
  * MS06 - Falha na Exclusão: "Erro: Não foi possível desativar o insumo devido a uma instabilidade no sistema. Tente novamente."
  * MS07 - Duplicidade: "Erro: Já existe um insumo cadastrado com o mesmo nome e marca."

* Mensagens de Alerta e Confirmação
  * MS08 - Confirmação de Exclusão: "Tem certeza que deseja desativar este insumo do sistema?"
  * MS09 - Alerta de Campos Obrigatórios: "Atenção: Os campos Nome, Marca e Descrição devem ser preenchidos."


## Tabelas impactadas

1. Tabela Insumo (Principal)
   1. Campos principais: id_insumo, nome, marca, descricao

2. Tabela Ordem_Servico (Impacto Futuro)
   1. Relacionamento: insumos utilizados nos serviços

| **Requisitos envolvidos** |                  |
| ------------------------- | :--------------- |
| RF01                      | Manter insumo    |
| RF01.1                    | Cadastrar insumo |
| RF01.2                    | Alterar insumo   |
| RF01.3                    | Consultar insumo |
| RF01.4                    | Excluir insumo   |


| Testes de Aceitação (TA)                                              |
|-------- | :-----------------------------------------------------------|
| Código  | Descrição                                                   |
| ------- | ----------------------------------------------------------- |
| TA01.01 | Verificar se todos os dados informados são válidos.         |
| TA01.02 | Verificar se está salvando os dados do insumo.              |
| TA01.03 | Verificar se está consultando dados do insumo corretamente. |
| TA01.04 | Verificar se está atualizando dados do insumo corretamente. |
| TA01.05 | Verificar se está suspendendo dados do insumo corretamente. |
| TA01.06 | Verificar se não permite cadastro duplicado.                |

| ----------------------- | --------- |
| **Prioridade**          | Essencial |
| **Estimativa**          | 2 h       |
| **Tempo Gasto (real):** | 30 m      |
| **Tamanho Funcional**   |           |
| **Analista**            | José      |
| **Desenvolvedor**       | Riam      |
| **Revisor**             | Ariadny   |
| **Testador**            | Ariadny   |


### User Story US05 - Manter Insumo

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US05</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Cadastrar, atualizar, visualizar e deletar dados do insumo.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US05 - Manter insumo</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em>o administrador</em>, quero <em>adicionar, visualizar, atualizar e remover</em> dados do insumo para <em>manter o controle dos materiais utilizados no sistema</em>.
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Critérios de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>O sistema deve exibir mensagem de erro caso os dados estejam inválidos.</li>
        <li>O sistema deve impedir cadastro duplicado de insumos.</li>
        <li>O sistema deve exibir mensagem de insumo inexistente ao consultar um insumo não cadastrado ou suspenso.</li>
        <li>O sistema deve exibir mensagem de erro caso não consiga excluir o insumo.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Testes de Aceitação</strong></td>
    <td style="padding:6px;">
      <ul>
        <li>TA01 - Cadastro bem-sucedido com dados válidos.</li>
        <li>TA02 - Validação de dados ao cadastrar, atualizar e consultar.</li>
        <li>TA03 - Bloqueio de cadastro duplicado.</li>
        <li>TA04 - Tentativa de exclusão sem sucesso retorna erro.</li>
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
        <li><strong>Analista:</strong> José</li>
        <li><strong>Desenvolvedor:</strong> Riam</li>
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
