import streamlit as st


# 1. Comprehensive Developmental Data 


development_data = {
    #  INFANTS 
    "1 Month": {
        "expected_height": 54,
        "experiences": "Adapting to the world, recognizing parents' voices, keeping hands in tight fists.",
        "activities": "High-contrast (black and white) cards, gentle singing, tummy time on chest.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+High-Contrast+Cards",
        "daily_calories": "400 - 450 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Newborn Bottle",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Newborn Bottle",
        "snacks": "1. No solids yet\n2. No solids yet\n3. No solids yet",
        "sweets": "1. Strictly prohibited\n2. Strictly prohibited\n3. Strictly prohibited",
        "juices": "1. Milk only\n2. Milk only\n3. Milk only",
        "nutritional_elements": "Lactose, Milk fats, Vitamin D drops.",
        "prep_method": "Prepare formula using sterilized warm water. Strictly milk only.",
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
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Anti-colic Bottle",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Anti-colic Bottle",
        "snacks": "1. No solids\n2. No solids\n3. No solids",
        "sweets": "1. Strictly prohibited\n2. Strictly prohibited\n3. Strictly prohibited",
        "juices": "1. Milk only\n2. Milk only\n3. Milk only",
        "nutritional_elements": "Proteins, lactose, balanced vitamins.",
        "prep_method": "Ensure bottle is angled to keep the nipple full of milk to reduce gas.",
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
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Bottle",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Bottle",
        "snacks": "1. No solids\n2. No solids\n3. No solids",
        "sweets": "1. Strictly prohibited\n2. Strictly prohibited\n3. Strictly prohibited",
        "juices": "1. Milk only\n2. Milk only\n3. Milk only",
        "nutritional_elements": "Calcium, healthy fats for brain development.",
        "prep_method": "Keep feeding environment calm. No solids before 4-6 months.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Milk+Bottle",
        "challenges": "Obstacle: Distracted eating.",
        "tips": "How to overcome: Feed in a quiet, dimly lit room."
    },
    "4 Months": {
        "expected_height": 64,
        "experiences": "Rolling from tummy to back, grasping objects, mimicking facial expressions.",
        "activities": "Mirror play, reading large-picture books.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Mirror+Play",
        "daily_calories": "550 - 600 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Bottle",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Milk via Bottle",
        "snacks": "1. No solids\n2. No solids\n3. No solids",
        "sweets": "1. Strictly prohibited\n2. Strictly prohibited\n3. Strictly prohibited",
        "juices": "1. Milk only\n2. Milk only\n3. Milk only",
        "nutritional_elements": "Iron stores start depleting; rely on fortified formula/breastmilk.",
        "prep_method": "Continue exclusive milk feeding unless pediatrician advises starting purees.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Milk+Bottle",
        "challenges": "Obstacle: 4-month sleep regression.",
        "tips": "How to overcome: Establish strong sleep associations (bath, book, bed)."
    },
    "5 Months": {
        "expected_height": 66,
        "experiences": "Sitting with support, moving objects from hand to hand.",
        "activities": "Textured fabric books, singing nursery rhymes.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Textured+Books",
        "daily_calories": "550 - 650 kcal",
        "breakfast": "1. Formula Milk\n2. Breastmilk\n3. Milk via Bottle",
        "meals": "1. Formula Milk\n2. Breastmilk\n3. Early tasting of single puree (if advised)",
        "snacks": "1. No solids\n2. No solids\n3. No solids",
        "sweets": "1. Strictly prohibited\n2. Strictly prohibited\n3. Strictly prohibited",
        "juices": "1. Milk only\n2. Milk only\n3. Milk only",
        "nutritional_elements": "Zinc, Vitamin D, Fats.",
        "prep_method": "If starting purees, boil zucchini/carrots without salt and blend into a very watery liquid.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Training+Bottle",
        "challenges": "Obstacle: Early teething signs (drooling, biting).",
        "tips": "How to overcome: Offer a clean, cold washcloth to chew on."
    },
    "6 Months": {
        "expected_height": 68,
        "experiences": "Sitting without support, responding to name, early consonant babbling.",
        "activities": "Reaching for toys, water play during bath time.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Sitting+&+Reaching",
        "daily_calories": "600 - 650 kcal",
        "breakfast": "1. Apple puree\n- **Prep:** Steam and blend.\n2. Mashed banana\n- **Prep:** Mash until smooth.\n3. Oat cereal\n- **Prep:** Cook in water.",
        "meals": "1. Zucchini puree\n- **Prep:** Steam without salt.\n2. Sweet potato mash\n- **Prep:** Bake and blend.\n3. Carrot puree\n- **Prep:** Boil and puree.",
        "snacks": "1. Milk feed\n- **Prep:** Serve at body temp.\n2. Cucumber stick (for teething)\n- **Prep:** Chill in fridge.\n3. Breastmilk/Formula",
        "sweets": "1. Mashed natural dates\n- **Prep:** Soak and mash tiny amounts.\n2. Baked pear puree\n3. Mashed sweet potato",
        "juices": "1. Boiled/cooled water\n- **Prep:** Small sips.\n2. Milk\n3. Diluted unsweetened chamomile",
        "nutritional_elements": "Iron (crucial), Zinc, Vitamin D.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Vegetable+Puree",
        "challenges": "Obstacle: Teething pain and digestive changes.",
        "tips": "How to overcome: Introduce one new food every 3 days to check for allergies."
    },
    "7 Months": {
        "expected_height": 70,
        "experiences": "Passing objects between hands easily, crawling attempts, babbling 'ba-ba'.",
        "activities": "Hiding toys under blankets (object permanence).",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Peek-a-boo+Toys",
        "daily_calories": "650 - 700 kcal",
        "breakfast": "1. Mashed boiled egg yolk\n- **Prep:** Hard-boil, remove white.\n2. Avocado mash\n- **Prep:** Mash soft avocado.\n3. Oat cereal with apple puree",
        "meals": "1. Lentil mash\n- **Prep:** Boil yellow lentils.\n2. Pea puree\n- **Prep:** Steam and blend.\n3. Mashed butternut squash",
        "snacks": "1. Steamed carrot sticks\n- **Prep:** Steam until squishy.\n2. Milk feed\n3. Unsweetened yogurt (plain)",
        "sweets": "1. Yogurt with a drop of date puree\n2. Baked apple\n3. Banana mash",
        "juices": "1. Water\n2. Milk\n3. Drop of fresh orange in water",
        "nutritional_elements": "Calcium, Iron, Vitamin C.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Mashed+Food+Bowl",
        "challenges": "Obstacle: Constipation from new solid foods.",
        "tips": "How to overcome: Offer small sips of water and pear puree."
    },
    "8 Months": {
        "expected_height": 71,
        "experiences": "Crawling, pulling to stand, pointing at objects.",
        "activities": "Stacking soft rings, playing with safe kitchen bowls.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Stacking+Rings",
        "daily_calories": "700 - 750 kcal",
        "breakfast": "1. Scrambled egg yolk\n- **Prep:** Cook with tiny olive oil.\n2. Mashed papaya\n3. Wheat cereal (iron-fortified)",
        "meals": "1. Minced chicken with soft rice\n- **Prep:** Boil and shred micro-pieces.\n2. Mashed potato & spinach\n3. Soft fish mash (no bones)",
        "snacks": "1. Teething crackers (sugar-free)\n2. Peach slices (steamed)\n3. Milk feed",
        "sweets": "1. Sugar-free banana pancake\n- **Prep:** 1 egg yolk + banana, pan-fried.\n2. Baked sweet potato\n3. Applesauce",
        "juices": "1. Water\n2. Milk\n3. Diluted fresh apple juice (drops)",
        "nutritional_elements": "Protein, Omega-3 for brain, Iron.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Minced+Chicken+&+Rice",
        "challenges": "Obstacle: Separation anxiety.",
        "tips": "How to overcome: Play peek-a-boo to teach that you come back."
    },
    "9 Months": {
        "expected_height": 72,
        "experiences": "Pincer grasp (thumb and index), understanding 'no'.",
        "activities": "Crawling through tunnels, sorting shapes.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Crawling+Tunnels",
        "daily_calories": "750 - 800 kcal",
        "breakfast": "1. Cottage cheese\n- **Prep:** Mash pasteurized cheese.\n2. Oatmeal with fruit\n3. Mashed boiled egg",
        "meals": "1. Soft beef meatballs\n- **Prep:** Minced fine, baked soft.\n2. Lentil & carrot soup\n3. Soft pasta bits with tomato",
        "snacks": "1. Steamed broccoli florets\n2. Banana chunks\n3. Yogurt",
        "sweets": "1. Date paste with yogurt\n2. Baked pear with cinnamon\n3. Soft oat balls",
        "juices": "1. Water\n2. Milk\n3. Fresh strained guava drops in water",
        "nutritional_elements": "Vitamin A, Iron, Calcium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Soft+Meatballs+&+Veggies",
        "challenges": "Obstacle: Refusing to be spoon-fed.",
        "tips": "How to overcome: Encourage independent feeding with safe finger foods."
    },
    "10 Months": {
        "expected_height": 73,
        "experiences": "Cruising along furniture, waving goodbye.",
        "activities": "Push-toys to practice walking, simple puzzles.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Push+Toys",
        "daily_calories": "800 - 850 kcal",
        "breakfast": "1. Whole wheat toast bits\n- **Prep:** Soak in milk if too hard.\n2. Scrambled eggs\n3. Fruit yogurt",
        "meals": "1. Chicken and vegetable stew\n- **Prep:** Cook until very tender.\n2. Fish and sweet potato mash\n3. Fava beans (skinless)",
        "snacks": "1. Melon slices\n2. Soft cheese cubes\n3. Milk",
        "sweets": "1. Homemade fruit popsicle\n- **Prep:** Freeze blended fruit (no sugar).\n2. Date & oat cookies (soft)\n3. Baked apple",
        "juices": "1. Water\n2. Milk\n3. Diluted carrot juice",
        "nutritional_elements": "Complex carbs, Zinc, Omega-3.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Chicken+Stew",
        "challenges": "Obstacle: Waking up standing in the crib.",
        "tips": "How to overcome: Teach them how to safely sit back down from a standing position during the day."
    },
    "11 Months": {
        "expected_height": 74,
        "experiences": "Standing alone for a few seconds, understanding simple instructions.",
        "activities": "Building blocks, reading interactive books.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Building+Blocks",
        "daily_calories": "850 - 900 kcal",
        "breakfast": "1. Pancakes (Banana & Egg)\n- **Prep:** Pan-fry in tiny butter.\n2. Foul (Fava beans) with olive oil\n3. Porridge",
        "meals": "1. Soft rice with chicken\n2. Macaroni with hidden veggie sauce\n3. Baked salmon flakes",
        "snacks": "1. Apple slices (steamed)\n2. Hummus with soft bread\n3. Cheese sticks",
        "sweets": "1. Mahalabia (Rice pudding)\n- **Prep:** Sweeten with date syrup.\n2. Fresh berries\n3. Oat & banana muffins",
        "juices": "1. Water\n2. Milk\n3. Fresh strawberry blend (diluted)",
        "nutritional_elements": "Fiber, Protein, Vitamin B.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Macaroni+&+Veggies",
        "challenges": "Obstacle: Throwing food on the floor.",
        "tips": "How to overcome: Do not react heavily. Calmly remove the plate if they persist."
    },
    
   # TODDLERS TO TEENS (1 TO 16 YEARS)
    "1 Year": {
        "expected_height": 75,
        "experiences": "Walking with support or independently, first clear words.",
        "activities": "Sensory play with sand/water, large blocks.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Large+Blocks+(1+Year)",
        "daily_calories": "900 - 1000 kcal",
        "breakfast": "1. Scrambled eggs\n- **Prep:** Cook on low heat with olive oil.\n2. Fava beans (Foul)\n- **Prep:** Mash with olive oil & cumin.\n3. Whole wheat toast with cheese",
        "meals": "1. Shredded chicken & mashed potatoes\n- **Prep:** Boil potatoes, shred chicken.\n2. Lentil soup\n3. Soft fish fillet with rice",
        "snacks": "1. Peach slices\n- **Prep:** Cut into thin slices.\n2. Soft cheese cubes\n3. Hummus dip",
        "sweets": "1. Date & oat energy balls\n- **Prep:** Roll soaked dates and oats.\n2. Homemade fruit yogurt\n3. Baked sweet potato",
        "juices": "1. Fresh Guava juice\n- **Prep:** Strain seeds, no sugar.\n2. Diluted apple juice\n3. Milk",
        "nutritional_elements": "Omega-3, Calcium, Vitamin C.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Toddler+Plate+(Chicken,+Potatoes)",
        "challenges": "Obstacle: Resistance to naps.",
        "tips": "How to overcome: Stick strictly to the daily nap schedule."
    },
    "2 Years": {
        "expected_height": 87,
        "experiences": "Running, explosive vocabulary, asserting independence ('Terrible Twos').",
        "activities": "Finger painting, running in the park, simple puzzles.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Finger+Painting+(2+Years)",
        "daily_calories": "1000 - 1400 kcal",
        "breakfast": "1. Oatmeal with berries\n- **Prep:** Cook oats in whole milk.\n2. Hard-boiled egg & cucumber\n3. Peanut butter on toast",
        "meals": "1. Rice with small lean meatballs & peas\n- **Prep:** Bake meatballs until soft.\n2. Whole wheat pasta with veggie sauce\n3. Grilled chicken strips with corn",
        "snacks": "1. Cucumber sticks\n- **Prep:** Peel and cut into sticks.\n2. Whole milk yogurt\n3. Apple slices",
        "sweets": "1. Homemade banana ice cream\n- **Prep:** Blend frozen bananas.\n2. Dark chocolate square (small)\n3. Carrot cake muffin (sugar-free)",
        "juices": "1. Orange & Carrot blend\n- **Prep:** Juice fresh.\n2. Watermelon juice\n3. Cold Hibiscus with honey",
        "nutritional_elements": "Fiber for digestion, Protein, Vitamin A.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Healthy+Toddler+Meal",
        "challenges": "Obstacle: Severe temper tantrums in public.",
        "tips": "How to overcome: Offer simple choices (e.g., 'red cup or blue cup?')."
    },
    "3 Years": {
        "expected_height": 95,
        "experiences": "Imaginative play, asking 'why' constantly, toilet training.",
        "activities": "Riding a tricycle, coloring with crayons.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Tricycle+Riding+(3+Years)",
        "daily_calories": "1200 - 1400 kcal",
        "breakfast": "1. Boiled eggs & sweet potato\n- **Prep:** Slice thinly.\n2. Fava beans with tomato\n3. Cheese sandwich with cucumber",
        "meals": "1. Grilled chicken & quinoa\n- **Prep:** Grill chicken breast.\n2. Beef stew with carrots\n3. Fish sticks (baked)",
        "snacks": "1. Walnuts\n- **Prep:** Crush slightly.\n2. Grapes (cut lengthwise)\n3. Plain milk",
        "sweets": "1. Baked apples with cinnamon\n- **Prep:** Bake until soft.\n2. Oatmeal & raisin cookies\n3. Rice pudding with honey",
        "juices": "1. Fresh Mango juice\n- **Prep:** In moderation.\n2. Lemon-Mint cooler\n3. Fresh Peach juice",
        "nutritional_elements": "Complex carbohydrates, Calcium, Vitamin B12.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Fun-shaped+Healthy+Sandwich",
        "challenges": "Obstacle: Picky eating and fear of the dark.",
        "tips": "How to overcome: Do not force feed. Use a dim nightlight."
    },
    "4 Years": {
        "expected_height": 103,
        "experiences": "Cooperative play, sharing toys, distinguishing fantasy from reality.",
        "activities": "Gymnastics basics, playground climbing, hide-and-seek.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Playground+Climbing+(4+Years)",
        "daily_calories": "1200 - 1400 kcal",
        "breakfast": "1. Whole wheat pancakes\n- **Prep:** Sweeten with banana.\n2. Veggie omelet\n3. Granola with yogurt",
        "meals": "1. Baked salmon with spinach pasta\n- **Prep:** Boil pasta, mix with spinach.\n2. Lentil soup\n3. Chicken shawarma (homemade)",
        "snacks": "1. Roasted chickpeas\n- **Prep:** Toss in olive oil, roast.\n2. Sliced bell peppers\n3. Cottage cheese",
        "sweets": "1. Homemade fruit popsicles\n- **Prep:** Freeze blended fruit.\n2. Dark chocolate dipped strawberries\n3. Healthy sweet potato brownies",
        "juices": "1. Fresh Pomegranate juice\n- **Prep:** Strain well.\n2. Kiwi & Apple blend\n3. Fresh Cantaloupe juice",
        "nutritional_elements": "Magnesium, Iron from leafy greens, Omega-3.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Salmon+and+Spinach+Pasta",
        "challenges": "Obstacle: Testing boundaries, occasional lying.",
        "tips": "How to overcome: Set clear rules with logical consequences."
    },
    "5 Years": {
        "expected_height": 110,
        "experiences": "School readiness, wanting to please friends.",
        "activities": "Swimming lessons, basic football, arts and crafts.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Swimming+Lessons+(5+Years)",
        "daily_calories": "1400 - 1600 kcal",
        "breakfast": "1. Peanut butter on toast\n- **Prep:** Use whole grain bread.\n2. Cereal with milk\n3. Scrambled eggs",
        "meals": "1. Lean turkey sandwich\n- **Prep:** Add lettuce and tomato.\n2. Baked chicken & roasted veggies\n3. Minced meat with rice",
        "snacks": "1. Fruit salad\n- **Prep:** Mix colorful seasonal fruits.\n2. Cheese sticks\n3. Almonds",
        "sweets": "1. Yogurt with honey\n- **Prep:** Drizzle honey lightly.\n2. Carrot cake (low sugar)\n3. Fruit skewers",
        "juices": "1. Orange juice\n- **Prep:** Freshly squeezed.\n2. Watermelon blend\n3. Cold milk",
        "nutritional_elements": "Vitamin C for immunity, Zinc, Protein.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Turkey+Sandwich+&+Carrots",
        "challenges": "Obstacle: Separation anxiety at school gates.",
        "tips": "How to overcome: Create a visual morning chart. Keep goodbyes quick."
    },
    "6 Years": {
        "expected_height": 115,
        "experiences": "First grade transition, losing baby teeth.",
        "activities": "Cycling without training wheels, team sports.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Cycling+(6+Years)",
        "daily_calories": "1400 - 1600 kcal",
        "breakfast": "1. Fortified cereal with milk\n- **Prep:** Serve cold or warm.\n2. Egg sandwich\n3. Avocado toast",
        "meals": "1. Beef strips with broccoli & rice\n- **Prep:** Stir fry with light soy sauce.\n2. Fish fillet with potatoes\n3. Lentil soup",
        "snacks": "1. Almonds\n- **Prep:** Raw or dry roasted.\n2. Fresh fruit\n3. Yogurt",
        "sweets": "1. Baked apples\n- **Prep:** Bake with cinnamon.\n2. Peanut butter balls\n3. Dark chocolate",
        "juices": "1. Lemonade with mint\n- **Prep:** Low sugar.\n2. Apple juice\n3. Berry smoothie",
        "nutritional_elements": "Calcium & Vitamin D for new teeth.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Baked+Fish+and+Potatoes",
        "challenges": "Obstacle: Backtalk and frustration with homework.",
        "tips": "How to overcome: Praise effort, not just grades."
    },
    "7 Years": {
        "expected_height": 122,
        "experiences": "Growing independence, strong sense of fairness.",
        "activities": "Martial arts, reading storybooks, complex Lego.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Martial+Arts+(7+Years)",
        "daily_calories": "1600 - 1800 kcal",
        "breakfast": "1. Eggs & whole wheat bread\n- **Prep:** Boil or scramble.\n2. Oatmeal with honey\n3. White cheese & tomatoes",
        "meals": "1. Grilled salmon & quinoa\n- **Prep:** Grill lightly.\n2. Vegetable stew with lean meat\n3. Chicken wrap",
        "snacks": "1. Mixed nuts\n- **Prep:** Keep unsalted.\n2. Cherry tomatoes\n3. Air-popped popcorn",
        "sweets": "1. Fruit parfait\n- **Prep:** Layer yogurt and fruits.\n2. Dates\n3. Healthy oat cookies",
        "juices": "1. Hibiscus (Karkadeh)\n- **Prep:** Serve cold.\n2. Orange juice\n3. Milk",
        "nutritional_elements": "Complex Carbohydrates, Antioxidants, Protein.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Vegetable+Stew",
        "challenges": "Obstacle: Fear of failure, perfectionism.",
        "tips": "How to overcome: Share your own daily mistakes."
    },
    "8 Years": {
        "expected_height": 128,
        "experiences": "Peer groups matter, understanding complex emotions.",
        "activities": "Basketball, painting, learning a musical instrument.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Basketball+(8+Years)",
        "daily_calories": "1600 - 1800 kcal",
        "breakfast": "1. Oatmeal with nuts\n- **Prep:** Mix well.\n2. Fava beans with olive oil\n3. Peanut butter toast",
        "meals": "1. Rice, beans, and grilled chicken\n- **Prep:** Grill chicken, mix rice and beans.\n2. Spinach & cheese omelet\n3. Beef stir-fry",
        "snacks": "1. Popcorn (air-popped)\n- **Prep:** No heavy butter.\n2. Carrot sticks with hummus\n3. Grapes",
        "sweets": "1. Greek yogurt with honey\n- **Prep:** Mix well.\n2. Banana bread (low sugar)\n3. Dark chocolate",
        "juices": "1. Mango juice\n- **Prep:** Fresh.\n2. Watermelon blend\n3. Lemonade",
        "nutritional_elements": "Iron, Vitamin E, Fiber.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Rice,+Beans,+Chicken",
        "challenges": "Obstacle: Screen time battles.",
        "tips": "How to overcome: Create a written 'screen-time contract'."
    },
    "9 Years": {
        "expected_height": 133,
        "experiences": "Forming selective friendships, mastering hobbies.",
        "activities": "Robotics/coding basics, advanced team sports.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Coding/Robotics+(9+Years)",
        "daily_calories": "1600 - 2000 kcal",
        "breakfast": "1. Greek yogurt & fruit\n- **Prep:** Top with fresh fruit.\n2. Scrambled eggs\n3. Pancakes (whole wheat)",
        "meals": "1. Lentil soup & whole wheat bread\n- **Prep:** Serve hot.\n2. Roasted chicken & sweet corn\n3. Tuna pasta salad",
        "snacks": "1. Boiled corn\n- **Prep:** Boil without butter.\n2. Dark chocolate square\n3. Milk",
        "sweets": "1. Baked pear\n- **Prep:** Bake with cinnamon.\n2. Oat & date balls\n3. Fruit salad",
        "juices": "1. Strawberry juice\n- **Prep:** Fresh, low sugar.\n2. Guava juice\n3. Apple juice",
        "nutritional_elements": "Calcium before puberty growth spurts, B Vitamins.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Roasted+Chicken+&+Corn",
        "challenges": "Obstacle: Dealing with mean behavior at school.",
        "tips": "How to overcome: Role-play how to respond to unkind peers."
    },
    "10 Years": {
        "expected_height": 138,
        "experiences": "Approaching puberty, seeking privacy.",
        "activities": "Track and field, drama clubs, science experiments.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Science+Experiments+(10+Years)",
        "daily_calories": "1800 - 2000 kcal",
        "breakfast": "1. Scrambled eggs with spinach\n- **Prep:** Cook together.\n2. Avocado toast\n3. Oatmeal",
        "meals": "1. Grilled steak & sweet potato mash\n- **Prep:** Grill steak, mash potatoes.\n2. Tuna salad\n3. Chicken stew",
        "snacks": "1. Pecans\n- **Prep:** Raw.\n2. Boiled egg\n3. Apple",
        "sweets": "1. Rice pudding\n- **Prep:** Light honey.\n2. Dark chocolate\n3. Baked banana",
        "juices": "1. Orange & Carrot juice\n- **Prep:** Freshly squeezed.\n2. Lemon-Mint\n3. Milk",
        "nutritional_elements": "High Iron (crucial for girls), Zinc, Calcium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Steak+&+Sweet+Potato",
        "challenges": "Obstacle: Pre-puberty mood swings.",
        "tips": "How to overcome: Respect their growing need for personal space."
    },
    "11 Years": {
        "expected_height": 144,
        "experiences": "Puberty beginning, high body image awareness.",
        "activities": "Competitive sports, photography, writing.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Photography+(11+Years)",
        "daily_calories": "1800 - 2200 kcal",
        "breakfast": "1. Avocado toast\n- **Prep:** Top with a poached egg.\n2. Fava beans\n3. Yogurt with nuts",
        "meals": "1. Chicken liver & onions with salad\n- **Prep:** Sauté with garlic.\n2. Steamed seafood\n3. Beef with brown rice",
        "snacks": "1. Organic berries\n- **Prep:** Wash well.\n2. Walnuts\n3. Smoothie",
        "sweets": "1. Avocado chocolate mousse\n- **Prep:** Blend avocado, cocoa, honey.\n2. Dates\n3. Fruit skewers",
        "juices": "1. Green juice (Spinach/Apple)\n- **Prep:** Blend and strain.\n2. Pomegranate juice\n3. Hibiscus",
        "nutritional_elements": "Increased calories, Folate, Calcium for bones.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Seafood+&+Salad",
        "challenges": "Obstacle: Body image insecurities.",
        "tips": "How to overcome: Focus entirely on health and strength, never on weight."
    },
    "12 Years": {
        "expected_height": 150,
        "experiences": "Identity exploration, growth spurts.",
        "activities": "Football, swimming, learning a language.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Swimming+(12+Years)",
        "daily_calories": "2000 - 2400 kcal",
        "breakfast": "1. Protein oats\n- **Prep:** Mix oats, milk, peanut butter.\n2. Eggs and toast\n3. Cereal",
        "meals": "1. Chickpeas & rice with lean meat\n- **Prep:** Add lemon to chickpeas.\n2. Grilled chicken wrap\n3. Salmon and pasta",
        "snacks": "1. Mixed nuts\n- **Prep:** Unsalted.\n2. Fruit salad\n3. Protein bar (homemade)",
        "sweets": "1. Banana ice cream\n- **Prep:** Freeze and blend bananas.\n2. Dark chocolate\n3. Baked apple",
        "juices": "1. Watermelon juice\n- **Prep:** Fresh.\n2. Lemonade\n3. Milk",
        "nutritional_elements": "Protein for muscle mass, Omega-3.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Healthy+Chicken+Wrap",
        "challenges": "Obstacle: Rebellion against household rules.",
        "tips": "How to overcome: Start negotiating chores to give them control."
    },
    "13 Years": {
        "expected_height": 156,
        "experiences": "Teenage phase, peer acceptance focus, growth spurts.",
        "activities": "Gym/fitness basics, team sports, coding.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Gym/Fitness+(13+Years)",
        "daily_calories": "2200 - 2600 kcal",
        "breakfast": "1. Eggs & whole grain bread\n- **Prep:** Boil or fry lightly.\n2. Greek yogurt with chia seeds\n3. Protein smoothie",
        "meals": "1. Quinoa & fresh salmon\n- **Prep:** Grill salmon, boil quinoa.\n2. Lentil soup & roasted veggies\n3. Grilled steak with sweet potato",
        "snacks": "1. Almonds\n- **Prep:** Raw.\n2. Peanut butter sandwich\n3. Hard-boiled eggs",
        "sweets": "1. Avocado chocolate mousse\n- **Prep:** Blend avocado, cocoa, honey.\n2. Dark chocolate squares (70%+)\n3. Homemade protein bars",
        "juices": "1. Beetroot & Apple juice\n- **Prep:** Great Iron booster.\n2. Green juice\n3. Cold Hibiscus",
        "nutritional_elements": "Maximum caloric need, Calcium, Iron, Zinc.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Quinoa+&+Salmon+Bowl",
        "challenges": "Obstacle: Late-night texting, sleep deprivation.",
        "tips": "How to overcome: Establish tech-free zones in bedrooms at night."
    },
    "14 Years": {
        "expected_height": 163,
        "experiences": "Abstract thinking, moral compass, high energy needs.",
        "activities": "Specialized sports, debate clubs.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Debate/Clubs+(14+Years)",
        "daily_calories": "2200 - 2800 kcal",
        "breakfast": "1. Smoothie bowl\n- **Prep:** Blend fruits thickly, top with nuts.\n2. Veggie omelet\n3. Fava beans",
        "meals": "1. Whole wheat pasta, local beef, tomatoes\n- **Prep:** Toss pasta with olive oil.\n2. Bean salad & boiled eggs\n3. Chicken shawarma (homemade)",
        "snacks": "1. Trail mix\n- **Prep:** Nuts and dried fruits.\n2. Dark chocolate\n3. Fruit",
        "sweets": "1. Healthy brownies\n- **Prep:** Made with sweet potato.\n2. Fruit popsicles\n3. Yogurt parfait",
        "juices": "1. Pomegranate juice\n- **Prep:** Fresh.\n2. Kiwi & Apple blend\n3. Cantaloupe juice",
        "nutritional_elements": "Complex Carbohydrates, High Protein, Vitamin D.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Beef+Pasta+&+Vegetables",
        "challenges": "Obstacle: Academic stress, procrastination.",
        "tips": "How to overcome: Help break large study tasks into 20-minute steps."
    },
    "15 Years": {
        "expected_height": 168,
        "experiences": "Exploring future paths, nearing adult height.",
        "activities": "Weight training, music, leadership programs.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Weight+Training+(15+Years)",
        "daily_calories": "2200 - 2800 kcal",
        "breakfast": "1. Protein smoothie\n- **Prep:** Blend oats, milk, banana, peanut butter.\n2. Avocado toast\n3. Eggs",
        "meals": "1. Grilled chicken & fava beans\n- **Prep:** Grill chicken breast.\n2. Steak & asparagus\n3. Fish and rice",
        "snacks": "1. Macadamia nuts\n- **Prep:** Raw.\n2. Roasted oats\n3. Cheese",
        "sweets": "1. Baked apples\n- **Prep:** Add cinnamon.\n2. Date balls\n3. Dark chocolate",
        "juices": "1. Mango juice\n- **Prep:** In moderation.\n2. Orange juice\n3. Milk",
        "nutritional_elements": "Balanced macros, hydration, Magnesium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Protein+Smoothie",
        "challenges": "Obstacle: Social exclusion, peer drama.",
        "tips": "How to overcome: Listen more than you speak; validate their feelings."
    },
    "16 Years": {
        "expected_height": 173,
        "experiences": "Adult physical maturity, college/career thinking.",
        "activities": "Advanced hobbies, career workshops, driving prep.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Career+Prep+(16+Years)",
        "daily_calories": "2400 - 3000 kcal",
        "breakfast": "1. Omelet & whole grain toast\n- **Prep:** Add veggies to omelet.\n2. Protein oats\n3. Fava beans with olive oil",
        "meals": "1. Seafood & large mixed salad\n- **Prep:** Teach them to cook their own healthy meals.\n2. Grilled poultry & roasted veggies\n3. Beef stir-fry",
        "snacks": "1. Premium nuts\n- **Prep:** Keep unsalted.\n2. Greek yogurt\n3. Fruits",
        "sweets": "1. Fruit salad\n- **Prep:** Fresh seasonal fruits.\n2. Healthy oat cookies\n3. Dark chocolate",
        "juices": "1. Lemon-Mint\n- **Prep:** Low sugar.\n2. Fresh juices\n3. Milk",
        "nutritional_elements": "Adult nutritional needs, limiting processed sugars.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Large+Mixed+Salad+&+Seafood",
        "challenges": "Obstacle: Anxiety about the future and exams.",
        "tips": "How to overcome: Assure them that it is okay not to have life fully figured out yet."
    }
}

# 2. Vaccinations Data

vaccine_data = {
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
    st.title("🏃 Activities, Comprehensive Diet & Milestones")
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
            
            st.subheader("🍎 Clinical Nutrition & Diet Plan")
            st.info(f"**🔥 Daily Calories:** {info.get('daily_calories', 'Varies')}")
            
            # Nutrition Tabs
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["🍳 Breakfast", "🍲 Main Meals", "🥨 Snacks", "🧁 Sweets", "🧃 Juices/Drinks"])
            
            with tab1:
                st.write("**Healthy Breakfast Options & Preparation:**")
                st.write(info.get('breakfast', 'Balanced breakfast'))
            with tab2:
                st.write("**Healthy Lunch/Dinner Options & Preparation:**")
                st.write(info.get('meals', 'Balanced meals'))
            with tab3:
                st.write("**Healthy Snacks & Preparation:**")
                st.write(info.get('snacks', 'Healthy snacks'))
            with tab4:
                st.write("**Healthy Sweets & Preparation (No added refined sugar):**")
                st.write(info.get('sweets', 'Natural sweets'))
            with tab5:
                st.write("**Drinks & Juices:**")
                st.write(info.get('juices', 'Water and Milk'))
                if age_selection < 1.0:
                    st.error("⚠️ Medical Note: Juices and added sugars are strictly prohibited for infants under 1 year.")

            st.markdown(f"**🧪 Key Nutrients Needed:** {info.get('nutritional_elements', 'Balanced diet essential for growth.')}")
            
            with st.expander(f"👩‍🍳 View Food Ideas & Inspiration"):
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

