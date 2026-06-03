import streamlit as st
from PIL import Image

# Έκδοση 5.4 - Σταθερή έκδοση χωρίς σφάλματα επικόλλησης
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ ULTIMATE", page_icon="🌳", layout="wide")

# Στυλ σελίδας για επαγγελματική εμφάνιση
st.markdown("""
<style>
    .main { background-color: #f4f7f6; }
    .report-card { 
        background-color: white; 
        padding: 20px; 
        border-radius: 12px; 
        border-left: 10px solid #1b5e20; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
        margin-bottom: 20px; 
    }
    .stButton>button { 
        background-color: #1b5e20; 
        color: white; 
        font-weight: bold; 
        height: 3.5em; 
        width: 100%;
        border-radius: 10px;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμιο Σύστημα Στρατηγικής")
st.caption("Σύνθεση Χημείας Εδάφους, Φυσιολογίας, Υδρολογίας και Μετεωρολογίας")
st.write("---")

# 1. ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ (ΡΥΘΜΙΣΕΙΣ)
st.sidebar.header("🧠 Παράμετροι")
crop_choice = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age_choice = st.sidebar.selectbox("Ηλικία Καλλιέργειας:", ["1-7 ετών (Νεαρή Φυτεία)", "8-40 ετών (Πλήρης Παραγωγή)", "40+ ετών (Υπερήλικα Δέντρα)"])
stage_choice = st.sidebar.selectbox("Φαινολογικό Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Εμφάνιση ανθοταξίας (Μούρο)", "Άνθηση", "Καρπόδεση", "Ανάπτυξη καρπού", "Ωρίμανση"])
method_choice = st.sidebar.radio("Σύστημα Άρδευσης:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
yield_choice = st.sidebar.radio("Πέρυσι η παραγωγή ήταν:", ["Υπερβολική (ON)", "Κανονική", "Μειωμένη (OFF)"])

# 2. ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 Αρχεία Ανάλυσης")
uploaded_files = st.file_uploader("Ανεβάστε Φωτογραφίες ή PDF (Πολλαπλή επιλογή)", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"✅ Φορτώθηκαν {len(uploaded_files)} αρχεία.")
    with st.expander("Προβολή Αρχείων"):
        for f in uploaded_files:
            if "image" in f.type:
                st.image(Image.open(f), use_container_width=True)
            else:
                st.write(f"📄 Αρχείο: {f.name}")

st.write("---")

# 3. ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ ΕΡΓΑΣΤΗΡΙΟΥ
st.header("🔬 Δεδομένα Εδάφους")
col1, col2, col3 = st.columns(3)
with col1:
    ph_val = st.number_input("pH Εδάφους", value=7.8, step=0.1)
    om_val = st.number_input("Οργανική Ουσία (%)", value=0.9, step=0.1)
with col2:
    k_val = st.number_input("Κάλιο (K) ppm", value=150.0)
    mg_val = st.number_input("Μαγνήσιο (Mg) ppm", value=250.0)
with col3:
    b_val = st.number_input("Βόριο (B) ppm", value=0.24)
    ca_val = st.number_input("Ασβέστιο (Ca) meq/100g", value=8.0)

# 4. ΕΚΤΕΛΕΣΗ ΠΟΡΙΣΜΑΤΟΣ (BUSINESS LOGIC)
if st.button("🚀 ΕΚΔΟΣΗ ΠΑΓΚΟΣΜΙΑΣ ΓΕΩΠΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.write("---")
    st.header("📋 Επιστημονικό Πόρισμα Στρατηγικής")
    
    # ΕΝΟΤΗΤΑ 1: ΧΗΜΕΙΑ ΕΔΑΦΟΥΣ
    st.write("### 1. Χημεία Εδάφους (BCSR)")
    st.markdown("<div class='report-card'>", unsafe_allow_html=True)
    if ph_val > 7.5:
        st.error(f"❌ pH {ph_val}: Ο Φώσφορος και τα Ιχνοστοιχεία είναι κλειδωμένα. Προτιμήστε χηλικές μορφές.")
    if k_val / (mg_val + 0.1) < 0.5:
        st.warning("⚠️ ΑΝΤΑΓΩΝΙΣΜΟΣ: Το Μαγνήσιο εμποδίζει την απορρόφηση Καλίου.")
    if om_val < 1.5:
        st.error(f"🔴 ΧΑΜΗΛΗ ΟΡΓΑΝΙΚΗ ΟΥΣΙΑ ({om_val}%): Το έδαφος δεν συγκρατεί θρεπτικά.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ΕΝΟΤΗΤΑ 2: ΦΥΣΙΟΛΟΓΙΑ & ΙΣΤΟΡΙΚΟΤΗΤΑ
    st.write("### 2. Φυσιολογία & Ιστορικότητα")
    st.markdown("<div class='report-card'>", unsafe_allow_html=True)
    st.write(f"• **Κατηγορία Ηλικίας:** {age_choice}")
    if yield_choice == "Υπερβολική (ON)":
        st.warning("📉 ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑ: Τα αποθέματα του δέντρου είναι εξαντλημένα. Κίνδυνος ακαρπίας.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ΕΝΟΤΗΤΑ 3: ΥΔΡΟΛΟΓΙΑ
    st.write("### 3. Υδρολογία")
    st.markdown("<div class='report-card'>", unsafe_allow_html=True)
    if method_choice == "Ξερικό (Rainfed)":
        st.info("🚫 ΞΕΡΙΚΟ: Αποφύγετε εδαφική λίπανση χωρίς βροχή. Χρησιμοποιήστε μόνο διαφυλλικούς ψεκασμούς.")
    else:
        st.success("💧 ΠΟΤΙΣΤΙΚΟ: Ιδανικές συνθήκες για υδρολίπανση.")
    st.markdown("</div>", unsafe_allow_html=True)

    # ΕΝΟΤΗΤΑ 4: ΜΟΝΑΔΕΣ ΛΙΠΑΝΣΗΣ
    st.write("### 4. Πρόγραμμα Μονάδων ανά Στρέμμα")
    n_col, p_col, k_col = st.columns(3)
    n_col.metric("Άζωτο (N)", "12-14 μον.")
    p_col.metric("Φώσφορος (P)", "4-6 μον.")
    k_col.metric("Κάλιο (K)", "15-18 μον.")
    
    if stage_choice == "Εμφάνιση ανθοταξίας (Μούρο)":
        st.info("🌸 ΣΤΑΔΙΟ ΜΟΥΡΟΥ: Ψεκασμός με Βόριο και Ψευδάργυρο τώρα.")

    st.write("---")
    st.success("✅ Η ανάλυση ολοκληρώθηκε επιτυχώς από τη ΓΕΩΠΡΟΝΟΙΑ.")
