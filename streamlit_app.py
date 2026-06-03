import streamlit as st
from PIL import Image

# Έκδοση 5.3 - Η απόλυτη και σταθερή έκδοση
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ ULTIMATE", page_icon="🌳", layout="wide")

# Στυλ σελίδας
st.markdown("""
<style>
    .main { background-color: #f4f7f6; }
    .report-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 10px solid #1b5e20; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
        margin-bottom: 15px; 
    }
    .stButton>button { 
        background-color: #1b5e20; 
        color: white; 
        font-weight: bold; 
        height: 3.5em; 
        width: 100%;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμιο Σύστημα Στρατηγικής")
st.caption("Σύνθεση Χημείας Εδάφους, Φυσιολογίας, Υδρολογίας και Μετεωρολογίας")
st.write("---")

# 1. ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("🧠 Παράμετροι")
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age_cat = st.sidebar.selectbox("Ηλικία Καλλιέργειας:", ["1-7 ετών (Νεαρή Φυτεία)", "8-40 ετών (Πλήρης Παραγωγή)", "40+ ετών (Υπερήλικα Δέντρα)"])
stage = st.sidebar.selectbox("Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Εμφάνιση ανθοταξίας (Μούρο)", "Άνθηση", "Καρπόδεση", "Ανάπτυξη καρπού", "Ωρίμανση"])
method = st.sidebar.radio("Σύστημα Άρδευσης:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
yield_stat = st.sidebar.radio("Πέρυσι η παραγωγή ήταν:", ["Υπερβολική (ON)", "Κανονική", "Μειωμένη (OFF)"])

# 2. ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 Αρχεία Ανάλυσης")
uploaded_files = st.file_uploader("Ανεβάστε Φωτογραφίες ή PDF", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"✅ Φορτώθηκαν {len(uploaded_files)} αρχεία.")
    with st.expander("Προβολή Αρχείων"):
        for f in uploaded_files:
            if "image" in f.type:
                st.image(Image.open(f), width=250)
            else:
                st.write(f"📄 Αρχείο: {f.name}")

st.write("---")

# 3. ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ
st.header("🔬 Δεδομένα Εργαστηρίου")
col1, col2, col3 = st.columns(3)
with col1:
    ph_val = st.number_input("pH Εδάφους", value=7.8)
    om_val = st.number_input("Οργανική Ουσία (%)", value=0.9)
with col2:
    k_val = st.number_input("Κάλιο (ppm)", value=150.0)
    m
