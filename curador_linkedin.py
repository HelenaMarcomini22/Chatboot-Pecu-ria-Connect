from google.adk.agents import Agent
from utils.call_agent import call_agent

def agente_curador_linkedin(plano, resumo=None):
    agent = Agent(
        name="CuradorDeConteudoLinkedIn",
        model="gemini-2.0-flash",
        instruction="""
        Você é um especialista em curadoria de conteúdo para o LinkedIn. Com base no plano fornecido e no resumo opcional, crie um post envolvente que destaque os principais pontos e incentive a interação.
        """,
    )
    entrada = f"Plano do post:\n{plano}\nResumo da Notícia:\n{resumo or 'Não fornecido'}"
    return call_agent(agent, entrada)