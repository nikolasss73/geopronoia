import streamlit as st
from PIL import Image

# Ρυθμίσεις Παγκόσμιας Αυθεντίας - Version 5.1 (Stable)
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ ULTIMATE", page_icon="🌳", layout="wide")

# Επαγγελματικό Στυλ
st.markdown("""
    <style>
    .main { background-color: #f4f7f6; }
    .report-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 10px solid #1b5e20; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .engine-header { color: #1b5e20; font-weight: bold; border-bottom: 2px solid #e8f5e9; padding-bottom: 5px; margin-top: 20px; }
    .stButton>button { width: 100%; background-color: #1b5e20; color: white; font-weight: bold; height: 3.5em; border-radius: 10px; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμιο Σύστημα Γεωργικής Στρατηγικής")
st.caption("Ενοποιημένη Ανάλυση Χημείας Εδάφους, Φυσιολογίας, Υδρολογίας & Μετεωρολογίας")
st.write("---")

# 1. ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ - ΡΥΘΜΙΣΕΙΣ
st.sidebar.header("🧠 Παράμετροι Συστημάτων")

crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])

age_category = st.sidebar.selectbox("Ηλικία Καλλιέργειας:", [
    "Νεαρή Φυτεία (1-7 ετών)", 
    "Πλήρης Παραγωγή (8-40 ετών)", 
    "Υπερήλικα Δέντρα (άνω των 40 ετών)"
])

stage = st.sidebar.selectbox("Φαινολογικό Στάδιο (BBCH):", [
    "Έκπτυξη οφθαλμών", 
    "Εμφάνιση ανθοταξίας (Μούρο)", 
    "Άνθηση", 
    "Καρπόδεση", 
    "Ανάπτυξη καρπού", 
    "Ωρίμανση"
])

method = st.sidebar.radio("Σύστημα Άρδευσης:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
prev_yield = st.sidebar.radio("Πέρυσι η παραγωγή ήταν:", ["Υπερβολική (Χρονιά ON)", "Κανονική", "Μειωμένη (Χρονιά OFF)"])

# 2. ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 Αρχεία Ανάλυσης (Φωτογραφίες & PDF)")
uploaded_files = st.file_uploader("Ανεβάστε όλα τα αρχεία της ανάλυσης μαζί", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"✅ Φορτώθηκαν {len(uploaded_files)} αρχεία.")
    with st.expander("Προεπισκόπηση Αρχείων"):
        cols = st.columns(4)
        for idx, file in enumerate(uploaded_files):
            with cols[idx % 4]:
                if "image" in file.type:
                    st.image(Image.open(file), use_container_width=True)
                else:
                    st.write(f"📄 PDF: {file.name}")

st.write("---")

# 3. ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ ΕΡΓΑΣΤΗΡΙΟΥ
st.header("🔬 Δεδομένα Εδάφους & Θρέψης")
c1, c2, c3 = st.columns(3)
with c1:
    ph = st.number_input("pH Εδάφους", value=7.8, step=0.1)
    om = st.number_input("Οργανική Ουσία (%)", value=0.9, step=0.1)
with c2:
    potassium = st.number_input("Κάλιο (K) ppm", value=150.0)
    magnesium = st.number_input("Μαγνήσιο (Mg) ppm", value=250.0)
with c3:
    boron = st.number_input("Βόριο (B) ppm", value=0.24)
    calcium = st.number_input("Ασβέστιο (Ca) meq/100g", value=8.0)

# 4. ΕΚΤΕΛΕΣΗ ΤΩΝ 5 ΜΗΧΑΝΩΝ
if st.button("🚀 ΕΚΔΟΣΗ ΠΑΓΚΟΣΜΙΑΣ ΓΕΩΠΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.write("---")
    st.header("📋 Επιστημονική Ετυμηγορία ΓΕΩΠΡΟΝΟΙΑ")
    
    # ΜΗΧΑΝΗ 1: ΧΗΜΕΙΑ ΕΔΑΦΟΥΣ
    st.markdown("<div class='engine-header'>1. ΜΗΧΑΝΗ ΔΥΝΑΜΙΚΗΣ ΧΗΜΕΙΑΣ ΕΔΑΦΟΥΣ (BCSR)</d
