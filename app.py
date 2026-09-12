import streamlit as st


# 1. Comprehensive Developmental Data (Ages 1 to 16)

development_data = {
    1.0: {
        "motor": "Walking with support, standing alone. Activities: Safe home obstacle courses with pillows (Free) or indoor play areas (Premium).",
        "psycho": "Separation anxiety peaks. Starts imitating parents' daily tasks.",
        "nutrition": "Budget: Mashed potatoes, boiled egg yolks, seasonal local fruits. | Premium: Mashed avocado, pureed salmon.",
        "challenges": "Problem: Sleep regression & Teething. | Solution: Maintain a strict bedtime routine and use cold, clean teething rings.",
        "tips": "Engage in floor play. Read board books together daily to boost cognitive skills."
    },
    2.0: {
        "motor": "Running, climbing furniture. Activities: Chasing bubbles in the park, dancing to music (Free) or toddler gymnastics (Premium).",
        "psycho": "Independence phase ('Terrible Twos'). They will say 'no' often to assert control.",
        "nutrition": "Budget: Fava beans (well-mashed), cottage cheese, rice. | Premium: Lean beef meatballs, fresh berries.",
        "challenges": "Problem: Severe temper tantrums. | Solution: Stay calm, ensure they are safe, and ignore the crying until they calm down.",
        "tips": "It is very helpful to offer them simple choices (e.g., 'red shirt or blue shirt?') to satisfy their need for independence."
    },
    3.0: {
        "motor": "Riding a tricycle, jumping. Activities: Drawing with chalk on the sidewalk (Free) or swimming lessons (Premium).",
        "psycho": "Imaginative play begins. Asks 'why' constantly.",
        "nutrition": "Budget: Boiled eggs, local yogurt, sweet potatoes. | Premium: Walnuts, fresh asparagus.",
        "challenges": "Problem: Picky eating. | Solution: Do not force feed. Keep offering healthy options in fun shapes.",
        "tips": "Encourage independent dressing. Answer their 'why' questions patiently to build curiosity."
    },
    4.0: {
        "motor": "Hopping on one foot, catching a bounced ball. Activities: Hide and seek, building forts (Free) or martial arts basics (Premium).",
        "psycho": "Cooperative play with others. Distinguishing fantasy from reality.",
        "nutrition": "Budget: Chickpeas, spinach, whole wheat pasta. | Premium: Baked salmon, quinoa.",
        "challenges": "Problem: Testing boundaries. | Solution: Set clear, simple rules and follow through with logical consequences.",
        "tips": "Teach them how to name their feelings (e.g., 'I see you are angry')."
    },
    5.0: {
        "motor": "Using a fork and spoon well, drawing a person. Activities: Helping with safe household chores (Free) or team sports (Premium).",
        "psycho": "Wants to please friends, follows rules better.",
        "nutrition": "Budget: Lentil soup, cheese sandwiches, carrots. | Premium: Lean turkey cuts, organic greens.",
        "challenges": "Problem: Separation anxiety at school. | Solution: Make goodbyes quick and positive. Do not linger.",
        "tips": "Encourage them to tell stories to develop their vocabulary and confidence."
    },
    6.0: {
        "motor": "Skipping, riding a bicycle without training wheels. Activities: Local park tag games (Free) or structured football/ballet (Premium).",
        "psycho": "School transition. Strong desire to learn and show off new skills.",
        "nutrition": "Budget: Peanut butter, milk, roasted potatoes. | Premium: Almond butter, fresh fish.",
        "challenges": "Problem: Backtalk and defiance. | Solution: Do not argue back. Set strict limits on disrespectful tone.",
        "tips": "Praise their effort in schoolwork, not just the final grades."
    },
    7.0: {
        "motor": "Tying shoelaces independently, better balance.",
        "psycho": "Growing independence. Complains about fairness.",
        "nutrition": "Budget: Whole wheat bread, white cheese, tomatoes. | Premium: Grilled salmon, mixed nuts.",
        "challenges": "Problem: Fear of failure. | Solution: Share your own mistakes to show that failing is a normal part of learning.",
        "tips": "Give them small daily responsibilities like setting the dinner table."
    },
    8.0: {
        "motor": "Fluid movements in sports, high physical confidence.",
        "psycho": "Peer groups become very important. Likes group games.",
        "nutrition": "Budget: Beans, rice, seasonal greens. | Premium: Grass-fed meat, pistachios.",
        "challenges": "Problem: Screen time battles. | Solution: Create a 'screen-time contract'. Offer outdoor play as a better alternative.",
        "tips": "Listen to their social dramas without always trying to 'fix' them."
    },
    9.0: {
        "motor": "Advanced hand-eye coordination. Great time for skill mastery.",
        "psycho": "Peer pressure starts. Forming deeper, selective friendships.",
        "nutrition": "Budget: Affordable dairy, boiled corn, lentils. | Premium: Greek yogurt, roasted duck.",
        "challenges": "Problem: Dealing with bullies or mean behavior. | Solution: Keep open dialogue. Role-play how to respond to unkind peers.",
        "tips": "Encourage reading non-fiction books about topics they love."
    },
    10.0: {
        "motor": "Stamina increases significantly.",
        "psycho": "Approaching puberty. Seeking more privacy and independence.",
        "nutrition": "Budget: Dark leafy greens, eggs, affordable fish. | Premium: Pecans, premium steak.",
        "challenges": "Problem: Pre-puberty mood swings. | Solution: Show patience and respect their growing need for personal space.",
        "tips": "Start having gentle, open conversations about body changes."
    },
    11.0: {
        "motor": "Growth spurts start (especially for girls).",
        "psycho": "Mood swings increase due to hormonal shifts.",
        "nutrition": "Budget: Spinach, local fruits, chicken liver. | Premium: Premium seafood, organic berries.",
        "challenges": "Problem: Body image insecurities. | Solution: Focus conversations on health and strength, never on weight or appearance.",
        "tips": "Validate their feelings even if they seem dramatic to you."
    },
    12.0: {
        "motor": "Growth spurts for boys, occasional clumsiness.",
        "psycho": "Identity exploration. May challenge family rules.",
        "nutrition": "Budget: Canned tuna, chickpeas, rice. | Premium: Mixed nuts, premium protein cuts.",
        "challenges": "Problem: Rebellion against rules. | Solution: Start negotiating some rules with them to give them a sense of control.",
        "tips": "Keep family dinners a priority to maintain connection."
    },
    13.0: {
        "motor": "Body changes become obvious, increased muscle mass.",
        "psycho": "Teenage phase begins. High focus on peer acceptance.",
        "nutrition": "Budget: Lentils, roasted chicken, whole grain bread. | Premium: Quinoa, fresh salmon.",
        "challenges": "Problem: Late-night texting and sleep deprivation. | Solution: Establish tech-free zones, especially in bedrooms at night.",
        "tips": "Respect their privacy, but stay involved in their life from a distance."
    },
    14.0: {
        "motor": "High energy needs due to rapid maturation.",
        "psycho": "Abstract thinking develops. Strong moral compass.",
        "nutrition": "Budget: Legumes, eggs, pasta, local beef. | Premium: Extra virgin olive oil, premium steak.",
        "challenges": "Problem: Academic stress and procrastination. | Solution: Help them break large tasks into small, manageable steps.",
        "tips": "Encourage them to volunteer or help others to build empathy."
    },
    15.0: {
        "motor": "Nearing adult height.",
        "psycho": "Exploring romantic interests, planning for the future.",
        "nutrition": "Budget: Fava beans, local fruits, oats. | Premium: Protein smoothies, macadamia nuts.",
        "challenges": "Problem: Social exclusion or drama. | Solution: Listen without judgment. Never minimize their feelings.",
        "tips": "Treat them more like young adults. Ask for their opinions on family matters."
    },
    16.0: {
        "motor": "Reaching near adult physical maturity and strength.",
        "psycho": "Stronger sense of self. Thinking about college or careers.",
        "nutrition": "Budget: Affordable poultry, eggs, seasonal vegetables. | Premium: Assorted premium nuts, seafood.",
        "challenges": "Problem: Anxiety about the future. | Solution: Guide them gently without dictating their choices.",
        "tips": "Celebrate their independence and prepare them for real-world responsibilities."
    }
}


# 2. Vaccinations Data

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


# 3. Calculations

def calculate_expected_weight(age_years):
    return (age_years * 2) + 8

def check_weight_status(actual_weight, expected_weight):
    if actual_weight < (expected_weight * 0.85):
        return "Underweight", "⚠️"
    elif actual_weight > (expected_weight * 1.20):
        return "Overweight", "🔴"
    else:
        return "Normal Weight", "✅"


# 4. Streamlit UI & Navigation

st.set_page_config(page_title="Child Growth Tracker", page_icon="👶", layout="wide")

# Sidebar - Family Info
st.sidebar.image("https://images.unsplash.com/photo-1519689680058-324335c77eba?w=400", use_container_width=True)
st.sidebar.title("👨‍👩‍👦 Family Profile")
father_name = st.sidebar.text_input("Father's Name:")
mother_name = st.sidebar.text_input("Mother's Name:")
child_name = st.sidebar.text_input("Child's Name:")

def get_parents_address():
    if father_name and mother_name:
        return f"{father_name} and {mother_name}"
    elif father_name:
        return father_name
    elif mother_name:
        return mother_name
    else:
        return "Parents"

def get_child_name():
    return child_name if child_name else "your child"

st.sidebar.markdown("---")
st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Go to:", ["📊 Growth & Vitals", "🍽️ Tips & Nutrition", "💉 Vaccinations"])


# PAGE 1: Growth & Vitals

if page == "📊 Growth & Vitals":
    st.title("👶 Child Growth Tracker")
    st.write(f"Welcome {get_parents_address()}! Let's check how {get_child_name()} is growing today.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Child's Age (Years):", min_value=1.0, max_value=16.0, value=2.0, step=1.0)
    with col2:
        actual_weight = st.number_input("Current Weight (kg):", min_value=0.0, max_value=120.0, value=0.0, step=0.5)

    if st.button("Analyze Growth", type="primary"):
        expected_weight = calculate_expected_weight(age)
        
        st.subheader(f"Results for {get_child_name()}")
        if age > 12:
            st.warning("Note: Weight formulas vary heavily during teenage years due to growth spurts.")
            
        st.info(f"⚖️ **Expected Ideal Weight:** ~{expected_weight} kg")
        
        if actual_weight > 0:
            status, icon = check_weight_status(actual_weight, expected_weight)
            st.metric(label="Weight Status", value=f"{icon} {status}", delta=f"{actual_weight - expected_weight:.1f} kg from ideal")
            
        closest_age = round(age)
        if closest_age in development_data:
            info = development_data[closest_age]
            
            st.markdown("### 🏃 Physical & Motor Skills")
            st.write(info['motor'])
            
            st.markdown("### 🧠 Psychological State")
            st.write(info['psycho'])
            
            st.error(f"⚠️ **Common Challenge:** {info['challenges']}")
            st.success(f"💡 **Parenting Tip for {get_parents_address()}:** {info['tips']}")


# PAGE 2: Tips & Nutrition

elif page == "🍽️ Tips & Nutrition":
    st.title("🍽️ Nutrition & Parenting Tips")
    st.write(f"Dear {get_parents_address()}, select {get_child_name()}'s age to get inclusive dietary and parenting advice.")
    
    # Updated to show ages 1 to 16
    age_selection = st.selectbox("Select Age (Years):", [float(x) for x in range(1, 17)])
    
    if age_selection in development_data:
        info = development_data[age_selection]
        
        st.subheader(f"Nutrition for a {int(age_selection)}-year-old")
        st.info(f"🍎 **Dietary Options:**\n\n{info['nutrition']}")
        
        st.subheader("Parenting Advice")
        st.warning(f"🛡️ **Challenge you might face:**\n\n{info['challenges']}")
        st.success(f"💡 **How to support {get_child_name()}:**\n\n{info['tips']}")


# PAGE 3: Vaccinations

elif page == "💉 Vaccinations":
    st.title("💉 Vaccination Schedule & Care")
    st.warning("Note: Always consult your pediatrician. Normal symptoms usually subside within 24-48 hours.")
    
    selected_month = st.selectbox("Select Vaccination Age:", list(vaccine_data.keys()))
    
    st.markdown("---")
    st.subheader(f"Schedule for {selected_month}")
    st.write(f"**Required Vaccines for {get_child_name()}:** {vaccine_data[selected_month]['vaccines']}")
    
    st.error(f"🌡️ **Normal Post-Vaccine Symptoms to expect:**\n\n{vaccine_data[selected_month]['symptoms']}")
    
    st.success(f"**Home Care Tips for {get_parents_address()}:**\n- Apply cold compresses to the injection site.\n- Offer plenty of fluids.\n- Use paracetamol only if advised by a doctor.")
