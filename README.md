# pracitce_recipes_db
practicing application/sql/db relations

simple application allowing the storage of a recipe database with a few fields.

the application can implement two methods on the data set

"all" and "find" 
- where find must be followed by indication of the search condition

## Setup

```shell

# Enter the directory
; cd recipes_directory


# Run the app
; python app.py

# Get all records
python3 app.py get_all

# find method with specified condition
% python3 app.py find --condition "rating=2"
```

