# Trabalho prático - Agente autonômos com LLMs 🚀

Bem-vindo ao projeto `NlP-01-2025`, desenvolvido no contexto do trabalho prático da disciplina de NLP de 2025, ministrada no [Programa de Pós-Graduação em Informática (PPGI)](https://ppgi.ufam.edu.br/). Este projeto explora a construção de sistemas baseados em agentes autônomos orquestrados por LLMs, com suporte a ferramentas externas como RAG (Recuperação de Informação) e e chamadas de APIs externas.

A solução utiliza o framework [crewAI](https://www.crewai.com/), que facilita a criação e coordenação de múltiplos agentes colaborativos para resolver tarefas complexas de forma distribuída.

## 🎯 Detalhes

Este respositório contém um sistema de agentes autônomos que colaboram entre si para gerar uma postagem para o um blog fictício, a partir de um tema e uma base de conhecimento fornecida. O sistema usa:

- Usar RAG para consultar/colectar informações em bases de dados, recurso [Knowledge](https://docs.crewai.com/en/concepts/knowledge).
- Utilizar a ferramenta `SerperDevTool` para consultar informações adicionais na busca do Google.
- O conteúdo final é o arquivo `output/review_final_blog_post.md`, um post no formato da ferramenta [Jekyll](https://jekyllrb.com/) pronto para publicação.

## 🛠️ Instalação

O projeto requer `Python >=3.10 e <3.14`. Utilizamos o gerenciador de pacotes uv para facilitar a instalação.

1. Instale o uv:

```bash
pip install uv
```

2. Instale as dependências do projeto:

```bash
uv pip install -r requirements.txt
````

Ou, se estiver usando o CLI do crewAI:

```bash
crewai install
```

## ⚙️ Configuração

Crie um arquivo `.env`, baseado no arquivo `.env.template`, na raiz do projeto e adicione sua chave da OpenAI:

```ini
MODEL=gpt-4.1
OPENAI_API_KEY=
SERPAPI_API_KEY=
```

Para mais informações sobre o funcionamento do projeto, consulte:

- **Agentes**: src/nlp_ufam/config/agents.py
- **Tarefas**: src/nlp_ufam/config/tasks.py
- **Pipeline e lógica**: src/nlp_ufam/crew.py
- **Entrada e execução personalizada**: src/nlp_ufam/main.py

## ▶️ Execução
Para iniciar a orquestração dos agentes, execute no terminal:

```bash
uv run main.py
```

Esse comando inicializa os agentes definidos e os coloca para executar suas tarefas colaborativamente, com base nas configurações do projeto. Os resultados serão gerados na pasta output/.

## 📁 Estrutura do Projeto

```bash
./
├── knowledge/
├── output/                 # Resultados gerados (ex: postagem final)
├── src/nlp_ufam/
|   ├── config/
│   |    ├── agents.py         # Definição dos agentes
│   |    └── tasks.py          # Tarefas atribuídas aos agentes
|   ├── crew.py                # Composição e lógica dos agentes
|   ├── knowledge.py           # Basese de conhecimentos disponíveis WEB e PDF
|   ├── tools.pys              # Ferramentas personalizadas (acesso ao web com SerperDevTool)
└── main.py                 # Script principal de execução