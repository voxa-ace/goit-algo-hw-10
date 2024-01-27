from pulp import LpProblem, LpVariable, LpMaximize, value, PULP_CBC_CMD

# Defining the optimization problem
model = LpProblem("Maximize-Production", LpMaximize)

# Variables that represent the amount of lemonade and fruit juice produced
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Creating a silver object with output disabled
solver = PULP_CBC_CMD(msg=False)

# Resource settings
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Resource utilization rates
water_per_lemonade = 2
sugar_per_lemonade = 1
lemon_juice_per_lemonade = 1
fruit_puree_per_juice = 2
water_per_juice = 1

# Goal function: maximizing the total number of products produced
model += lemonade + fruit_juice

# Resource constraints
model += water_per_lemonade * lemonade + water_per_juice * fruit_juice <= water_limit
model += sugar_per_lemonade * lemonade <= sugar_limit
model += lemon_juice_per_lemonade * lemonade <= lemon_juice_limit
model += fruit_puree_per_juice * fruit_juice <= fruit_puree_limit

# Solving the problem
model.solve(solver)

# Output of results
lemonade_output = value(lemonade)
fruit_juice_output = value(fruit_juice)
total_production = lemonade_output + fruit_juice_output

print(f"Lemonade Production: {lemonade_output} units, Fruit Juice Production: {fruit_juice_output} units")
print(f"Total Number of Products: {total_production} units")
