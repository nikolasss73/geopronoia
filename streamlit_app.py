import streamlit as st
from PIL import Image
import base64

# Ρυθμίσεις Παγκόσμιας Αυθεντίας - Version 6.0
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ GOLD", page_icon="🌳", layout="wide")

st.markdown("""
<style>
    .report-title { color: #1b5e20; font-size: 32px; font-weight: bold; text-align: center; border-bottom: 4px solid #1b5e20; padding-bottom: 10px; }
    .section-header { background-color: #1b5e20; color: white; padding: 12px; border-radius: 8px; margin-top: 25px; font-size: 22px; font-weight: bold; }
    .advice-box { background-color: #f1f8e9; border-left: 10px solid #2e7d32; padding: 25px; margin: 15px 0; border-radius: 12px; font-size: 19px; line-height: 1.6; color: #1b5e20; }
    .critical-box { background-color: #ffebee; border-left: 10px solid #d32f2f; padding: 25px; margin: 15px 0; border-radius: 12px; font-size: 19px; line-height: 1.6; color: #b71c1c; }
    .stButton>button { background-color: #1b5e20; color: white; font-weight: bold; height: 4.5em; width: 100%; border-radius: 15px; font-size: 24px; box-shadow: 0 6px 12px rgba(0,0,0,0.2); }
    .unit-card { background-color: #e8f5e9; border: 1px solid #1b5e20; padding: 15px; border-radius: 10px; text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμιο Σύστημα Στ
