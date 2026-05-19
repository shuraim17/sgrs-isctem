# Manual do Utilizador — SGRS ISCTEM
### Sistema de Gestão de Requisição de Salas

Bem-vindo ao **SGRS**, o portal unificado para a gestão de espaços académicos no ISCTEM. Este documento serve como guia completo para as funcionalidades disponíveis nos diferentes perfis de acesso.

---

## 1. Acesso e Registo

### 1.1 Criar Conta
Para novos utilizadores (Docentes ou Representantes de Estudantes):
1. Aceda à página de **Registo**.
2. Preencha os dados pessoais:
   - **Nome Completo**.
   - **Telemóvel**: O sistema prefixa automaticamente com `+258`. Introduza os 9 dígitos (ex: 841234567).
3. Credenciais:
   - **Email Institucional**: Deve terminar em `@isctem.ac.mz`.
   - **Email Secundário**: Para fins de recuperação de conta.
   - **Palavra-passe**: Mínimo de 6 caracteres.
4. Escolha a sua função no sistema.

### 1.2 Recuperação de Acesso
Se esqueceu a sua senha:
1. No ecrã de Login, clique em **"Esqueceu a senha?"**.
2. Introduza o seu email institucional.
3. Escolha o método de recepção:
   - **SMS**: Receberá a sua senha diretamente no telemóvel registado.
   - **Email Secundário**: Receberá um link oficial de redefinição no seu email principal e uma notificação no secundário.

---

## 2. Perfil: Docente / Representante

### 2.1 Dashboard (Início)
Visualize o resumo das suas atividades, incluindo o total de requisições, pedidos aprovados e pendentes.

### 2.2 Requisitar Espaço
1. Clique no botão **"Nova Requisição"**.
2. Selecione o **Tipo de Espaço**: Sala de Aula, Anfiteatro, Laboratório Informático ou Sala de Reuniões.
3. Escolha a **Data** desejada.
4. Defina o **Horário**: Os horários disponíveis são restritos ao horário de funcionamento da faculdade (configurado pelo Administrador).
5. Clique em **"Submeter Pedido"**.

### 2.3 Consultar Disponibilidade (Calendário)
Aceda ao menu **"Calendário"** para ver, em tempo real, quais as salas e horários que já se encontram ocupados. Isso ajuda a planear a sua requisição sem conflitos.

### 2.4 Comprovativos
Para pedidos já aprovados pelo Gestor:
1. Aceda ao menu **"Comprovativos"**.
2. Clique em **"Ver e Baixar"** no card da requisição.
3. Uma pré-visualização do PDF aparecerá com o logótipo institucional e um QR Code de validação.
4. Clique em **"Baixar PDF"** para guardar o documento.

---

## 3. Perfil: Gestor Académico

### 3.1 Gestão de Pedidos
No menu principal, o Gestor visualiza todos os pedidos **Pendentes**:
- Clique no ícone verde (**Check**) para aprovar.
- Clique no ícone vermelho (**X**) para recusar.
*O Docente receberá uma notificação automática (Email/SMS) com o novo estado.*

### 3.2 Relatório de Ocupação
Visualização detalhada de todas as reservas confirmadas:
- Inclui o nome da sala, data, horário e o contacto (telemóvel ou email) do responsável.
- Possibilidade de pesquisar/filtrar por qualquer campo na barra de pesquisa.

### 3.3 Emissão de Comprovativos
O Gestor pode, a partir do Relatório, gerar o PDF de reserva para qualquer docente, caso seja solicitado fisicamente.

---

## 4. Perfil: Administrador do Sistema

### 4.1 Gestão de Utilizadores
1. Clique em **"Utilizadores"**.
2. É possível visualizar a lista completa de membros.
3. **Editar**: Clique no ícone de edição para alterar o nome, função ou contactos de um utilizador.
4. **Eliminar**: Remove permanentemente o acesso de uma conta.

### 4.2 Configuração de Horários
1. Clique no menu **"Horário"**.
2. Defina a hora de **Abertura** e **Fecho** da faculdade.
3. Estas definições bloqueiam automaticamente as escolhas de horários feitas pelos docentes no formulário de requisição.

### 4.3 Histórico Global
Acesso a todas as requisições realizadas no sistema para auditoria e controlo estatístico.

---

## 5. Notas Técnicas e Segurança
- O sistema utiliza **Supabase** para garantir a segurança dos dados e tempo real (Realtime).
- A tecnologia **"Liquid Glass"** garante que a interface seja responsiva e fluida em dispositivos móveis e desktops.
- Todos os comprovativos possuem um link encriptado no QR Code que remete para a página de verificação oficial (`comprovativo.html`).

---
**Suporte Técnico**
ISCTEM – Instituto Superior de Ciências e Tecnologia de Moçambique © 2026
