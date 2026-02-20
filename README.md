# 🎈 Santander Assistant IA

Um assistente de IA para o Santander com tutorial interativo sobre Spec-Driven Development.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

## Como executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o app principal

```bash
streamlit run streamlit_app.py
```

### 3. Executar o visualizador do tutorial

Para visualizar o tutorial interativo com as tags customizadas:

```bash
streamlit run tutorial_viewer.py
```

O tutorial_viewer.py processa as tags especiais como `<Accordion>`, `<Card>`, `<Steps>`, `<Tabs>`, `<Tip>`, `<Note>` e `<Warning>` e as converte em componentes interativos do Streamlit.

## Estrutura do projeto

- `streamlit_app.py` - App principal
- `tutorial_viewer.py` - Visualizador do tutorial SDD
- `METODOLOGIA SDD/TutorialCompleto.md` - Tutorial sobre Spec-Driven Development
- `requirements.txt` - Dependências Python
