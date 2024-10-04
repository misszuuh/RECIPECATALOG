import requests


url = "http://127.0.0.1:8000"

def authentication(username, password):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"username": username, "password": password}
    resp = requests.post(f"{url}/login/", headers=headers, data=data)
    if resp.status_code == 200:
        return resp.json()["access_token"]
    return None


def list_recipes(token):
    if not token:
        print("Failed to authenticate")
        return
    resp = requests.get(f"{url}/recipes/", headers={"Authorization": f"Bearer {token}"})
    if resp.status_code == 200:
        recipes = resp.json()
        for i, recipe in enumerate(recipes, 1):
            print("*" * 25)
            print(f"{i}: {recipe['name']}")
            print(recipe["ingredients"])
            print(recipe["instructions"])
            print(recipe["prep_time"])
            print(recipe["cooking_time"])
            print(recipe["total_time"])
    else:
        print("Failed to fetch recipes")
        print(resp.text)


def add_recipe(token):
    if not token:
        print("Failed to authenticate")
        return

    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ")
    instructions = input("Enter instructions: ")
    prep_time = input("Enter you prep_time: ")
    cooking_time = input("Enter you cook_time: ")
    total_time = input("Enter you total_time:")

    
    data = {
        "name": name,
        "ingredients": ingredients,
        "instructions": instructions,
        "prep_time": prep_time,
        "cooking_time": cooking_time,
        "total_time": total_time,
    }
    
    resp = requests.post(f"{url}/recipes/", headers={"Authorization": f"Bearer {token}"}, json=data)
    if resp.status_code == 201:
        print("Recipe added successfully!")
    else:
        print("Failed to add recipe")
        print(resp.text)


def update_recipe(token):
    if not token:
        print("Failed to authenticate")
        return
    recipe_id = input("Enter the ID of the recipe to update: ")
    name = input("Enter new recipe name: ")
    ingredients = input("Enter new ingredients (comma-separated): ")
    instructions = input("Enter new instructions: ")
    prep_time = input("Enter new prep time: ")
    cooking_time = input("Enter new cooking_time: ")
    total_time = input("Enter new total_time: ")
    
    data = {
        "name": name,
        "ingredients": ingredients.split(','),
        "instructions": instructions,
        "prep_time": prep_time,
        "cooking_time": cooking_time,
        "total_time": total_time
    }
    
    resp = requests.put(f"{url}/recipes/{recipe_id}/", headers={"Authorization": f"Bearer {token}"}, json=data)
    if resp.status_code == 200:
        print("Recipe updated successfully!")
    else:
        print("Failed to update recipe")
        print(resp.text)

    

def delete_recipe(token):
    if not token:
        print("Failed to authenticate")
        return
    recipe_id = input("Enter the ID of the recipe to delete: ")
    
    resp = requests.delete(f"{url}/recipes/{recipe_id}/", headers={"Authorization": f"Bearer {token}"})
    if resp.status_code == 204:
        print("Recipe deleted successfully!")
    else:
        print("Failed to delete recipe")
        print(resp.text)

def search_recipe(token):
    if not token:
        print("Failed to authenticate")
        return
    query = input("Enter the name of the recipe to search: ")
    
    resp = requests.get(f"{url}/recipes/?search={query}", headers={"Authorization": f"Bearer {token}"})
    if resp.status_code == 200:
        recipes = resp.json()
        if recipes:
            for i, recipe in enumerate(recipes, 1):
                print("*" * 25)
                print(f"{i}: {recipe['name']}")
                print(recipe["ingredients"])
                print(recipe["instructions"])
                print(recipe["prep_time"])
                print(recipe["cooking_time"])
                print(recipe["total_time"])
        else:
            print("No recipes found.")
    else:
        print("Failed to search recipes")
        print(resp.text)

print("Welcome to Recipe Catalog Management System")
while True:
    print("""
Choose a Choice:
          
1. Register
2. Login          
0. Exit
""")
    
    Choice = input("Your input: ")

    
    if Choice == '2':
        print("Please enter credentials")
        username = input("Username: ")
        password = input("Password: ")
        token= authentication(username=username, password=password)
        if not token :
            print('Invalid credentials')
            break
        print("Logged In Successfully!")

        while True:
            print("""
Choose a Choice:

1. List all recipes
2. Add recipe
3. Update recipe
4. Delete recipe
5. Search recipe
6. Logout
""")    

            logged_in_Choice = input("Your input: ")

            if logged_in_Choice == '1':
             list_recipes(token)
            elif logged_in_Choice == '2':
                add_recipe(token)
            elif logged_in_Choice == '3':
                update_recipe(token)
            elif logged_in_Choice == '4':
                delete_recipe(token)
            elif logged_in_Choice == '5':
                search_recipe(token)
            elif logged_in_Choice == '6':
                    print('Successfully logged out')
                    break
            else:
                print("\n\nInvalid Option selected\n\n")
    elif Choice == '0':
        print("Thank you for using the app")
        break
    else:
        print("\n\nInvalid option selected\n\n")



        





















# import requests

# url = "http://127.0.0.1:8000"

# def authentication(username, password):
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}
#     data = {"username": username, "password": password}
#     resp = requests.post(f"{url}/login/", headers=headers, data=data)
#     if resp.status_code == 200:
#         return resp.json()["access_token"]
#     return None

# def list_recipes(token):
#     if not token:
#         print("Failed to authenticate")
#         return
#     resp = requests.get(f"{url}/posts/", headers={"Authorization": f"Bearer {token}"})
#     if resp.status_code == 200:
#         posts = resp.json()
#         for i, post in enumerate(posts, 1):
#             print("*" * 25)
#             print(f"{i}: {post['name']}")
#             print(post["ingredients"])
#             print(post["instructions"])
#     else:
#         print("Failed to fetch posts")
#         print(resp.text)

# print("Welcome to the Recipe Catalog Management")
# while True:
#     print("""
# Choose an Option:

# 1. Login
# 0. Exit
# """)
#     option = input("Your input: ")

#     if option == '1':
#         print("Please enter credentials")
#         username = input("Username: ")
#         password = input("Password: ")
#         token = authentication(username=username, password=password)
#         if not token:
#             print('Invalid credentials')
#             break
#         print("Successfully Logged In")
#         while True:
#             print("""
# Choose an option:

# 1. List posts
# 0. Logout
# """)
#             logged_in_option = input("Your input: ")
#             if logged_in_option == '1':
#                 list_recipes(token)
#             elif logged_in_option == '0':
#                 print('Successfully logged out')
#                 break
#             else:
#                 print("\n\nInvalid Option selected\n\n")
#     elif option == '0':
#         print("Thank you for using the app")
#         break
#     else:
#         print("\n\nInvalid option selected\n\n")




























