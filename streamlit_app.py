import streamlit as st
from PIL import Image

# Ρυθμίσεις Παγκόσμιας Αυθεντίας - Version 5.0
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
st.caption("Σύνθεση Χημείας Εδάφους, Φυσιολογίας Φυτών, Υδρολογίας και Μετεωρολογίας")
st.write("---")

# 1. ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ - ΟΙ 5 ΜΗΧΑΝΕΣ ΥΠΟΛΟΓΙΣΜΟΥ
st.sidebar.header("🧠 Ρυθμίσεις Συστημάτων")

# Μηχανή Φαινολογίας & Ηλικίας
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age_category = st.sidebar.selectbox("Ηλικία Καλλιέργειας:", [
    "Νεαρή Φυτεία (1-7 ετών): Εστίαση σε ρίζα/σκελετό", 
    "Πλήρης Παραγωγή (8-40 ετών): Μέγιστη καρποφορία", 
    "Υπερήλικα Δέντρα (άνω των 40 ετών): Αναζωογόνηση"
])
stage = st.sidebar.selectbox("Φαινολογικό Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Εμφάνιση ανθοταξίας (Μούρο)", "Άνθηση", "Καρπόδεση", "Ανάπτυξη καρπού", "Ωρίμανση"])

# Μηχανή Υδρολογίας & Ιστορικότητας
method = st.sidebar.radio("Σύστημα Άρδευσης:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
prev_yield = st.sidebar.radio("Πέρυσι η παραγωγή ήταν:", ["Υπερβολική (Χρονιά ON)", "Κανονική", "Μειωμένη (Χρονιά OFF)"])

st.sidebar.markdown("---")
st.sidebar.info("Βάσει μοντέλων Marschner, Albrecht και κλίμακας BBCH.")

# 2. ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 Ανέβασμα Αρχείων Ανάλυσης")
uploaded_files = st.file_uploader("Ανεβάστε Φωτογραφίες ή PDF (Πολλαπλή επιλογή)", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

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

# 3. ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ ΕΡΓΑΣΤΗΡΙΟΥ (DATA INPUT)
st.header("🔬 Επιβεβαίωση Τιμών Εργαστηρίου")
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

# 4. ΕΚΤΕΛΕΣΗ ΤΩΝ 5 ΜΗΧΑΝΩΝ (LOGIC)
if st.button("🚀 ΕΚΔΟΣΗ ΠΑΓΚΟΣΜΙΑΣ ΓΕΩΠΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.write("---")
    
    # ΜΗΧΑΝΗ 1: ΧΗΜΕΙΑ ΕΔΑΦΟΥΣ (BCSR)
    st.markdown("<div class='engine-header'>1. ΜΗΧΑΝΗ ΔΥΝΑΜΙΚΗΣ ΧΗΜΕΙΑΣ ΕΔΑΦΟΥΣ</div>", unsafe_allow_html=True)
    if ph > 7.5:
        st.error(f"❌ **ΜΠΛΟΚΑΡΙΣΜΑ ΣΤΟΙΧΕΙΩΝ:** Λόγω pH {ph}, ο Φώσφορος και τα Ιχνοστοιχεία είναι 'κλειδωμένα'.")
    if potassium / (magnesium + 0.1) < 0.5:
        st.warning("⚠️ **ΑΝΤΑΓΩΝΙΣΜΟΣ ΚΑΤΙΟΝΤΩΝ:** Το Μαγνήσιο εμποδίζει την απορρόφηση Καλίου.")
    if om < 1.5:
        st.error(f"🔴 **ΧΑΜΗΛΗ CEC:** Με {om}% οργανική ουσία, το έδαφος δεν συγκρατεί θρεπτικά.")

    # ΜΗΧΑΝΗ 2 & 4: ΦΥΣΙΟΛΟΓΙΑ & ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑ (C/N)
    st.markdown("<div class='engine-header'>2. ΦΥΣΙΟΛΟΓΙΑ & ΙΣΤΟΡΙΚΟΤΗΤΑ (C/N RATIO)</div>", unsafe_allow_html=True)
    st.write(f"• **Ηλικιακό Μοντέλο:** {age_category}")
    if prev_yield == "Υπερβολική (Χρονιά ON)":
        st.warning("📉 **ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑ:** Τα αποθέματα Άνθρακα/Αζώτου
