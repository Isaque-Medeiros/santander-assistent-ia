# Guia para Hospedar o TutorialCompleto.md Funcionalmente

## Visão Geral

Este guia explica como hospedar e visualizar o arquivo `TutorialCompleto.md` de forma interativa, utilizando um aplicativo Streamlit que processa marcações customizadas (tags) para renderizar componentes como accordions, cards, steps, tabs, tips, notes e warnings.

## Arquivos Principais

- `tutorial_viewer.py`: Aplicativo Streamlit principal que lê e renderiza o tutorial.
- `METODOLOGIA SDD/TutorialCompleto.md`: Arquivo Markdown com conteúdo do tutorial e tags customizadas.
- `requirements.txt`: Lista de dependências Python.

## Componentes Customizados Suportados

O `tutorial_viewer.py` reconhece e renderiza as seguintes tags:

- `<AccordionGroup>`: Grupos de accordions expansíveis.
- `<CardGroup cols=X>`: Grupos de cards em colunas.
- `<Steps>`: Lista numerada de passos.
- `<Tabs>`: Abas para organizar conteúdo.
- `<Tip>`, `<Note>`, `<Warning>`: Componentes de informação com ícones.

## Passos para Hospedar

### 1. Configurar o Ambiente Python

Certifique-se de ter um ambiente virtual Python configurado. Se não tiver, execute:

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 2. Instalar Dependências

Instale as dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

Isso instalará o Streamlit e outras bibliotecas necessárias.

### 3. Executar o Aplicativo

Para iniciar o servidor Streamlit, execute:

```bash
streamlit run tutorial_viewer.py
```

Por padrão, o aplicativo será acessível em `http://localhost:8501`.

### 4. Acessar o Tutorial

Abra seu navegador e navegue para o endereço fornecido pelo Streamlit (geralmente `http://localhost:8501`). Você verá o tutorial renderizado com todos os componentes interativos.

## Funcionalidades do tutorial_viewer.py

- **Leitura do Arquivo**: Lê o `TutorialCompleto.md` da pasta `METODOLOGIA SDD/`.
- **Processamento de Tags**: Usa expressões regulares para identificar e extrair conteúdo das tags customizadas.
- **Renderização Streamlit**: Converte as tags em componentes Streamlit apropriados (expanders, columns, tabs, etc.).
- **Layout Responsivo**: Utiliza `layout="wide"` para melhor visualização.

## Estrutura do Código

O `tutorial_viewer.py` contém funções específicas para cada tipo de componente:

- `render_accordion_group()`: Processa `<Accordion>` tags.
- `render_card_group()`: Processa `<CardGroup>` e `<Card>` tags.
- `render_steps()`: Processa `<Steps>` e `<Step>` tags.
- `render_tabs()`: Processa `<Tabs>` e `<Tab>` tags.
- `render_info_components()`: Processa `<Tip>`, `<Note>`, `<Warning>` tags.

## Solução de Problemas

- **Arquivo não encontrado**: Certifique-se de que `METODOLOGIA SDD/TutorialCompleto.md` existe no caminho correto.
- **Porta ocupada**: Se a porta 8501 estiver em uso, o Streamlit sugerirá uma porta alternativa.
- **Dependências faltando**: Execute `pip install -r requirements.txt` novamente.
- **Ambiente virtual**: Ative o ambiente virtual antes de executar comandos Python.

## Hospedagem em Produção

Para hospedar em produção, considere usar serviços como:
- Streamlit Cloud
- Heroku
- AWS EC2
- Google Cloud Run

Certifique-se de incluir todos os arquivos necessários (tutorial_viewer.py, TutorialCompleto.md, requirements.txt) no repositório.

## Conclusão

Seguindo estes passos, você poderá visualizar o `TutorialCompleto.md` como um site interativo, com todas as marcações das tags funcionando corretamente. O aplicativo Streamlit transforma o Markdown estático em uma experiência dinâmica e organizada.