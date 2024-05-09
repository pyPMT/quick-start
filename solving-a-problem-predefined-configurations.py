# Step 1: Import the solve function from the pypmt.apis module
from pypmt.apis import solve
import os

# Step 2: Define the path to the domain and problem files
domainfile = os.path.join(os.path.dirname(__file__), 'numeric-pddl-problem/domain.pddl')
problemfile = os.path.join(os.path.dirname(__file__), 'numeric-pddl-problem/problem.pddl')

# Step 3: Call the solve function with the domain and problem files
plan = solve(domainfile, problemfile, "r2e")
print(plan)



from pypmt.config import config
from pypmt.encoders.basic import EncoderSequential
from pypmt.planner.SMT import SMTSearch

config.set('encoder', EncoderSequential)
config.set('search', SMTSearch)
plan = solve(domainfile, problemfile)

