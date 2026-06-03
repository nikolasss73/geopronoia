import streamlit as st
from PIL import Image

# ΓΕΩΠΡΟΝΟΙΑ GOLD v6.1 - ΣΤΑΘΕΡΗ ΕΚΔΟΣΗ
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ", layout="wide")

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Παγκόσμια Αυθεντία Θρέψης")
st.write("---")

# ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("📍 Ρυθμίσεις")
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα"])
age = st.sidebar.selectbox("Ηλικία:", ["1-7 ετών", "8-40 ετών", "40+ ετών"])
stage = st.sidebar.selectbox("Στάδιο:", ["Μούρο", "Άνθηση", "Καρπόδεση", "Ωρίμανση"])
method = st.sidebar.radio("Σύστημα:", ["Ξερικό", "Ποτιστικό"])
yield_prev = st.sidebar.radio("Πέρυσι παραγωγή:", ["Υπερβολική", "Κανονική", "Μειωμένη"])

# ΑΝΕΒΑΣΜΑ ΑΡΧΕΙΩΝ
st.header("📂 1. Ανέβασμα Αρχείων")
files = st.file_uploader("Ανεβάστε Φωτογραφίες ή PDF", accept_multiple_files=True)
if files:
    st.success(f"Φορτώθηκαν {len(files)} αρχεία.")

# ΕΙΣΑΓΩΓΗ ΤΙΜΩΝ
st.header("🔬 2. Τιμές Εργαστηρίου")
c1, c2, c3 = st.columns(3)
ph = c1.number_input("pH Εδάφους", value=6.17)
om = c1.number_input("Οργανική Ουσία (%)", value=0.90)
k_val = c2.number_input("Κάλιο (ppm)", value=150.0)
mg_val = c2.number_input("Μαγνήσιο (ppm)", value=200.0)
boron = c3.number_input("Βόριο (ppm)", value=0.24)
calcium = c3.number_input("Ασβέστιο (meq)", value=6.0)

if st.button("🚀 ΕΚΔΟΣΗ ΕΠΙΣΤΗΜΟΝΙΚΗΣ ΕΚΘΕΣΗΣ"):
    st.header("📋 ΠΟΡΙΣΜΑ ΓΕΩΠΡΟΝΟΙΑ")
    
    # ΜΗΧΑΝΗ 1: ΧΗΜΕΙΑ (ALBRECHT)
    st.subheader("1. Χημεία Εδάφους")
    if om < 1.5:
        st.error(f"🔴 ΚΡΙΣΙΜΟ: Χαμηλή Οργανική Ουσία ({om}%). Χρειάζεστε κοπριά ή χουμικά.")
    
    k_mg_ratio = k_val / (mg_val + 0.1)
    if k_mg_ratio < 0.5:
        st.warning(f"⚠️ ΑΝΤΑΓΩΝΙΣΜΟΣ: Το Μαγνήσιο μπλοκάρει το Κάλιο. Ρίξτε Κάλιο μόνο διαφυλλικά.")
    
    if ph > 7.5:
        st.error(f"🚫 pH {ph}: Ο Φώσφορος είναι κλειδωμένος. Χρησιμοποιήστε χηλικές μορφές.")

    # ΜΗΧΑΝΗ 2 & 4: ΦΥΣΙΟΛΟΓΙΑ & ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑ
    st.subheader("2. Φυσιολογία & Ιστορικότητα")
    st.write(f"• Ηλικιακό μοντέλο: {age}")
    if yield_prev == "Υπερβολική":
        st.warning("📉 ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑ: Το δέντρο είναι εξαντλημένο. Χρειάζεται άμεσα Αμινοξέα.")

    # ΜΗΧΑΝΗ 3: ΥΔΡΟΛΟΓΙΑ
    st.subheader("3. Διαχείριση Νερού")
    if method == "Ξερικό":
        st.info("🚫 ΞΕΡΙΚΗ ΔΙΑΧΕΙΡΙΣΗ: Η ρίζα δεν τραβάει λίπασμα χωρίς βροχή. Μόνο ψεκασμοί στα φύλλα.")
    else:
        st.success("💧 ΠΟΤΙΣΤΙΚΟ: Ιδανικό για υδρολίπανση.")

    # ΜΗΧΑΝΗ 5: ΣΤΡΑΤΗΓΙΚΗ
    st.subheader("4. Πρόγραμμα Μονάδων ανά Στρέμμα")
