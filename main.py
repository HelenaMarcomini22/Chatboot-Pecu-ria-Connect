from agents.buscador_preco import agente_busca_preco
from agents.planejador_post import agente_planejador
from agents.resumidor_noticias import agente_resumo_noticias
from agents.curador_linkedin import agente_curador_linkedin

def main():
    noticias_pecuaria = [
        "Notícia A sobre alta nos custos de produção",
        "Notícia B sobre novas tecnologias no setor pecuário",
        "Notícia C sobre mudanças climáticas e impacto na pecuária",
    ]
    
    resumos = agente_resumo_noticias(noticias_pecuaria)
    print("\n📰 Resumos das notícias:\n", resumos)

    plano_post = agente_planejador("Impacto dos custos na pecuária", resumos)
    print("\n📅 Post Planejado:\n", plano_post)

    post_linkedin = agente_curador_linkedin(plano_post, resumo=noticias_pecuaria[0])
    print("\n🔍 Post para LinkedIn:\n", post_linkedin)

    preco = agente_busca_preco()
    print("\n💰 Preço arroba do Boi:\n", preco)
    
if __name__ == "__main__":
    main()
