st.sidebar.image("https://images.unsplash.com/photo-1519689680058-324335c77eba?w=400", use_container_width=True)
st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Go to:", ["📊 Growth & Vitals", "🍽️ Tips & Nutrition", "💉 Vaccinations"])
st.sidebar.markdown("---")
st.sidebar.info("Designed for monitoring child development and health milestones.")







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




import streamlit as st

development_data = {
    1.0: {
        "motor": "Walking with support, standing alone briefly, pincer grasp.",
        "psycho": "Separation anxiety peaks. Starts imitating parents.",
        "nutrition": "Budget: Mashed potatoes, boiled egg yolks. | Premium: Mashed avocado, pureed salmon.",
        "challenges": "Problem: Sleep regression & Teething. | Solution: Maintain a strict bedtime routine and use cold teething rings."
    },
    2.0: {
        "motor": "Running, kicking a ball forward, climbing furniture.",
        "psycho": "Independence phase ('Terrible Twos'). Say 'no' often.",
        "nutrition": "Budget: Fava beans, cottage cheese, rice. | Premium: Lean beef meatballs, berries.",
        "challenges": "Problem: Severe temper tantrums. | Solution: Stay calm, ignore the crying if safe, and redirect their attention."
    },
    3.0: {
        "motor": "Riding a tricycle, standing on one foot for a second.",
        "psycho": "Imaginative play begins. Asks 'why' constantly.",
        "nutrition": "Budget: Boiled eggs, local yogurt, sweet potatoes. | Premium: Fresh berries, walnuts.",
        "challenges": "Problem: Picky eating & Fear of the dark. | Solution: Make food shapes fun, use a dim nightlight."
    },
    4.0: {
        "motor": "Hopping on one foot, catching a bounced ball.",
        "psycho": "Cooperative play. Distinguishing fantasy from reality.",
        "nutrition": "Budget: Chickpeas, spinach, whole wheat pasta. | Premium: Avocado slices, baked salmon.",
        "challenges": "Problem: Testing boundaries. | Solution: Set clear, simple rules. Explain the difference between stories and truth."
    },
    5.0: {
        "motor": "Using a fork and spoon well, drawing a person.",
        "psycho": "Wants to please friends, follows rules better.",
        "nutrition": "Budget: Lentil soup, cheese sandwiches. | Premium: Lean turkey, asparagus.",
        "challenges": "Problem: Separation anxiety at school. | Solution: Make goodbyes quick and positive."
    },
    6.0: {
        "motor": "Skipping, riding a bicycle without training wheels.",
        "psycho": "School transition. Strong desire to learn.",
        "nutrition": "Budget: Peanut butter, milk, roasted potatoes. | Premium: Quinoa salad, fresh fish.",
        "challenges": "Problem: Backtalk and defiance. | Solution: Don't argue back. Set limits on disrespectful tone."
    },
    7.0: {
        "motor": "Tying shoelaces independently, better balance.",
        "psycho": "Growing independence. Complains about fairness.",
        "nutrition": "Budget: Whole wheat bread, white cheese, tomatoes. | Premium: Grilled salmon, mixed nuts.",
        "challenges": "Problem: Perfectionism & fear of failure. | Solution: Praise effort rather than the result."
    },
    8.0: {
        "motor": "Improved coordination, fluid movements in sports.",
        "psycho": "Peer groups become very important.",
        "nutrition": "Budget: Fava beans, rice, seasonal greens. | Premium: Grass-fed meat, pistachios.",
        "challenges": "Problem: Screen time battles. | Solution: Create a visual schedule. Offer outdoor play as a reward."
    },
    9.0: {
        "motor": "High energy, advanced hand-eye coordination.",
        "psycho": "Peer pressure starts. Forming deeper friendships.",
        "nutrition": "Budget: Beans, affordable dairy. | Premium: Greek yogurt, almonds, roasted duck.",
        "challenges": "Problem: Dealing with bullies. | Solution: Keep open dialogue. Role-play how to respond."
    },
    10.0: {
        "motor": "Fine motor skills perfected, stamina increases.",
        "psycho": "Approaching puberty. Seeking more privacy.",
        "nutrition": "Budget: Dark leafy greens, lentils, affordable fish. | Premium: Pecans, premium salmon.",
        "challenges": "Problem: Pre-puberty mood swings. | Solution: Show patience and respect their need for space."
    },
    11.0: {
        "motor": "Growth spurts start (especially for girls).",
        "psycho": "Mood swings begin due to hormones.",
        "nutrition": "Budget: Eggs, spinach, seasonal fruits. | Premium: Lean steak, walnuts.",
        "challenges": "Problem: Body image insecurities. | Solution: Focus conversations on health and strength."
    },
    12.0: {
        "motor": "Growth spurts for boys, occasional clumsiness.",
        "psycho": "Identity exploration. May challenge rules.",
        "nutrition": "Budget: Canned tuna, chickpeas, rice. | Premium: Mixed nuts, premium protein cuts.",
        "challenges": "Problem: Rebellion against family rules. | Solution: Start negotiating some rules with them."
    },
    13.0: {
        "motor": "Body changes become obvious, increased muscle mass.",
        "psycho": "Teenage phase. Focus on body image.",
        "nutrition": "Budget: Lentils, roasted chicken, whole grain bread. | Premium: Quinoa, fresh seafood.",
        "challenges": "Problem: Screen addiction & late-night texting. | Solution: Establish tech-free zones."
    },
    14.0: {
        "motor": "Physical maturation continues, high energy needs.",
        "psycho": "Strong focus on peer acceptance. Abstract thinking.",
        "nutrition": "Budget: Legumes, eggs, pasta, local beef. | Premium: Steak, extra virgin olive oil.",
        "challenges": "Problem: Academic stress and procrastination. | Solution: Help them break large tasks into small steps."
    },
    15.0: {
        "motor": "Nearing adult height (especially girls).",
        "psycho": "Exploring romantic interests, planning for the future.",
        "nutrition": "Budget: Fava beans, local fruits. | Premium: Protein smoothies, pistachios.",
        "challenges": "Problem: Social exclusion. | Solution: Listen without judgment. Never minimize their feelings."
    },
    16.0: {
        "motor": "Reaching near adult physical maturity and strength.",
        "psycho": "Seeking deeper relationships, stronger sense of self.",
        "nutrition": "Budget: Oats, affordable poultry. | Premium: Seafood, assorted premium nuts.",
        "challenges": "Problem: Anxiety about the future. | Solution: Guide them gently without dictating choices."
    }
}

accine_data = {
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


def calculate_vitals(age_years):
    weight = (age_years * 2) + 8
    height = (age_years * 6) + 77
    return weight, height
def check_weight_status(actual_weight, expected_weight):
    if actual_weight < (expected_weight * 0.85):
        return "Underweight"
    elif actual_weight > (expected_weight * 1.20):
        return "Overweight"
    else:
        return "Normal Weight"


def calculate_feeding(weight):
    daily_intake_ml = weight * 120
    single_feed = daily_intake_ml / 8
    return daily_intake_ml, single_feed

def calculate_calories(age_years):
    return 1000 + (age_years * 100)


st.set_page_config(page_title="Child Growth Tracker", page_icon="👶", layout="centered")

st.title("👶 Child Growth & Development Tracker")
st.image("https://images.unsplash.com/photo-1519689680058-324335c77eba?w=800", caption="Watching them grow, step by step", use_container_width=True)
st.write("Welcome! This tool helps you track your child's physical and psychological milestones.")
st.markdown("---")


col1, col2 = st.columns(2)
with col1:
    parent_name = st.text_input("Your Name:")
with col2:
    child_name = st.text_input("Child's Name:")

age = st.number_input(f"Child's Age in Years (e.g., 2.0, 7.5):", min_value=0.5, max_value=16.0, value=2.0, step=0.5)


if st.button("Generate Comprehensive Report", type="primary") or (parent_name and child_name):
    if parent_name and child_name:
        weight, height = calculate_vitals(age)
        
        st.markdown("---")
        st.subheader(f"📊 Report for {child_name}")
        
        if age > 12.0:
            st.warning("Note: Standard height/weight formulas vary after puberty due to growth spurts.")
        

        v_col1, v_col2 = st.columns(2)
        with v_col1:
            st.info(f"⚖️ **Expected Weight:** {weight} kg")
        with v_col2:
            st.info(f"📏 **Expected Height:** {height} cm")
            
   
        st.subheader("🍽️ Nutrition & Daily Intake")
        if age <= 2.0:
            daily_intake_ml, single_feed = calculate_feeding(weight)
            st.success(f"🍼 **Milk-Dependent Diet**\n\nTotal Daily Milk: {round(daily_intake_ml)} ml\n\nSingle Feed (every 3 hrs): {round(single_feed)} ml")
        else:
            daily_calories = calculate_calories(age)
            st.success(f"🥘 **Solid Foods Diet**\n\nExpected Daily Calories: ~{round(daily_calories)} kcal\n\nRoutine: 3 Main Meals + 2 Snacks")

        
        st.subheader("🧠 Developmental Milestones")
        closest_age = round(age)
        if closest_age in development_data:
            info = development_data[closest_age]
            st.write(f"🏃 **Motor Skills:** {info['motor']}")
            st.write(f"💡 **Psychology (Advice for {parent_name}):** {info['psycho']}")
            st.error(f"⚠️ **Challenges & Solutions:** {info['challenges']}")
            st.write(f"🍎 **Nutrition Variety:** {info['nutrition']}")
        else:
            st.info("Data for this specific age is currently being updated.")
    else:
        st.error("Please enter both your name and your child's name to generate the report.")
