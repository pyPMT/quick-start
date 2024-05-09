# Step 1: Import the config variable, the required encoder and the search technique
import os
from pypmt.apis import solve
from pypmt.config import config
from pypmt.encoders.basic import EncoderSequential
from pypmt.planner.SMT import SMTSearch

# Step 2: Set the encoder and search technique in the configuration
config.set('encoder', EncoderSequential)
config.set('search', SMTSearch)

# Step 3: Define the path to the domain and problem files
domainfile = os.path.join(os.path.dirname(__file__), 'numeric-pddl-problem/domain.pddl')
problemfile = os.path.join(os.path.dirname(__file__), 'numeric-pddl-problem/problem.pddl')

# Step 4: Call the solve function with the domain and problem files
plan = solve(domainfile, problemfile)
print(plan)

