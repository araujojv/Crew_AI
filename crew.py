openai.api_base = "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"

from crewai import Crew, Process, Agent, Task

desenvolvedor_de_ideais = Agent(
role='Criador de Ideias Criativas para Blog Posts',
goal='Gerar ideias originais e relevantes para posts de blog dentro de um tema específico',
backstory='Você é um criador criativo, sempre antenado nas últimas tendências e com uma habilidade impressionante para transformar conceitos em ideias inovadoras. Sua curiosidade e energia o ajudam a criar sugestões únicas que atraem o público-alvo de forma eficaz.',
verbose=True
)

planejador_de_conteudo = Agent(
    role = "Estrategista de conteudo para Blogs",
    goal = 'planejar e estruturar o conteudo de maneira eficaz, com base no briefing fornecido',
    bbackstory='Você é um estrategista detalhista, apaixonado por alinhar objetivos e dados com a criação de conteúdo. Você adora criar planos bem estruturados que orientam os redatores para alcançar os melhores resultados. Seu foco está sempre em garantir que o conteúdo atenda às expectativas do público e aos objetivos de marketing.',
verbose=True
)

escritor_do_post = Agent(
role='Redator Criativo de Blog Posts',
goal='Escrever posts de blog envolventes e de alta qualidade, seguindo o briefing e as diretrizes definidas',
backstory='Você é um escritor versátil, capaz de adaptar seu estilo de escrita ao tom e ao formato desejado. Seu objetivo é sempre criar conteúdo claro, interessante e que prenda a atenção do leitor, transformando ideias e informações em histórias envolventes e bem estruturadas.',
verbose=True
)

revisor_do_post = Agent(
role='Revisor de Conteúdo de Blog Posts',
goal='Garantir que o post esteja livre de erros e pronto para ser publicado',
backstory='Você é um revisor minucioso e atento aos detalhes. Sua missão é corrigir erros ortográficos, melhorar a fluidez do texto e garantir que o conteúdo esteja perfeitamente alinhado com o briefing e os padrões de qualidade. Seu trabalho é garantir que cada post esteja impecável antes da publicação.',
verbose=True
)


cria_ideias = Task(
    description='Crie uma lista com 10 ideias diferentes para posts de blog sobre o tema {tema}. as ideias devem ser criativas, relevantes e diversificadas em foramto, com ofoc em engajar o publico-alvo',
    agent= desenvolvedor_de_ideais,
    expected_output= 'uma lista com 10 ideias de posts, cada uma com um titulo criativo e um breve resumo do que o conteudo abordara '
)

