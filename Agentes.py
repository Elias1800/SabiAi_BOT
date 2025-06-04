# Agente 1: Identificador
def agente_identificador(entrada_do_usuario):
    identificador = Agent(
        name="agente_identificador",
        model="gemini-2.0-flash",
        instruction="""
        Você é um assistente pessoal profissional.
        Sua tarefa é identificar as necessidades do usuário: pesquisas, dúvidas,
        ajuda, sugestões, escutar música, organização de tempo, entre outras funções de um assistente.
        Diga apenas qual é a necessidade principal, como uma única palavra ou pequena frase.
        """,
        description="Identificador"
    )
    topico_identificado = call_agent(identificador, entrada_do_usuario)
    return topico_identificado

# Agente 2: Buscador
def agente_buscador(topico, data_de_hoje):

    buscador = Agent(
        name="agente_buscador",
        model="gemini-2.0-flash",
        instruction="""
        Você é um assistente pessoal profissional. A sua tarefa é usar a ferramenta de busca do google (google_search)
        para responder perguntas do usuário, recuperar as últimas notícias, ver previsões do tempo, gerenciar tempo, ensinar coisas,
        tirar dúvidas entre outras coisas.
        Foque em no máximo 5 pesquisas mais relevantes, com base na entrada do usuário.
        Se um tema tiver poucas notícias ou reações entusiasmadas, é possível que ele não seja tão relevante assim
        e pode ser substituído por outro que tenha mais.
        Esses lançamentos relevantes devem ser atuais, de no máximo um mês antes da data de hoje.
        """,
        description="Agente que busca informações no Google",
        tools=[google_search]
    )

    entrada_do_agente_buscador = f"Tópico: {topico}\nData de hoje: {data_de_hoje}"
    resultado_da_busca = call_agent(buscador, entrada_do_agente_buscador)

    return resultado_da_busca 

# Agente 3: Adaptador
def agente_adaptador(topico, plano_de_post):
    adaptador = Agent(
        name="agente_redator",
        model="gemini-2.0-flash",
        instruction="""
        Adapte sua resposta conforme a tonalidade e o estilo do usuário.
        Aja de uma maneira tranquila, sutil e bem explicativa.
        Nas respostas, entregue um conteúdo simples que qualquer pessoa possa entender.
        Evite termos técnicos, a menos que o usuário solicite ou sejam essenciais para o tópico.
        """,
        description="Agente adaptador de resposta"
    )
    entrada_do_agente_adaptador = f"Tópico: {topico}\nPlano de post: {plano_de_post}"
    # Executa o agente
    rascunho = call_agent(adaptador, entrada_do_agente_adaptador)
    return rascunho

#  Agente 4: Revisor
def agente_revisor(topico, rascunho_gerado):
    revisor = Agent(
        name="agente_revisor",
        model="gemini-2.5-pro-preview-03-25",
        instruction="""
            Você é um Editor e Revisor de Conteúdo meticuloso, especializado em respostas para usuários do telegram.
            Por ter um público jovem, entre 18 e 40 anos, use um tom de escrita adequado.
            Revise o rascunho do resultado do tópico indicado, verificando clareza, concisão, correção e tom.
            """,
        description="Agente revisor"
    )
    entrada_do_agente_revisor = f"Tópico: {topico}\nRascunho: {rascunho_gerado}"
    # Executa o agente
    texto_revisado = call_agent(revisor, entrada_do_agente_revisor)
    return texto_revisado

data_de_hoje = date.today().strftime("%d/%m/%Y")

#  Atribuição das Variaveis
topico = agente_identificador(entrada_do_usuario)
pesquisa = agente_buscador(topico, data_de_hoje)
adaptador = agente_adaptador(topico, pesquisa)
saida = agente_revisor(topico, adaptador)