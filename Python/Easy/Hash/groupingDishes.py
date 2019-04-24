def groupingDishes(dishes = {}):
    ingredients_dishes = {}

    menu = [dishes[idx][0] for idx in range(len(dishes))]

    dish_ingredients = {}
    for dish in dishes:
        dish_ingredients[dish[0]] = dish[1:]

    for dish, ingredients in dish_ingredients.items():
       for ingredient in ingredients:
           if ingredient not in ingredients_dishes:
                ingredients_dishes[ingredient] = [dish]
                continue
           if ingredient  in ingredients_dishes:
               ingredients_dishes[ingredient].append(dish)
    results = []

    for ingredient, dishes in sorted(ingredients_dishes.items()):
        if len(dishes) > 1:
            ingredients_dishes[ingredient] = sorted(dishes)
            results.append([ingredient] + sorted(dishes))

    return results

if __name__ == '__main__':
    dishes = [["Salad","Tomato","Cucumber","Salad","Sauce"],
 ["Pizza","Tomato","Sausage","Sauce","Dough"],
 ["Quesadilla","Chicken","Cheese","Sauce"],
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]
    print(groupingDishes(dishes))

