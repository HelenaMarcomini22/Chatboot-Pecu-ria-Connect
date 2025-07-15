from google.adk.agents import Agent
from google.adk.tools import google_search
from utils.call_agent import call_agent

def agente_busca_preco(produto="arroba do boi"):
    agent = Agent(name="BuscadorDePrecos",
                  model="gemini-2.0-flash",
                  instruction=f"""
                  Você é um especialista em informações de mercado pecuário. 
                  Busque o preço atualizado de "{produto}" com google_search.
                  Retorne valor, data da cotação e fonte. Mencione variações regionais, se houver.
                    """,
                    tools=[google_search]
                    )
    entrada = f"Qual o preço atual de {produto}?"
    return call_agent(agent, entrada)
    