import streamlit as st
from PIL import Image

# Ρυθμίσεις Παγκόσμιας Αυθεντίας
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ ULTIMATE AI", page_icon="🌳", layout="wide")

st.markdown("""
    <style>
    .engine-card { background-color: #ffffff; padding: 20px; border-radius: 15px; border-left: 8px solid #1b5e20; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .stButton>button { background-color: #1b5e20; color: white; font-weight: bold; height: 3.5em; border-radius: 10px; }
    .sidebar-info { font-size: 14px; color: #555; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Ολοκληρωμένο Σύστημα Λήψης Αποφάσεων")
st.write("---")

# 1. ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ - ΡΥΘΜΙΣΕΙΣ ΜΗΧΑΝΩΝ
st.sidebar.header("🧠 Ρυθμίσεις Συστημάτων")

# Μηχανή Φαινολογίας & Ηλικίας
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age_category = st.sidebar.selectbox("Ηλικία Καλλιέργειας:", [
    "Νεαρή Φυτεία (1-7 ετών)", 
    "Πλήρης Παραγωγή (8-40 ετών)", 
    "Υπερήλικα Δέντρα (άνω των 40 ετών)"
])
stage = st.sidebar.selectbox("Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Εμφάνιση ανθοταξίας (Μούρο)", "Άνθηση", "Καρπόδεση", "Ανάπτυξη καρπού", "Ωρίμανση"])

# Μηχανή Υδρολογίας & Ιστορικότητας
method = st.sidebar.radio("Σύστημα Άρδευσης:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
prev_yield = st.sidebar.radio("Πέρυσι η παραγωγή ήταν:", ["Υπερβολική (Χρονιά ON)", "Κανονική", "Μειωμένη (Χρονιά OFF)"])

st.sidebar.markdown("---")
st.sidebar.caption("💡 Η ΓΕΩΠΡΟΝΟΙΑ συνδυάζει Χημεία Εδάφους, Φυσιολογία, Υδρολογία και Μετεωρολογία.")

# 2. ΚΥΡΙΟ ΜΕΝΟΥ - ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 Ανέβασμα Πολλαπλών Αρχείων")
uploaded_files = st.file_uploader("Ανεβάστε Φωτογραφίες Ανάλυσης ή PDF (Πολλαπλή επιλογή)", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"✅ Φορτώθηκαν {len(uploaded_files)} αρχεία.")
    with st.expander("Δείτε τα αρχεία σας"):
        cols = st.columns(4)
        for idx, file in enumerate(uploaded_files):
            with cols[idx % 4]:
                if "image" in file.type:
                    st.image(Image.open(file), use_container_width=True, caption=file.name)
                else:
                    st.write(f"📄 {file.name} (PDF)")

st.write("---")

# 3. ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ ΕΡΓΑΣΤΗΡΙΟΥ
st.header("🔬 Επιβεβαίωση Τιμών Εργαστηρίου")
c1, c2, c3 = st.columns(3)
with c1:
    ph = st.number_input("pH Εδάφους", value=7.8)
    om = st.number_input("Οργανική Ουσία (%)", value=0.9)
with c2:
    potassium = st.number_input("Κάλιο (ppm)", value=150.0)
    magnesium = st.number_input("Μαγνήσιο (ppm)", value=250.0)
with c3:
    boron = st.number_input("Βόριο (ppm)", value=0.24)
    calcium = st.number_input("Ασβέστιο (meq/100g)", value=8.0)

# 4. ΕΚΤΕΛΕΣΗ ΤΩΝ 5 ΜΗΧΑΝΩΝ
if st.button("🚀 ΕΚΔΟΣΗ ΠΑΓΚΟΣΜΙΑΣ ΓΕΩΠΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.write("---")
    st.header("📋 Επιστημονική Ετυμηγορία & Πρόγραμμα Θρέψης")
    
    # ΜΗΧΑΝΗ 1: ΧΗΜΕΙΑ ΕΔΑΦΟΥΣ (BCSR)
    st.subheader("1️⃣ Δυναμική Χημεία Εδάφους")
    with st.container():
        st.markdown("<div class='engine-card'>", unsafe_allow_html=True)
        if ph > 7.5:
            st.error(f"❌ **ΜΠΛΟΚΑΡΙΣΜΑ ΣΤΟΙΧΕΙΩΝ:** Λόγω pH {ph}, ο Φώσφορος κα
