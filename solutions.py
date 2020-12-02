"""
This file is used for dynamically loading each of the solutions, and keeping the clutter out of the main.py file
"""

total_loaded = 0 # used for the count of loaded solutions
try: # when this errors it will stop
    for i in range(25): # try to import all
        exec(f"from workspace import day{i + 1}") # import one of the functions, will error if it doesnt exist
        exec(f"day{i + 1} = day{i + 1}()") # initialize it
        total_loaded += 1 # add one since it was sucessfull
except: # once it fails, if it does
    pass
