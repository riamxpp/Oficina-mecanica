# User Story US01 - Manter Usuário
## Manter usuário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de usuário. Um usuário tem os atributos nome, CPF, email, telefone e endereço. O sistema não terá mecanismo de login, o administrador (adm) do sistema será responsável por cadastrar o usuário. Além disso o adm poderá alterar alguns dados, como o e-mail ou nome. O administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os usuários comuns do sistema. |

## Regras de negócios 

| Regra de Negócio | Descrição |
| :--- | :--- |
| **RN01 - Preenchimento Obrigatório** | Para cadastrar um usuário, é indispensável o preenchimento dos atributos principais: nome, CPF, e-mail, telefone e endereço. |
| **RN02 - Restrição de Acesso (Perfil)** | Como o sistema não possui mecanismo de login próprio para usuários comuns, apenas o "Administrador" tem permissão para adicionar, alterar, remover e listar os usuários do sistema. |
| **RN03 - Validação de Dados** | O sistema não deve processar o salvamento de informações e deve exibir mensagem de erro caso os dados estejam inválidos durante o cadastro ou atualização. |
| **RN04 - Atualização de Dados** | O administrador do sistema tem a permissão de alterar os dados cadastrais do usuário (com destaque para campos como e-mail ou nome). |
| **RN05 - Notificação de Inexistência** | O sistema deve exibir mensagem de usuário inexistente caso o administrador tente pesquisar/consultar um usuário que não está cadastrado. |
| **RN06 - Regra de Remoção (Suspensão)** | Ao solicitar a exclusão de um usuário, os dados devem ser suspensos/desativados no sistema. O sistema deve exibir mensagem de erro caso não consiga deletar o usuário. |

## Mensagens 

* **Mensagens de Sucesso**
  * MS01 - Sucesso no Cadastro: "Usuário cadastrado com sucesso!"
  * MS02 - Sucesso na Edição: "Dados do usuário atualizados com sucesso!"
  * MS03 - Sucesso na Exclusão/Suspensão: "O usuário foi suspenso/removido com sucesso!"

* **Mensagens de Erro**
  * MS04 - Dados Inválidos: "Erro: Informações inválidas detectadas. Por favor, verifique os dados informados e tente novamente."
  * MS05 - Usuário Inexistente: "Erro: O usuário pesquisado não está cadastrado no sistema."
  * MS06 - Falha na Exclusão: "Erro: Não foi possível deletar o usuário. Ocorreu um problema no sistema, tente novamente."

* **Mensagens de Alerta e Confirmação**
  * MS07 - Confirmação de Exclusão: "Tem certeza que deseja suspender/remover este usuário do sistema?"
  * MS08 - Alerta de Campos Obrigatórios: "Atenção: Os campos nome, CPF, e-mail, telefone e endereço devem ser preenchidos obrigatoriamente."
  

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Manter usuário |
| RF01.1        | Cadastrar Usuário  |
| RF01.2        | Alterar Usuário  |
| RF01.3        | Consultar Usuários        |
| RF01.4        | Excluir Usuário |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 10 hr                               | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Ariadny                             | 
| **Desenvolvedor**         | Riam                                | 
| **Revisor**               | José                                | 
| **Testador**              | José                                | 

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| Código | Descrição |
|--------|----------------------------------------------------|
| TA01.01| Verificar se todos os dados informados são válidos. |
| TA01.02| Verificar se está salvando os dados do cliente. |
| TA01.03| Verificar se está consultando dados do clientes corretamente. |
| TA01.04| Verificar se está atualizando dados do clientes corretamente. |
| TA01.05| Verificar se está suspendendo dados do clientes corretamente. |


### User Story US01 - Manter Usuario

<table>
  <tr>
    <th colspan="2" style="text-align:left;background:#e0e0e0;padding:8px;">📌 User Story - US01</th>
  </tr>
  <tr>
    <td style="width:25%;padding:6px;"><strong>Título</strong></td>
    <td style="padding:6px;">Cadastrar, atualizar, visualizar e deletar dados do usuário.</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Identificação</strong></td>
    <td style="padding:6px;">US01 - Manter usuário</td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Story</strong></td>
    <td style="padding:6px;">
      Como <em> o administrador </em>, quero <em> adicionar, visualizar, atualizar e remover</em>, para <em>conseguir manter o sistema</em>.
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
        <li>O sistema deve exibir mensagem de usuário inexistente caso ele tente pesquisar um usuário não cadastrado.</li>
        <li>O sistema deve exibir mensagem de erro caso não consiga deletar usuário.</li>
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
        <li><strong>Analista:</strong> Riam</li>
        <li><strong>Desenvolvedor:</strong> Riam</li>
        <li><strong>Revisor:</strong> Ariadny</li>
        <li><strong>Testador:</strong> José</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td style="padding:6px;"><strong>Protótipo</strong></td>
    <td style="padding:6px;">
    </td>
  </tr>
</table>
