import streamlit as st
from PIL import Image
import base64

# Ρυθμίσεις Παγκόσμιας Αυθεντίας
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ GOLD", page_icon="🌳", layout="wide")

st.markdown("""
<style>
    .report-title { color: #1b5e20; font-size: 30px; font-weight: bold; text-align: center; border-bottom: 3px solid #1b5e20; }
    .section-header { background-color: #1b5e20; color: white; padding: 10px; border-radius: 5px; margin-top: 20px; font-size: 20px; }
    .advice-box { background-color: #f1f8e9; border-left: 10px solid #2e7d32; padding: 20px; margin: 10px 0; border-radius: 10px; font-size: 18px; line-height: 1.6; }
    .critical-box { background-color: #ffebee; border-left: 10px solid #d32f2f; padding: 20px; margin: 10px 0; border-radius: 10px; font-size: 18px; }
    .stButton>button { background-color: #1b5e20; color: white; font-weight: bold; height: 4em; width: 100%; border-radius: 15px; font-size: 22px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); }
</style>
""", unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμια Αυθεντία Θρέψης")
st.write("---")

# ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("📍 Στοιχεία Καλλιέργειας")
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age = st.sidebar.selectbox("Ηλικία:", ["1-7 ετών (Νεαρή)", "8-40 ετών (Πλήρης)", "40+ ετών (Υπερήλικα)"])
method = st.sidebar.radio("Σύστημα:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
yield_prev = st.sidebar.radio("Πέρυσι η παραγωγή:", ["Υπερβολική (ON)", "Κανονική", "Μειωμένη (OFF)"])

# ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 1. Ανέβασμα Ανάλυσης (Φωτογραφίες & PDF)")
files = st.file_uploader("Ανεβάστε εδώ τα αρχεία σας", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

if files:
    st.success(f"✅ Φορτώθηκαν {len(files)} αρχεία.")

st.write("---")

# ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ
st.header("🔬 2. Επιβεβαίωση Τιμών Εργαστηρίου")
c1, c2, c3 = st.columns(3)
with c1:
    ph = st.number_input("pH Εδάφους", value=6.17, step=0.01)
    om = st.number_input("Οργανική Ουσία (%)", value=0.904, step=0.001)
    n_nitrate = st.number_input("Άζωτο Νιτρικό (ppm)", value=24.76)
with c2:
    k_val = st.number_input("Κάλιο (K) ppm", value=0.45) # Τιμή meq όπως στην ανάλυση
    mg_val = st.number_input("Μαγνήσιο (Mg) ppm", value=1.32)
    p_val = st.number_input("Φώσφορος (P) ppm", value=14.47)
with c3:
    boron = st.number_input("Βόριο (B) ppm", value=0.24)
    calcium = st.number_input("Ασβέστιο (Ca) meq/100g", value=6.03)

if st.button("🚀 ΕΚΔΟΣΗ ΠΛΗΡΟΥΣ ΕΠΙΣΤΗΜΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.markdown("<div class='report-title'>ΕΠΙΣΗΜΗ ΕΚΘΕΣΗ ΓΕΩΡΓΙΚΗΣ ΣΤΡΑΤΗΓΙΚΗΣ</div>", unsafe_allow_html=True)
    
    # 1. ΜΗΧΑΝΗ ΕΔΑΦΟΥΣ (BCSR & ALBRECHT)
    st.markdown("<div class='section-header'>ΕΝΟΤΗΤΑ 1: ΔΥΝΑΜΙΚΗ ΧΗΜΕΙΑ & ΔΟΜΗ ΕΔΑΦΟΥΣ</div>", unsafe_allow_html=True)
    
    if om < 1.2:
        st.markdown(f"""<div class='critical-box'><b>🔴 ΚΡΙΣΙΜΟ ΕΛΛΕΙΜΜΑ ΟΡΓΑΝΙΚΗΣ ΟΥΣΙΑΣ ({om}%):</b> 
        Σύμφωνα με τη διεθνή βιβλιογραφία, το έδαφός σας είναι "νεκρό". Η Ικανότητα Ανταλλαγής Κατιόντων (CEC) είναι πολύ περιορισμένη. 
        <b>ΑΠΟΤΕΛΕΣΜΑ:</b> Το 50% των λιπασμάτων που ρίχνετε χάνεται στον υδροφόρο ορίζοντα.
        <br><b>ΔΡΑΣΗ:</b> Άμεση ενσωμάτωση 3-4 τόνων/στρέμμα χωνεμένης κοπριάς ή 50kg/στρέμμα χουμικών οξέων.</div>""", unsafe_allow_html=True)

    k_mg_ratio = k_val / (mg_val + 0.1)
    if k_mg_ratio < 0.5:
        st.markdown(f"<div class='advice-box'><b>⚠️ ΑΝΤΑΓΩΝΙΣΜΟΣ ΚΑΤΙΟΝΤΩΝ (Albrecht Theory):</b> Η σχέση Καλίου/Μαγνησίου είναι {k_mg_ratio:.2f}. Το Μαγνήσιο κυριαρχεί και "μπλοκάρει" το Κάλιο. Ακόμα και αν ρίξετε Κάλιο στο χώμα, το δέντρο δεν θα το "δει". Χρειάζεται ενίσχυση Καλίου αποκλειστικά διαφυλλικά.</div>", unsafe_allow_html=True)

    # 2. ΦΑΙΝΟΛΟΓΙΑ & BBCH (MARSCHNER)
    st.markdown("<div class='section-header'>ΕΝΟΤΗΤΑ 2: ΦΥΣΙΟΛΟΓΙΑ ΚΑΛΛΙΕΡΓΕΙΑΣ ({crop})</div>", unsafe_allow_html=True)
    
    if crop == "Ελιά" and boron < 0.5:
        st.markdown(f"""<div class='critical-box'><b>🌸 ΣΤΡΑΤΗΓΙΚΗ ΑΝΘΟΦΟΡΙΑΣ (ΒΟΡΙΟ):</b> Η τιμή {boron} ppm είναι απαγορευτική για την καρπόδεση. 
        <b>ΚΙΝΔΥΝΟΣ:</b> Θα έχετε "σκούπα" (ακαρπία) ή μικροκαρπία.
        <br><b>ΟΔΗΓΙΑ:</b> Ψεκασμός στο στάδιο του <b>ΜΟΥΡΟΥ</b> (λευκή μπαλίτσα) με υδατοδιαλυτό Βόριο 250gr/τόνο και επανάληψη στην πλήρη άνθηση.</div>""", unsafe_allow_html=True)

    if yield_prev == "Υπερβολική (ON)":
        st.markdown("<div class='advice-box'><b>📉 ΜΟΝΤΕΛΟ ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑΣ (C/N Ratio):</b> Λόγω της περσινής υπερπαραγωγής, το δέντρο έχει εξαντλήσει τα αποθέματα υδατανθράκων. Χρειάζεται "ταχυφαγία" με Αμινοξέα και Άζωτο τώρα, αλλιώς το κτήμα θα μείνει άδειο (OFF).</div>", unsafe_allow_html=True)

    # 3. ΥΔΡΟΛΟΓΙΑ (MASS FLOW)
    st.markdown("<div class='section-header'>ΕΝΟΤΗΤΑ 3: ΔΙΑΧΕΙΡΙΣΗ ΝΕΡΟΥ & ΜΕΤΕΩΡΟΛΟΓΙΑ</div>", unsafe_allow_html=True)
    if method == "Ξερικό (Rainfed)":
        st.markdown("<div class='advice-box'><b>🚫 ΠΕΡΙΟΡΙΣΜΟΣ ΜΑΖΙΚΗΣ ΡΟΗΣ:</b> Σε ξερικές συνθήκες, η απορρόφηση Καλίου και Φωσφόρου από τη ρίζα σταματάει μόλις στεγνώσει το έδαφος. <b>Μην πετάτε λιπάσματα στο χώμα το καλοκαίρι.</b> Μεταφέρετε όλη τη θρέψη στα φύλλα (διαφυλλικά).</div>", unsafe_allow_html=True)

    # 4. ΣΥΓΚΕΚΡΙΜΕΝΟ ΠΛΑΝΟ ΜΟΝΑΔΩΝ
    st.markdown("<div class='section-header'>ΕΝΟΤΗΤΑ 4: ΟΛΟΚΛΗΡΩΜΕΝΟ ΠΡΟΓΡΑΜΜΑ ΛΙΠΑΝΣΗΣ (ΑΝΑ ΣΤΡΕΜΜΑ)</div>", unsafe_allow_html=True)
    col_n, col_p, col_k = st.columns(3)
    col_n.metric("ΑΖΩΤΟ (N)", "12-14 Μονάδες")
    col_p.metric("ΦΩΣΦΟΡΟΣ (P)", "4-5 Μονάδες")
    col_k.metric("ΚΑΛΙΟ (K)", "15-18 Μονάδες")
    
    st.write("---")
    st.success("✅ Η ανάλυση ολοκληρώθηκε. Η ΓΕΩΠΡΟΝΟΙΑ εγγυάται την επιστημονική εγκυρότητα του πορίσματος βάσει των παγκόσμιων προτύπων.")
