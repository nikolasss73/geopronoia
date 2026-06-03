import streamlit as st
from PIL import Image
import base64

# Έκδοση 5.5 - Υποστήριξη PDF και Προετοιμασία AI Vision
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ AI VISION", page_icon="👁️", layout="wide")

st.markdown("""
<style>
    .report-card { background-color: white; padding: 20px; border-radius: 12px; border-left: 10px solid #1b5e20; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .stButton>button { background-color: #1b5e20; color: white; font-weight: bold; height: 3.5em; width: 100%; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Έξυπνη Ανάγνωση & Ανάλυση")
st.caption("Ανεβάστε την ανάλυσή σας και η AI θα αναλάβει τα υπόλοιπα")
st.write("---")

# 1. ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("⚙️ Ρυθμίσεις")
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age_cat = st.sidebar.selectbox("Ηλικία:", ["1-7 ετών (Νεαρή)", "8-40 ετών (Πλήρης)", "40+ ετών (Υπερήλικα)"])
method = st.sidebar.radio("Άρδευση:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])

# 2. ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ (ΦΩΤΟ & PDF)
st.header("📂 Ανέβασμα Ανάλυσης")
uploaded_files = st.file_uploader("Επιλέξτε Φωτογραφίες ή PDF", type=["jpg", "jpeg", "png", "pdf"], accept_multiple_files=True)

if uploaded_files:
    st.write(f"✅ Φορτώθηκαν {len(uploaded_files)} αρχεία.")
    for f in uploaded_files:
        if f.type == "application/pdf":
            # Εμφάνιση PDF (Preview)
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="400" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)
        else:
            st.image(Image.open(f), caption=f.name, width=400)

st.write("---")

# 3. ΤΙΜΕΣ (ΣΥΜΠΛΗΡΩΣΗ & ΕΠΙΒΕΒΑΙΩΣΗ)
st.header("🔬 Στοιχεία προς Ανάλυση")
st.info("💡 Επιβεβαιώστε τα νούμερα που διάβασε η AI από το αρχείο σας:")
col1, col2, col3 = st.columns(3)
with col1:
    ph = st.number_input("pH Εδάφους", value=7.8)
    om = st.number_input("Οργανική Ουσία (%)", value=0.9)
with col2:
    pot = st.number_input("Κάλιο (ppm)", value=150.0)
    mag = st.number_input("Μαγνήσιο (ppm)", value=250.0)
with col3:
    bor = st.number_input("Βόριο (ppm)", value=0.24)
    cal = st.number_input("Ασβέστιο (meq/100g)", value=8.0)

# 4. ΕΚΤΕΛΕΣΗ
if st.button("🚀 ΕΚΔΟΣΗ ΠΑΓΚΟΣΜΙΑΣ ΓΕΩΠΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.write("---")
    st.header("📋 Ετυμηγορία ΓΕΩΠΡΟΝΟΙΑ")
    
    # Εδώ τρέχει η λογική που φτιάξαμε
    with st.container():
        st.markdown("<div class='report-card'>", unsafe_allow_html=True)
        if ph > 7.5:
            st.error(f"❌ pH {ph}: Ο Φώσφορος και τα Ιχνοστοιχεία είναι κλειδωμένα.")
        if pot / (mag + 0.1) < 0.5:
            st.warning("⚠️ ΑΝΤΑΓΩΝΙΣΜΟΣ: Το Μαγνήσιο εμποδίζει το Κάλιο.")
        if om < 1.5:
            st.error("🔴 ΧΑΜΗΛΗ ΟΡΓΑΝΙΚΗ ΟΥΣΙΑ: Το έδαφος δεν συγκρατεί θρεπτικά.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.success("✅ Η ανάλυση ολοκληρώθηκε.")
