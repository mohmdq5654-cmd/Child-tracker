import streamlit as st

# ==========================================
# 1. Developmental Data (Ages 1 to 16)
# ==========================================
development_data = {
    1.0: {
        "motor": "Walking with support, standing alone briefly.",
        "psycho": "Separation anxiety peaks. Starts imitating parents.",
        "nutrition": "Mashed potatoes, boiled egg yolks, soft fruits.",
        "tips": "Engage in floor play. Read board books daily."
    },
    2.0: {
        "motor": "Running, kicking a ball forward, climbing furniture.",
        "psycho": "Independence phase ('Terrible Twos'). Say 'no' often.",
        "nutrition": "Fava beans, cottage cheese, rice, small meatballs.",
        "tips": "Establish a consistent bedtime routine. Offer choices (e.g., 'red shirt or blue shirt?')."
    },
    3.0: {
        "motor": "Riding a tricycle, standing on one foot.",
        "psycho": "Imaginative play begins. Asks 'why' constantly.",
        "nutrition": "Boiled eggs, yogurt, sweet potatoes, fresh berries.",
        "tips": "Encourage independent dressing. Answer their 'why' questions patiently."
    }
}

# ==========================================
# 2. Vaccinations Data
# ==========================================
vaccine_data = {
    "2 Months": {
        "vaccines": "Hexavalent (DTP, Polio, Hep B, Hib), Rotavirus, Pneumococcal.",
        "symptoms": "Mild fever, fussiness, sleepiness, slight redness or swelling at the injection site."
    },
    "4 Months": {
        "vaccines": "Hexavalent, Rotavirus, Pneumococcal.",
        "symptoms": "Similar to 2 months: Low-grade fever, irritability, decreased appetite for a day."
    },
    "6 Months": {
        "vaccines": "Hexavalent, Polio drops, Pneumococcal.",
        "symptoms": "Mild fever, crying more than usual, localized redness."
    },
    "9 Months": {
        "vaccines": "Meningococcal, Polio drops.",
        "symptoms": "Usually very mild. Slight fever or fatigue."
    },
    "12 Months": {
        "vaccines": "MMR (Measles, Mumps, Rubella), Polio.",
        "symptoms": "Fever or mild rash may appear 7-10 days AFTER the vaccine. Mild swelling of glands."
    },
    "18 Months": {
        "vaccines": "Booster DTP, Polio, MMR booster.",
        "symptoms": "Soreness in the arm/leg, fever, tiredness."
    }
}

# ==========================================
# 3. Calculations
# ==========================================
def calculate_expected_weight(age_years):
    return (age_years * 2) + 8

def check_weight_status(actual_weight, expected_weight):
    if actual_weight < (expected_weight * 0.85):
        return "Underweight (نحافة)", "⚠️"
    elif actual_weight > (expected_weight * 1.20):
        return "Overweight (سمنة)", "🔴"
    else:
        return "Normal Weight (طبيعي)", "✅"

# ==========================================
# 4. Streamlit UI & Navigation
# ==========================================
st.set_page_config(page_title="Child Growth Tracker", page_icon="👶", layout="centered")

# Sidebar Navigation
st.sidebar.image("https://images.unsplash.com/photo-1519689680058-324335c77eba?w=400", use_container_width=True)
st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Go to:", ["📊 Growth & Vitals", "🍽️ Tips & Nutrition", "💉 Vaccinations"])
st.sidebar.markdown("---")
st.sidebar.info("Designed for monitoring child development and health milestones.")

# ------------------------------------------
# PAGE 1: Growth & Vitals
# ------------------------------------------
if page == "📊 Growth & Vitals":
    st.title("👶 Child Growth Tracker")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        child_name = st.text_input("Child's Name:")
    with col2:
        age = st.number_input(f"Age (Years):", min_value=0.5, max_value=16.0, value=2.0, step=0.5)
    
    actual_weight = st.number_input("Current Weight (kg) [Optional]:", min_value=0.0, max_value=100.0, value=0.0, step=0.5)

    if st.button("Analyze Growth", type="primary"):
        expected_weight = calculate_expected_weight(age)
        
        st.subheader(f"Results for {child_name if child_name else 'your child'}")
        st.info(f"⚖️ **Expected Ideal Weight:** {expected_weight} kg")
        
        # BMI / Weight Status Logic
        if actual_weight > 0:
            status, icon = check_weight_status(actual_weight, expected_weight)
            st.metric(label="Weight Status", value=f"{icon} {status}", delta=f"{actual_weight - expected_weight:.1f} kg from ideal")
            
        # Motor & Psycho Milestones
        closest_age = round(age)
        if closest_age in development_data:
            st.write(f"🏃 **Motor Skills:** {development_data[closest_age]['motor']}")
            st.write(f"🧠 **Psychology:** {development_data[closest_age]['psycho']}")

# ------------------------------------------
# PAGE 2: Tips & Nutrition
# ------------------------------------------
elif page == "🍽️ Tips & Nutrition":
    st.title("🍽️ Nutrition & Parenting Tips")
    st.write("Select your child's age to get specific dietary and parenting advice.")
    
    age_selection = st.selectbox("Select Age (Years):", [1.0, 2.0, 3.0])
    
    if age_selection in development_data:
        info = development_data[age_selection]
        st.success(f"🍎 **Recommended Diet:**\n\n{info['nutrition']}")
        st.info(f"💡 **Parenting Tips:**\n\n{info['tips']}")

# ------------------------------------------
# PAGE 3: Vaccinations
# ------------------------------------------
elif page == "💉 Vaccinations":
    st.title("💉 Vaccination Schedule & Care")
    st.warning("Note: Always consult your pediatrician. Normal symptoms usually subside within 24-48 hours.")
    
    selected_month = st.selectbox("Select Vaccination Age:", list(vaccine_data.keys()))
    
    st.markdown("---")
    st.subheader(f"Schedule for {selected_month}")
    st.write(f"**Required Vaccines:** {vaccine_data[selected_month]['vaccines']}")
    
    st.error(f"🌡️ **Normal Post-Vaccine Symptoms:**\n\n{vaccine_data[selected_month]['symptoms']}")
    
    st.success("**Home Care Tips:**\n- Apply cold compresses to the injection site.\n- Offer plenty of fluids (breastmilk or formula for infants).\n- Use paracetamol only if advised by a doctor (do not use prophylactically).")
