import streamlit as st


# 1. Comprehensive Developmental Data

development_data = {

    "1 Month": {
        "expected_height": 54,
        "experiences": "Adapting to the world, recognizing parents' voices, keeping hands in tight fists.",
        "activities": "High-contrast (black and white) cards, gentle singing, tummy time on chest.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+High-Contrast+Cards",
        "daily_calories": "400 - 450 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Newborn Bottle\n- **Prep:** Prepare formula using sterilized warm water strictly to manufacturer instructions.",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Newborn Bottle\n- **Prep:** Ensure bottle is angled to keep the nipple full of milk to reduce gas.",
        "snacks": "1. No solids yet\n- **Prep:** Digestive system is not ready for solids.",
        "sweets": "1. Strictly prohibited\n- **Prep:** No sugars or sweet flavors.",
        "juices": "1. Milk only\n- **Prep:** No water or juices needed.",
        "nutritional_elements": "Lactose, Milk fats, Vitamin D drops.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Newborn+Feeding+Bottle",
        "challenges": "Obstacle: Day/night confusion.",
        "tips": "How to overcome: Keep lights dim and voices low during night feeds."
    },
    "2 Months": {
        "expected_height": 58,
        "experiences": "First social smiles, cooing sounds, following objects with eyes.",
        "activities": "Tummy time on a play mat, colorful dangling toys.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Tummy+Time",
        "daily_calories": "450 - 500 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Anti-colic Bottle\n- **Prep:** Serve milk at body temperature.",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Anti-colic Bottle\n- **Prep:** Mix formula gently to avoid creating air bubbles.",
        "snacks": "1. No solids\n- **Prep:** Milk only.",
        "sweets": "1. Strictly prohibited\n- **Prep:** Avoid completely.",
        "juices": "1. Milk only\n- **Prep:** No juices allowed.",
        "nutritional_elements": "Proteins, lactose, balanced vitamins.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Anti-Colic+Bottle",
        "challenges": "Obstacle: Evening fussiness (witching hour).",
        "tips": "How to overcome: Use gentle rocking, swaddling, and white noise."
    },
    "3 Months": {
        "expected_height": 61,
        "experiences": "Holding head up well, discovering hands, laughing.",
        "activities": "Soft rattles, mimicking baby's sounds, gentle massage.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Soft+Rattles",
        "daily_calories": "500 - 550 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Bottle\n- **Prep:** Feed in a calm environment.",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Bottle\n- **Prep:** Ensure steady milk flow.",
        "snacks": "1. No solids\n- **Prep:** Stick to milk.",
        "sweets": "1. Strictly prohibited\n- **Prep:** Avoid completely.",
        "juices": "1. Milk only\n- **Prep:** Avoid completely.",
        "nutritional_elements": "Calcium, healthy fats for brain development.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Milk+Bottle",
        "challenges": "Obstacle: Distracted eating.",
        "tips": "How to overcome: Feed in a quiet, dimly lit room."
    },
    "6 Months": {
        "expected_height": 68,
        "experiences": "Sitting without support, responding to name, early consonant babbling.",
        "activities": "Reaching for toys, water play during bath time.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Sitting+&+Reaching",
        "daily_calories": "600 - 650 kcal",
        "breakfast": "1. Apple puree\n- **Prep:** Steam and blend.\n2. Mashed banana\n- **Prep:** Mash until perfectly smooth.",
        "meals": "1. Zucchini puree\n- **Prep:** Steam without salt, blend runny.\n2. Sweet potato mash\n- **Prep:** Bake and mash with formula.",
        "snacks": "1. Milk feed\n- **Prep:** Serve at body temp.\n2. Cucumber stick (for teething)\n- **Prep:** Chill in fridge (monitor closely).",
        "sweets": "1. Mashed natural dates\n- **Prep:** Soak one date and mash a tiny amount.",
        "juices": "1. Boiled/cooled water\n- **Prep:** Small sips only.",
        "nutritional_elements": "Iron (crucial), Zinc, Vitamin D.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Vegetable+Puree",
        "challenges": "Obstacle: Teething pain and digestive changes.",
        "tips": "How to overcome: Introduce one new food every 3 days to check for allergies."
    },
    "9 Months": {
        "expected_height": 72,
        "experiences": "Pincer grasp (thumb and index), understanding 'no'.",
        "activities": "Crawling through tunnels, sorting shapes.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Crawling+Tunnels",
        "daily_calories": "750 - 800 kcal",
        "breakfast": "1. Cottage cheese\n- **Prep:** Mash pasteurized cheese.\n2. Oatmeal with fruit\n- **Prep:** Cook well with water/milk.",
        "meals": "1. Soft beef meatballs\n- **Prep:** Minced fine, baked very soft.\n2. Lentil soup\n- **Prep:** Cook lentils until they fall apart.",
        "snacks": "1. Steamed broccoli florets\n- **Prep:** Steam until soft enough to squish.\n2. Banana chunks\n- **Prep:** Cut into safe sizes.",
        "sweets": "1. Baked pear with cinnamon\n- **Prep:** Bake until tender.",
        "juices": "1. Water / Milk\n- **Prep:** Offer in a sippy cup.",
        "nutritional_elements": "Vitamin A, Iron, Calcium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Soft+Meatballs+&+Veggies",
        "challenges": "Obstacle: Refusing to be spoon-fed.",
        "tips": "How to overcome: Encourage independent feeding with safe finger foods."
    },
   
    "1 Year": {
        "expected_height": 75,
        "experiences": "Walking with support or independently, first clear words.",
        "activities": "Sensory play with sand/water, large blocks.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Large+Blocks",
        "daily_calories": "900 - 1000 kcal",
        "breakfast": "1. Scrambled eggs\n- **Prep:** Cook on low heat with olive oil.\n2. Fava beans (Foul)\n- **Prep:** Mash with olive oil & cumin.",
        "meals": "1. Shredded chicken & mashed potatoes\n- **Prep:** Boil potatoes, shred chicken safely.\n2. Soft fish fillet with rice\n- **Prep:** Ensure 100% bone-free.",
        "snacks": "1. Peach slices\n- **Prep:** Cut into thin slices.\n2. Hummus dip\n- **Prep:** Blend until smooth.",
        "sweets": "1. Date & oat energy balls\n- **Prep:** Roll soaked dates and oats.",
        "juices": "1. Fresh Guava juice\n- **Prep:** Strain seeds perfectly, no sugar.",
        "nutritional_elements": "Omega-3, Calcium, Vitamin C.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Toddler+Plate",
        "challenges": "Obstacle: Resistance to naps.",
        "tips": "How to overcome: Stick strictly to the daily nap schedule."
    },
    "3 Years": {
        "expected_height": 95,
        "experiences": "Imaginative play, asking 'why' constantly, toilet training.",
        "activities": "Riding a tricycle, coloring with crayons.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Tricycle+Riding",
        "daily_calories": "1200 - 1400 kcal",
        "breakfast": "1. Boiled eggs & sweet potato\n- **Prep:** Slice thinly.\n2. Cheese sandwich with cucumber\n- **Prep:** Use soft whole grain bread.",
        "meals": "1. Grilled chicken & quinoa\n- **Prep:** Grill chicken breast.\n2. Fish sticks (baked)\n- **Prep:** Coat in whole wheat crumbs, bake.",
        "snacks": "1. Walnuts\n- **Prep:** Crush slightly.\n2. Grapes\n- **Prep:** ALWAYS cut lengthwise.",
        "sweets": "1. Rice pudding with honey\n- **Prep:** Light honey instead of sugar.",
        "juices": "1. Lemon-Mint cooler\n- **Prep:** Blend with water and mint.",
        "nutritional_elements": "Complex carbohydrates, Calcium, Vitamin B12.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Healthy+Sandwich",
        "challenges": "Obstacle: Picky eating and fear of the dark.",
        "tips": "How to overcome: Do not force feed. Use a dim nightlight."
    },
    "6 Years": {
        "expected_height": 115,
        "experiences": "First grade transition, losing baby teeth.",
        "activities": "Cycling without training wheels, team sports.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Cycling",
        "daily_calories": "1400 - 1600 kcal",
        "breakfast": "1. Fortified cereal with milk\n- **Prep:** Serve cold or warm.\n2. Avocado toast\n- **Prep:** Mash on whole wheat bread.",
        "meals": "1. Beef strips with broccoli & rice\n- **Prep:** Stir fry with light soy sauce.\n2. Lentil soup\n- **Prep:** Serve with lemon.",
        "snacks": "1. Almonds\n- **Prep:** Raw or dry roasted.\n2. Fresh fruit\n- **Prep:** Apple or pear slices.",
        "sweets": "1. Baked apples\n- **Prep:** Bake with cinnamon.\n2. Dark chocolate\n- **Prep:** Small piece.",
        "juices": "1. Lemonade with mint\n- **Prep:** Low sugar.\n2. Berry smoothie\n- **Prep:** Blend with milk.",
        "nutritional_elements": "Calcium & Vitamin D for new teeth.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Baked+Fish",
        "challenges": "Obstacle: Backtalk and frustration with homework.",
        "tips": "How to overcome: Praise effort, not just grades."
    },
    "10 Years": {
        "expected_height": 138,
        "experiences": "Approaching puberty, seeking privacy.",
        "activities": "Track and field, drama clubs, science experiments.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Science+Experiments",
        "daily_calories": "1800 - 2000 kcal",
        "breakfast": "1. Scrambled eggs with spinach\n- **Prep:** Cook together.\n2. Oatmeal\n- **Prep:** Cook with milk and fruits.",
        "meals": "1. Grilled steak & sweet potato mash\n- **Prep:** Grill steak, mash potatoes.\n2. Tuna salad\n- **Prep:** Mix with olive oil, no mayo.",
        "snacks": "1. Pecans\n- **Prep:** Raw.\n2. Boiled egg\n- **Prep:** Serve with a pinch of cumin.",
        "sweets": "1. Rice pudding\n- **Prep:** Light honey.\n2. Baked banana\n- **Prep:** Bake in oven.",
        "juices": "1. Orange & Carrot juice\n- **Prep:** Freshly squeezed.",
        "nutritional_elements": "High Iron (crucial for girls), Zinc, Calcium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Steak+&+Sweet+Potato",
        "challenges": "Obstacle: Pre-puberty mood swings.",
        "tips": "How to overcome: Respect their growing need for personal space."
    },
    "16 Years": {
        "expected_height": 173,
        "experiences": "Adult physical maturity, college/career thinking.",
        "activities": "Advanced hobbies, career workshops, driving prep.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Career+Prep",
        "daily_calories": "2400 - 3000 kcal",
        "breakfast": "1. Omelet & whole grain toast\n- **Prep:** Add veggies to omelet.\n2. Protein oats\n- **Prep:** Add peanut butter.",
        "meals": "1. Seafood & large mixed salad\n- **Prep:** Teach them to cook their own healthy meals.\n2. Beef stir-fry\n- **Prep:** Use colorful bell peppers.",
        "snacks": "1. Premium nuts\n- **Prep:** Keep unsalted.\n2. Greek yogurt\n- **Prep:** Top with berries.",
        "sweets": "1. Fruit salad\n- **Prep:** Fresh seasonal fruits.\n2. Healthy oat cookies\n- **Prep:** Bake with minimal sugar.",
        "juices": "1. Lemon-Mint\n- **Prep:** Low sugar.\n2. Fresh juices\n- **Prep:** No added sugars.",
        "nutritional_elements": "Adult nutritional needs, limiting processed sugars.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Large+Mixed+Salad",
        "challenges": "Obstacle: Anxiety about the future and exams.",
        "tips": "How to overcome: Assure them that it is okay not to have life fully figured out yet."
    }
}

# Add missing intermediate years automatically to prevent errors if selected
for age in range(4, 16):
    if f"{age} Years" not in development_data and age not in [6, 10]:
        development_data[f"{age} Years"] = development_data["6 Years"].copy()


# 2. Vaccinations Data

vaccine_data = {
    "At Birth (0-1 Month)": {
        "vaccines": "BCG (Tuberculosis), Hepatitis B (1st dose), OPV (Oral Polio - Zero dose).", 
        "symptoms": "Mild fever. A small red pimple/scar will form at the BCG injection site after a few weeks."
    },
    "2 Months": {"vaccines": "Hexavalent, Rotavirus, Pneumococcal.", "symptoms": "Mild fever, sleepiness, swelling at injection site."},
    "4 Months": {"vaccines": "Hexavalent, Rotavirus, Pneumococcal.", "symptoms": "Low-grade fever, irritability, decreased appetite."},
    "6 Months": {"vaccines": "Hexavalent, Polio drops, Pneumococcal.", "symptoms": "Mild fever, localized redness."},
    "9 Months": {"vaccines": "Meningococcal, Polio drops.", "symptoms": "Usually very mild. Slight fever."},
    "12 Months": {"vaccines": "MMR, Polio.", "symptoms": "Fever or mild rash 7-10 days AFTER vaccine."},
    "18 Months": {"vaccines": "Booster DTP, Polio, MMR booster.", "symptoms": "Soreness, fever, tiredness."}
}


# 3. Calculations

def calculate_expected_weight(age_years):
    if age_years < 1.0:
        age_months = age_years * 12
        return round((age_months + 9) / 2, 1)
    elif age_years <= 6.0:
        return round((age_years * 2) + 8, 1)
    else:
        return round(((age_years * 7) - 5) / 2, 1)

def check_weight_status(actual_weight, expected_weight):
    if actual_weight < (expected_weight * 0.85): return "Underweight", "⚠️"
    elif actual_weight > (expected_weight * 1.20): return "Overweight", "🔴"
    else: return "Normal Weight", "✅"

def check_height_status(actual_height, expected_height):
    if actual_height < (expected_height * 0.95): return "Shorter than average", "⬇️"
    elif actual_height > (expected_height * 1.05): return "Taller than average", "⬆️"
    else: return "Normal Height", "✅"

def calculate_daily_milk(weight_kg):
    return round(weight_kg * 150)


# 4. Streamlit Configuration & State

st.set_page_config(page_title="Child Growth Tracker", page_icon="👶", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS
st.markdown("""
<style>
    /* Hide the sidebar */
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    /* CSS for the Wheel Buttons */
    .wheel-btn button {
        width: 200px !important;
        height: 200px !important;
        border-radius: 50% !important;
        border: 4px solid #4CAF50 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #333333 !important;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.3s ease 0s !important;
        margin: 10px auto !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        white-space: pre-wrap !important; 
    }
    .wheel-btn button:hover {
        background-color: #4CAF50 !important;
        color: #ffffff !important;
        transform: translateY(-7px) scale(1.05) !important;
        box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4) !important;
    }
</style>
""", unsafe_allow_html=True)

#  Session State
if 'page_state' not in st.session_state: st.session_state.page_state = "Setup"
if 'parent_name' not in st.session_state: st.session_state.parent_name = ""
if 'child_name' not in st.session_state: st.session_state.child_name = ""

def navigate(page_name):
    st.session_state.page_state = page_name


# 5. Routing Logic (The App Flow)



if st.session_state.page_state == "Setup":
    st.title("👶 Welcome to Child Growth Tracker")
    st.write("Let's personalize your experience. Please enter your details:")
    st.markdown("---")
    
    parent = st.text_input("Enter your name (Parent):", value=st.session_state.parent_name)
    child = st.text_input("Enter your baby's name:", value=st.session_state.child_name)
    
    if st.button("🚀 Enter Dashboard"):
        if parent and child:
            st.session_state.parent_name = parent
            st.session_state.child_name = child
            navigate("Wheel")
            st.rerun()
        else:
            st.error("Please enter both names to continue.")

#  MAIN WHEEL 
elif st.session_state.page_state == "Wheel":
    st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>👋 Welcome {st.session_state.parent_name} & Baby {st.session_state.child_name}! 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Choose an option from the wheel below:</h3><br><br>", unsafe_allow_html=True)
    
    # 2x2 Grid for the "Wheel" layout
    col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
    
    with col2:
        st.markdown('<div class="wheel-btn">', unsafe_allow_html=True)
        st.button("📊\nGrowth & Vitals", on_click=navigate, args=("Growth",), key="btn_growth")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="wheel-btn">', unsafe_allow_html=True)
        st.button("💉\nVaccinations", on_click=navigate, args=("Vaccinations",), key="btn_vax")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="wheel-btn">', unsafe_allow_html=True)
        st.button("🏃\nDiet & Activities", on_click=navigate, args=("Activities",), key="btn_act")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="wheel-btn">', unsafe_allow_html=True)
        st.button("👤\nEdit Profile", on_click=navigate, args=("Setup",), key="btn_prof")
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 3: GROWTH & VITALS ---
elif st.session_state.page_state == "Growth":
    st.button("🔙 Back to Main Wheel", on_click=navigate, args=("Wheel",))
    st.markdown("---")
    
    st.title("📊 Growth & Vitals Tracker")
    st.info("Tip: For infants under 1 year, use decimals (e.g., 0.5 for 6 months).")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Child's Age (Years):", min_value=0.1, max_value=16.0, value=1.0, step=0.1)
    with col2:
        actual_weight = st.number_input("Current Weight (kg):", min_value=1.0, max_value=120.0, value=10.0, step=0.5)
    with col3:
        actual_height = st.number_input("Current Height (cm):", min_value=30.0, max_value=200.0, value=75.0, step=1.0)

    if st.button("Analyze Growth", type="primary"):
        expected_weight = calculate_expected_weight(age)
        
        # Determine expected height based on age matching
        if age < 1.0:
            months = round(age * 12)
            dict_key = f"{months} Month" if months == 1 else f"{months} Months"
        else:
            years = round(age)
            dict_key = f"{years} Year" if years == 1 else f"{years} Years"
            
        expected_height = development_data.get(dict_key, {}).get("expected_height", 100)
        
        st.subheader(f"Results for {st.session_state.child_name}")
        
        if age < 1.0:
            daily_milk = calculate_daily_milk(actual_weight if actual_weight > 0 else expected_weight)
            feed_amount = round(daily_milk / 6)
            st.success(f"🍼 **Infant Milk Requirement:** ~{daily_milk} ml per day (approx {feed_amount} ml every 4 hours).")

        if age > 12:
            st.warning("Note: Weight and height formulas vary heavily during teenage years due to growth spurts.")
            
        r_col1, r_col2 = st.columns(2)
        with r_col1:
            st.info(f"⚖️ **Expected Ideal Weight:** ~{expected_weight} kg")
            w_status, w_icon = check_weight_status(actual_weight, expected_weight)
            st.metric(label="Weight Status", value=f"{w_icon} {w_status}", delta=f"{actual_weight - expected_weight:.1f} kg")
        with r_col2:
            st.info(f"📏 **Expected Ideal Height:** ~{expected_height} cm")
            h_status, h_icon = check_height_status(actual_height, expected_height)
            st.metric(label="Height Status", value=f"{h_icon} {h_status}", delta=f"{actual_height - expected_height:.1f} cm")

#  ACTIVITIES & DIET 
elif st.session_state.page_state == "Activities":
    st.button("🔙 Back to Main Wheel", on_click=navigate, args=("Wheel",))
    st.markdown("---")
    
    st.title("🏃 Activities, Comprehensive Diet & Milestones")
    
    # Generate clean list of ages (1-11 Months, then 1-16 Years)
    age_options = [f"{m} Month" if m == 1 else f"{m} Months" for m in range(1, 12)]
    age_options += [f"{y} Year" if y == 1 else f"{y} Years" for y in range(1, 17)]
    
    age_selection = st.selectbox("Select Age:", age_options)
    
    # Use fallback to 6 Years if intermediate year is missing in dictionary
    data_key = age_selection if age_selection in development_data else "6 Years"
    info = development_data[data_key]
        
    st.markdown(f"### 🌟 What to Expect")
    st.write(info['experiences'])
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎨 Recommended Activities")
        st.success(info['activities'])
        with st.expander(f"📷 View Activity Inspiration"):
            if 'activity_image' in info:
                st.image(info['activity_image'], use_container_width=True)
        
        st.subheader("🍎 Clinical Nutrition & Diet Plan")
        st.info(f"**🔥 Daily Calories:** {info.get('daily_calories', 'Varies')}")
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍳 Breakfast", "🍲 Main Meals", "🥨 Snacks", "🧁 Sweets", "🧃 Drinks"])
        
        with tab1:
            st.write(info.get('breakfast', 'Balanced breakfast'))
        with tab2:
            st.write(info.get('meals', 'Balanced meals'))
        with tab3:
            st.write(info.get('snacks', 'Healthy snacks'))
        with tab4:
            st.write(info.get('sweets', 'Natural sweets'))
        with tab5:
            st.write(info.get('juices', 'Water and Milk'))
            if "Month" in age_selection:
                st.error("⚠️ Medical Note: Juices and added sugars are strictly prohibited for infants under 1 year.")

        st.markdown(f"**🧪 Key Nutrients Needed:** {info.get('nutritional_elements', '')}")
        with st.expander(f"👩‍🍳 View Food Ideas & Inspiration"):
            if 'food_image' in info:
                st.image(info['food_image'], use_container_width=True)
            
    with col2:
        st.subheader("🚧 Obstacles & Challenges")
        st.error(info['challenges'])
        st.subheader("🛠️ How to Overcome Them")
        st.success(info['tips'])

# VACCINATIONS 
elif st.session_state.page_state == "Vaccinations":
    st.button("🔙 Back to Main Wheel", on_click=navigate, args=("Wheel",))
    st.markdown("---")
    
    st.title("💉 Vaccination Schedule & Care")
    st.warning("Note: Always consult your pediatrician. Normal symptoms usually subside within 24-48 hours.")
    
    selected_month = st.selectbox("Select Vaccination Age:", list(vaccine_data.keys()))
    
    st.subheader(f"Schedule for {selected_month}")
    st.write(f"**Required Vaccines for {st.session_state.child_name}:** {vaccine_data[selected_month]['vaccines']}")
    
    st.error(f"🌡️ **Normal Post-Vaccine Symptoms to expect:**\n\n{vaccine_data[selected_month]['symptoms']}")
    st.success(f"**Home Care Tips for {st.session_state.parent_name}:**\n- Apply cold compresses to the injection site.\n- Offer plenty of fluids.\n- Use paracetamol only if advised by a doctor.")
