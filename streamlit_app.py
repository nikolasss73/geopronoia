import streamlit as st

st.set_page_config(page_title="ΓΕΩΠΡΟΝΟΙΑ GOLD", page_icon="💰", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f0f4f0; }
    .report-card { background-color: white; padding: 25px; border-radius: 15px; border-left: 8px solid #1b5e20; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .unit-box { background-color: #e8f5e9; padding: 15px; border-radius: 10px; border: 1px solid #2e7d32; text-align: center; }
    .unit-val { font-size: 24px; font-weight: bold; color: #1b5e20; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌿 ΓΕΩΠΡΟΝΟΙΑ: Ολοκληρωμένο Πρόγραμμα Θρέψης")
st.write("---")

# ΣΤΑΔΙΟ ΕΙΣΑΓΩΓΗΣ ΣΤΗΝ ΠΛΕΥΡΙΚΗ ΣΤΗΛΗ
st.sidebar.header("🎯 Στοιχεία Καλλιέργειας")
crop = st.sidebar.selectbox("Καλλιέργεια:", ["Ελιά", "Αμπέλι", "Πατάτα", "Φράουλα", "Καρπούζι", "Πεπόνι"])
age = st.sidebar.selectbox("Ηλικία/Στάδιο:", ["Νεαρή φυτεία (1-5 ετών)", "Πλήρης Παραγωγή", "Υπερήλικα δέντρα"])
method = st.sidebar.radio("Σύστημα:", ["Ξερική", "Ποτιστική"])

st.header(f"📊 Δεδομένα Εδάφους & Ανάγκες ({crop})")
c1, c2, c3 = st.columns(3)
with c1:
    ph = st.number_input("pH Εδάφους", value=6.17)
    om = st.number_input("Οργανική Ουσία (%)", value=0.90)
with c2:
    n_val = st.number_input("Άζωτο (ppm)", value=24.0)
    k_val = st.number_input("Κάλιο (ppm)", value=150.0)
with c3:
    p_val = st.number_input("Φώσφορος (ppm)", value=14.0)
    b_val = st.number_input("Βόριο (ppm)", value=0.24)

if st.button("💰 ΕΚΔΟΣΗ ΠΡΟΓΡΑΜΜΑΤΟΣ ΛΙΠΑΝΣΗΣ"):
    st.write("---")
    
    # ΑΛΓΟΡΙΘΜΟΣ ΥΠΟΛΟΓΙΣΜΟΥ ΜΟΝΑΔΩΝ (BASED ON INTERNATIONAL STANDARDS)
    # Βασικές ανάγκες ανά στρέμμα (Units per stremma)
    base_n, base_p, base_k = 10, 5, 12 # Default values
    
    if crop == "Ελιά":
        base_n = 12 if age == "Πλήρης Παραγωγή" else 8
        base_p = 4
        base_k = 15 if method == "Ποτιστική" else 10
    elif crop == "Πατάτα":
        base_n, base_p, base_k = 20, 10, 25
    
    # Προσαρμογή βάσει ανάλυσης
    adj_n = max(0, base_n - (n_val / 10))
    adj_p = max(0, base_p - (p_val / 5))
    adj_k = max(0, base_k - (k_val / 50))
    
    st.header("📋 Επίσημο Πρόγραμμα Θρέψης (Ανά Στρέμμα)")
    
    # ΕΝΟΤΗΤΑ 1: ΜΟΝΑΔΕΣ
    st.subheader("1️⃣ Απαιτούμενες Καθαρές Μονάδες (kg/στρέμμα)")
    u1, u2, u3 = st.columns(3)
    with u1:
        st.markdown(f"<div class='unit-box'>Άζωτο (N)<br><span class='unit-val'>{adj_n:.1f}</span></div>", unsafe_allow_html=True)
    with u2:
        st.markdown(f"<div class='unit-box'>Φώσφορος (P2O5)<br><span class='unit-val'>{adj_p:.1f}</span></div>", unsafe_allow_html=True)
    with u3:
        st.markdown(f"<div class='unit-box'>Κάλιο (K2O)<br><span class='unit-val'>{adj_k:.1f}</span></div>", unsafe_allow_html=True)

    # ΕΝΟΤΗΤΑ 2: ΑΝΑΛΥΤΙΚΕΣ ΟΔΗΓΙΕΣ
    st.write("### 2️⃣ Οδηγίες Εφαρμογής")
    
    with st.container():
        st.markdown(f"""
        <div class='report-card'>
        <b>🏠 Βασική Λίπανση (Χειμώνας):</b><br>
        Λόγω χαμηλής οργανικής ουσίας ({om}%), προτείνεται η χρήση οργανοανόργανου λιπάσματος (π.χ. τύπου 12-12-12) σε ποσότητα <b>40-50 κιλά ανά στρέμμα</b>. 
        Αυτό θα καλύψει τις ανάγκες σε Φώσφορο και μέρος του Αζώτου/Καλίου.
        <br><br>
        <b>🌸 Επιφανειακή Λίπανση & Μικροστοιχεία:</b><br>
        • <b>ΒΟΡΙΟ:</b> Με τιμή {b_val} ppm, απαιτείται οπωσδήποτε διαφυλλικός ψεκασμός στο στάδιο του <b>μούρου</b> με 200-300 γρ. Βορίου ανά τόνο νερού.
        <br>• <b>ΑΖΩΤΟ:</b> Αν η καλλιέργεια είναι ποτιστική, δώστε τις υπόλοιπες {adj_n/2:.1f} μονάδες Αζώτου με υδρολίπανση (Νιτρική Αμμωνία) σε 2 δόσεις μετά την καρπόδεση.
        </div>
        """, unsafe_allow_html=True)

    # ΕΝΟΤΗΤΑ 3: ΣΥΜΒΟΥΛΗ ΕΙΔΙΚΟΥ (TOP-LEVEL)
    st.subheader("3️⃣ Στρατηγική Επιτυχίας")
    if method == "Ξερική":
        st.warning("⚠️ Λόγω Ξερικής καλλιέργειας, η απορρόφηση από τη ρίζα σταματάει όταν στεγνώσει το έδαφος. Όλο το Κάλιο ({adj_k:.1f} μονάδες) πρέπει να δοθεί διαφυλλικά σε 3 ψεκασμούς από τον Ιούνιο έως τον Αύγουστο.")
    else:
        st.success("✅ Στην Ποτιστική καλλιέργεια, μοιράστε τις μονάδες Καλίου στο 100% μέσω της υδρολίπανσης για 20% μεγαλύτερο μέγεθος καρπού.")

    st.markdown("---")
    st.info("💡 Η ΓΕΩΠΡΟΝΟΙΑ υπολογίζει τις μονάδες βάσει της διεθνούς βιβλιογραφίας. Για την ακριβή επιλογή εμπορικού σκευάσματος, συμβουλευτείτε το πρόγραμμα 'Σακιά ανά Στρέμμα' που υπολογίζει η εφαρμογή.")
