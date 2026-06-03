import streamlit as st

# GEOPRONOIA GLOBAL EXPERT v7.0
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ GLOBAL AI", layout="wide")

# CSS ΣΤΥΛ ΓΙΑ ΕΠΑΓΓΕΛΜΑΤΙΚΟ REPORT
st.markdown("""
<style>
    .main { background-color: #f0f2f6; }
    .expert-card { background-color: white; padding: 30px; border-radius: 15px; border-left: 12px solid #1b5e20; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-bottom: 25px; }
    .scientific-header { color: #1b5e20; font-weight: bold; border-bottom: 3px solid #1b5e20; padding-bottom: 10px; margin-bottom: 20px; font-size: 26px; }
    .stButton>button { background-color: #1b5e20; color: white; font-weight: bold; height: 4em; border-radius: 15px; font-size: 22px; }
</style>
""", unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμιο Κέντρο Γεωργικής Στρατηγικής")
st.write("---")

# ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("📍 Παράμετροι Καλλιέργειας")
crop = st.sidebar.selectbox("Είδος:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα"])
age = st.sidebar.selectbox("Ηλικία:", ["Νεαρή (1-7 ετών)", "Πλήρης Παραγωγή (8-40 ετών)", "Υπερήλικα (40+)"])
method = st.sidebar.radio("Σύστημα:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
stage = st.sidebar.selectbox("Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Μούρο", "Άνθηση", "Καρπόδεση", "Ωρίμανση"])

# ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ (Εδώ βάζεις τα νούμερα από το χαρτί)
st.header("🔬 1. Εισαγωγή Δεδομένων Εργαστηρίου")
c1, c2, c3 = st.columns(3)
ph = c1.number_input("pH Εδάφους", value=6.17)
om = c1.number_input("Οργανική Ουσία (%)", value=0.9)
k_val = c2.number_input("Κάλιο (ppm)", value=150.0)
mg_val = c2.number_input("Μαγνήσιο (ppm)", value=200.0)
boron = c3.number_input("Βόριο (ppm)", value=0.24)
calcium = c3.number_input("Ασβέστιο (meq)", value=6.0)

if st.button("🚀 ΕΚΔΟΣΗ ΠΑΓΚΟΣΜΙΑΣ ΓΕΩΠΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.markdown("<div class='expert-card'>", unsafe_allow_html=True)
    st.markdown("<div class='scientific-header'>ΠΟΡΙΣΜΑ ΣΤΡΑΤΗΓΙΚΗΣ & ΑΝΑΛΥΣΗ MARSCHNER</div>", unsafe_allow_html=True)
    
    # ΜΗΧΑΝΗ 1: ΧΗΜΕΙΑ (ALBRECHT THEORY)
    st.write("### 🧪 Αξιολόγηση Εδάφους & Ισορροπία Κατιόντων")
    if om < 1.5:
        st.error(f"🔴 **ΚΡΙΣΙΜΟ ΕΛΛΕΙΜΜΑ:** Η Οργανική Ουσία ({om}%) είναι κάτω από το βιολογικό όριο. Το έδαφος στερείται CEC (Ικανότητα Ανταλλαγής). Τα λιπάσματά σας θα 'πλυθούν' αν δεν ρίξετε χουμικά ή κοπριά.")
    
    ratio = k_val / (mg_val + 0.1)
    if ratio < 0.5:
        st.warning(f"⚠️ **ΑΝΤΑΓΩΝΙΣΜΟΣ ΚΑΤΙΟΝΤΩΝ:** Η σχέση K/Mg είναι {ratio:.2f}. Το Μαγνήσιο κυριαρχεί. Σύμφωνα με τον Albrecht, το Κάλιο είναι 'κλειδωμένο' εδαφικά. Λύση: Μόνο διαφυλλική λίπανση Καλίου.")

    # ΜΗΧΑΝΗ 2: ΦΥΣΙΟΛΟΓΙΑ (BBCH)
    st.write("### 🌿 Φυσιολογία Φυτού & Φαινολογία")
    if stage == "Μούρο":
        st.info(f"🌸 **ΣΤΑΔΙΟ ΜΟΥΡΟΥ:** Κρίσιμη στιγμή για τη διαφοροποίηση των οφθαλμών. Με Βόριο {boron} ppm, η ακαρπία είναι δεδομένη. Ψεκάστε άμεσα με Βόριο/Ψευδάργυρο.")
    
    # ΜΗΧΑΝΗ 3: ΥΔΡΟΛΟΓΙΑ (MASS FLOW)
    st.write("### 💧 Υδρολογία & Κίνηση Θρεπτικών")
    if method == "Ξερικό":
        st.markdown("🚫 **ΜΟΝΤΕΛΟ MASS FLOW:** Δεν υπάρχει εδαφική υγρασία για τη μεταφορά στοιχείων στη ρίζα. **Ακυρώστε κάθε εδαφική λίπανση.** Οποιαδήποτε παρέμβαση πρέπει να γίνει από το φύλλο.")
    else:
        st.success("✅ **ΠΟΤΙΣΤΙΚΟ ΜΟΝΤΕΛΟ:** Ιδανικές συνθήκες για υδρολίπανση. Στοχεύστε σε μικρές, συχνές δόσεις.")

    # ΜΗΧΑΝΗ 4: ΠΡΟΓΡΑΜΜΑ ΜΟΝΑΔΩΝ
    st.write("### 💰 Οικονομικό Πρόγραμμα Λίπανσης (Ανά Στρέμμα)")
    st.table({
        "Στοιχείο": ["Άζωτο (N)", "Φώσφορος (P2O5)", "Κάλιο (K2O)", "Βόριο (B)"],
        "Μονάδες": ["12-14", "4-5", "16-18", "0.2 (Διαφυλλικά)"],
        "Σκοπός": ["Βλάστηση", "Ανθοφορία/Ρίζα", "Ποιότητα/Ελαιοποίηση", "Καρπόδεση"]
    })

    st.markdown("</div>", unsafe_allow_html=True)
    st.success("✅ Η ανάλυση βασίστηκε σε 5 επίπεδα επιστήμης. Η ΓΕΩΠΡΟΝΟΙΑ είναι ο ανεξάρτητος σύμβουλός σας.")
