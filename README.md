# ONE AI AGENT

> **Agente de IA com RAG para consulta de documentos institucionais**

Projeto desenvolvido para o programa **ONE (Oracle Next Education) AI for Tech**, em parceria com a Alura.

O **ONE AI Agent** simula um assistente de IA para a escola de inglês fictícia **Common Ground**. O agente consulta documentos institucionais, recupera informações relevantes e utiliza esse contexto para gerar respostas fundamentadas.

---

## OBJETIVO

O projeto tem como objetivo construir um agente capaz de:

- consultar documentos previamente fornecidos;
- encontrar informações relevantes para uma pergunta;
- utilizar essas informações como contexto;
- gerar respostas utilizando o Gemini;
- indicar as fontes utilizadas.

A arquitetura utiliza **RAG (Retrieval-Augmented Generation)** para conectar recuperação de informações e geração de respostas.

---

## ARQUITETURA

O fluxo principal do sistema é:

```text
Documentos
    ↓
Document Loader
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retrieval
    ↓
Contexto relevante
    ↓
Gemini
    ↓
Resposta + fontes
```

A interface do agente é construída com *Streamlit*.

---

## TECNOLOGIAS

| Tecnologia | Utilização |
|---|---|
| **Python** | Desenvolvimento do agente |
| **Google Gemini API** | Geração de respostas |
| **Gemini Embeddings** | Representação dos documentos |
| **ChromaDB** | Armazenamento e busca vetorial |
| **Streamlit** | Interface web |
| **Git + GitHub** | Controle de versão |

---

## ESTRUTURA DO PROJETO

```text
ONE_AI_Agent/
│
├── app.py
├── build_vector_store.py
├── chunker.py
├── document_loader.py
├── embedding.py
├── rag.py
├── vector_store.py
├── requirements.txt
│
├── documents/
│   ├── academic_benefits.csv
│   ├── academic_policy.md
│   ├── assessment_and_feedback.md
│   ├── attendance and make-up policy.md
│   ├── student progression and placement.md
│   └── teacher_handbook.md
│
└── chroma_db/
```

*A pasta `chroma_db/` é criada localmente e não é versionada no Git.*

---

## BASE DOCUMENTAL

A coleção contém documentos fictícios relacionados à Common Ground, incluindo:

- políticas acadêmicas;
- avaliação e feedback;
- frequência e reposição;
- progressão e placement;
- manual de professores;
- benefícios para professores.

---

## CONFIGURAÇÃO

### INSTALAR DEPENDÊNCIAS

*Execute o comando abaixo no terminal:*

```powershell
pip install -r requirements.txt
```

### CONFIGURAR A API KEY

*Crie um arquivo `.env` na raiz do projeto.*

```text
GEMINI_API_KEY=sua_chave_aqui
```

*O arquivo `.env` está incluído no `.gitignore` e não deve ser enviado ao GitHub.*

### CONSTRUIR A BASE VETORIAL

*Execute:*

```powershell
python build_vector_store.py
```

*Esse processo:*

1. carrega os documentos;
2. cria os chunks;
3. gera os embeddings;
4. armazena os vetores no ChromaDB.

### EXECUTAR A APLICAÇÃO

*Execute:*

```powershell
python -m streamlit run app.py
```

*A aplicação será disponibilizada localmente pelo Streamlit.*

---

## RAG

O sistema divide o processo em duas etapas principais.

### RETRIEVAL

O agente transforma a pergunta em um embedding e busca no ChromaDB os trechos mais relevantes dos documentos.

### GENERATION

Os trechos recuperados são enviados ao Gemini como contexto.

*O modelo recebe instruções para:*

- utilizar somente o contexto fornecido;
- não inventar informações;
- informar quando os documentos não contêm a resposta;
- apresentar a resposta de forma clara e concisa.

---

## STATUS DO PROJETO

### CONCLUÍDO

- [x] Carregamento dos documentos
- [x] Chunking dos documentos
- [x] Geração de embeddings
- [x] Armazenamento no ChromaDB
- [x] Busca semântica
- [x] Estrutura do RAG
- [x] Interface Streamlit
- [x] Configuração de dependências
- [x] Proteção da API Key
- [x] Tratamento do limite diário da API

### EM VALIDAÇÃO

- [ ] Reconstrução da base com novo chunking
- [ ] Validação final do retrieval
- [ ] Validação completa do RAG
- [ ] Integração final da interface
- [ ] Deploy na OCI

---

## CONTEXTO

Este projeto foi desenvolvido como parte dos estudos do programa **ONE AI for Tech**, com foco na aplicação prática de conceitos de:

**IA generativa · Embeddings · Bancos vetoriais · RAG · Python · Git · Cloud**