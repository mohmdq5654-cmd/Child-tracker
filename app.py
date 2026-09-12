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
        "nutrition": "Budget: Fava beans, cottage cheese, rice. | Premium: Lean beef meatballs, berries, quinoa.",
        "challenges": "Problem: Severe temper tantrums. | Solution: Stay calm, ignore the crying if safe, and redirect their attention to a new toy."
    },
    3.0: {
        "motor": "Riding a tricycle, standing on one foot for a second.",
        "psycho": "Imaginative play begins. Asks 'why' constantly.",
        "nutrition": "Budget: Boiled eggs, local yogurt, sweet potatoes. | Premium: Fresh berries, walnuts, grilled chicken.",
        "challenges": "Problem: Picky eating & Fear of the dark. | Solution: Make food shapes fun, and use a dim nightlight in their room."
    },
    4.0: {
        "motor": "Hopping on one foot, catching a bounced ball.",
        "psycho": "Cooperative play with other kids. Distinguishing fantasy from reality.",
        "nutrition": "Budget: Chickpeas, spinach, whole wheat pasta. | Premium: Avocado slices, baked salmon, organic milk.",
        "challenges": "Problem: Testing boundaries & 'Imaginary' lying. | Solution: Set clear, simple rules. Gently explain the difference between a story and the truth."
    },
    5.0: {
        "motor": "Using a fork and spoon well, drawing a person.",
        "psycho": "Wants to please friends, follows rules better.",
        "nutrition": "Budget: Lentil soup, cheese sandwiches, dates. | Premium: Lean turkey, asparagus, blueberries.",
        "challenges": "Problem: Separation anxiety at kindergarten. | Solution: Make goodbyes quick and positive. Always pick them up on time."
    },
    6.0: {
        "motor": "Skipping, riding a bicycle without training wheels.",
        "psycho": "School transition. Strong desire to learn.",
        "nutrition": "Budget: Peanut butter, milk, roasted potatoes. | Premium: Quinoa salad, fresh fish, strawberries.",
        "challenges": "Problem: Backtalk and defiance. | Solution: Don't argue back. Set limits on disrespectful tone, but praise good communication."
    },
    7.0: {
        "motor": "Tying shoelaces independently, better balance.",
        "psycho": "Growing independence. Complains about fairness.",
        "nutrition": "Budget: Whole wheat bread, white cheese, tomatoes. | Premium: Grilled salmon, mixed premium nuts.",
        "challenges": "Problem: Perfectionism & fear of failure. | Solution: Praise their 'effort' rather than the 'result'. Normalize making mistakes."
    },
    8.0: {
        "motor": "Improved coordination, fluid movements in sports.",
        "psycho": "Peer groups become very important.",
        "nutrition": "Budget: Fava beans, rice, seasonal greens. | Premium: Grass-fed meat, pistachios, mangoes.",
        "challenges": "Problem: Screen time battles. | Solution: Create a visual schedule. Offer outdoor play as a reward."
    },
    9.0: {
        "motor": "High energy, advanced hand-eye coordination.",
        "psycho": "Peer pressure starts. Forming deeper friendships.",
        "nutrition": "Budget: Beans, affordable dairy, homemade baked goods. | Premium: Greek yogurt, almonds, roasted duck.",
        "challenges": "Problem: Dealing with bullies or peer drama. | Solution: Keep open dialogue. Role-play how to respond to unkind kids."
    },
    10.0: {
        "motor": "Fine motor skills perfected, stamina increases.",
        "psycho": "Approaching puberty. Seeking more privacy.",
        "nutrition": "Budget: Dark leafy greens, lentils, affordable fish. | Premium: Pecans, premium salmon, organic veggies.",
        "challenges": "Problem: Pre-puberty mood swings. | Solution: Show patience, avoid taking outbursts personally, and respect their need for space."
    },
    11.0: {
        "motor": "Growth spurts start (especially for girls).",
        "psycho": "Mood swings begin due to hormones.",
        "nutrition": "Budget: Eggs, spinach, seasonal fruits, chicken breast. | Premium: Lean steak, walnuts, high-protein smoothies.",
        "challenges": "Problem: Body image insecurities. | Solution: Focus conversations on 'health and strength' rather than weight or appearance."
    },
    12.0: {
        "motor": "Growth spurts for boys, occasional clumsiness.",
        "psycho": "Identity exploration. May challenge rules.",
        "nutrition": "Budget: Canned tuna, chickpeas, rice, oranges. | Premium: Mixed nuts, premium protein cuts, avocado oil.",
        "challenges": "Problem: Rebellion against family rules. | Solution: Start negotiating some rules with them to give them a healthy sense of control."
    },
    13.0: {
        "motor": "Body changes become obvious, increased muscle mass.",
        "psycho": "Teenage phase. Focus on body image.",
        "nutrition": "Budget: Lentils, roasted chicken, whole grain bread. | Premium: Quinoa, fresh seafood, hazelnut.",
        "challenges": "Problem: Screen addiction & late-night texting. | Solution: Establish 'tech-free zones' (like the dinner table) and collect phones before bed."
    },
    14.0: {
        "motor": "Physical maturation continues, high energy needs.",
        "psycho": "Strong focus on peer acceptance. Abstract thinking.",
        "nutrition": "Budget: Legumes, eggs, pasta, local beef. | Premium: Steak, extra virgin olive oil, diverse berries.",
        "challenges": "Problem: Academic stress and procrastination. | Solution: Help them break large tasks into small steps. Avoid extreme pressure."
    },
    15.0: {
        "motor": "Nearing adult height (especially girls).",
        "psycho": "Exploring romantic interests, planning for the future.",
        "nutrition": "Budget: Fava beans, local fruits, potatoes. | Premium: Protein smoothies, pistachios, organic chicken.",
        "challenges": "Problem: Romantic heartbreak or social exclusion. | Solution: Listen without judgment. Never minimize their feelings by saying 'it's just a phase'."
    },
    16.0: {
        "motor": "Reaching near adult physical maturity and strength.",
        "psycho": "Seeking deeper relationships, stronger sense of self.",
        "nutrition": "Budget: Oats, affordable poultry, seasonal salads. | Premium: Seafood, assorted premium nuts, beef tenderloin.",
        "challenges": "Problem: Anxiety about the future (college/career). | Solution: Guide them gently without dictating choices. Treat them more like young adults."
    }
}

def calculate_vitals(age_years):
   
    weight = (age_years * 2) + 8
    
    height = (age_years * 6) + 77
    
    return weight, height

def calculate_feeding(weight):
    daily_intake_ml = weight * 120
    single_feed = daily_intake_ml / 8
    return daily_intake_ml , single_feed
def calculate_calories(age_years):
    calories = 1000 + (age_years * 100)
    return calories

print("Welcome to Child Growth Tracker! ")
parent_name = input("What is your name? ")
child_name = input("What is your child's name? ")
age = float(input(f"How old is {child_name} in years?): "))


weight, height = calculate_vitals(age)
daily_intake_ml , single_feed = calculate_feeding(weight)

if age > 12.0:
    print("[Note: Standard weight/height formulas vary greatly after puberty due to growth spurts.]")
print("\n=====================================")
print(f" Growth Report for {child_name}")
print("=====================================")
print(f" Weight: {weight} kg")
print(f" Height: {height} cm")
print("=====================================\n")
if age <= 2.0:
    daily_intake_ml, single_feed = calculate_feeding(weight)
    print(" [Diet: Milk Dependent]")
    print(f" Total Daily Milk: {round(daily_intake_ml)} ml")
    print(f" Single Feed (every 3 hrs): {round(single_feed)} ml")
    if age >= 0.5:
        print(" ⚠️ Note: Begin introducing pureed solid foods alongside milk.")
else:
    daily_calories = calculate_calories(age)
    print("️ [Diet: Solid Foods Dependent]")
    print(f" Expected Daily Calories: ~{round(daily_calories)} kcal")
    print(" Recommended Routine: 3 Main Meals + 2 Healthy Snacks")

if age in development_data:
    info = development_data[age]
    print("\n--- Developmental Milestones ---")
    print(f" Motor Skills: {info['motor']}")
    print(f" Challenges & Solutions: {info['challenges']}")
    print(f" Psychological (Advice for {parent_name}): {info['psycho']}")
    print(f" Nutrition: {info['nutrition']}")
else:
    closest_age = round(age)
    if closest_age in development_data:
        info = development_data[closest_age]
        print(f"\n---  Milestones (Approximate for {closest_age} years) ---")
        print(f" Motor Skills: {info['motor']}")
        print(f" Psychology (Advice for {parent_name}): {info['psycho']}")
        print(f"Challenges & Solutions: {info['challenges']}")
        print(f" Nutrition Variety:\n   {info['nutrition']}")
    else:
        print("\n[Note: Detailed developmental advice for this age is being updated.]")
    
print("=====================================\n")


