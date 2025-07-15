from google.adk.agents import Agent
from utils.call_agent import call_agent

def agente_resumo_noticias(noticias):
    agent = Agent(
        name="ResumidorDeNoticias",
        model="gemini-2.0-flash",
        instruction="""
        Você é um especialista em resumir notícias. Analise as seguintes notícias e forneça um resumo conciso de cada uma, destacando os pontos mais importantes.
        """,
    )
    entrada = "Resuma as seguintes notícias:\n"+"\n".join(noticias)
    return call_agent(agent, entrada)