from django.shortcuts import render
import random
def classifiers():
    vegClassification = {"Veg": 1, "Non-Veg": 2}
    countClassification = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
    cuisineClassification = {
        "North Indian": 1,
        "South Indian": 2,
        "Gujarati Cuisine": 3,
        "Punjabi Cuisine": 4,
        "Chinese Cuisine": 5,
        "Italian Cuisine": 6,
        "Other Cuisines": 7,
    }
    foodClassification = {
        "Biryani": 1,
        "Butter Chicken": 2,
        "Masala Dosa": 3,
        "Samosa": 4,
        "Tandoori Chicken": 5,
        "Paneer Tikka": 6,
        "Chole Bhature": 7,
        "Rajma Chawal": 8,
        "Pani Puri": 9,
        "Gulab Jamun": 10,
        "Chicken Tikka Masala": 11,
        "Dhokla": 12,
        "Idli": 13,
        "Aloo Paratha": 14,
        "Fish Curry": 15,
        "Vada Pav": 16,
        "Pav Bhaji": 17,
        "Chicken Biryani": 18,
        "Hyderabadi Dum Biryani": 19,
        "Rasgulla": 20,
        "Palak Paneer": 21,
        "Papdi Chaat": 22,
        "Dal Makhani": 23,
        "Mutton Curry": 24,
        "Poha": 25,
        "Malai Kofta": 26,
        "Aloo Tikki": 27,
        "Kadai Paneer": 28,
        "Chaat": 29,
        "Gajar Ka Halwa": 30,
        "Tandoori Roti": 31,
        "Matar Paneer": 32,
        "Jalebi": 33,
        "Kachori": 34,
        "Chicken Curry": 35,
        "Pulao": 36,
        "Rasmalai": 37,
        "Shahi Paneer": 38,
        "Pakora": 39,
        "Chicken 65": 40,
        "Mango Lassi": 41,
        "Kulfi": 42,
        "Chicken Korma": 43,
        "Chapati": 44,
        "Gobi Manchurian": 45,
        "Mysore Masala Dosa": 46,
        "Upma": 47,
        "Dal Tadka": 48,
        "Kheer": 49,
        "Aloo Gobi": 50,
        "Chicken Chettinad": 51,
        "Phirni": 52,
        "Mutton Biryani": 53,
        "Laccha Paratha": 54,
        "Chicken Shawarma": 55,
        "Shahi Tukda": 56,
        "Raj Kachori": 57,
        "Chicken Fry": 58,
        "Dahi Puri": 59,
        "Aloo Matar": 60,
        "Butter Naan": 61,
        "Dal Fry": 62,
        "Chicken Tandoori": 63,
        "Papad": 64,
        "Chicken Do Pyaza": 65,
        "Veg Pulao": 66,
        "Mutton Korma": 67,
        "Pani Puri": 68,
        "Egg Curry": 69,
        "Chicken Kebab": 70,
        "Chilli Chicken": 71,
        "Rava Dosa": 72,
        "Onion Uttapam": 73,
        "Puran Poli": 74,
        "Keema Matar": 75,
        "Kadai Chicken": 76,
        "Fish Fry": 77,
        "Vegetable Biryani": 78,
        "Aloo Jeera": 79,
        "Chicken Handi": 80,
        "Mango Pickle": 81,
        "Pongal": 82,
        "Tawa Pulao": 83,
        "Veg Manchurian": 84,
        "Chicken Salna": 85,
        "Egg Fried Rice": 86,
        "Tamarind Rice": 87,
        "Chicken 555": 88,
        "Chicken Kolhapuri": 89,
        "Ghee Rice": 90,
        "Mushroom Tikka": 91,
        "Chicken Manchurian": 92,
        "Keema Paratha": 93,
        "Bhindi Masala": 94,
        "Kadhi Pakora": 95,
        "Chicken Vindaloo": 96,
        "Chicken Kali Mirch": 97,
        "Lemon Rice": 98,
        "Chicken Patiala": 99,
        "Chicken Reshmi Kebab": 100,
        "Dhansak": 101,
        "Kheema Pav": 102,
        "Puran Poli": 103,
        "Khandvi": 104,
        "Dabeli": 105,
        "Kathi Rolls": 106,
        "Kozhukattai": 107,
        "Mysore Pak": 108,
        "Neer Dosa": 109,
        "Undhiyu": 110,
        "Pesarattu": 111,
        "Akki Roti": 112,
        "Misal Pav": 113,
        "Aloo Bonda": 114,
        "Medu Vada": 115,
        "Pav Bhaji": 116,
        "Vada Pav": 117,
        "Ragda Patties": 118,
        "Kulfi": 119,
        "Ras Malai": 120,
        "Litti Chokha": 121,
        "Ghevar": 122,
        "Baingan Bharta": 123,
        "Pindi Chole": 124,
        "Gujarati Kadhi": 125,
        "Malabar Parotta": 126,
        "Chettinad Chicken": 127,
        "Korma": 128,
        "Mughlai Paratha": 129,
        "Rogan Josh": 130,
        "Aamras Puri": 131,
        "Kadhi Pakora": 132,
        "Malpua": 133,
        "Papri Chaat": 134,
        "Shrikhand": 135,
        "Pootharekulu": 136,
        "Coorg Pandi Curry": 137,
        "Avial": 138,
        "Puttu": 139,
        "Thalassery Biryani": 140,
        "Kappa Meen Curry": 141,
        "Idiyappam": 142,
        "Juices": 143,
        "Pizza": 144,
        "Burger": 145,
        "Pasta": 146,
        "Milk Shakes": 147,
        "Chinese": 148,
    }

    all = []
    vegKeys = list(vegClassification.keys())
    cuisineKeys = list(cuisineClassification.keys())
    foodKeys = list(foodClassification.keys())
    for i in range(2500):
        randomVeg = random.randint(0, 1)
        randomCount = random.randint(3, 5)
        randomCuisine = random.randint(1, 4)
        randomFood = random.randint(1, 16)
        l = [vegKeys[randomVeg], randomCount]
        allCuis = []
        for i in range(randomCuisine):
            cuis = cuisineKeys[random.randint(0, 6)]
            if cuis in allCuis:
                i = -1
            else:
                allCuis.append(cuis)
        l.append(allCuis)
        allFood = []
        for i in range(randomFood):
            food = foodKeys[random.randint(0, 141)]
            if food in allFood:
                i = -1
            else:
                allFood.append(food)
        l.append(allFood)
        all.append(l)
    return all


data = classifiers()


def analyze_residents_likes(residents_likes):
    total_count = len(residents_likes)
    veg_count = 0
    cuisine_preferences = {}
    food_item_preferences = {}

    for resident in residents_likes:
        preference = resident[0]
        if preference == "Veg":
            veg_count += 1

        cuisines = resident[2]
        for cuisine in cuisines:
            if cuisine in cuisine_preferences:
                cuisine_preferences[cuisine] += 1
            else:
                cuisine_preferences[cuisine] = 1
        food_items = resident[3]
        for food_item in food_items:
            if food_item in food_item_preferences:
                food_item_preferences[food_item] += 1
            else:
                food_item_preferences[food_item] = 1

    veg_percentage = (veg_count / total_count) * 100
    cuisine_preferences = {
        k: (v / total_count) * 100
        for k, v in sorted(
            cuisine_preferences.items(), key=lambda x: x[1], reverse=True
        )
    }
    food_item_preferences = {
        k: (v / total_count) * 100
        for k, v in sorted(
            food_item_preferences.items(), key=lambda x: x[1], reverse=True
        )
    }

    return veg_percentage, cuisine_preferences, food_item_preferences


def analysis(data):
    a = []
    veg_percentage, cuisine_preferences, food_item_preferences = analyze_residents_likes(data)
    
    a.append("Veg percentage: {:.2f}%".format(veg_percentage))
    a.append("\nCuisine preferences:")
    for cuisine, percentage in cuisine_preferences.items():
        a.append("\n- {}: {:.2f}%".format(cuisine, percentage))
    a.append("\nPreferred food items:")
    for food_item, percentage in food_item_preferences.items():
        a.append("\n- {}: {:.2f}%".format(food_item, percentage))
    
    str = " ".join(a)
    return str


# Create your views here.

def sell_food(request):
    return render(request, 'vendors/spoil.html')


def dashboard(request):
    output = analysis(data)
    return render(request,'vendors/dashboard.html',{'output':output})



