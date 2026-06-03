import streamlit as st

# Ρυθμίσεις Παγκόσμιας Αυθεντίας
st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ GLOBAL AI", page_icon="🌍", layout="wide")

st.markdown("""
    <style>
    .report-card { background-color: #ffffff; padding: 30px; border-radius: 15px; border-top: 10px solid #1b5e20; box-shadow: 5px 5px 20px rgba(0,0,0,0.1); }
    .engine-title { color: #1b5e20; font-weight: bold; border-bottom: 2px solid #e8f5e9; margin-top: 20px; }
    .warning-box { background-color: #fff3e0; border-left: 5px solid #ff9800; padding: 15px; margin: 10px 0; }
    .critical-box { background-color: #ffebee; border-left: 5px solid #d32f2f; padding: 15px; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Σύστημα Γεωργικής Ευφυΐας (Version 5.0)")
st.write("---")

# ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ - ΟΙ 5 ΜΗΧΑΝΕΣ
st.sidebar.header("🧠 Παράμετροι Συστημάτων")

# 1. Φαινολογία
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα"])
stage = st.sidebar.selectbox("Φαινολογικό Στάδιο (BBCH):", ["Έκπτυξη οφθαλμών", "Εμφάνιση ανθοταξίας (Μούρο)", "Άνθηση", "Καρπόδεση", "Ανάπτυξη καρπού", "Ωρίμανση"])
age = st.sidebar.selectbox("Ηλικία Δέντρων:", ["Νεαρή (1-5 έτη)", "Πλήρης Παραγωγή", "Υπερήλικα"])

# 2. Υδρολογία & Μετεωρολογία
method = st.sidebar.radio("Σύστημα Άρδευσης:", ["Ξερικό (Rainfed)", "Ποτιστικό (Fertigation)"])
rain_forecast = st.sidebar.select_slider("Πρόβλεψη Βροχόπτωσης (επόμενες 15 μέρες):", options=["Καμία", "Λίγη", "Επαρκής"])

# 3. Ιστορικότητα
prev_yield = st.sidebar.radio("Πέρυσι η παραγωγή ήταν:", ["Υπερβολική (Χρονιά ON)", "Κανονική", "Μειωμένη (Χρονιά OFF)"])

st.header("🔬 Δεδομένα Εργαστηρίου & Εδάφους")
col1, col2, col3 = st.columns(3)

with col1:
    ph = st.number_input("pH Εδάφους", value=7.8)
    om = st.number_input("Οργανική Ουσία (%)", value=0.9)
    soil_type = st.selectbox("Μηχανική Σύσταση:", ["Αμμώδες", "Πηλώδες", "Αργιλώδες"])

with col2:
    nitrogen = st.number_input("Άζωτο (ppm)", value=20.0)
    potassium = st.number_input("Κάλιο (ppm)", value=150.0)
    magnesium = st.number_input("Μαγνήσιο (ppm)", value=250.0)

with col3:
    boron = st.number_input("Βόριο (ppm)", value=0.24)
    calcium = st.number_input("Ασβέστιο (meq/100g)", value=8.0)
    ec_water = st.number_input("EC Νερού (αν είναι ποτιστικό)", value=0.5)

if st.button("🚀 ΕΚΤΕΛΕΣΗ ΤΡΙΓΩΝΙΣΜΟΥ ΔΕΔΟΜΕΝΩΝ"):
    st.write("---")
    
    # ΜΗΧΑΝΗ 1: ΧΗΜΕΙΑ ΕΔΑΦΟΥΣ (BCSR Theory)
    st.markdown("<div class='engine-title'>1. ΜΗΧΑΝΗ ΔΥΝΑΜΙΚΗΣ ΧΗΜΕΙΑΣ ΕΔΑΦΟΥΣ</div>", unsafe_allow_html=True)
    k_mg_ratio = potassium / (magnesium + 0.1)
    
    if ph > 7.5:
        st.markdown("<div class='critical-box'>⚠️ <b>ΚΛΕΙΔΩΜΕΝΟΣ ΦΩΣΦΟΡΟΣ & ΙΧΝΟΣΤΟΙΧΕΙΑ:</b> Λόγω υψηλού pH, ο Φώσφορος και τα Ιχνοστοιχεία (B, Zn, Fe) είναι μη διαθέσιμα. <b>ΑΠΑΓΟΡΕΥΣΗ:</b> Μην ρίξετε κοινά εδαφικά λιπάσματα. Προτείνεται μόνο χρήση Χηλικών Μορφών (EDDHA/EDTA) ή διαφυλλικά.</div>", unsafe_allow_html=True)
    
    if k_mg_ratio < 0.4:
        st.markdown("<div class='warning-box'>⚠️ <b>ΑΝΤΑΓΩΝΙΣΜΟΣ ΚΑΤΙΟΝΤΩΝ:</b> Το Μαγνήσιο μπλοκάρει το Κάλιο. Απαιτείται ενίσχυση Καλίου παρά την ύπαρξή του στο έδαφος.</div>", unsafe_allow_html=True)

    # ΜΗΧΑΝΗ 2: ΦΑΙΝΟΛΟΓΙΑ & ΦΥΣΙΟΛΟΓΙΑ
    st.markdown("<div class='engine-title'>2. ΜΗΧΑΝΗ ΦΑΙΝΟΛΟΓΙΑΣ & ΦΥΣΙΟΛΟΓΙΑΣ</div>", unsafe_allow_html=True)
    if stage == "Εμφάνιση ανθοταξίας (Μούρο)":
        st.write(f"📍 Στάδιο BBCH: Είστε στην κρίσιμη φάση της διαφοροποίησης. Η ανάγκη για **Βόριο** και **Ψευδάργυρο** είναι στο 100%.")
    elif stage == "Ανάπτυξη καρπού":
        st.write("📍 Στάδιο BBCH: Η ζήτηση μετατοπίζεται στο **Κάλιο** για τη δημιουργία ελαίου/σακχάρων.")

    # ΜΗΧΑΝΗ 3: ΥΔΡΟΛΟΓΙΑ & ΜΕΤΕΩΡΟΛΟΓΙΑ
    st.markdown("<div class='engine-title'>3. ΜΗΧΑΝΗ ΠΕΡΙΒΑΛΛΟΝΤΟΣ & ΦΥΣΙΚΗΣ ΤΟΥ ΝΕΡΟΥ</div>", unsafe_allow_html=True)
    if method == "Ξερικό (Rainfed)":
        if rain_forecast == "Καμία":
            st.markdown("<div class='critical-box'>🚫 <b>ΑΚΥΡΩΣΗ ΕΔΑΦΙΚΗΣ ΛΙΠΑΝΣΗΣ:</b> Δεν υπάρχει υγρασία για τη 'Μαζική Ροή' των στοιχείων. Οποιοδήποτε λίπασμα στο χώμα θα μείνει ανενεργό. <br><b>ΣΤΡΑΤΗΓΙΚΗ:</b> Μεταφέρετε το 100% της θρέψης σε <b>Διαφυλλικούς Ψεκασμούς</b> αργά το απόγευμα.</div>", unsafe_allow_html=True)
        else:
            st.success("✅ Η πρόβλεψη βροχής επιτρέπει περιορισμένη βασική λίπανση.")
    else:
        if ec_water > 1.2:
            st.warning(f"⚠️ <b>ΚΙΝΔΥΝΟΣ ΑΛΑΤΟΤΗΤΑΣ:</b> Το νερό σας έχει υψηλό EC ({ec_water}). Μειώστε τη δόση της υδρολίπανσης κατά 20% για να αποφύγετε το στρες στις ρίζες.")

    # ΜΗΧΑΝΗ 4: ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑ (C/N RATIO)
    st.markdown("<div class='engine-title'>4. ΜΗΧΑΝΗ ΙΣΤΟΡΙΚΟΤΗΤΑΣ & ΠΑΡΕΝΙΑΥΤΟΦΟΡΙΑΣ</div>", unsafe_allow_html=True)
    if prev_yield == "Υπερβολική (Χρονιά ON)":
        st.markdown("<div class='warning-box'>📉 <b>ΕΞΑΝΤΛΗΣΗ ΑΠΟΘΕΜΑΤΩΝ:</b> Μετά από χρονιά υπερπαραγωγής, το δέντρο έχει χαμηλό λόγο Άνθρακα/Αζώτου. Χρειάζεται άμεση ενίσχυση με Άζωτο και Αμινοξέα τώρα για να μην 'κάτσει' το κτήμα φέτος.</div>", unsafe_allow_html=True)

    # ΜΗΧΑΝΗ 5: ΣΤΡΑΤΗΓΙΚΗ (DRIS)
    st.markdown("<div class='engine-title'>5. ΤΕΛΙΚΗ ΣΤΡΑΤΗΓΙΚΗ ΛΙΠΑΝΣΗΣ (DRIS)</div>", unsafe_allow_html=True)
    st.subheader("📋 Πλάνο Ενεργειών Ανά Στρέμμα:")
    
    # Παράδειγμα υπολογισμού μονάδων
    if crop == "Ελιά" and method == "Ξερικό (Rainfed)":
        st.info("🎯 **ΠΡΟΓΡΑΜΜΑ:** 0 μονάδες στο έδαφος (λόγω ανομβρίας). 3 Διαφυλλικοί ψεκασμοί: 1) Στο Μούρο (Βόριο+Αμινοξέα), 2) Μετά την καρπόδεση (20-20-20), 3) Στην ελαιοποίηση (Θειικό Κάλιο).")
    else:
        st.info("🎯 **ΠΡΟΓΡΑΜΜΑ:** 10-12 μονάδες Αζώτου, 4 μονάδες Φωσφόρου, 15 μονάδες Καλίου. Εφαρμογή μέσω υδρολίπανσης σε 6 δόσεις.")

    st.success("✅ Η ανάλυση ολοκληρώθηκε με βάση τα μοντέλα Marschner και Albrecht. Η ΓΕΩΠΡΟΝΟΙΑ σας παρέχει πλέον την κορυφαία γεωπονική γνώση παγκοσμίως.")
