from crewai import Task
from src.nlp_01_2025.config.agents import planner, writer, editor


plan = Task(
    description=(
        "Realize uma pesquisa aprofundada sobre o tema: {topic}, consultando fontes confiáveis como blogs técnicos, documentações oficiais, exemplos de código e casos de uso reais. "
        "Identifique informações relevantes e atualizadas (considerando o ano atual: {current_year}), incluindo boas práticas, dicas úteis, atalhos (hacks), erros comuns e aplicações práticas. "
        "Utilize essas informações para elaborar um plano de conteúdo completo que será usado pelo Redator de Conteúdo na produção do artigo. "
        "Certifique-se de que o plano seja útil, coeso e orientado para o público-alvo."
    ),
    expected_output=(
        "Um documento de planejamento de conteúdo em formato Markdown contendo:"
        "\n1. Estrutura detalhada com tópicos e subtópicos sugeridos;"
        "\n2. Análise do público-alvo (nível técnico, necessidades, dores e objetivos);"
        "\n3. Lista de palavras-chave de SEO a serem utilizadas no texto;"
        "\n4. Sugestão de exemplo prático de código para ilustrar o tema;"
        "\n5. Fontes confiáveis (links, blogs, artigos, documentações) que embasam o conteúdo;"
        "\n6. Observações adicionais para orientar o Redator de Conteúdo."
    ),
    agent=planner,
    output_file='output/content_plan.md',
    verbose=True
)


write = Task(
    description=(
        "Utilize o plano de conteúdo e o contexto fornecido para desenvolver um artigo completo em formato Markdown, pronto para publicação em um blog estático feito com Jekyll. "
        "Expanda cada tópico em uma seção coesa e informativa, seguindo a estrutura sugerida no planejamento: Introdução, Enunciado do Problema, Código (com explicações e dados fictícios), Conclusão ('Antes de Você Ir') e Referências. "
        "Incorpore palavras-chave de SEO de forma natural no texto."
    ),
    expected_output=(
        "Um artigo completo e detalhado em formato Markdown, contendo:"
        "\n- Seções bem definidas com no mínimo 3 parágrafos cada;"
        "\n- Códigos explicados em blocos pequenos, com exemplos práticos e conjuntos de dados fictícios;"
        "\n- Imagens relevantes extraídas da base de conhecimento, se disponíveis;"
        "\n- Links externos úteis e confiáveis, que complementem o conteúdo;"
        "\n- Conclusão clara, envolvente e baseada nos aprendizados do artigo;"
        "\n- Formatação compatível com Jekyll (sem blocos de código com crases triplas e com front matter opcional)."
    ),
    agent=writer,
    markdown=True,
    output_file='output/draft_blog_post.md',
    verbose=True,
)

edit = Task(
    description=(
        "Revise o artigo escrito, garantindo correção gramatical, clareza, fluidez e alinhamento com o estilo definido pelo autor. "
        "Certifique-se de que o texto esteja coeso, com vocabulário adequado ao público-alvo e em conformidade com os padrões editoriais. "
        "Avalie se há equilíbrio entre opiniões e fatos, e, quando necessário, sugira ajustes para melhorar a imparcialidade ou a consistência argumentativa. "
    ),
    expected_output=(
        "Um artigo revisado, bem escrito e formatado em Markdown, pronto para publicação em um blog Jekyll. "
        "O texto deve ter tempo estimado de leitura entre 6 e 10 minutos. "
        "O conteúdo deve ser fluido, livre de erros gramaticais, com estilo consistente e linguagem acessível. "
    
    ),
    agent=editor,
    markdown=True,
    output_file='review_final_blog_post.md',
    verbose=True
)
