import streamlit as st


# 1. Comprehensive Developmental Data (Ages 0.25 to 16)

development_data = {
    0.25: {
        "expected_height": 61,
        "experiences": "Beginning to smile, holding head up briefly, tracking objects.",
        "activities": "Tummy time on a soft mat, dangling colorful toys, singing.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Tummy+Time+(3+Months)",
        "daily_calories": "400 - 500 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Newborn Bottle",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Newborn Bottle",
        "snacks": "1. No solids yet\n2. No solids yet\n3. No solids yet",
        "sweets": "1. Strictly prohibited\n2. Strictly prohibited\n3. Strictly prohibited",
        "juices": "1. Milk only\n2. Milk only\n3. Milk only",
        "nutritional_elements": "Lactose for energy, Milk fats for brain, Vitamin D drops.",
        "prep_method": "Prepare formula using sterilized warm water strictly to manufacturer instructions. No added water or solids.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Newborn+Feeding+Bottle",
        "challenges": "Obstacle: Night waking and day/night confusion.",
        "tips": "How to overcome: Keep lights dim and voices low during night feeds."
    },
    0.33: {
        "expected_height": 64,
        "experiences": "Holding head steady, smiling spontaneously, reaching for toys.",
        "activities": "Sitting with support, playing with rattles, interactive mirroring.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Playing+with+Rattles+(4+Months)",
        "daily_calories": "500 - 600 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Anti-colic Bottle",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Anti-colic Bottle",
        "snacks": "1. No solids yet\n2. No solids yet\n3. No solids yet",
        "sweets": "1. Strictly prohibited\n2. Strictly prohibited\n3. Strictly prohibited",
        "juices": "1. Milk only\n2. Milk only\n3. Milk only",
        "nutritional_elements": "Proteins, lactose, balanced vitamins.",
        "prep_method": "Mix formula gently to avoid creating air bubbles. Keep everything strictly milk-based.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Anti-Colic+Bottle",
        "challenges": "Obstacle: The 4-month sleep regression.",
        "tips": "How to overcome: Stick to a consistent bedtime routine. Be patient."
    },
    0.5: {
        "expected_height": 68,
        "experiences": "Rolling over, sitting without support, babbling.",
        "activities": "Reaching for toys, water play during bath time.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Sitting+&+Reaching+(6+Months)",
        "daily_calories": "600 - 650 kcal",
        "breakfast": "1. Apple puree\n2. Pear puree\n3. Mashed banana with milk",
        "meals": "1. Zucchini puree\n2. Carrot puree\n3. Sweet potato mash",
        "snacks": "1. Milk feed\n2. Cucumber stick (for teething gnawing)\n3. Soft avocado mash",
        "sweets": "1. Mashed natural dates (tiny amount)\n2. Baked apple puree\n3. Mashed sweet potato",
        "juices": "1. Milk\n2. Small sips of boiled/cooled water\n3. Very diluted, unsweetened chamomile tea",
        "nutritional_elements": "Iron (crucial at this age), Zinc, Vitamin D.",
        "prep_method": "Steam vegetables/fruits without salt or sugar. Blend into a very runny puree using breastmilk/formula.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Training+Bottle+&+Vegetable+Puree",
        "challenges": "Obstacle: Teething pain starting.",
        "tips": "How to overcome: Provide cold, clean teething rings."
    },
    0.75: {
        "expected_height": 72,
        "experiences": "Crawling, pulling to stand, using pincer grasp.",
        "activities": "Stacking soft rings, crawling through tunnels.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Crawling+&+Stacking+(9+Months)",
        "daily_calories": "700 - 800 kcal",
        "breakfast": "1. Oat cereal with mashed fruit\n2. Mashed boiled egg yolk\n3. Unsweetened plain yogurt",
        "meals": "1. Soft lentil mash\n2. Minced chicken with soft rice\n3. Mashed peas & carrots",
        "snacks": "1. Soft steamed carrot sticks\n2. Sugar-free teething biscuits\n3. Banana slices",
        "sweets": "1. Yogurt with a drop of mashed dates\n2. Sugar-free banana pancakes (2 ingredients)\n3. Baked soft pear",
        "juices": "1. Water\n2. Milk\n3. Drops of fresh orange juice mixed heavily with water",
        "nutritional_elements": "Iron-rich foods, Calcium, healthy fats.",
        "prep_method": "Food can be thicker now (mashed, not pureed). Mash lentils well. Bake pancakes using only egg and banana.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Mashed+Food+Bowl+&+Bottle",
        "challenges": "Obstacle: Stranger and separation anxiety.",
        "tips": "How to overcome: Do not sneak away; say a quick, cheerful goodbye."
    },
    1.0: {
        "expected_height": 75,
        "experiences": "Walking with support, standing alone, first words.",
        "activities": "Sensory play with sand/water, large blocks.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Large+Blocks+(1+Year)",
        "daily_calories": "900 - 1000 kcal",
        "breakfast": "1. Scrambled eggs\n2. Well-mashed fava beans (Foul) with olive oil\n3. Whole wheat toast with cottage cheese",
        "meals": "1. Shredded chicken & mashed potatoes\n2. Lentil soup\n3. Soft fish fillet with rice",
        "snacks": "1. Peach slices\n2. Soft cheese cubes\n3. Hummus dip with soft bread",
        "sweets": "1. Homemade fruit yogurt\n2. Date & oat energy balls (very soft)\n3. Baked sweet potato with a pinch of cinnamon",
        "juices": "1. Fresh Guava juice (strained, no sugar)\n2. Diluted fresh apple juice\n3. Fresh strawberry blend",
        "nutritional_elements": "Omega-3, Calcium for bones, Vitamin C.",
        "prep_method": "Cut all solid food into very small pieces. Blend juices with water/milk instead of sugar. Roll dates and oats for healthy sweets.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Toddler+Plate+(Chicken,+Potatoes,+Veggies)",
        "challenges": "Obstacle: Resistance to naps.",
        "tips": "How to overcome: Stick strictly to the daily nap schedule."
    },
    2.0: {
        "expected_height": 87,
        "experiences": "Running, explosive vocabulary, asserting independence.",
        "activities": "Finger painting, running in the park, simple puzzles.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Finger+Painting+(2+Years)",
        "daily_calories": "1000 - 1400 kcal",
        "breakfast": "1. Oatmeal with berries\n2. Hard-boiled egg & cucumber\n3. Peanut butter on whole wheat toast",
        "meals": "1. Rice with small lean meatballs & peas\n2. Whole wheat pasta with hidden veggie sauce\n3. Grilled chicken strips with sweet corn",
        "snacks": "1. Cucumber sticks\n2. Whole milk yogurt\n3. Apple slices",
        "sweets": "1. Homemade banana ice cream (frozen blended bananas)\n2. Dark chocolate square (small)\n3. Carrot cake muffin (sugar-free)",
        "juices": "1. Orange & Carrot blend\n2. Fresh Watermelon juice\n3. Cold Hibiscus (Karkadeh) with a dash of honey",
        "nutritional_elements": "Fiber for digestion, Protein, Vitamin A.",
        "prep_method": "Bake meatballs until very soft. Blend veggies into pasta sauce to hide them. Use frozen bananas for healthy ice cream.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Healthy+Toddler+Meal+(Pasta+&+Meatballs)",
        "challenges": "Obstacle: Severe temper tantrums ('Terrible Twos').",
        "tips": "How to overcome: Offer simple choices (e.g., 'red cup or blue cup?')."
    },
    3.0: {
        "expected_height": 95,
        "experiences": "Imaginative play, asking 'why' constantly, toilet training.",
        "activities": "Riding a tricycle, coloring with crayons.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Tricycle+Riding+(3+Years)",
        "daily_calories": "1200 - 1400 kcal",
        "breakfast": "1. Boiled eggs & sweet potato\n2. Fava beans with tomato & cumin\n3. Cheese sandwich with cucumber",
        "meals": "1. Grilled chicken & quinoa\n2. Beef stew with carrots & potatoes\n3. Fish sticks (baked, not fried)",
        "snacks": "1. Walnuts (if safe/no allergy)\n2. Grapes (cut lengthwise)\n3. Plain milk",
        "sweets": "1. Baked apples with cinnamon\n2. Oatmeal & raisin cookies (low sugar)\n3. Rice pudding (Mahalabia) with honey",
        "juices": "1. Fresh Mango juice (in moderation)\n2. Lemon-Mint cooler\n3. Fresh Peach juice",
        "nutritional_elements": "Complex carbohydrates, Calcium, Vitamin B12.",
        "prep_method": "Cut grapes lengthwise to prevent choking. Bake fish sticks using whole wheat breadcrumbs. Sweeten Mahalabia with honey instead of sugar.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Fun-shaped+Healthy+Sandwich",
        "challenges": "Obstacle: Picky eating and fear of the dark.",
        "tips": "How to overcome: Do not force feed. Use a dim nightlight."
    },
    4.0: {
        "expected_height": 103,
        "experiences": "Cooperative play, sharing toys, distinguishing fantasy from reality.",
        "activities": "Gymnastics basics, playground climbing, hide-and-seek.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Playground+Climbing+(4+Years)",
        "daily_calories": "1200 - 1400 kcal",
        "breakfast": "1. Whole wheat pancakes (sweetened with banana)\n2. Veggie omelet\n3. Granola with yogurt",
        "meals": "1. Baked salmon with spinach pasta\n2. Lentil soup with whole grain bread\n3. Chicken shawarma (homemade on whole wheat wrap)",
        "snacks": "1. Roasted chickpeas\n2. Sliced bell peppers\n3. Cottage cheese",
        "sweets": "1. Homemade fruit popsicles\n2. Dark chocolate dipped strawberries\n3. Healthy brownies (made with sweet potato)",
        "juices": "1. Fresh Pomegranate juice\n2. Kiwi & Apple blend\n3. Fresh Cantaloupe juice",
        "nutritional_elements": "Magnesium, Iron from leafy greens, Omega-3.",
        "prep_method": "Make pancakes using banana and egg. Freeze blended fresh fruits in popsicle molds for healthy summer sweets.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Salmon+and+Spinach+Pasta",
        "challenges": "Obstacle: Testing boundaries, occasional lying.",
        "tips": "How to overcome: Set clear rules with logical consequences."
    },

    **{age: {
        "expected_height": 110 + int((age-5)*5.5),
        "experiences": "School focus, growing independence, peer social development.",
        "activities": "Team sports, swimming, martial arts, reading.",
        "activity_image": f"https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Sports+&+Reading+({int(age)}+Years)",
        "daily_calories": f"{1400 + int((age-5)*100)} - {1600 + int((age-5)*100)} kcal",
        "breakfast": "1. Protein oatmeal\n2. Avocado toast with egg\n3. Fava beans with olive oil",
        "meals": "1. Grilled chicken with roasted veggies\n2. Beef stir-fry with brown rice\n3. Tuna salad with whole wheat pasta",
        "snacks": "1. Mixed unsalted nuts\n2. Fresh fruit salad\n3. Air-popped popcorn",
        "sweets": "1. Peanut butter energy bites\n2. Greek yogurt with honey and berries\n3. Baked cinnamon bananas",
        "juices": "1. Fresh Orange juice\n2. Hibiscus (Karkadeh) tea\n3. Lemonade with mint (low sugar)",
        "nutritional_elements": "High Protein, Calcium, Iron, Vitamin C, Zinc.",
        "prep_method": "Grill or bake meats instead of frying. Use olive oil. Sweeten desserts with honey or dates naturally.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Healthy+Balanced+Plate",
        "challenges": "Obstacle: Academic stress and screen time battles.",
        "tips": "How to overcome: Create a screen-time contract and break study tasks into small steps."
    } for age in range(5, 17)}
}

development_data[13.0] = {
    "expected_height": 156,
    "experiences": "Teenage phase, peer acceptance focus, growth spurts.",
    "activities": "Gym/fitness basics, team sports, coding, volunteering.",
    "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Gym/Fitness+(13+Years)",
    "daily_calories": "2200 - 2600 kcal (High need for growth)",
    "breakfast": "1. Eggs & whole grain bread\n2. Greek yogurt with oats & chia seeds\n3. Protein smoothie (milk, banana, peanut butter)",
    "meals": "1. Quinoa & fresh salmon\n2. Lentil soup & roasted veggies\n3. Grilled steak with sweet potato mash",
    "snacks": "1. Almonds\n2. Peanut butter sandwich\n3. Hard-boiled eggs",
    "sweets": "1. Avocado chocolate mousse\n2. Dark chocolate squares (70%+ cacao)\n3. Homemade protein bars",
    "juices": "1. Beetroot & Apple juice (Iron booster)\n2. Fresh Green juice (Spinach/Apple)\n3. Cold Hibiscus",
    "nutritional_elements": "Maximum caloric need, Calcium for bone density, Iron (especially for girls), Zinc.",
    "prep_method": "Roast vegetables to enhance flavor. Blend avocado with cocoa powder and honey for a healthy, high-fat chocolate mousse.",
    "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Quinoa+&+Salmon+Bowl",
    "challenges": "Obstacle: Late-night texting, sleep deprivation.",
    "tips": "How to overcome: Establish tech-free zones in bedrooms at night."
}

# 2. Vaccinations Data

Vaccine_data = {
    "At Birth (0-1 Month)": {
        "vaccines": "BCG (Tuberculosis), Hepatitis B (1st dose), OPV (Oral Polio - Zero dose).", 
        "symptoms": "Mild fever. A small red pimple/scar will form at the BCG injection site (usually left arm) after a few weeks, which is normal."
    },
    "2 Months": {"vaccines": "Hexavalent, Rotavirus, Pneumococcal.", "symptoms": "Mild fever, sleepiness, swelling at injection site."},
    "4 Months": {"vaccines": "Hexavalent, Rotavirus, Pneumococcal.", "symptoms": "Low-grade fever, irritability, decreased appetite."},
    "6 Months": {"vaccines": "Hexavalent, Polio drops, Pneumococcal.", "symptoms": "Mild fever, localized redness."},
    "9 Months": {"vaccines": "Meningococcal, Polio drops.", "symptoms": "Usually very mild. Slight fever."},
    "12 Months": {"vaccines": "MMR, Polio.", "symptoms": "Fever or mild rash 7-10 days AFTER vaccine."},
    "18 Months": {"vaccines": "Booster DTP, Polio, MMR booster.", "symptoms": "Soreness, fever, tiredness."}

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
    st.info("Tip: For infants under 1 year, use decimals (e.g., 0.5 for 6 months, 0.8 for 9 months).")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Child's Age (Years):", min_value=0.1, max_value=16.0, value=1.0, step=0.1)
    with col2:
        actual_weight = st.number_input("Current Weight (kg):", min_value=1.0, max_value=120.0, value=10.0, step=0.5)
    with col3:
        actual_height = st.number_input("Current Height (cm):", min_value=30.0, max_value=200.0, value=75.0, step=1.0)

    if st.button("Analyze Growth", type="primary"):
        expected_weight = calculate_expected_weight(age)
        closest_age = round(age * 2) / 2 if age < 1 else round(age)
        expected_height = development_data.get(closest_age, {}).get("expected_height", 100)
        
        st.subheader(f"Results for {get_child_name()}")
        
        # Milk Calculator for Infants
        if age < 1.0:
            daily_milk = calculate_daily_milk(actual_weight if actual_weight > 0 else expected_weight)
            feed_amount = round(daily_milk / 6)
            st.success(f"🍼 **Infant Milk Requirement:** ~{daily_milk} ml per day (approx {feed_amount} ml every 4 hours).")

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

lif page == "🏃 Activities & Milestones":
    st.title("🏃 Activities, Nutrition & Milestones")
    st.write(f"Dear {get_parents_address()}, here is what to expect and how to support {get_child_name()} at this age.")
    
    age_options = [0.25, 0.33, 0.5, 0.75] + [float(x) for x in range(1, 17)]
    
    def format_age_label(x):
        if x == 0.25: return "3 Months (Infant)"
        elif x == 0.33: return "4 Months (Infant)"
        elif x == 0.5: return "6 Months (Infant)"
        elif x == 0.75: return "9 Months (Infant)"
        else: return f"{int(x)} Years"

    age_selection = st.selectbox("Select Age:", age_options, format_func=format_age_label)
    
    if age_selection in development_data:
        info = development_data[age_selection]
        
        st.markdown(f"### 🌟 What to Expect")
        st.write(info['experiences'])
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎨 Recommended Activities")
            st.success(info['activities'])
            with st.expander(f"📷 View Activity Inspiration for {get_child_name()}"):
                if 'activity_image' in info:
                    st.image(info['activity_image'], caption="Activity Idea Placeholder", use_container_width=True)
            
            st.subheader("🍎 Nutrition & Diet Plan")
            st.info(f"""
            **🔥 Daily Calories:** {info.get('daily_calories', 'Varies')}
            **🍽️ Meals per day:** {info.get('meals_per_day', '3 meals')}
            
            **🍱 Meals Variety:**
            {info.get('meals_variety', 'Balanced diet')}
            
            **🥨 Healthy Snacks:**
            {info.get('snacks', 'Fruits and nuts')}
            
            **🧪 Key Nutrients Needed:** 
            {info.get('nutritional_elements', 'Balanced diet essential for growth.')}
            """)
            
            with st.expander(f"🍳 View Preparation Method & Food Ideas"):
                st.write(f"**How to prepare:** {info.get('prep_method', 'Prepare balanced meals with safe cuts.')}")
                if 'food_image' in info:
                    st.image(info['food_image'], caption="Meal Idea Placeholder", use_container_width=True)
                
        with col2:
            st.subheader("🚧 Obstacles & Challenges")
            st.error(info['challenges'])
            
            st.subheader("🛠️ How to Overcome Them")
            st.success(info['tips'])


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
