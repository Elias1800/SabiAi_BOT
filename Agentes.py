import google.generativeai as genai
import asyncio
from datetime import date

API_KEY = "AIzaSyAc06fu1ntOt63CeA67hOrXpl5LDdIyWp8"  # coloque sua chave da Google Gemini aqui
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")
data_de_hoje = date.today().strftime("%d/%m/%Y")

async def call_agent(prompt: str) -> str:
    def run_sync():
        response = model.generate_content(prompt)
        return response.text.strip()
    return await asyncio.to_thread(run_sync)

async def agente_identificador(entrada_do_usuario):
    prompt = f"""
Você é um assistente pessoal profissional.
Sua tarefa é identificar as necessidades do usuário: pesquisas, dúvidas,
ajuda, sugestões, escutar música, organização de tempo, entre outras funções de um assistente.
Diga apenas qual é a necessidade principal, como uma única palavra ou pequena frase.

Texto do usuário: "{entrada_do_usuario}"
"""
    return await call_agent(prompt)

async def agente_buscador(topico, data_de_hoje):
    prompt = f"""
Você é um assistente pessoal profissional. A sua tarefa é usar a ferramenta de busca do google (google_search)
para responder perguntas do usuário, recuperar as últimas notícias, ver previsões do tempo, gerenciar tempo, ensinar coisas,
tirar dúvidas entre outras coisas.
Foque em no máximo 5 pesquisas mais relevantes, com base na entrada do usuário.
Se um tema tiver poucas notícias ou reações entusiasmadas, é possível que ele não seja tão relevante assim
e pode ser substituído por outro que tenha mais.
Esses lançamentos relevantes devem ser atuais, de no máximo um mês antes da data de hoje.

Tópico: {topico}
Data de hoje: {data_de_hoje}
"""
    return await call_agent(prompt)

async def agente_adaptador(topico, plano_de_post):
    prompt = f"""
Adapte sua resposta conforme a tonalidade e o estilo do usuário.
Aja de uma maneira tranquila, sutil e bem explicativa.
Nas respostas, entregue um conteúdo simples que qualquer pessoa possa entender.
Evite termos técnicos, a menos que o usuário solicite ou sejam essenciais para o tópico.

Tópico: {topico}
Plano de post: {plano_de_post}
"""
    return await call_agent(prompt)

async def agente_revisor(topico, rascunho_gerado):
    prompt = f"""
Você é um Editor e Revisor de Conteúdo meticuloso, especializado em respostas para usuários do telegram.
Por ter um público jovem, entre 18 e 40 anos, use um tom de escrita adequado.
Revise o rascunho do resultado do tópico indicado, verificando clareza, concisão, correção e tom.

Tópico: {topico}
Rascunho: {rascunho_gerado}
"""
    return await call_agent(prompt)