# Step 1: Import the solve function from the pypmt.apis module
from pypmt.apis import solve, dump_smtlib
import os

# Step 2: Define the path to the domain and problem files, and the file to dump the encoding
domainfile = os.path.join(os.path.dirname(__file__), 'numeric-pddl-problem/domain.pddl')
problemfile = os.path.join(os.path.dirname(__file__), 'numeric-pddl-problem/problem.pddl')
dump_smtlib_file = os.path.join(os.path.dirname(__file__), 'dump.smt2')

# Step 3: Call the solve function with the domain, problem dumpfiles files, the bound and the configuration name
dump_smtlib(domainfile, problemfile, dump_smtlib_file, bound=10, config_name="seq")
