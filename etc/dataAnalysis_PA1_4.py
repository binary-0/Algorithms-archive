import json

# 레시피 정보
recipes = {
    "Vegetable_Stir_Fry": ["Carrot", "Bell_Pepper", "Soy_Sauce"],
    "Carrot_Soup": ["Carrot", "Chicken_Broth", "Cream"],
    "Garlic_Chicken": ["Garlic", "Butter", "Rosemary"],
    "Onion_Rings": ["Onion", "Flour", "Egg"],
    "Garlic_Bread": ["Bread", "Garlic", "Butter"]
}

# 재료별 칼로리 값 정보 
ingredient_calories = {
    "Carrot": 25, "Bell_Pepper": 20, "Soy_Sauce": 5, 
    "Chicken_Broth": 15, "Cream": 300,"Garlic": 5, 
    "Butter": 1024, "Rosemary": 0, "Onion": 40, 
    "Flour": 500, "Egg": 155, "Bread": 265  
}

BMR = 0
recommCal = 0

if health_data[0] == "male":
	BMR = 88.362 + (13.397 * health_data[1]) + (4.799 * health_data[2]) - (5.677 * health_data[3])
else:
	BMR = 447.593 + (9.247 * health_data[1]) + (3.092 * health_data[2]) - (4.330 * health_data[3])
	
recommCal = int((BMR * 1.55) / 3)

N_sorted_names_by_calories = []
calcList = []

for key, val in recipes.items():
	sumCalorie = 0
	for ingred in val:
		sumCalorie += ingredient_calories[ingred]
	if sumCalorie <= recommCal:
		calcList.append([key, sumCalorie])

calcList.sort(reverse=True, key=lambda x: x[1])

for item in calcList:
	N_sorted_names_by_calories.append(item[0])
 
 # N_sorted_names_by_calories 리스트 변수 값을 출력
print(N_sorted_names_by_calories)