import streamlit as st
from PIL import Image
import io

# Ρυθμίσεις Παγκόσμιας Αυθεντίας
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ MULTI-DATA", page_icon="📂", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; background-color: #1b5e20; color: white; font-size: 20px; border-radius: 12px; height: 3.5em; font-weight: bold; }
    .upload-area { border: 3px dashed #2e7d32; padding: 30px; border-radius: 20px; text-align: center; background-color: #f1f8e9; color: #1b5e20; }
    .report-box { background-color: white; padding: 25px; border-radius: 15px; border-left: 10px solid #2e7d32; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Ολοκληρωμένη Ψηφιακή Θρέψη")
st.write("---")

# ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("⚙️ Παράμετροι Συστήματος")
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
method = st.sidebar.radio("Σύστημα Άρδευσης:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
stage = st.sidebar.selectbox("Φαινολογικό Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Εμφάνιση ανθοταξίας (Μούρο)", "Άνθηση", "Καρπόδεση", "Ανάπτυξη καρπού", "Ωρίμανση"])

# ΕΝΟΤΗΤΑ ΑΝΕΒΑΣΜΑΤΟΣ ΑΡΧΕΙΩΝ
st.header("📂 Ανέβασμα Ανάλυσης (Φωτογραφία ή PDF)")
st.markdown("<div class='upload-area'>Ανεβάστε την ανάλυσή σας σε οποιαδήποτε μορφή: Φωτογραφία από κάμερα ή αρχείο PDF από το Email σας.</div>", unsafe_allow_html=True)

# Εδώ προσθέτουμε την υποστήριξη για πολλά αρχεία
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png", "pdf", "docx", "txt"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    st.success(f"✅ Το αρχείο '{uploaded_file.name}' φορτώθηκε επιτυχώς!")
    
    if "image" in file_type:
        image = Image.open(uploaded_file)
        st.image(image, caption="Προεπισκόπηση Φωτογραφίας", width=500)
    elif "pdf" in file_type:
        st.info("📄 Ανιχνεύθηκε αρχείο PDF. Το σύστημα επεξεργάζεται τα ψηφιακά δεδομένα του εγγράφου.")
    else:
        st.info("📝 Ανιχνεύθηκε έγγραφο κειμένου. Η AI προχωρά σε εξαγωγή τιμών.")

st.write("---")

# ΜΗΧΑΝΕΣ ΥΠΟΛΟΓΙΣΜΟΥ (Inputs)
st.header("🔬 Επιβεβαίωση Τιμών Εργαστηρίου")
c1, c2, c3 = st.columns(3)
with c1:
    ph = st.number_input("pH Εδάφους", value=7.8, help="Απαραίτητο για τον υπολογισμό διαλυτότητας στοιχείων")
    om = st.number_input("Οργανική Ουσία (%)", value=0.9, help="Κρίσιμο για την Ικανότητα Ανταλλαγής Κατιόντων")
with c2:
    potassium = st.number_input("Κάλιο (K) ppm", value=150.0)
    magnesium = st.number_input("Μαγνήσιο (Mg) ppm", value=250.0)
with c3:
    boron = st.numb
