# Examples

This folder contains examples to demonstrate the use of the SAT Solver.

Before running the examples, make sure that Python can find the modules in the `src` directory. If Python is not able to find the modules, you can modify the `PYTHONPATH` to include the path to the `src` directory in your project:

```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project"
```

## Example 1
This example takes a predefined set of clauses and applies the SAT solver to them:

```python 
from src.sat_functions import sat_solver

# Define a set of clauses
clauses = [
    # ...
    # Add your clauses here
    # ...
]

# Solve the SAT problem with the defined clauses
satisfied_clauses = sat_solver(clauses, num_particles=50, num_iterations=100)

# Print the resulting clauses
print(satisfied_clauses)

```


## Example 2
This example demonstrates how to read clauses from a CNF file, solve the SAT problem, and write the resulting clauses to a new CNF file:
```python
from src.sat_functions import sat_solver, write_clauses_to_cnf, read_cnf

# Read clauses from a CNF file
clauses = read_cnf('./sample.cnf')

# Solve the SAT problem with the read clauses
satisfied_clauses = sat_solver(clauses, num_particles=50, num_iterations=100)

# Write the resulting clauses to a new CNF file
write_clauses_to_cnf(satisfied_clauses, 'result.cnf')

# Print a completion message
print('Results is saved in result.cnf')

```
