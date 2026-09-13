import streamlit as st



# 1. Comprehensive Developmental Data (Ages 0.25 to 16)

development_data = {
    0.25: {
        "expected_height": 61,
        "experiences": "Beginning to smile at people, holding head up briefly during tummy time, tracking moving objects with eyes.",
        "activities": "Tummy time on a soft mat, dangling colorful toys, gentle talking, and singing.",
        "activity_image": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Formula milk feeding using a newborn feeding bottle.",
        "nutritional_elements": "Formula milk nutrients, Vitamin D drops as prescribed, and proper hydration.",
        "prep_method": "Prepare formula precisely according to instructions using warm sterilized water in a newborn bottle.",
        "food_image": "https://images.unsplash.com/photo-1601614349339-44ecfba3eeb4?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Night waking and adjusting to day/night cycles. Constant crying spells.",
        "tips": "How to overcome: Establish a calming bedtime routine early (dim lights, quiet sounds). Check for wet diapers or hunger before they fully wake up."
    },
    0.33: {
        "expected_height": 64,
        "experiences": "Holding head steady without support, smiling spontaneously, reaching for toys with one hand.",
        "activities": "Sitting with support, playing with rattles, interactive mirroring.",
        "activity_image": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Formula milk feeding using an anti-colic feeding bottle.",
        "nutritional_elements": "Proteins, lactose for energy, and balanced vitamins.",
        "prep_method": "Mix formula powder thoroughly in an anti-colic bottle to reduce air swallowing.",
        "food_image": "https://images.unsplash.com/photo-1594895697334-8c430e70a049?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Sleep regression (the 4-month sleep shift) and increased fussiness.",
        "tips": "How to overcome: Be patient. Use white noise machines to help them link sleep cycles. Watch for early hunger cues."
    },
    0.5: {
        "expected_height": 68,
        "experiences": "Rolling over in both directions, sitting without support, babbling consonant sounds.",
        "activities": "Reaching for hanging toys, water play during bath time, interactive peek-a-boo.",
        "activity_image": "https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Formula milk via training bottle, plus very early introduction of single-ingredient purees.",
        "nutritional_elements": "Iron, Zinc, and Vitamin D.",
        "prep_method": "Steam single vegetables thoroughly and blend into a smooth puree. Prepare formula in a separate bottle.",
        "food_image": "https://images.unsplash.com/photo-1579737976241-7667d4642ab6?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Teething pain starting and digestive changes due to solid foods.",
        "tips": "How to overcome: Provide safe, clean teething rings. Introduce one new food at a time and wait 3 days to check for allergies."
    },
    0.75: {
        "expected_height": 72,
        "experiences": "Crawling, pulling to stand, using pincer grasp (thumb and index finger).",
        "activities": "Stacking soft rings, crawling through safe tunnels, playing hiding games.",
        "activity_image": "https://images.unsplash.com/photo-1596464716127-f2a82984de30?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Formula milk in a bottle combined with mashed table foods.",
        "nutritional_elements": "Iron-rich foods, Calcium, and healthy fats.",
        "prep_method": "Mash soft-cooked vegetables and proteins. Keep formula ready in a secure feeding bottle.",
        "food_image": "https://images.unsplash.com/photo-1589139612301-38e91f0f0c05?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Stranger anxiety and separation anxiety peaking.",
        "tips": "How to overcome: Do not sneak away when leaving; say a quick, cheerful goodbye. Keep mealtimes social."
    },
    1.0: {
        "expected_height": 75,
        "experiences": "Walking with support or independently, standing alone briefly, pincer grasp mastered.",
        "activities": "Sensory play with water/sand, large building blocks, and listening to music.",
        "activity_image": "https://images.unsplash.com/photo-1587654780228-568ea467b789?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Mashed potatoes, boiled egg yolks. | Premium: Mashed avocado, pureed salmon.",
        "nutritional_elements": "Healthy fats (Omega-3), Calcium, Iron, and Vitamin C.",
        "prep_method": "Boil potatoes and eggs until very soft. Mash with a fork adding a little water.",
        "food_image": "https://images.unsplash.com/photo-1512152272829-e3139592d56f?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Resistance to nap times and increased mobility hazards.",
        "tips": "How to overcome: Child-proof the house thoroughly. Stick strictly to the daily nap schedule even if they resist."
    },
    2.0: {
        "expected_height": 87,
        "experiences": "Running, climbing furniture, explosive vocabulary growth, and asserting independence.",
        "activities": "Finger painting, running in the park, simple puzzles, and dancing.",
        "activity_image": "https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Fava beans, cottage cheese, rice, small meatballs. | Premium: Lean beef, fresh berries.",
        "nutritional_elements": "Protein for muscle growth, Fiber for digestion, and Vitamin A.",
        "prep_method": "Mash fava beans with olive oil. Bake small, bite-sized lean beef meatballs until soft.",
        "food_image": "https://images.unsplash.com/photo-1529042419736-862d41872146?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Severe temper tantrums in public and saying 'no' to everything.",
        "tips": "How to overcome: Stay calm and ignore the tantrum if they are safe. Offer simple choices (e.g., 'red shirt or blue shirt?') to satisfy their need for control."
    },
    3.0: {
        "expected_height": 95,
        "experiences": "Imaginative play begins, asking 'why' constantly, and learning toilet independence.",
        "activities": "Riding a tricycle, coloring with crayons, basic swimming water-play.",
        "activity_image": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Boiled eggs, local yogurt, sweet potatoes. | Premium: Walnuts, fresh asparagus.",
        "nutritional_elements": "Complex carbohydrates, Calcium, and Vitamin B12.",
        "prep_method": "Bake sweet potatoes until very soft, serve with yogurt. Hard-boil and slice eggs thinly.",
        "food_image": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Picky eating phases and fear of the dark or 'monsters'.",
        "tips": "How to overcome: Do not force feed; keep offering healthy options. Use a dim nightlight and check under the bed together to build security."
    },
    4.0: {
        "expected_height": 103,
        "experiences": "Cooperative play, making friends, sharing toys, and distinguishing fantasy from reality.",
        "activities": "Gymnastics basics, drawing shapes, playground climbing, hide-and-seek.",
        "activity_image": "https://images.unsplash.com/photo-1540479859555-17af45c78602?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Chickpeas, spinach, whole wheat pasta. | Premium: Baked salmon, quinoa.",
        "nutritional_elements": "Magnesium, Iron from leafy greens, and Omega-3.",
        "prep_method": "Boil whole wheat pasta and mix with finely chopped spinach and cheese.",
        "food_image": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Testing boundaries, occasional lying (blurring fantasy and reality).",
        "tips": "How to overcome: Set clear, simple rules and follow through with logical consequences. Explain the difference between a 'story' and 'the truth' gently."
    },
    5.0: {
        "expected_height": 110,
        "experiences": "School readiness phase, wanting to please friends, following rules better.",
        "activities": "Swimming lessons, basic football, arts and crafts, helping with chores.",
        "activity_image": "https://images.unsplash.com/photo-1560272564-c83b66b1ad12?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Lentil soup, cheese sandwiches, carrots. | Premium: Lean turkey cuts, organic greens.",
        "nutritional_elements": "Protein, Vitamin C for immunity, and Zinc.",
        "prep_method": "Cook red lentils with carrots and onions into a smooth soup. Cut sandwiches into shapes.",
        "food_image": "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Morning routines are chaotic; separation anxiety at school gates.",
        "tips": "How to overcome: Create a visual morning chart with pictures. Make goodbyes at school quick and positive."
    },
    6.0: {
        "expected_height": 115,
        "experiences": "First grade transition, losing baby teeth, eager to show off reading/writing.",
        "activities": "Cycling without training wheels, team sports, board games.",
        "activity_image": "https://images.unsplash.com/photo-1526685848783-500e57469a59?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Peanut butter, milk, roasted potatoes. | Premium: Almond butter, fresh fish.",
        "nutritional_elements": "Calcium and Vitamin D for adult teeth, healthy fats for focus.",
        "prep_method": "Spread peanut butter on toast. Bake fish with lemon and olive oil.",
        "food_image": "https://images.unsplash.com/photo-1484723091791-0fee1568c074?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Backtalk, defiance, and frustration with homework.",
        "tips": "How to overcome: Praise effort in schoolwork, not just final grades. Do not argue back to defiance; set limits on disrespectful tone calmly."
    },
    7.0: {
        "expected_height": 122,
        "experiences": "Growing independence, strong sense of fairness, improved logical thinking.",
        "activities": "Martial arts, reading storybooks, building complex Lego.",
        "activity_image": "https://images.unsplash.com/photo-1585366119957-e9730b6d0f60?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Whole wheat bread, white cheese, tomatoes. | Premium: Grilled salmon, mixed nuts.",
        "nutritional_elements": "Complex Carbohydrates, Antioxidants, and Protein.",
        "prep_method": "Grill salmon lightly. Serve cheese and tomato cubes with whole wheat bread.",
        "food_image": "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Fear of failure, perfectionism, and feeling things are 'unfair'.",
        "tips": "How to overcome: Share your own daily mistakes to show that failing is normal. Listen to their complaints about fairness before correcting them."
    },
    8.0: {
        "expected_height": 128,
        "experiences": "Peer groups matter, understanding complex emotions, group games with rules.",
        "activities": "Basketball, painting, swimming, learning a musical instrument.",
        "activity_image": "https://images.unsplash.com/photo-1519766304817-4f37bda74a26?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Beans, rice, seasonal greens. | Premium: Grass-fed beef, pistachios.",
        "nutritional_elements": "Iron, Vitamin E, and Fiber.",
        "prep_method": "Cook rice with mixed vegetables. Stir-fry beef strips with bell peppers.",
        "food_image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Intense screen time battles and video game attachment.",
        "tips": "How to overcome: Create a written 'screen-time contract' together. Enforce rules strictly but offer outdoor play or board games as an alternative."
    },
    9.0: {
        "expected_height": 133,
        "experiences": "Forming selective friendships, mastering hobbies and skills.",
        "activities": "Robotics/coding basics, advanced team sports, scouting.",
        "activity_image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Affordable dairy, boiled corn, lentils. | Premium: Greek yogurt, roasted chicken.",
        "nutritional_elements": "Calcium before puberty growth spurts, Lean Protein, B Vitamins.",
        "prep_method": "Boil sweet corn. Mix Greek yogurt with honey and fruits.",
        "food_image": "https://images.unsplash.com/photo-1511690743698-d9d85f2fbf38?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Dealing with mean behavior or bullying at school.",
        "tips": "How to overcome: Keep dialogue open at bedtime. Role-play how to respond to unkind peers confidently without fighting."
    },
    10.0: {
        "expected_height": 138,
        "experiences": "Approaching puberty, seeking privacy, early physical changes.",
        "activities": "Track and field, advanced arts, drama clubs, science experiments.",
        "activity_image": "https://images.unsplash.com/photo-1521199320875-10cecc0431da?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Dark leafy greens, eggs, fish. | Premium: Pecans, steak.",
        "nutritional_elements": "High Iron, Zinc, and Calcium.",
        "prep_method": "Scramble eggs with spinach. Grill steak with sweet potato mash.",
        "food_image": "https://images.unsplash.com/photo-1600891964092-4316c288032e?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Pre-puberty mood swings and sensitivity to criticism.",
        "tips": "How to overcome: Show extreme patience. Do not mock their feelings. Respect their growing need for personal space (e.g., knocking on doors)."
    },
    11.0: {
        "expected_height": 144,
        "experiences": "Puberty beginning, hormonal mood swings, high body image awareness.",
        "activities": "Competitive sports, photography, writing, tech hobbies.",
        "activity_image": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Spinach, local fruits, chicken liver. | Premium: Seafood, organic berries.",
        "nutritional_elements": "Increased calories, Iron, Folate, and Calcium.",
        "prep_method": "Sauté chicken liver with onions and garlic. Steam seafood with herbs.",
        "food_image": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Body image insecurities and comparing themselves to others.",
        "tips": "How to overcome: Focus conversations entirely on health and strength, never on weight or physical appearance. Compliment their character."
    },
    12.0: {
        "expected_height": 150,
        "experiences": "Identity exploration, growth spurts, challenging family rules.",
        "activities": "Football, swimming, creative writing, learning a language.",
        "activity_image": "https://images.unsplash.com/photo-1518659727409-f8319f3a9e33?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Canned tuna, chickpeas, rice. | Premium: Mixed nuts, protein cuts.",
        "nutritional_elements": "Protein for muscle mass, Omega-3 for brain health.",
        "prep_method": "Tuna salad with chickpeas, lemon juice, and olive oil.",
        "food_image": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Rebellion against household rules; desire to be treated like an adult.",
        "tips": "How to overcome: Stop dictating and start negotiating. Give them a sense of control by letting them choose *when* to do chores, as long as they get done."
    },
    13.0: {
        "expected_height": 156,
        "experiences": "Teenage phase, peer acceptance focus, social media, increased muscle mass.",
        "activities": "Gym/fitness basics, team sports, coding, volunteering.",
        "activity_image": "https://images.unsplash.com/photo-1526502787834-a1141bc19dfa?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Lentils, roasted chicken, whole grain bread. | Premium: Quinoa, salmon.",
        "nutritional_elements": "Maximum caloric need, Calcium, Iron, and Zinc.",
        "prep_method": "Roast chicken with root vegetables. Boil quinoa in broth.",
        "food_image": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Late-night texting, social media addiction, and sleep deprivation.",
        "tips": "How to overcome: Establish tech-free zones in bedrooms at night. Lead by example by keeping your own phone away during family time."
    },
    14.0: {
        "expected_height": 163,
        "experiences": "Abstract thinking, moral compass, high energy needs.",
        "activities": "Specialized sports, debate clubs, community service.",
        "activity_image": "https://images.unsplash.com/photo-1529686548545-095116345ecb?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Legumes, eggs, pasta, local beef. | Premium: Olive oil, steak.",
        "nutritional_elements": "Complex Carbohydrates, High Protein, Vitamin D.",
        "prep_method": "Whole wheat pasta with olive oil, garlic, tomatoes, and parmesan.",
        "food_image": "https://images.unsplash.com/photo-1555949258-eb67b1ef0ceb?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Academic stress, procrastination, and fear of exams.",
        "tips": "How to overcome: Do not add to the pressure. Help them break large study tasks into small, manageable 20-minute steps."
    },
    15.0: {
        "expected_height": 168,
        "experiences": "Exploring romantic interests, planning future high school paths.",
        "activities": "Weight training, music, leadership programs, part-time jobs.",
        "activity_image": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Fava beans, local fruits, oats. | Premium: Protein smoothies, macadamia nuts.",
        "nutritional_elements": "Balanced macros, hydration, Magnesium for muscles.",
        "prep_method": "Blend oats, milk, banana, and peanut butter for a smoothie.",
        "food_image": "https://images.unsplash.com/photo-1553530666-ba11a7da3888?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Social exclusion, peer drama, and feeling misunderstood.",
        "tips": "How to overcome: Listen more than you speak. Do not try to fix their social problems immediately; just validate their feelings."
    },
    16.0: {
        "expected_height": 173,
        "experiences": "Adult physical maturity, stronger sense of self, college/career thinking.",
        "activities": "Advanced hobbies, career workshops, driving preparation.",
        "activity_image": "https://images.unsplash.com/photo-1469041797191-50ace28483c3?auto=format&fit=crop&w=600&q=80",
        "nutrition": "Budget: Poultry, eggs, vegetables. | Premium: Premium nuts, seafood.",
        "nutritional_elements": "Adult nutritional needs, maximizing whole foods.",
        "prep_method": "Grill chicken breast and serve with a large mixed salad.",
        "food_image": "https://images.unsplash.com/photo-1534080564583-6be75777b70a?auto=format&fit=crop&w=600&q=80",
        "challenges": "Obstacle: Extreme anxiety about the future, university, and entering adulthood.",
        "tips": "How to overcome: Celebrate their independence. Assure them that it is okay not to have their whole life figured out yet."
       
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
        with r_col1:
            st.info(f"⚖️ **Expected Ideal Weight:** ~{expected_weight} kg")
            w_status, w_icon = check_weight_status(actual_weight, expected_weight)
            st.metric(label="Weight Status", value=f"{w_icon} {w_status}", delta=f"{actual_weight - expected_weight:.1f} kg")
        with r_col2:
            st.info(f"📏 **Expected Ideal Height:** ~{expected_height} cm")
            h_status, h_icon = check_height_status(actual_height, expected_height)
            st.metric(label="Height Status", value=f"{h_icon} {h_status}", delta=f"{actual_height - expected_height:.1f} cm")
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
    
    # Generate age list including 0.5 (6 months)
  
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
                    st.image(info['activity_image'], caption="Activity Idea", use_container_width=True)
            
            st.subheader("🍎 Nutrition & Elements")
            st.info(f"**Diet:** {info['nutrition']}\n\n**Key Elements Needed:** {info.get('nutritional_elements', 'Balanced diet essential for growth.')}")
            with st.expander(f"🍳 View Preparation Method & Food Ideas"):
                st.write(f"**How to prepare:** {info.get('prep_method', '')}")
                if 'food_image' in info:
                    st.image(info['food_image'], caption="Healthy Meal Inspiration", use_container_width=True)
                
       with col2:
            st.subheader("🚧 Obstacles & Challenges")
            st.error(info['challenges'])
            
            st.subheader("🛠️ How to Overcome Them")
            st.success(info['tips'])


             #Image and Recipe
            with st.expander(f"🍳 View Preparation Method & Food Ideas for {get_child_name()}"):
                st.write(f"**How to prepare:** {info.get('prep_method', 'Prepare balanced meals with safe cuts.')}")
                if 'food_image' in info:
                    st.image(info['food_image'], caption="Healthy Meal Inspiration", use_container_width=True)
                
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
