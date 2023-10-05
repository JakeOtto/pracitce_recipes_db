from lib.database_connection import DatabaseConnection
from lib.recipe_repository import *
import argparse


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("recipe_directory_db.sql")


recipe_repository = Recipe_repository(connection)


# Retrieve all artists
def get_all():
    recipes = recipe_repository.all()
    for recipe in recipes:
        print(recipe)

def find(condition):
    results = recipe_repository.find(condition)
    print (results)

def main():
    parser = argparse.ArgumentParser(description="Recipe Repository CLI")
    parser.add_argument("action", choices=["get_all", "find"], help="Action to perform")
    parser.add_argument("--condition", help="Search condition for 'find' action")

    args = parser.parse_args()

    if args.action == "get_all":
        get_all()
    elif args.action == "find":
        find(args.condition)

if __name__ == "__main__":
    main()

