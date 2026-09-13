import streamlit as st
import re

# 1. Comprehensive Developmental Data 

development_data = {
    
    "1 Month": {
        "expected_height": 54,
        "experiences": "Adapting to the world, recognizing parents' voices, keeping hands in tight fists.",
        "activities": "High-contrast (black and white) cards, gentle singing, tummy time on chest.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+High-Contrast+Cards",
        "daily_calories": "400 - 450 kcal",
        "breakfast": "1. Formula Milk\n- **Prep:** Prepare using sterilized warm water strictly to instructions.\n2. Breastmilk\n- **Prep:** Mother should maintain a highly nutritious diet.\n3. Milk via Newborn Bottle\n- **Prep:** Ensure slow flow nipple is used.",
        "meals": "1. Formula Milk\n- **Prep:** Feed on demand.\n2. Breastmilk\n- **Prep:** Ensure proper latching.\n3. Milk via Newborn Bottle\n- **Prep:** Burp mid-feed to prevent gas.",
        "snacks": "1. No solids yet\n- **Prep:** Digestive system is not ready.\n2. Milk only\n- **Prep:** Do not offer water.\n3. Milk only\n- **Prep:** Stick to milk.",
        "sweets": "1. Strictly prohibited\n- **Prep:** No sugars.\n2. Strictly prohibited\n- **Prep:** No honey (risk of botulism).\n3. Strictly prohibited\n- **Prep:** No sweeteners.",
        "juices": "1. Milk only\n- **Prep:** No water needed.\n2. Milk only\n- **Prep:** No herbal teas.\n3. Milk only\n- **Prep:** No fruit juices.",
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
        "breakfast": "1. Formula Milk\n- **Prep:** Serve at body temperature.\n2. Breastmilk\n- **Prep:** Mother should stay hydrated.\n3. Milk via Anti-colic Bottle\n- **Prep:** Angle bottle to keep nipple full of milk.",
        "meals": "1. Formula Milk\n- **Prep:** Mix gently to avoid air bubbles.\n2. Breastmilk\n- **Prep:** Feed every 3-4 hours.\n3. Milk via Anti-colic Bottle\n- **Prep:** Use bottles with air vents.",
        "snacks": "1. No solids\n- **Prep:** Milk only.\n2. No solids\n- **Prep:** Avoid cereals in bottles.\n3. No solids\n- **Prep:** Milk only.",
        "sweets": "1. Strictly prohibited\n- **Prep:** Avoid completely.\n2. Strictly prohibited\n- **Prep:** No sugars.\n3. Strictly prohibited\n- **Prep:** No honey.",
        "juices": "1. Milk only\n- **Prep:** No juices allowed.\n2. Milk only\n- **Prep:** No water.\n3. Milk only\n- **Prep:** Strict milk diet.",
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
        "breakfast": "1. Formula Milk\n- **Prep:** Feed in a calm environment.\n2. Breastmilk\n- **Prep:** Nurse on demand.\n3. Milk via Bottle\n- **Prep:** Ensure steady milk flow.",
        "meals": "1. Formula Milk\n- **Prep:** Check temperature on wrist.\n2. Breastmilk\n- **Prep:** Burp frequently.\n3. Milk via Bottle\n- **Prep:** Clean bottles thoroughly.",
        "snacks": "1. No solids\n- **Prep:** Stick to milk.\n2. No solids\n- **Prep:** Digestive tract maturing.\n3. No solids\n- **Prep:** Milk only.",
        "sweets": "1. Strictly prohibited\n- **Prep:** Avoid completely.\n2. Strictly prohibited\n- **Prep:** No sugar.\n3. Strictly prohibited\n- **Prep:** No honey.",
        "juices": "1. Milk only\n- **Prep:** Avoid completely.\n2. Milk only\n- **Prep:** No juices.\n3. Milk only\n- **Prep:** No teas.",
        "nutritional_elements": "Calcium, healthy fats for brain development.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Milk+Bottle",
        "challenges": "Obstacle: Distracted eating as they notice surroundings.",
        "tips": "How to overcome: Feed in a quiet, dimly lit room."
    },
    "4 Months": {
        "expected_height": 64,
        "experiences": "Rolling from tummy to back, grasping objects, mimicking facial expressions.",
        "activities": "Mirror play, reading large-picture books.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Mirror+Play",
        "daily_calories": "550 - 600 kcal",
        "breakfast": "1. Formula Milk\n- **Prep:** Standard prep.\n2. Breastmilk\n- **Prep:** Nurse on demand.\n3. Milk via Bottle\n- **Prep:** Increase volume slightly per feed.",
        "meals": "1. Formula Milk\n- **Prep:** Standard prep.\n2. Breastmilk\n- **Prep:** Nurse fully.\n3. Single ingredient tasting (Only if pediatrician advised)\n- **Prep:** 1 spoon of extremely watery pureed rice cereal.",
        "snacks": "1. No solids\n- **Prep:** Milk only.\n2. No solids\n- **Prep:** Milk only.\n3. No solids\n- **Prep:** Milk only.",
        "sweets": "1. Strictly prohibited\n- **Prep:** Avoid completely.\n2. Strictly prohibited\n- **Prep:** Avoid completely.\n3. Strictly prohibited\n- **Prep:** Avoid completely.",
        "juices": "1. Milk only\n- **Prep:** Milk only.\n2. Milk only\n- **Prep:** Milk only.\n3. Milk only\n- **Prep:** Milk only.",
        "nutritional_elements": "Iron stores start depleting; rely on fortified formula.",
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
        "breakfast": "1. Formula Milk\n- **Prep:** Standard prep.\n2. Breastmilk\n- **Prep:** Standard prep.\n3. Milk via Bottle\n- **Prep:** Standard prep.",
        "meals": "1. Formula Milk\n- **Prep:** Standard prep.\n2. Zucchini water puree (tasting)\n- **Prep:** Steam zucchini, blend with milk into a liquid.\n3. Carrot water puree (tasting)\n- **Prep:** Boil carrot, blend into a very watery liquid.",
        "snacks": "1. Milk feed\n- **Prep:** Milk only.\n2. Milk feed\n- **Prep:** Milk only.\n3. Milk feed\n- **Prep:** Milk only.",
        "sweets": "1. Strictly prohibited\n- **Prep:** Avoid completely.\n2. Strictly prohibited\n- **Prep:** Avoid completely.\n3. Strictly prohibited\n- **Prep:** Avoid completely.",
        "juices": "1. Milk only\n- **Prep:** Milk only.\n2. Small sips of boiled water\n- **Prep:** Cool down completely.\n3. Milk only\n- **Prep:** Milk only.",
        "nutritional_elements": "Zinc, Vitamin D, Fats.",
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
        "breakfast": "1. Apple puree\n- **Prep:** Peel, core, and steam apple until soft. Blend with formula.\n2. Mashed banana\n- **Prep:** Mash thoroughly with a fork until perfectly smooth.\n3. Oat cereal\n- **Prep:** Cook fine oats in water until mushy.",
        "meals": "1. Zucchini puree\n- **Prep:** Steam peeled zucchini without salt, blend runny.\n2. Sweet potato mash\n- **Prep:** Bake until tender, remove skin, and blend with warm water.\n3. Carrot puree\n- **Prep:** Boil carrots until very soft, blend smoothly.",
        "snacks": "1. Milk feed\n- **Prep:** Serve at body temp.\n2. Cucumber stick (for teething)\n- **Prep:** Wash well, peel, chill in fridge (monitor closely).\n3. Milk feed\n- **Prep:** Primary nutrition is still milk.",
        "sweets": "1. Mashed natural dates\n- **Prep:** Soak one date in warm water until soft, peel, mash tiny amount.\n2. Baked pear puree\n- **Prep:** Bake pear, remove skin, blend.\n3. Sweet potato puree\n- **Prep:** Naturally sweet, serve plain.",
        "juices": "1. Boiled/cooled water\n- **Prep:** Offer small sips with meals.\n2. Milk\n- **Prep:** Main drink.\n3. Diluted unsweetened chamomile\n- **Prep:** Brew weak chamomile, cool completely.",
        "nutritional_elements": "Iron (crucial), Zinc, Vitamin D.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Vegetable+Puree",
        "challenges": "Obstacle: Teething pain and digestive changes from solids.",
        "tips": "How to overcome: Introduce one new food every 3 days to check for allergies."
    },
    "7 Months": {
        "expected_height": 70,
        "experiences": "Passing objects between hands easily, crawling attempts, babbling.",
        "activities": "Hiding toys under blankets (object permanence).",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Peek-a-boo",
        "daily_calories": "650 - 700 kcal",
        "breakfast": "1. Mashed boiled egg yolk\n- **Prep:** Hard-boil, remove white, mash yolk with formula.\n2. Avocado mash\n- **Prep:** Mash soft avocado until creamy.\n3. Oat cereal with apple puree\n- **Prep:** Mix plain cooked oats with steamed apple.",
        "meals": "1. Lentil mash\n- **Prep:** Boil yellow lentils until they fall apart, mash well.\n2. Pea puree\n- **Prep:** Steam peas, remove skins if possible, blend.\n3. Mashed butternut squash\n- **Prep:** Bake squash until soft, mash.",
        "snacks": "1. Steamed carrot sticks\n- **Prep:** Steam until easily squished between fingers.\n2. Milk feed\n- **Prep:** Maintain regular milk intake.\n3. Unsweetened plain yogurt\n- **Prep:** Serve small amounts, ensure it's pasteurized.",
        "sweets": "1. Yogurt with a drop of date puree\n- **Prep:** Mix unsweetened plain yogurt with finely mashed date.\n2. Baked apple\n- **Prep:** Bake until soft, mash.\n3. Banana mash\n- **Prep:** Mash ripe banana.",
        "juices": "1. Water\n- **Prep:** Sips from a cup.\n2. Milk\n- **Prep:** In bottle.\n3. Drop of fresh orange in water\n- **Prep:** Heavily dilute fresh orange juice with water.",
        "nutritional_elements": "Calcium, Iron, Vitamin C.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Mashed+Food+Bowl",
        "challenges": "Obstacle: Constipation from new solid foods.",
        "tips": "How to overcome: Offer small sips of water and pear puree."
    },
    "8 Months": {
        "expected_height": 71,
        "experiences": "Crawling efficiently, pulling to stand, pointing at objects.",
        "activities": "Stacking soft rings, playing with safe kitchen bowls.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Stacking+Rings",
        "daily_calories": "700 - 750 kcal",
        "breakfast": "1. Scrambled egg yolk\n- **Prep:** Cook yolk softly with a tiny drop of olive oil.\n2. Mashed papaya\n- **Prep:** Mash soft, ripe papaya.\n3. Wheat cereal (iron-fortified)\n- **Prep:** Mix with breastmilk/formula.",
        "meals": "1. Minced chicken with soft rice\n- **Prep:** Boil chicken thoroughly, shred into micro-pieces, mix with overcooked mushy rice.\n2. Mashed potato & spinach\n- **Prep:** Boil potatoes, steam spinach, mash together.\n3. Soft fish mash (no bones)\n- **Prep:** Bake white fish, ensure absolutely no bones, mash.",
        "snacks": "1. Teething crackers (sugar-free)\n- **Prep:** Choose baby-safe, meltable crackers.\n2. Peach slices (steamed)\n- **Prep:** Peel, steam until soft, cut thinly.\n3. Milk feed\n- **Prep:** Regular feed.",
        "sweets": "1. Sugar-free banana pancake\n- **Prep:** Mash banana, mix with 1 egg yolk, pan-fry tiny drops.\n2. Baked sweet potato\n- **Prep:** Serve naturally sweet.\n3. Applesauce\n- **Prep:** Homemade, no sugar.",
        "juices": "1. Water\n- **Prep:** Practice with open cup.\n2. Milk\n- **Prep:** Main hydration.\n3. Diluted fresh apple juice\n- **Prep:** Just a few drops in water.",
        "nutritional_elements": "Protein, Omega-3 for brain, Iron.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Minced+Chicken+&+Rice",
        "challenges": "Obstacle: Separation anxiety peaks.",
        "tips": "How to overcome: Play peek-a-boo to teach that you come back."
    },
    "9 Months": {
        "expected_height": 72,
        "experiences": "Pincer grasp (thumb and index), understanding 'no', cruising.",
        "activities": "Crawling through tunnels, sorting shapes.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Crawling+Tunnels",
        "daily_calories": "750 - 800 kcal",
        "breakfast": "1. Cottage cheese\n- **Prep:** Mash pasteurized low-salt cheese.\n2. Oatmeal with fruit\n- **Prep:** Cook well with water/milk, add mashed fruit.\n3. Mashed boiled egg\n- **Prep:** Boil and mash whole egg (if egg white introduced safely).",
        "meals": "1. Soft beef meatballs\n- **Prep:** Mince beef very fine, bake until extremely soft, cut into tiny bites.\n2. Lentil & carrot soup\n- **Prep:** Cook lentils and carrots until they fall apart.\n3. Soft pasta bits with tomato\n- **Prep:** Overcook small pasta, mix with fresh blended tomato.",
        "snacks": "1. Steamed broccoli florets\n- **Prep:** Steam until soft enough to squish in gums.\n2. Banana chunks\n- **Prep:** Cut into safe, small sizes.\n3. Yogurt\n- **Prep:** Plain, unsweetened.",
        "sweets": "1. Date paste with yogurt\n- **Prep:** Mix homemade date paste with yogurt.\n2. Baked pear with cinnamon\n- **Prep:** Bake until tender, add a pinch of cinnamon.\n3. Soft oat balls\n- **Prep:** Roll soaked oats into tiny balls.",
        "juices": "1. Water\n- **Prep:** Offer in a sippy cup.\n2. Milk\n- **Prep:** In bottle/cup.\n3. Fresh strained guava drops in water\n- **Prep:** Ensure no seeds.",
        "nutritional_elements": "Vitamin A, Iron, Calcium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Soft+Meatballs+&+Veggies",
        "challenges": "Obstacle: Refusing to be spoon-fed.",
        "tips": "How to overcome: Encourage independent feeding with safe finger foods."
    },
    "10 Months": {
        "expected_height": 73,
        "experiences": "Cruising along furniture, waving goodbye, responding to simple requests.",
        "activities": "Push-toys to practice walking, simple puzzles.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Push+Toys",
        "daily_calories": "800 - 850 kcal",
        "breakfast": "1. Whole wheat toast bits\n- **Prep:** Soak in milk if too hard, cut into tiny squares.\n2. Scrambled eggs\n- **Prep:** Cook fully, cut into bites.\n3. Fruit yogurt\n- **Prep:** Mix plain yogurt with mashed fruit.",
        "meals": "1. Chicken and vegetable stew\n- **Prep:** Cook until very tender, cut into small pieces.\n2. Fish and sweet potato mash\n- **Prep:** Ensure fish is bone-free, mix with potato.\n3. Fava beans (skinless)\n- **Prep:** Remove skin, mash well.",
        "snacks": "1. Melon slices\n- **Prep:** Cut very thin, soft pieces.\n2. Soft cheese cubes\n- **Prep:** Pasteurized, low sodium.\n3. Milk feed\n- **Prep:** Regular feed.",
        "sweets": "1. Homemade fruit popsicle\n- **Prep:** Freeze blended fruit (no sugar) in baby-safe molds.\n2. Date & oat cookies (soft)\n- **Prep:** Bake soft, chewable cookies.\n3. Baked apple\n- **Prep:** Mash lightly.",
        "juices": "1. Water\n- **Prep:** Frequent sips.\n2. Milk\n- **Prep:** Regular intake.\n3. Diluted carrot juice\n- **Prep:** Freshly juiced, mixed with water.",
        "nutritional_elements": "Complex carbs, Zinc, Omega-3.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Chicken+Stew",
        "challenges": "Obstacle: Waking up standing in the crib.",
        "tips": "How to overcome: Teach them how to safely sit back down from a standing position during the day."
    },
    "11 Months": {
        "expected_height": 74,
        "experiences": "Standing alone for a few seconds, saying 'mama'/'dada' with meaning.",
        "activities": "Building blocks, reading interactive books.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Building+Blocks",
        "daily_calories": "850 - 900 kcal",
        "breakfast": "1. Pancakes (Banana & Egg)\n- **Prep:** Pan-fry in tiny amount of butter/oil.\n2. Foul (Fava beans) with olive oil\n- **Prep:** Mash well, add oil.\n3. Porridge\n- **Prep:** Cook oats with milk until thick.",
        "meals": "1. Soft rice with chicken\n- **Prep:** Small grains, shredded chicken.\n2. Macaroni with hidden veggie sauce\n- **Prep:** Overcook macaroni, blend veggies into sauce.\n3. Baked salmon flakes\n- **Prep:** Flake cooked salmon, check for bones.",
        "snacks": "1. Apple slices (steamed)\n- **Prep:** Steam to soften.\n2. Hummus with soft bread\n- **Prep:** Thin layer of hummus on bread bits.\n3. Cheese sticks\n- **Prep:** Soft, pasteurized cheese.",
        "sweets": "1. Mahalabia (Rice pudding)\n- **Prep:** Sweeten with date syrup, not sugar.\n2. Fresh berries\n- **Prep:** Cut in half or quarters.\n3. Oat & banana muffins\n- **Prep:** Bake softly.",
        "juices": "1. Water\n- **Prep:** Hydration.\n2. Milk\n- **Prep:** Primary drink.\n3. Fresh strawberry blend (diluted)\n- **Prep:** Blend and dilute heavily.",
        "nutritional_elements": "Fiber, Protein, Vitamin B.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Macaroni+&+Veggies",
        "challenges": "Obstacle: Throwing food on the floor.",
        "tips": "How to overcome: Do not react heavily. Calmly remove the plate if they persist."
    },
    

    "1 Year": {
        "expected_height": 75,
        "experiences": "Walking with support or independently, first clear words, pointing.",
        "activities": "Sensory play with sand/water, large blocks, pushing carts.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Large+Blocks",
        "daily_calories": "900 - 1000 kcal",
        "breakfast": "1. Scrambled eggs\n- **Prep:** Cook on low heat with olive oil.\n2. Fava beans (Foul)\n- **Prep:** Mash with olive oil & cumin.\n3. Whole wheat toast with cottage cheese\n- **Prep:** Spread cheese thinly.",
        "meals": "1. Shredded chicken & mashed potatoes\n- **Prep:** Boil potatoes, shred chicken safely.\n2. Soft fish fillet with rice\n- **Prep:** Ensure 100% bone-free.\n3. Lentil soup\n- **Prep:** Serve thick with soft bread bits.",
        "snacks": "1. Peach slices\n- **Prep:** Cut into thin slices.\n2. Hummus dip\n- **Prep:** Blend until smooth, serve with cucumber.\n3. Soft cheese cubes\n- **Prep:** Cut small.",
        "sweets": "1. Date & oat energy balls\n- **Prep:** Roll soaked dates and oats.\n2. Homemade fruit yogurt\n- **Prep:** Mix plain yogurt with mashed fruit.\n3. Baked sweet potato\n- **Prep:** Serve warm and mashed.",
        "juices": "1. Fresh Guava juice\n- **Prep:** Strain seeds perfectly, no sugar.\n2. Diluted apple juice\n- **Prep:** Half juice, half water.\n3. Milk\n- **Prep:** Whole cow's milk can now be introduced.",
        "nutritional_elements": "Omega-3, Calcium, Vitamin C.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Toddler+Plate",
        "challenges": "Obstacle: Resistance to naps.",
        "tips": "How to overcome: Stick strictly to the daily nap schedule."
    },
    "2 Years": {
        "expected_height": 87,
        "experiences": "Running, explosive vocabulary (2-3 word sentences), asserting independence.",
        "activities": "Finger painting, running in the park, simple puzzles.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Finger+Painting",
        "daily_calories": "1000 - 1400 kcal",
        "breakfast": "1. Oatmeal with berries\n- **Prep:** Cook oats in whole milk.\n2. Hard-boiled egg & cucumber\n- **Prep:** Slice cucumber thinly.\n3. Peanut butter on toast\n- **Prep:** Spread thinly on whole wheat bread.",
        "meals": "1. Rice with small lean meatballs & peas\n- **Prep:** Bake meatballs until soft.\n2. Whole wheat pasta with veggie sauce\n- **Prep:** Blend veggies into the tomato sauce.\n3. Grilled chicken strips with corn\n- **Prep:** Cut chicken into manageable strips.",
        "snacks": "1. Cucumber sticks\n- **Prep:** Peel and cut into sticks.\n2. Whole milk yogurt\n- **Prep:** Serve plain or with fruit.\n3. Apple slices\n- **Prep:** Cut thin.",
        "sweets": "1. Homemade banana ice cream\n- **Prep:** Blend frozen bananas.\n2. Dark chocolate square (small)\n- **Prep:** Offer as a rare treat.\n3. Carrot cake muffin (sugar-free)\n- **Prep:** Bake using applesauce for sweetness.",
        "juices": "1. Orange & Carrot blend\n- **Prep:** Juice fresh.\n2. Watermelon juice\n- **Prep:** Blend and strain.\n3. Cold Hibiscus with honey\n- **Prep:** Lightly sweeten.",
        "nutritional_elements": "Fiber for digestion, Protein, Vitamin A.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Toddler+Pasta+Meal",
        "challenges": "Obstacle: Severe temper tantrums in public ('Terrible Twos').",
        "tips": "How to overcome: Offer simple choices (e.g., 'red cup or blue cup?')."
    },
    "3 Years": {
        "expected_height": 95,
        "experiences": "Imaginative play, asking 'why' constantly, toilet training.",
        "activities": "Riding a tricycle, coloring with crayons, playing catch.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Tricycle+Riding",
        "daily_calories": "1200 - 1400 kcal",
        "breakfast": "1. Boiled eggs & sweet potato\n- **Prep:** Slice thinly.\n2. Cheese sandwich with cucumber\n- **Prep:** Use soft whole grain bread.\n3. Fava beans with tomato\n- **Prep:** Mash lightly.",
        "meals": "1. Grilled chicken & quinoa\n- **Prep:** Grill chicken breast.\n2. Fish sticks (baked)\n- **Prep:** Coat in whole wheat crumbs, bake.\n3. Beef stew with carrots\n- **Prep:** Cook meat until tender.",
        "snacks": "1. Walnuts\n- **Prep:** Crush slightly.\n2. Grapes\n- **Prep:** ALWAYS cut lengthwise.\n3. Plain milk\n- **Prep:** Serve in a cup.",
        "sweets": "1. Rice pudding with honey\n- **Prep:** Light honey instead of sugar.\n2. Baked apples with cinnamon\n- **Prep:** Bake until soft.\n3. Oatmeal & raisin cookies\n- **Prep:** Bake soft.",
        "juices": "1. Lemon-Mint cooler\n- **Prep:** Blend with water and mint.\n2. Fresh Mango juice\n- **Prep:** In moderation.\n3. Fresh Peach juice\n- **Prep:** Blend fresh peaches.",
        "nutritional_elements": "Complex carbohydrates, Calcium, Vitamin B12.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Healthy+Sandwich",
        "challenges": "Obstacle: Picky eating and fear of the dark.",
        "tips": "How to overcome: Do not force feed. Use a dim nightlight."
    },
    "4 Years": {
        "expected_height": 103,
        "experiences": "Cooperative play, sharing toys, distinguishing fantasy from reality.",
        "activities": "Gymnastics basics, playground climbing, hide-and-seek.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Playground+Climbing",
        "daily_calories": "1200 - 1400 kcal",
        "breakfast": "1. Whole wheat pancakes\n- **Prep:** Sweeten with banana.\n2. Veggie omelet\n- **Prep:** Mix egg with chopped spinach.\n3. Granola with yogurt\n- **Prep:** Use soft granola.",
        "meals": "1. Baked salmon with spinach pasta\n- **Prep:** Boil pasta, mix with spinach.\n2. Lentil soup\n- **Prep:** Serve with whole grain bread.\n3. Chicken shawarma (homemade)\n- **Prep:** Use whole wheat wrap.",
        "snacks": "1. Roasted chickpeas\n- **Prep:** Toss in olive oil, roast.\n2. Sliced bell peppers\n- **Prep:** Serve with hummus.\n3. Cottage cheese\n- **Prep:** Serve plain.",
        "sweets": "1. Homemade fruit popsicles\n- **Prep:** Freeze blended fruit.\n2. Dark chocolate dipped strawberries\n- **Prep:** Dip half the strawberry.\n3. Healthy sweet potato brownies\n- **Prep:** Bake using mashed sweet potato.",
        "juices": "1. Fresh Pomegranate juice\n- **Prep:** Strain well.\n2. Kiwi & Apple blend\n- **Prep:** Blend fresh.\n3. Fresh Cantaloupe juice\n- **Prep:** Blend with ice.",
        "nutritional_elements": "Magnesium, Iron from leafy greens, Omega-3.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Salmon+and+Spinach+Pasta",
        "challenges": "Obstacle: Testing boundaries, occasional lying.",
        "tips": "How to overcome: Set clear rules with logical consequences."
    },
    "5 Years": {
        "expected_height": 110,
        "experiences": "School readiness, wanting to please friends, following rules better.",
        "activities": "Swimming lessons, basic football, arts and crafts.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Swimming+Lessons",
        "daily_calories": "1400 - 1600 kcal",
        "breakfast": "1. Peanut butter on toast\n- **Prep:** Use whole grain bread.\n2. Cereal with milk\n- **Prep:** Choose low sugar, high fiber cereal.\n3. Scrambled eggs\n- **Prep:** Cook with tomatoes.",
        "meals": "1. Lean turkey sandwich\n- **Prep:** Add lettuce and tomato.\n2. Baked chicken & roasted veggies\n- **Prep:** Roast carrots and zucchini.\n3. Minced meat with rice\n- **Prep:** Mix meat with peas.",
        "snacks": "1. Fruit salad\n- **Prep:** Mix colorful seasonal fruits.\n2. Cheese sticks\n- **Prep:** Serve plain.\n3. Almonds\n- **Prep:** Dry roasted.",
        "sweets": "1. Yogurt with honey\n- **Prep:** Drizzle honey lightly.\n2. Carrot cake (low sugar)\n- **Prep:** Bake using whole wheat flour.\n3. Fruit skewers\n- **Prep:** Put grapes and melon on safe sticks.",
        "juices": "1. Orange juice\n- **Prep:** Freshly squeezed.\n2. Watermelon blend\n- **Prep:** Blend fresh.\n3. Cold milk\n- **Prep:** Serve in a glass.",
        "nutritional_elements": "Vitamin C for immunity, Zinc, Protein.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Turkey+Sandwich+&+Carrots",
        "challenges": "Obstacle: Separation anxiety at school gates.",
        "tips": "How to overcome: Create a visual morning chart. Keep goodbyes quick."
    },
    "6 Years": {
        "expected_height": 115,
        "experiences": "First grade transition, losing baby teeth, eager to show off skills.",
        "activities": "Cycling without training wheels, team sports.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Cycling",
        "daily_calories": "1400 - 1600 kcal",
        "breakfast": "1. Fortified cereal with milk\n- **Prep:** Serve cold or warm.\n2. Avocado toast\n- **Prep:** Mash on whole wheat bread.\n3. Egg sandwich\n- **Prep:** Boil egg, slice in bread.",
        "meals": "1. Beef strips with broccoli & rice\n- **Prep:** Stir fry with light soy sauce.\n2. Lentil soup\n- **Prep:** Serve with lemon.\n3. Fish fillet with potatoes\n- **Prep:** Bake fish with herbs.",
        "snacks": "1. Almonds\n- **Prep:** Raw or dry roasted.\n2. Fresh fruit\n- **Prep:** Apple or pear slices.\n3. Yogurt\n- **Prep:** Serve plain.",
        "sweets": "1. Baked apples\n- **Prep:** Bake with cinnamon.\n2. Dark chocolate\n- **Prep:** Small piece.\n3. Peanut butter balls\n- **Prep:** Roll with oats.",
        "juices": "1. Lemonade with mint\n- **Prep:** Low sugar.\n2. Berry smoothie\n- **Prep:** Blend with milk.\n3. Apple juice\n- **Prep:** Freshly pressed.",
        "nutritional_elements": "Calcium & Vitamin D for new teeth.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Baked+Fish",
        "challenges": "Obstacle: Backtalk and frustration with homework.",
        "tips": "How to overcome: Praise effort, not just grades."
    },
    "7 Years": {
        "expected_height": 122,
        "experiences": "Growing independence, strong sense of fairness, logical thinking.",
        "activities": "Martial arts, reading storybooks, complex Lego.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Martial+Arts",
        "daily_calories": "1600 - 1800 kcal",
        "breakfast": "1. Eggs & whole wheat bread\n- **Prep:** Boil or scramble.\n2. Oatmeal with honey\n- **Prep:** Cook with milk.\n3. White cheese & tomatoes\n- **Prep:** Serve with cucumber.",
        "meals": "1. Grilled salmon & quinoa\n- **Prep:** Grill lightly.\n2. Vegetable stew with lean meat\n- **Prep:** Cook until tender.\n3. Chicken wrap\n- **Prep:** Use whole wheat tortilla.",
        "snacks": "1. Mixed nuts\n- **Prep:** Keep unsalted.\n2. Cherry tomatoes\n- **Prep:** Wash well.\n3. Air-popped popcorn\n- **Prep:** Pop without butter.",
        "sweets": "1. Fruit parfait\n- **Prep:** Layer yogurt and fruits.\n2. Dates\n- **Prep:** Serve plain.\n3. Healthy oat cookies\n- **Prep:** Bake soft.",
        "juices": "1. Hibiscus (Karkadeh)\n- **Prep:** Serve cold.\n2. Orange juice\n- **Prep:** Fresh.\n3. Milk\n- **Prep:** Serve cold.",
        "nutritional_elements": "Complex Carbohydrates, Antioxidants, Protein.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Vegetable+Stew",
        "challenges": "Obstacle: Fear of failure, perfectionism.",
        "tips": "How to overcome: Share your own daily mistakes."
    },
    "8 Years": {
        "expected_height": 128,
        "experiences": "Peer groups matter, understanding complex emotions, group games.",
        "activities": "Basketball, painting, learning a musical instrument.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Basketball",
        "daily_calories": "1600 - 1800 kcal",
        "breakfast": "1. Oatmeal with nuts\n- **Prep:** Mix well.\n2. Fava beans with olive oil\n- **Prep:** Mash lightly.\n3. Peanut butter toast\n- **Prep:** Spread on whole grain.",
        "meals": "1. Rice, beans, and grilled chicken\n- **Prep:** Grill chicken, mix rice and beans.\n2. Spinach & cheese omelet\n- **Prep:** Fold spinach inside.\n3. Beef stir-fry\n- **Prep:** Cook with bell peppers.",
        "snacks": "1. Popcorn (air-popped)\n- **Prep:** No heavy butter.\n2. Carrot sticks with hummus\n- **Prep:** Serve raw.\n3. Grapes\n- **Prep:** Serve washed.",
        "sweets": "1. Greek yogurt with honey\n- **Prep:** Mix well.\n2. Banana bread (low sugar)\n- **Prep:** Bake fresh.\n3. Dark chocolate\n- **Prep:** Small piece.",
        "juices": "1. Mango juice\n- **Prep:** Fresh.\n2. Watermelon blend\n- **Prep:** Blend with ice.\n3. Lemonade\n- **Prep:** Low sugar.",
        "nutritional_elements": "Iron, Vitamin E, Fiber.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Rice,+Beans,+Chicken",
        "challenges": "Obstacle: Intense screen time battles.",
        "tips": "How to overcome: Create a written 'screen-time contract'."
    },
    "9 Years": {
        "expected_height": 133,
        "experiences": "Forming selective friendships, mastering hobbies and skills.",
        "activities": "Robotics/coding basics, advanced team sports.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Coding",
        "daily_calories": "1600 - 2000 kcal",
        "breakfast": "1. Greek yogurt & fruit\n- **Prep:** Top with fresh fruit.\n2. Scrambled eggs\n- **Prep:** Cook with a little butter.\n3. Pancakes (whole wheat)\n- **Prep:** Serve with honey.",
        "meals": "1. Lentil soup & whole wheat bread\n- **Prep:** Serve hot.\n2. Roasted chicken & sweet corn\n- **Prep:** Roast in oven.\n3. Tuna pasta salad\n- **Prep:** Mix with olive oil.",
        "snacks": "1. Boiled corn\n- **Prep:** Boil without butter.\n2. Dark chocolate square\n- **Prep:** Serve plain.\n3. Milk\n- **Prep:** Drink cold.",
        "sweets": "1. Baked pear\n- **Prep:** Bake with cinnamon.\n2. Oat & date balls\n- **Prep:** Roll tightly.\n3. Fruit salad\n- **Prep:** Chop fresh fruits.",
        "juices": "1. Strawberry juice\n- **Prep:** Fresh, low sugar.\n2. Guava juice\n- **Prep:** Strain seeds.\n3. Apple juice\n- **Prep:** Freshly squeezed.",
        "nutritional_elements": "Calcium before puberty growth spurts, B Vitamins.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Roasted+Chicken+&+Corn",
        "challenges": "Obstacle: Dealing with mean behavior at school.",
        "tips": "How to overcome: Role-play how to respond to unkind peers."
    },
    "10 Years": {
        "expected_height": 138,
        "experiences": "Approaching puberty, seeking privacy, early physical changes.",
        "activities": "Track and field, drama clubs, science experiments.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Science+Experiments",
        "daily_calories": "1800 - 2000 kcal",
        "breakfast": "1. Scrambled eggs with spinach\n- **Prep:** Cook together.\n2. Avocado toast\n- **Prep:** Add salt/pepper.\n3. Oatmeal\n- **Prep:** Cook with milk and fruits.",
        "meals": "1. Grilled steak & sweet potato mash\n- **Prep:** Grill steak, mash potatoes.\n2. Tuna salad\n- **Prep:** Mix with olive oil, no mayo.\n3. Chicken stew\n- **Prep:** Cook with carrots and potatoes.",
        "snacks": "1. Pecans\n- **Prep:** Raw.\n2. Boiled egg\n- **Prep:** Serve with a pinch of cumin.\n3. Apple\n- **Prep:** Serve whole.",
        "sweets": "1. Rice pudding\n- **Prep:** Light honey.\n2. Baked banana\n- **Prep:** Bake in oven.\n3. Dark chocolate\n- **Prep:** Serve plain.",
        "juices": "1. Orange & Carrot juice\n- **Prep:** Freshly squeezed.\n2. Lemon-Mint\n- **Prep:** Blend with ice.\n3. Milk\n- **Prep:** Serve cold.",
        "nutritional_elements": "High Iron (crucial for girls), Zinc, Calcium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Steak+&+Sweet+Potato",
        "challenges": "Obstacle: Pre-puberty mood swings.",
        "tips": "How to overcome: Respect their growing need for personal space."
    },
    "11 Years": {
        "expected_height": 144,
        "experiences": "Puberty beginning, high body image awareness, mood swings.",
        "activities": "Competitive sports, photography, writing.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Photography",
        "daily_calories": "1800 - 2200 kcal",
        "breakfast": "1. Avocado toast\n- **Prep:** Top with a poached egg.\n2. Fava beans\n- **Prep:** Add olive oil.\n3. Yogurt with nuts\n- **Prep:** Serve cold.",
        "meals": "1. Chicken liver & onions with salad\n- **Prep:** Sauté with garlic.\n2. Steamed seafood\n- **Prep:** Serve with lemon.\n3. Beef with brown rice\n- **Prep:** Grill beef strips.",
        "snacks": "1. Organic berries\n- **Prep:** Wash well.\n2. Walnuts\n- **Prep:** Serve raw.\n3. Smoothie\n- **Prep:** Blend fruits with milk.",
        "sweets": "1. Avocado chocolate mousse\n- **Prep:** Blend avocado, cocoa, honey.\n2. Dates\n- **Prep:** Serve plain.\n3. Fruit skewers\n- **Prep:** Mix colorful fruits.",
        "juices": "1. Green juice (Spinach/Apple)\n- **Prep:** Blend and strain.\n2. Pomegranate juice\n- **Prep:** Strain seeds.\n3. Hibiscus\n- **Prep:** Serve cold.",
        "nutritional_elements": "Increased calories, Folate, Calcium for bones.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Seafood+&+Salad",
        "challenges": "Obstacle: Body image insecurities.",
        "tips": "How to overcome: Focus entirely on health and strength, never on weight."
    },
    "12 Years": {
        "expected_height": 150,
        "experiences": "Identity exploration, growth spurts, challenging family rules.",
        "activities": "Football, swimming, learning a language.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Swimming",
        "daily_calories": "2000 - 2400 kcal",
        "breakfast": "1. Protein oats\n- **Prep:** Mix oats, milk, peanut butter.\n2. Eggs and toast\n- **Prep:** Fry eggs lightly.\n3. Cereal\n- **Prep:** Whole grain with milk.",
        "meals": "1. Chickpeas & rice with lean meat\n- **Prep:** Add lemon to chickpeas.\n2. Grilled chicken wrap\n- **Prep:** Use whole wheat wrap.\n3. Salmon and pasta\n- **Prep:** Grill salmon, boil pasta.",
        "snacks": "1. Mixed nuts\n- **Prep:** Unsalted.\n2. Fruit salad\n- **Prep:** Chop fresh fruits.\n3. Protein bar (homemade)\n- **Prep:** Bake with oats and honey.",
        "sweets": "1. Banana ice cream\n- **Prep:** Freeze and blend bananas.\n2. Dark chocolate\n- **Prep:** Serve plain.\n3. Baked apple\n- **Prep:** Add cinnamon.",
        "juices": "1. Watermelon juice\n- **Prep:** Fresh.\n2. Lemonade\n- **Prep:** Low sugar.\n3. Milk\n- **Prep:** Drink plain.",
        "nutritional_elements": "Protein for muscle mass, Omega-3.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Healthy+Chicken+Wrap",
        "challenges": "Obstacle: Rebellion against household rules.",
        "tips": "How to overcome: Start negotiating chores to give them control."
    },
    "13 Years": {
        "expected_height": 156,
        "experiences": "Teenage phase, peer acceptance focus, major growth spurts.",
        "activities": "Gym/fitness basics, team sports, coding.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Gym/Fitness",
        "daily_calories": "2200 - 2600 kcal",
        "breakfast": "1. Eggs & whole grain bread\n- **Prep:** Boil or fry lightly.\n2. Greek yogurt with chia seeds\n- **Prep:** Mix well.\n3. Protein smoothie\n- **Prep:** Blend milk, banana, peanut butter.",
        "meals": "1. Quinoa & fresh salmon\n- **Prep:** Grill salmon, boil quinoa.\n2. Lentil soup & roasted veggies\n- **Prep:** Roast veggies with olive oil.\n3. Grilled steak with sweet potato\n- **Prep:** Grill steak medium-well.",
        "snacks": "1. Almonds\n- **Prep:** Raw.\n2. Peanut butter sandwich\n- **Prep:** Use whole wheat bread.\n3. Hard-boiled eggs\n- **Prep:** Serve with salt/pepper.",
        "sweets": "1. Avocado chocolate mousse\n- **Prep:** Blend avocado, cocoa, honey.\n2. Dark chocolate squares (70%+)\n- **Prep:** Serve plain.\n3. Homemade protein bars\n- **Prep:** Bake with oats and peanut butter.",
        "juices": "1. Beetroot & Apple juice\n- **Prep:** Great Iron booster, juice fresh.\n2. Green juice\n- **Prep:** Blend spinach and apple.\n3. Cold Hibiscus\n- **Prep:** Serve chilled.",
        "nutritional_elements": "Maximum caloric need, Calcium, Iron, Zinc.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Quinoa+&+Salmon+Bowl",
        "challenges": "Obstacle: Late-night texting, sleep deprivation.",
        "tips": "How to overcome: Establish tech-free zones in bedrooms at night."
    },
    "14 Years": {
        "expected_height": 163,
        "experiences": "Abstract thinking, moral compass, high energy needs.",
        "activities": "Specialized sports, debate clubs.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Debate+Clubs",
        "daily_calories": "2200 - 2800 kcal",
        "breakfast": "1. Smoothie bowl\n- **Prep:** Blend fruits thickly, top with nuts.\n2. Veggie omelet\n- **Prep:** Cook eggs with bell peppers.\n3. Fava beans\n- **Prep:** Mash with oil.",
        "meals": "1. Whole wheat pasta, local beef, tomatoes\n- **Prep:** Toss pasta with olive oil.\n2. Bean salad & boiled eggs\n- **Prep:** Mix beans with lemon/oil.\n3. Chicken shawarma (homemade)\n- **Prep:** Use whole wheat wrap.",
        "snacks": "1. Trail mix\n- **Prep:** Nuts and dried fruits.\n2. Dark chocolate\n- **Prep:** Serve plain.\n3. Fruit\n- **Prep:** Apple or banana.",
        "sweets": "1. Healthy brownies\n- **Prep:** Made with sweet potato.\n2. Fruit popsicles\n- **Prep:** Freeze blended fruit.\n3. Yogurt parfait\n- **Prep:** Layer yogurt and berries.",
        "juices": "1. Pomegranate juice\n- **Prep:** Fresh.\n2. Kiwi & Apple blend\n- **Prep:** Blend fresh.\n3. Cantaloupe juice\n- **Prep:** Blend with ice.",
        "nutritional_elements": "Complex Carbohydrates, High Protein, Vitamin D.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Beef+Pasta+&+Vegetables",
        "challenges": "Obstacle: Academic stress, procrastination.",
        "tips": "How to overcome: Help break large study tasks into 20-minute steps."
    },
    "15 Years": {
        "expected_height": 168,
        "experiences": "Exploring future paths, nearing adult height, romantic interests.",
        "activities": "Weight training, music, leadership programs.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Weight+Training",
        "daily_calories": "2200 - 2800 kcal",
        "breakfast": "1. Protein smoothie\n- **Prep:** Blend oats, milk, banana, peanut butter.\n2. Avocado toast\n- **Prep:** Add chili flakes (optional).\n3. Eggs\n- **Prep:** Boil or fry.",
        "meals": "1. Grilled chicken & fava beans\n- **Prep:** Grill chicken breast.\n2. Steak & asparagus\n- **Prep:** Grill together.\n3. Fish and rice\n- **Prep:** Bake fish with lemon.",
        "snacks": "1. Macadamia nuts\n- **Prep:** Raw.\n2. Roasted oats\n- **Prep:** Bake with honey.\n3. Cheese\n- **Prep:** Serve cubed.",
        "sweets": "1. Baked apples\n- **Prep:** Add cinnamon.\n2. Date balls\n- **Prep:** Roll with coconut.\n3. Dark chocolate\n- **Prep:** Serve plain.",
        "juices": "1. Mango juice\n- **Prep:** In moderation.\n2. Orange juice\n- **Prep:** Freshly squeezed.\n3. Milk\n- **Prep:** Drink cold.",
        "nutritional_elements": "Balanced macros, hydration, Magnesium.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Protein+Smoothie",
        "challenges": "Obstacle: Social exclusion, peer drama.",
        "tips": "How to overcome: Listen more than you speak; validate their feelings."
    },
    "16 Years": {
        "expected_height": 173,
        "experiences": "Adult physical maturity, college/career thinking.",
        "activities": "Advanced hobbies, career workshops, driving prep.",
        "activity_image": "https://placehold.co/600x400/E6F7FF/003366?text=Activity:+Career+Prep",
        "daily_calories": "2400 - 3000 kcal",
        "breakfast": "1. Omelet & whole grain toast\n- **Prep:** Add veggies to omelet.\n2. Protein oats\n- **Prep:** Add peanut butter.\n3. Fava beans with olive oil\n- **Prep:** Mash well.",
        "meals": "1. Seafood & large mixed salad\n- **Prep:** Teach them to cook their own healthy meals.\n2. Beef stir-fry\n- **Prep:** Use colorful bell peppers.\n3. Grilled poultry & roasted veggies\n- **Prep:** Roast in oven.",
        "snacks": "1. Premium nuts\n- **Prep:** Keep unsalted.\n2. Greek yogurt\n- **Prep:** Top with berries.\n3. Fruits\n- **Prep:** Serve fresh.",
        "sweets": "1. Fruit salad\n- **Prep:** Fresh seasonal fruits.\n2. Healthy oat cookies\n- **Prep:** Bake with minimal sugar.\n3. Dark chocolate\n- **Prep:** Serve plain.",
        "juices": "1. Lemon-Mint\n- **Prep:** Low sugar.\n2. Fresh juices\n- **Prep:** No added sugars.\n3. Milk\n- **Prep:** Drink plain.",
        "nutritional_elements": "Adult nutritional needs, limiting processed sugars.",
        "food_image": "https://placehold.co/600x400/FFF0F5/4A004A?text=Image:+Large+Mixed+Salad",
        "challenges": "Obstacle: Anxiety about the future and exams.",
        "tips": "How to overcome: Assure them that it is okay not to have life fully figured out yet."
    }
}

# Fill missing intermediate years and months to prevent errors
for age in range(4, 16):
    if f"{age} Years" not in development_data and age not in [6, 10]:
        development_data[f"{age} Years"] = development_data["6 Years"].copy()
for age in range(1, 12):
    if f"{age} Month" not in development_data and f"{age} Months" not in development_data:
        development_data[f"{age} Months" if age > 1 else "1 Month"] = development_data["6 Months"].copy()


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


# 3. Medical Calculations 

def calculate_expected_weight(age_years, gender):
    if age_years < 1.0:
        age_months = age_years * 12
        return round((age_months + 9) / 2, 1)
    elif age_years <= 7.0:
        return round((age_years * 2) + 8, 1)
    else:
     
        base_w = (age_years * 7 - 5) / 2
        
      
        if gender == "Boy":
            if age_years > 12:
                base_w += (age_years - 12) * 2.5 
        else: # Girl
            if 9 <= age_years <= 12:
                base_w += 2 
            elif age_years > 12:
                base_w -= (age_years - 12) * 1.5 
        
        return round(base_w, 1)

def calculate_expected_height(base_height, age_years, gender):
    who_girls_height = {
        5: 109.4, 6: 115.1, 7: 120.8, 8: 126.6, 9: 132.5,
        10: 138.6, 11: 145.0, 12: 151.2, 13: 156.4,
        14: 159.8, 15: 161.7, 16: 162.5
    }
    
    who_boys_height = {
        5: 110.0, 6: 116.0, 7: 121.7, 8: 127.3, 9: 132.6,
        10: 137.8, 11: 143.1, 12: 149.1, 13: 156.0,
        14: 163.2, 15: 170.0, 16: 173.5
    }

    if age_years >= 5.0:
        age_int = int(round(age_years))
        if age_int > 16: 
            age_int = 16
            
        if gender == "Girl":
            return who_girls_height.get(age_int, base_height)
        else:
            return who_boys_height.get(age_int, base_height)
            
    return base_height

def adjust_calories(base_cal_str, age_years, gender):
    if age_years <= 7.0:
        return base_cal_str
        
    nums = [int(s) for s in re.findall(r'\d+', base_cal_str)]
    if len(nums) >= 2:
        low, high = nums[0], nums[1]
        if gender == "Boy":
            if age_years >= 11:
                low += 250
                high += 350
        else: # Girl
            if age_years >= 13:
                low -= 200
                high -= 200
        return f"{low} - {high} kcal (Adjusted for {gender})"
    return base_cal_str

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

# 4. Streamlit 

st.set_page_config(page_title="Child Growth Tracker", page_icon="👶", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    [data-testid="collapsedControl"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    
    .wheel-btn button {
        width: 170px !important;
        height: 170px !important;
        border-radius: 50% !important;
        border: 6px dashed #4CAF50 !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
        color: #333333 !important;
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1) !important;
        transition: transform 0.8s ease-in-out, background-color 0.4s, color 0.4s !important; 
        margin: 0 auto !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        white-space: pre-wrap !important; 
    }
    .wheel-btn button:hover {
        background-color: #4CAF50 !important;
        color: #ffffff !important;
        transform: rotate(360deg) scale(1.1) !important; 
        box-shadow: 0px 15px 20px rgba(46, 229, 157, 0.4) !important;
    }
    .center-div {
        display: flex;
        justify-content: center;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)


if 'page_state' not in st.session_state: st.session_state.page_state = "Setup"
if 'parent_name' not in st.session_state: st.session_state.parent_name = ""
if 'child_name' not in st.session_state: st.session_state.child_name = ""
if 'child_gender' not in st.session_state: st.session_state.child_gender = "Boy" # Default gender

def navigate(page_name):
    st.session_state.page_state = page_name


# 5. Routing Logic



if st.session_state.page_state == "Setup":
    st.title("👶 Welcome to Child Growth Tracker")
    st.write("Let's personalize your experience. Please enter your details:")
    st.markdown("---")
    
    parent = st.text_input("Enter your name (Parent):", value=st.session_state.parent_name)
    child = st.text_input("Enter your baby's name:", value=st.session_state.child_name)
    gender = st.radio("Child's Gender:", ["Boy", "Girl"], index=0 if st.session_state.child_gender == "Boy" else 1)
    
    if st.button("🚀 Enter Dashboard"):
        if parent and child:
            st.session_state.parent_name = parent
            st.session_state.child_name = child
            st.session_state.child_gender = gender
            navigate("Wheel")
            st.rerun()
        else:
            st.error("Please enter both names to continue.")


elif st.session_state.page_state == "Wheel":
    st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>👋 Welcome {st.session_state.parent_name} & Baby {st.session_state.child_name}! 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Hover over the wheels below to spin them and choose your path!</h3><br>", unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns([1, 1, 1])
    with t2:
        st.markdown('<div class="wheel-btn center-div">', unsafe_allow_html=True)
        st.button("📊\nGrowth & Vitals", on_click=navigate, args=("Growth",), key="btn_growth")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write("") 
        
    m1, m2, m3 = st.columns([1, 0.2, 1])
    with m1:
        st.markdown('<div class="wheel-btn" style="float: right;">', unsafe_allow_html=True)
        st.button("🏃\nDiet & Activities", on_click=navigate, args=("Activities",), key="btn_act")
        st.markdown('</div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="wheel-btn" style="float: left;">', unsafe_allow_html=True)
        st.button("💉\nVaccinations", on_click=navigate, args=("Vaccinations",), key="btn_vax")
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write("") 
        
    b1, b2, b3 = st.columns([1, 1, 1])
    with b2:
        st.markdown('<div class="wheel-btn center-div">', unsafe_allow_html=True)
        st.button("👤\nEdit Profile", on_click=navigate, args=("Setup",), key="btn_prof")
        st.markdown('</div>', unsafe_allow_html=True)

GROWTH & VITALS ---
elif st.session_state.page_state == "Growth":
    st.button("🔙 Back to Main Wheel", on_click=navigate, args=("Wheel",))
    st.markdown("---")
    
    st.title("📊 Growth & Vitals Tracker")
    st.info(f"Viewing data adapted for a **{st.session_state.child_gender}**.")
    st.info("Tip: For infants under 1 year, use decimals (e.g., 0.5 for 6 months).")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Child's Age (Years):", min_value=0.1, max_value=16.0, value=1.0, step=0.1)
    with col2:
        actual_weight = st.number_input("Current Weight (kg):", min_value=1.0, max_value=120.0, value=10.0, step=0.5)
    with col3:
        actual_height = st.number_input("Current Height (cm):", min_value=30.0, max_value=200.0, value=75.0, step=1.0)

    if st.button("Analyze Growth", type="primary"):
        expected_weight = calculate_expected_weight(age, st.session_state.child_gender)
        
        if age < 1.0:
            months = round(age * 12)
            if months <= 0: months = 1
            if months > 11: months = 11
            dict_key = f"{months} Month" if months == 1 else f"{months} Months"
        else:
            years = round(age)
            if years > 16: years = 16
            dict_key = f"{years} Year" if years == 1 else f"{years} Years"
            
        base_height = development_data.get(dict_key, {}).get("expected_height", 100)
        expected_height = calculate_expected_height(base_height, age, st.session_state.child_gender)
        
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

# ACTIVITIES & DIET
elif st.session_state.page_state == "Activities":
    st.button("🔙 Back to Main Wheel", on_click=navigate, args=("Wheel",))
    st.markdown("---")
    
    st.title("🏃 Activities, Comprehensive Diet & Milestones")
    
    age_options = [f"{m} Month" if m == 1 else f"{m} Months" for m in range(1, 12)]
    age_options += [f"{y} Year" if y == 1 else f"{y} Years" for y in range(1, 17)]
    
    age_selection = st.selectbox("Select Age:", age_options)
    
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
        
        # Calculate numeric age for calorie
        age_num = float(age_selection.split()[0])
        if "Month" in age_selection:
            age_num = age_num / 12.0
            
        adjusted_cals = adjust_calories(info.get('daily_calories', 'Varies'), age_num, st.session_state.child_gender)
        st.info(f"**🔥 Daily Calories:** {adjusted_cals}")
        
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

#  VACCINATIONS
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
