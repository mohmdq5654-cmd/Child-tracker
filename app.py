import streamlit as st


# 1. Comprehensive Developmental Data (Ages 1 to 16)

development_data = {
    1.0: {
        "expected_height": 75,
        "experiences": "Transitioning from baby to toddler. Rapid physical growth and beginning to understand simple words. They are exploring their environment with all their senses.",
        "activities": "Sensory play (water/sand), large building blocks, listening to music, and rolling a soft ball.",
        "nutrition": "Budget: Mashed potatoes, boiled egg yolks, seasonal fruits. | Premium: Mashed avocado, pureed salmon.",
        "challenges": "Sleep regression & Teething.",
        "tips": "Engage in floor play. Read board books together daily to boost cognitive skills."
    },
    2.0: {
        "expected_height": 87,
        "experiences": "The 'Terrible Twos'. A huge explosion in vocabulary and a strong desire for independence. Emotions are very big and hard to control.",
        "activities": "Finger painting, running in the park, simple puzzles, and dancing to songs.",
        "nutrition": "Budget: Fava beans, cottage cheese, rice, small meatballs. | Premium: Lean beef, fresh berries.",
        "challenges": "Severe temper tantrums and saying 'no' to everything.",
        "tips": "Offer them simple choices (e.g., 'red shirt or blue shirt?') to satisfy their need for control."
    },
    3.0: {
        "expected_height": 95,
        "experiences": "Imaginative play begins. They start making up stories, asking 'why' constantly, and learning to use the toilet independently.",
        "activities": "Riding a tricycle, coloring with crayons, basic swimming water-play, and playing with clay.",
        "nutrition": "Budget: Boiled eggs, local yogurt, sweet potatoes. | Premium: Walnuts, fresh asparagus.",
        "challenges": "Picky eating and fear of the dark.",
        "tips": "Encourage independent dressing. Answer their 'why' questions patiently."
    },
    4.0: {
        "expected_height": 103,
        "experiences": "Cooperative play begins. They start making friends, sharing toys, and distinguishing fantasy from reality.",
        "activities": "Gymnastics basics, drawing shapes, playground climbing, and hide-and-seek.",
        "nutrition": "Budget: Chickpeas, spinach, whole wheat pasta. | Premium: Baked salmon, quinoa.",
        "challenges": "Testing boundaries and occasional lying (fantasy vs reality).",
        "tips": "Set clear, simple rules and follow through with logical consequences."
    },
    5.0: {
        "expected_height": 110,
        "experiences": "School readiness phase. They want to please friends, follow rules better, and show a strong desire to learn.",
        "activities": "Swimming lessons, basic football, arts and crafts, and helping with simple house chores.",
        "nutrition": "Budget: Lentil soup, cheese sandwiches, carrots. | Premium: Lean turkey cuts, organic greens.",
        "challenges": "Separation anxiety at school gates.",
        "tips": "Encourage them to tell stories to develop their vocabulary and confidence."
    },
    6.0: {
        "expected_height": 115,
        "experiences": "First grade transition. Losing baby teeth. They are eager to show off new skills like reading and writing.",
        "activities": "Cycling (without training wheels), team sports like football/ballet, and board games.",
        "nutrition": "Budget: Peanut butter, milk, roasted potatoes. | Premium: Almond butter, fresh fish.",
        "challenges": "Backtalk and defiance as they test new school behaviors at home.",
        "tips": "Praise their effort in schoolwork, not just the final grades."
    },
    7.0: {
        "expected_height": 122,
        "experiences": "Growing independence and a strong sense of fairness. They might complain if things feel 'unfair'. Logical thinking improves.",
        "activities": "Martial arts (Karate/Taekwondo), reading storybooks, building complex Lego models.",
        "nutrition": "Budget: Whole wheat bread, white cheese, tomatoes. | Premium: Grilled salmon, mixed nuts.",
        "challenges": "Fear of failure and perfectionism.",
        "tips": "Share your own mistakes to show that failing is a normal part of learning."
    },
    8.0: {
        "expected_height": 128,
        "experiences": "Peer groups become very important. They understand complex emotions and enjoy group games with rules.",
        "activities": "Basketball, painting, swimming, and learning a musical instrument.",
        "nutrition": "Budget: Beans, rice, seasonal greens. | Premium: Grass-fed meat, pistachios.",
        "challenges": "Screen time battles and video game attachment.",
        "tips": "Create a 'screen-time contract'. Offer outdoor play as a better alternative."
    },
    9.0: {
        "expected_height": 133,
        "experiences": "Forming deeper, selective friendships. They want to master skills and hobbies. Independence increases.",
        "activities": "Robotics/coding for kids, advanced team sports, and scouting.",
        "nutrition": "Budget: Affordable dairy, boiled corn, lentils. | Premium: Greek yogurt, roasted duck.",
        "challenges": "Dealing with bullies or mean behavior at school.",
        "tips": "Keep open dialogue. Role-play how to respond to unkind peers."
    },
    10.0: {
        "expected_height": 138,
        "experiences": "Approaching puberty. Seeking more privacy and showing early signs of physical changes. Friendships are crucial.",
        "activities": "Track and field, advanced arts, drama clubs, and science experiments.",
        "nutrition": "Budget: Dark leafy greens, eggs, affordable fish. | Premium: Pecans, premium steak.",
        "challenges": "Pre-puberty mood swings.",
        "tips": "Show patience and respect their growing need for personal space."
    },
    11.0: {
        "expected_height": 144,
        "experiences": "Puberty usually begins (especially for girls). Hormonal shifts cause mood swings. High awareness of body image.",
        "activities": "Competitive sports, photography, writing, and tech hobbies.",
        "nutrition": "Budget: Spinach, local fruits, chicken liver. | Premium: Premium seafood, organic berries.",
        "challenges": "Body image insecurities.",
        "tips": "Focus conversations on health and strength, never on weight or appearance."
    },
    12.0: {
        "expected_height": 150,
        "experiences": "Identity exploration. Boys begin growth spurts. They may challenge family rules to assert their identity.",
        "activities": "Football, swimming, creative writing, and learning a new language.",
        "nutrition": "Budget: Canned tuna, chickpeas, rice. | Premium: Mixed nuts, premium protein cuts.",
        "challenges": "Rebellion against rules.",
        "tips": "Start negotiating some rules with them to give them a sense of control."
    },
    13.0: {
        "expected_height": 156,
        "experiences": "Teenage phase begins. High focus on peer acceptance, social media, and body changes. Increased muscle mass.",
        "activities": "Gym/fitness basics, team sports, coding, and volunteering.",
        "nutrition": "Budget: Lentils, roasted chicken, whole grain bread. | Premium: Quinoa, fresh salmon.",
        "challenges": "Late-night texting and sleep deprivation.",
        "tips": "Establish tech-free zones, especially in bedrooms at night."
    },
    14.0: {
        "expected_height": 163,
        "experiences": "Abstract thinking develops. Strong moral compass. High energy needs due to rapid maturation.",
        "activities": "Specialized sports, arts, community service, and debate clubs.",
        "nutrition": "Budget: Legumes, eggs, pasta, local beef. | Premium: Extra virgin olive oil, premium steak.",
        "challenges": "Academic stress and procrastination.",
        "tips": "Help them break large tasks into small, manageable steps."
    },
    15.0: {
        "expected_height": 168,
        "experiences": "Exploring romantic interests, planning for the future (high school paths). Nearing adult height.",
        "activities": "Weight training, music, leadership programs, and part-time jobs (if applicable).",
        "nutrition": "Budget: Fava beans, local fruits, oats. | Premium: Protein smoothies, macadamia nuts.",
        "challenges": "Social exclusion or peer drama.",
        "tips": "Treat them more like young adults. Ask for their opinions on family matters."
    },
    16.0: {
        "expected_height": 173,
        "experiences": "Reaching near adult physical maturity. Stronger sense of self. Thinking heavily about college or careers.",
        "activities": "Advanced hobbies, career-oriented workshops, driving (where applicable).",
        "nutrition": "Budget: Affordable poultry, eggs, seasonal vegetables. | Premium: Assorted premium nuts, seafood.",
        "challenges": "Anxiety about the future and exams.",
        "tips": "Celebrate their independence and prepare them for real-world responsibilities."
    }
}


# 2. Vaccinations Data

vaccine_data = {
    "2 Months": {"vaccines": "Hexavalent, Rotavirus, Pneumococcal.", "symptoms": "Mild fever, sleepiness, swelling at injection site."},
    "4 Months": {"vaccines": "Hexavalent, Rotavirus, Pneumococcal.", "symptoms": "Low-grade fever, irritability, decreased appetite."},
    "6 Months": {"vaccines": "Hexavalent, Polio drops, Pneumococcal.", "symptoms": "Mild fever, localized redness."},
    "9 Months": {"vaccines": "Meningococcal, Polio drops.", "symptoms": "Usually very mild. Slight fever."},
    "12 Months": {"vaccines": "MMR, Polio.", "symptoms": "Fever or mild rash 7-10 days AFTER vaccine."},
    "18 Months": {"vaccines": "Booster DTP, Polio, MMR booster.", "symptoms": "Soreness, fever, tiredness."}
}


# 3. Calculations

def calculate_expected_weight(age_years):
    return (age_years * 2) + 8

def check_weight_status(actual_weight, expected_weight):
    if actual_weight < (expected_weight * 0.85): return "Underweight", "⚠️"
    elif actual_weight > (expected_weight * 1.20): return "Overweight", "🔴"
    else: return "Normal Weight", "✅"

def check_height_status(actual_height, expected_height):
    if actual_height < (expected_height * 0.95): return "Shorter than average", "⬇️"
    elif actual_height > (expected_height * 1.05): return "Taller than average", "⬆️"
    else: return "Normal Height", "✅"


# 4. Streamlit UI & Navigation

st.set_page_config(page_title="Child Growth Tracker", page_icon="👶", layout="wide")

# session state for persistent data
if 'father_name' not in st.session_state: st.session_state.father_name = ""
if 'mother_name' not in st.session_state: st.session_state.mother_name = ""
if 'child_name' not in st.session_state: st.session_state.child_name = ""

def get_parents_address():
    f = st.session_state.father_name
    m = st.session_state.mother_name
    if f and m: return f"{f} and {m}"
    elif f: return f
    elif m: return m
    else: return "Parents"

def get_child_name():
    c = st.session_state.child_name
    return c if c else "your child"

# Sidebar Navigation
st.sidebar.image("https://images.unsplash.com/photo-1519689680058-324335c77eba?w=400", use_container_width=True)
st.sidebar.title("📌 Menu")
page = st.sidebar.radio("Go to:", ["👤 Profile Setup", "📊 Growth & Vitals", "🏃 Activities & Milestones", "💉 Vaccinations"])


# PAGE 1: Profile Setup

if page == "👤 Profile Setup":
    st.title("👤 Family Profile Setup")
    st.write("Welcome! Please enter your details below. We will remember them as you navigate the app.")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.father_name = st.text_input("Father's Name:", value=st.session_state.father_name)
        st.session_state.mother_name = st.text_input("Mother's Name:", value=st.session_state.mother_name)
    with col2:
        st.session_state.child_name = st.text_input("Child's Name:", value=st.session_state.child_name)
        
    if st.session_state.father_name or st.session_state.mother_name or st.session_state.child_name:
        st.success("Profile updated! You can now navigate to other pages from the menu on the left.")


# PAGE 2: Growth & Vitals
elif page == "📊 Growth & Vitals":
    st.title("📊 Growth & Vitals Tracker")
    st.write(f"Welcome {get_parents_address()}! Let's check {get_child_name()}'s physical growth.")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Child's Age (Years):", min_value=1.0, max_value=16.0, value=2.0, step=1.0)
    with col2:
        actual_weight = st.number_input("Current Weight (kg):", min_value=1.0, max_value=120.0, value=12.0, step=0.5)
    with col3:
        actual_height = st.number_input("Current Height (cm):", min_value=40.0, max_value=200.0, value=87.0, step=1.0)

    if st.button("Analyze Growth", type="primary"):
        expected_weight = calculate_expected_weight(age)
        
        closest_age = round(age)
        expected_height = development_data.get(closest_age, {}).get("expected_height", 100)
        
        st.subheader(f"Results for {get_child_name()}")
        if age > 12:
            st.warning("Note: Weight and height formulas vary heavily during teenage years due to growth spurts.")
            
        r_col1, r_col2 = st.columns(2)
        
        # Weight Analysis
        with r_col1:
            st.info(f"⚖️ **Expected Ideal Weight:** ~{expected_weight} kg")
            w_status, w_icon = check_weight_status(actual_weight, expected_weight)
            st.metric(label="Weight Status", value=f"{w_icon} {w_status}", delta=f"{actual_weight - expected_weight:.1f} kg from ideal")
        
        # Height Analysis
        with r_col2:
            st.info(f"📏 **Expected Ideal Height:** ~{expected_height} cm")
            h_status, h_icon = check_height_status(actual_height, expected_height)
            st.metric(label="Height Status", value=f"{h_icon} {h_status}", delta=f"{actual_height - expected_height:.1f} cm from ideal")


# PAGE 3: Activities & Milestones

elif page == "🏃 Activities & Milestones":
    st.title("🏃 Activities, Nutrition & Milestones")
    st.write(f"Dear {get_parents_address()}, here is what to expect and how to support {get_child_name()} at this age.")
    
    age_selection = st.selectbox("Select Age (Years):", [float(x) for x in range(1, 17)])
    
    if age_selection in development_data:
        info = development_data[age_selection]
        
        st.markdown(f"### 🌟 What to Expect at Age {int(age_selection)}")
        st.write(info['experiences'])
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎨 Recommended Activities")
            st.success(info['activities'])
            
            st.subheader("🍎 Nutrition Options")
            st.info(info['nutrition'])
            
        with col2:
            st.subheader("🛡️ Common Challenge")
            st.error(info['challenges'])
            
            st.subheader("💡 Parenting Advice")
            st.warning(info['tips'])


# PAGE 4: Vaccinations

elif page == "💉 Vaccinations":
    st.title("💉 Vaccination Schedule & Care")
    st.warning("Note: Always consult your pediatrician. Normal symptoms usually subside within 24-48 hours.")
    
    selected_month = st.selectbox("Select Vaccination Age:", list(vaccine_data.keys()))
    
    st.markdown("---")
    st.subheader(f"Schedule for {selected_month}")
    st.write(f"**Required Vaccines for {get_child_name()}:** {vaccine_data[selected_month]['vaccines']}")
    
    st.error(f"🌡️ **Normal Post-Vaccine Symptoms to expect:**\n\n{vaccine_data[selected_month]['symptoms']}")
    
    st.success(f"**Home Care Tips for {get_parents_address()}:**\n- Apply cold compresses to the injection site.\n- Offer plenty of fluids.\n- Use paracetamol only if advised by a doctor.")
