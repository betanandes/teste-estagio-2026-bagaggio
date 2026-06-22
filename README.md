# Desafio Técnico Bagaggio — API de Gerenciamento de Usuários

Solução desenvolvida por **Roberta Fernandes** para o Desafio Técnico de Estágio 2026 da Bagaggio. O projeto original foi entregue com uma base de código funcional; minha missão foi investigar, identificar problemas e realizar as melhorias necessárias.

---

## 🛠️ Tecnologias

- Python 3.11+
- FastAPI
- SQLAlchemy 2.0
- SQLite
- Passlib + bcrypt
- Uvicorn

---

## ▶️ Como Executar

### 1. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente virtual

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicializar o banco de dados

```bash
python database/seed.py
```

> Isso cria o banco SQLite com 40 usuários de exemplo. Rode novamente a qualquer momento para resetar os dados.

### 5. Executar a API

```bash
uvicorn main:app --reload
```

### 6. Acessar a documentação interativa

```
http://localhost:8000/api/users/docs
```

---

## 📌 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/users/` | Criar novo usuário |
| `GET` | `/users/` | Listar todos os usuários |
| `GET` | `/users/{user_id}` | Buscar usuário por ID |
| `PATCH` | `/users/{user_id}` | Atualizar dados do usuário |
| `DELETE` | `/users/{user_id}` | Deletar usuário |

---

## 📁 Estrutura do Projeto

```
├── database/
│   ├── __init__.py       # Configuração do banco e sessão
│   └── seed.py           # Dados iniciais para desenvolvimento
├── entities/
│   └── user.py           # Modelo SQLAlchemy do usuário
├── repository/
│   └── users.py          # Camada de acesso ao banco de dados
├── routes/
│   └── users/
│       └── router.py     # Endpoints da API
├── main.py               # Ponto de entrada da aplicação
└── requirements.txt
```

---

## 🔧 Melhorias Realizadas

Assumi a base de código existente e realizei as seguintes correções e melhorias:

### Bugs críticos corrigidos

- **DELETE deletava o usuário errado** — a query buscava `user_id + 1` em vez de `user_id`, deletando sempre o registro seguinte ao solicitado
- **Verificação de duplicidade com campos trocados** — a checagem de email duplicado comparava `User.name` com `payload.email`, tornando-a ineficaz
- **Senha armazenada em texto puro** — adicionado hashing com bcrypt via passlib; senhas nunca são salvas em plaintext
- **Senha exposta nas respostas** — removido o campo `password` de todas as respostas da API

### Bugs de comportamento corrigidos

- **Impossível desativar usuário via PATCH** — `if payload.is_active` tratava `False` como falsy; corrigido para `if payload.is_active is not None`
- **GET retornava HTTP 200 para usuário não encontrado** — corrigido para retornar HTTP 404 com `HTTPException`
- **Email sem constraint de unicidade no banco** — adicionado `unique=True` ao campo `email` no modelo

### Melhorias de organização

- **Repository ignorado pelo router** — o arquivo `repository/users.py` existia mas era completamente ignorado; refatorado o router para usar suas funções, aplicando separação de responsabilidades
- **Funções mortas removidas do main.py** — removidas três funções sem uso e um endpoint de debug exposto em produção (`/debug/users-count`)

---

## 🔮 Melhorias Futuras Identificadas

Itens identificados durante a análise que não foram implementados por estarem fora do escopo de manutenção:

- **Testes automatizados** — não há testes no projeto; adicionar testes unitários para o repository e testes de integração para os endpoints com pytest seria o próximo passo natural
- **Variáveis de ambiente** — a URL do banco está hard-coded; uso de `python-dotenv` com um arquivo `.env` permitiria configuração por ambiente sem alterar código
- **Paginação com metadados** — o `GET /users/` aceita `skip` e `limit` mas não retorna total de registros ou número de páginas, o que seria útil para o cliente implementar navegação

---

## 👩‍💻 Autora

**Roberta Fernandes** — Desafio Técnico de Estágio 2026
