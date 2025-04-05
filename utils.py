import streamlit as st

def local_css(file_name):
    """Apply local CSS styles."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def display_tooltip(text, tooltip_text):
    """Display text with a tooltip for technical terms."""
    return f"""<span class="tooltip">{text}
    <span class="tooltiptext">{tooltip_text}</span>
    </span>"""

def create_term_definition(term, definition):
    """Create an expandable term definition for the glossary."""
    with st.expander(term):
        st.markdown(definition)

def get_sugarcane_growth_stage(days_after_harvest):
    """Return the growth stage based on days after harvest (DAH)."""
    if days_after_harvest < 100:
        return "Early Growth Stage"
    elif days_after_harvest < 180:
        return "Mid Growth Stage"
    elif days_after_harvest < 250:
        return "Late Growth Stage"
    else:
        return "Maturation Stage"
