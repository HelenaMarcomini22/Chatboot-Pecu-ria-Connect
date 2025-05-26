🤖 Agente Pecuário: Insights do Agronegócio com Gemini 2.0 Flash 📈

🌟 Visão Geral do Projeto
Este projeto demonstra uma poderosa aplicação da inteligência artificial para o setor pecuário, utilizando o modelo Gemini 2.0 Flash e a Google Agent Development Kit (ADK). Desenvolvemos uma suíte de agentes especializados que, trabalhando em conjunto, fornecem insights valiosos e automatizam tarefas rotineiras, desde a busca de preços de mercado até a geração de conteúdo estratégico para redes sociais.

Com o "Agente Pecuário", é possível obter:

Preços atualizados da arroba do boi.
Resumos concisos de notícias do setor.
Planos estratégicos para posts em redes sociais.
Posts otimizados para o LinkedIn, prontos para engajar o público.

🚀 Como Funciona

O coração deste projeto é a orquestração de agentes de IA especializados, cada um com uma função específica, que se comunicam e colaboram para entregar resultados completos. Veja o fluxo principal:

BuscadorDePrecos: Este agente utiliza a ferramenta Google Search para obter o preço mais recente da arroba do boi e outras commodities, fornecendo data e fonte da cotação.
ResumidorDeNoticias: Recebe uma lista de notícias do setor e gera resumos objetivos, destacando os pontos mais relevantes para o público pecuarista.
PlanejadorDeConteudo: Com base em tópicos e notícias resumidas, este agente usa o Google Search para criar um plano estratégico de conteúdo para o LinkedIn, identificando os pontos mais engajadores e o tema de maior potencial.
CuradorDeConteudoLinkedIn: Utilizando o plano gerado e, opcionalmente, um resumo de notícia, este agente redige um post profissional e engajador para o LinkedIn, incluindo hashtags relevantes.

🛠️ Tecnologias Utilizadas

Google Gemini 2.0 Flash: Modelo de linguagem grande e performático, ideal para tarefas de geração de texto e análise.
Google Agent Development Kit (ADK): Framework para construir e orquestrar agentes de IA.
Google Search Tool: Ferramenta integrada aos agentes para realizar buscas em tempo real e obter informações atualizadas.
IPython Display: Utilizado para renderizar a saída dos agentes de forma clara e formatada (Markdown, HTML).
Google Colab: Ambiente de desenvolvimento para execução e demonstração do código.

🎯 Por que isso é Importante?

No dinâmico mercado do agronegócio, ter acesso rápido a informações precisas e ser capaz de comunicar estrategicamente é crucial. Este projeto automatiza a coleta de dados de mercado, a análise de notícias e a criação de conteúdo, liberando tempo valioso para produtores, analistas e profissionais do setor se concentrarem em decisões estratégicas. É a inteligência artificial trabalhando a favor da eficiência e da competitividade no agronegócio brasileiro.

💡 Como Executar o Projeto

1. Configuração da API Key:

Certifique-se de ter uma GOOGLE_API_KEY configurada nas suas variáveis de ambiente ou no Google Colab (via userdata.get('GOOGLE_API_KEY')).

2. Instalação de Dependências:

%pip -q install google-genai
!pip install -q google-adk

3. Execução do Código:

O código fornecido no notebook (.ipynb) pode ser executado célula por célula. Cada agente é invocado através de funções dedicadas (agente_planejador, agente_busca_preco, etc.), demonstrando a interação e a saída de cada um.

📚 Exemplo de Uso (Trechos do Código)

# Exemplo de uso do Agente de Busca de Preços
preco_arroba = agente_busca_preco()
print("Preço da Arroba do Boi:", preco_arroba)

# Exemplo de Resumo de Notícias
noticias_pecuaria = ["Notícia A sobre alta nos custos de produção.", "Notícia B sobre novas tecnologias de pastagem."]
resumos_noticias = agente_resumo_noticias(noticias_pecuaria)
print("Resumos das Notícias:", resumos_noticias)

# Exemplo de Geração de Post para LinkedIn
plano_post = agente_planejador(topico="Impacto dos custos de produção na pecuária", lancamentos_buscados=resumos_noticias)
post_linkedin = agente_curador_linkedin(plano_do_post=plano_post, resumo_noticia=resumos_noticias[0])
print("Post para LinkedIn:", post_linkedin)

🤝 Contribuições

Sinta-se à vontade para explorar, testar e sugerir melhorias! Este projeto é um ponto de partida para muitas outras aplicações da IA no agronegócio.

Licença

Este projeto está sob a licença MIT License.
