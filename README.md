## Restaurant Recipes API ##

This project implements a FastAPI-based for managing recipes in a restaurant, utilizing SQLAlchemy for database interactions and Pydantic for data validation. The API allows users to perform CRUD operations (Create, Read, Update, Delete) on the recipes and filter them by total preparation time (prep time + cooking time).

## How to Set Up and Run the Application ##

    Prerequisites 

        [-Python 3.8+ installed on your system
         -PostgreSQL installed and a database named restaurant created
         -FastAPI, SQLAlchemy, and other necessary dependencies installed ]

    Setup Instructions and run the application 
      1.Create a virtual environment: 

          python -m venv venv
          source venv/bin/activate 

     2.If you have generated a requirements.txt file, you can manually install the required libraries.
       also you can install fastapi and sqlalchemy
           pip install fastapi[all]
           pip install sqlalchemy
     3.Start the FastAPI application using Uvicorn.
         Note: Before starting the FastAPI application using Uvicorn, make sure you open the folder that contains your application. For example, if your main folder is called RECIPECATALOG, and inside it, there is another folder called app, ensure that you navigate to that folder. Inside the app folder, you should have files such as main.py, models.py, schema.py, and database.py. Once you're in the correct folder, you can start the FastAPI application.

           uvicorn main:app --reload

     4.Access the application.

        After starting the server, your FastAPI application will be accessible at:
           http://127.0.0.1:8000
           
    5.Access the API documentation.

       FastAPI automatically generates interactive API documentation using Swagger:
          Swagger UI: http://127.0.0.1:8000/docs


## API Endpoints ##

   ## GET /recipes - Retrieve all recipes ##

    Purpose: Fetch all recipes from the database.
    Response: A list of all recipes with details such as name, ingredients, instructions, prep time, and cooking time.

   ## GET /recipes/{recipe_id} - Retrieve a specific recipe by ID ##

    Purpose: Fetch a recipe by its unique id.
    Path Parameter: recipe_id (integer) - The ID of the recipe.
    Response: The recipe details if found, or a 404 Not Found error if the recipe doesn't exist.

   ## POST /recipes - Add a new recipe ##

    Purpose: Create a new recipe by providing necessary details.
    Request Body: A JSON object containing the recipe information.


   ## PUT /recipes/{recipe_id} - Update an existing recipe ##

    Purpose: Update the details of an existing recipe by its ID.
    Path Parameter: recipe_id (integer) - The ID of the recipe to update.
    Request Body: The updated recipe information.

  ## DELETE /recipes/{recipe_id} - Remove a recipe from the catalog ##

    Purpose: Delete a specific recipe by its id.
    Path Parameter: recipe_id (integer) - The ID of the recipe to delete.
    Response: A success message or a 404 Not Found error if the recipe doesn't exist.

  ## GET /recipes?total_time - Filter recipes by total time (prep time + cooking time) ##

     Purpose: Retrieve all recipes that can be prepared within a given total time.
     Query : i use for loop to implement this.
     Response: A list of recipes matching the total time criteria, or an empty list if none match.

## Assumptions and Design Decisions ##
    Database: The API uses PostgreSQL as the database. You must have a PostgreSQL instance running and the database restaurant created.
    Model Design: The Restaurant model represents a recipe with fields like name, ingredients, instructions, prep_time, and cooking_time.
    Error Handling: Proper error handling is implemented to return 404 Not Found for missing resources and 400 Bad Request for invalid inputs.
    Validation: Pydantic models are used for validating request bodies and ensuring the data structure is correct before any database interaction occurs. 


## Authentication ##
Once the project is up and running, you can continue by managing recipes, users, and authentication through the provided API endpoints and using the CLI for additional operations like database initialization and task automation.

## Routers: ##
We use router object to be able to split up all of our routers or path operations into different files and then we import them just by calling , FastAPI routers also Router prefix then add a specific group name tag

    recipe.py: Handles all the operations related to managing recipes.
    user.py: Manages user registration, login
    auth.py: Manages user authentication logic.
    oauth.py: Implements OAuth2 authorization mechanisms.

## CLI:##
In app open folder called CLI inside that folder open file called CLI.py 
    cli.py: Command Line Interface for managing tasks like initializing the database, CRUD, registration, login and other tasks users want to perform.

 ## General adds ##

    User Authentication: Registration and login functionality.
    Authorization: OAuth2 implemented for secure access to the API.
    Recipe Management: Endpoints for CRUD recipes.
    CLI Tools: Custom command-line tools for managing app functionality. 