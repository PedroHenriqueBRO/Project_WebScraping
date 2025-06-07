# Projeto de Extração e Armazenamento de Dados de Países

Este projeto em Python realiza a extração de dados de países usando a API REST Countries, focando inicialmente nos países da Europa e América do Sul. Os dados extraídos são armazenados em um banco de dados PostgreSQL para consultas futuras.

---

## Funcionalidades atuais

- Uso da biblioteca `requests` para fazer requisições HTTP à API REST Countries.
- Conexão com banco de dados PostgreSQL via `psycopg2`.
- Criação e manipulação de tabelas SQL para armazenar dados dos países.
- Funções para inserir dados no banco (POST) e recuperar dados armazenados (GET).
- Web scraping básico para complementar a coleta de dados.    
- Implementação modular com classes para repositórios e serviços, facilitando expansão.

---

## Tecnologias usadas

- Python 3.x
- Biblioteca `requests`
- Biblioteca `psycopg2` para conexão PostgreSQL
- Banco de dados PostgreSQL
- SQL (DDL e DML) para manipulação de dados

---

## Estrutura do projeto

- **Repositórios**: responsáveis por operações diretas com o banco de dados.
- **Serviços**: fazem chamadas para a API REST Countries, processam os dados e usam os repositórios para armazenar.
- **Main script**: executa a sequência de criação das tabelas, coleta e armazenamento dos dados.

---

## Como usar

1. Configure e rode um servidor PostgreSQL localmente.
2. Ajuste os parâmetros de conexão (host, usuário, senha, banco) no módulo de conexão.
3. Execute o script principal para criar tabelas e importar os dados dos países.
4. Consulte os dados armazenados diretamente no banco ou usando as funções GET do projeto.

---

## Próximos passos

- Adicionar suporte para mais regiões/países.
- Implementar lógicas de negócio mais complexas para tratamento e análise dos dados.
- Evoluir para uma API REST que permita requisições externas.
- Inserir breakpoints e ferramentas de debugging para facilitar desenvolvimento e testes.

---

## Observações

Este projeto ainda não roda como uma API online, mas como um script que executa localmente, coletando e armazenando informações para uso futuro.

---

