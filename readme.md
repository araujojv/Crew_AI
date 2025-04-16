# 🧠 Crew_AI — Sistema Multiagente para Geração de Blog Posts com LLMs

Este projeto é um experimento utilizando o framework [CrewAI](https://github.com/crewAIInc/crewAI) em conjunto com a API da Groq para orquestrar um processo automatizado de **criação completa de posts para blog**, com base em um tema central. A proposta principal é simular uma equipe criativa automatizada, onde cada agente desempenha um papel específico no fluxo de produção de conteúdo.

---

## 🚀 Objetivo do Projeto

O propósito deste projeto foi **testar e explorar o funcionamento do CrewAI** com LLMs poderosos, como o `llama3-70b-8192` da Groq. Através de agentes coordenados, buscamos simular um pipeline completo de criação de conteúdo, desde a geração da ideia até a revisão final do post.

Este projeto teve caráter **experimental**, focado em compreender o potencial dos agentes autônomos para processos criativos.

---

## 🧠 Sobre os Agentes Criados

O projeto define uma equipe (`Crew`) com **4 agentes**, cada um com sua função clara e complementares no processo de criação de conteúdo.

### 1. 🧑‍🎨 Criador de Ideias Criativas para Blog Posts

- **Objetivo:** Gerar 10 ideias criativas e relevantes com foco em engajamento, sempre em português.
- **Backstory:** Um criador antenado e inovador, especializado em transformar conceitos em ideias envolventes.
- **Tarefas:** 
  - Geração de ideias
  - Seleção da melhor ideia com justificativa

### 2. 🧠 Estrategista de Conteúdo

- **Objetivo:** Elaborar um briefing detalhado e estratégico com base no tema e na ideia selecionada.
- **Backstory:** Planejador meticuloso, orientado por dados e com foco em entregar direcionamentos claros para redatores.
- **Tarefa:** 
  - Criação do briefing (objetivo, público, palavras-chave, tom etc.)

### 3. ✍️ Redator Criativo de Blog Posts

- **Objetivo:** Redigir o post completo com base no briefing, de forma clara, envolvente e bem estruturada.
- **Backstory:** Escritor versátil que transforma briefing em storytelling cativante.
- **Tarefa:** 
  - Escrever o conteúdo final do blog post

### 4. 🔍 Revisor de Conteúdo

- **Objetivo:** Garantir qualidade textual, correção gramatical e alinhamento ao briefing.
- **Backstory:** Profissional rigoroso, focado na entrega final e polida.
- **Tarefa:** 
  - Revisão e refinamento final do texto

---

## 📋 Tarefas Definidas

| Etapa | Tarefa | Agente Responsável |
|------|--------|---------------------|
| 1 | Criar 10 ideias criativas sobre o tema proposto | Criador de Ideias |
| 2 | Escolher a melhor ideia e justificar | Criador de Ideias |
| 3 | Planejar o conteúdo com briefing completo | Estrategista de Conteúdo |
| 4 | Escrever o blog post completo | Redator Criativo |
| 5 | Revisar o conteúdo final | Revisor de Conteúdo |

O processo foi definido como **sequencial**, passando de uma etapa à outra conforme a execução do Crew.

---

## 🤖 Sobre a API da Groq

Utilizamos a **LLM `llama3-70b-8192` via API da Groq**, que oferece respostas rápidas e eficazes, com suporte à linguagem natural e contextos extensos. A integração foi feita por meio da biblioteca `langchain_groq` com autenticação via `GROQ_API_KEY`.

```python
llm_groq = LLM(
    model="groq/llama3-70b-8192",
    temperature=0.7
)
```

Essa LLM foi usada por todos os agentes, proporcionando fluidez e coesão em todo o processo de geração de conteúdo.

---

## ⚙️ Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/araujojv/Crew_AI.git
cd Crew_AI
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install crewai crewai-tools langchain_groq
```

4. Configure sua chave da API Groq no ambiente:
```bash
export GROQ_API_KEY='sua-chave-aqui'  # ou use dotenv/.env
```

5. Execute o script principal:
```bash
python crew.py
```

---

## 💡 Exemplo de Tema Usado

```text
Tema: Aplicações com Marcenaria
```
> A equipe multiagente gerará ideias, escolherá a melhor, criará um briefing, escreverá o post e fará a revisão, tudo de forma automática.

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

Feito com ❤️ por [João Vitor](https://github.com/araujojv)