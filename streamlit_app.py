import streamlit as st
from PIL import Image

# Έκδοση 5.2 - Σταθερή έκδοση χωρίς σφάλματα
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ ULTIMATE", page_icon="🌳", layout="wide")

# Απλό και σταθερό στυλ
st.markdown("""
<style>
    .report-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 8px solid #1b5e20; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        margin-bottom: 15px; 
    }
    .stButton>button { 
        background-color: #1b5e20; 
        color: white; 
        font-weight: bold; 
        height: 3em; 
    }
</style>
""", unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμιο Σύστημα Στρατηγικής")
st.caption("Επιστημονική Ανάλυση βάσει Marschner, Albrecht και κλίμακας BBCH")
st.write("---")

# 1. ΡΥΘΜΙΣΕΙΣ ΣΤΗΝ ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("🧠 Ρυθμίσεις")
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age_cat = st.sidebar.selectbox("Ηλικία:", ["1-7 ετών (Νεαρή)", "8-40 ετών (Πλήρης)", "40+ ετών (Υπερήλικα)"])
stage = st.sidebar.selectbox("Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Εμφάνιση ανθοταξίας (Μούρο)", "Άνθηση", "Καρπόδεση", "Ανάπτυξη καρπού", "Ωρίμανση"])
method = st.sidebar.radio("Άρδευση:", ["Ξερικό", "Ποτιστικό"])
yield_stat = st.sidebar.radio("Πέρυσι παραγωγή:", ["Υπερβολική (ON)", "Κανονική", "Μειωμένη (OFF)"])

# 2. ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 Αρχεία Ανάλυσης")
uploaded_files = st.file_uploader("Ανεβάστε Φωτογραφίες ή PDF", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"✅ Φορτώθηκαν {len(uploaded_files)} αρχεία.")
    with st.expander("Προβολή αρχείων"):
        for f in uploaded_files:
