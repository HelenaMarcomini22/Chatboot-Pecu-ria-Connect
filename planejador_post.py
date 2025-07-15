from google.adk.agent import Agent
from google.adk.tools import google_search
from utils.call_agent import call_agent

def agente_planejador(topico, lancamento):
    agent = Agent(
        name="PlanejadorDeConteudo",
        model="gemini-2.0-flash",
        instruction="""
        Você é um especialista em redes sociais no agro. Use google_search para planejar um post para o LinkedIn com base nos lançamentos recentes. Escolha o tema mais engajador e crie um post que destaque os benefícios do produto, inclua uma chamada para ação e use hashtags relevantes. O post deve ser profissional e informativo, adequado para o público do LinkedIn.
        """,
        tools=[google_search],
    )
    entrada = f"Tópico: {topico}\nLançamentos buscados: {lancamentos}"
    return call_agent(agent, entrada)