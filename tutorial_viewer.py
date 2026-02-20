import streamlit as st
import re
from pathlib import Path

def render_tutorial():
    """Renderiza o tutorial com componentes customizados"""

    st.set_page_config(page_title="Tutorial SDD", layout="wide")
    st.title("📚 Tutorial Completo - Desenvolvimento Guiado por Especificações")

    # Ler o arquivo
    tutorial_path = Path("METODOLOGIA SDD/TutorialCompleto.md")
    if not tutorial_path.exists():
        st.error("Arquivo TutorialCompleto.md não encontrado!")
        return

    with open(tutorial_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dividir o conteúdo em seções principais
    sections = re.split(r'^#{1,2}\s+', content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        # Detectar e renderizar componentes customizados
        if '<AccordionGroup>' in section:
            render_accordion_group(section)
        elif '<CardGroup' in section:
            render_card_group(section)
        elif '<Steps>' in section:
            render_steps(section)
        elif '<Tabs>' in section:
            render_tabs(section)
        elif '<Tip>' in section or '<Note>' in section or '<Warning>' in section:
            render_info_components(section)
        else:
            # Renderizar como markdown normal
            st.markdown(section.strip())

        st.divider()

def render_accordion_group(content):
    """Renderiza AccordionGroup"""
    accordions = re.findall(r'<Accordion title="([^"]+)">(.*?)</Accordion>', content, re.DOTALL)

    for title, acc_content in accordions:
        with st.expander(title):
            st.markdown(acc_content.strip())

def render_card_group(content):
    """Renderiza CardGroup"""
    # Extrair número de colunas
    cols_match = re.search(r'<CardGroup cols=(\d+)>', content)
    num_cols = int(cols_match.group(1)) if cols_match else 2

    cards = re.findall(r'<Card title="([^"]*)"[^>]*>(.*?)</Card>', content, re.DOTALL)

    cols = st.columns(num_cols)
    for i, (title, card_content) in enumerate(cards):
        with cols[i % num_cols]:
            st.subheader(title)
            st.markdown(card_content.strip())

def render_steps(content):
    """Renderiza Steps"""
    steps = re.findall(r'<Step title="([^"]+)">(.*?)</Step>', content, re.DOTALL)

    st.header("Passos para implementação")

    for i, (title, step_content) in enumerate(steps, 1):
        st.subheader(f"{i}. {title}")
        st.markdown(step_content.strip())

def render_tabs(content):
    """Renderiza Tabs"""
    tabs_data = re.findall(r'<Tab title="([^"]+)">(.*?)</Tab>', content, re.DOTALL)

    if tabs_data:
        tab_titles = [title for title, _ in tabs_data]
        tabs = st.tabs(tab_titles)

        for i, (_, tab_content) in enumerate(tabs_data):
            with tabs[i]:
                st.markdown(tab_content.strip())

def render_info_components(content):
    """Renderiza Tip, Note, Warning"""
    # Tip
    tips = re.findall(r'<Tip>(.*?)</Tip>', content, re.DOTALL)
    for tip in tips:
        st.info(tip.strip())

    # Note
    notes = re.findall(r'<Note>(.*?)</Note>', content, re.DOTALL)
    for note in notes:
        st.info(f"📝 {note.strip()}")

    # Warning
    warnings = re.findall(r'<Warning>(.*?)</Warning>', content, re.DOTALL)
    for warning in warnings:
        st.warning(f"⚠️ {warning.strip()}")

    # Renderizar o resto como markdown
    clean_content = re.sub(r'</?(Tip|Note|Warning)>', '', content)
    if clean_content.strip():
        st.markdown(clean_content.strip())

if __name__ == "__main__":
    render_tutorial()