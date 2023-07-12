# SAT Solver

This project provides a set of Python modules and scripts for working with the Boolean satisfiability problem (SAT). This problem is fundamental in mathematical logic, computer science, and artificial intelligence.

## Installation

To install this project and all its dependencies, you can use pip:

```bash
pip install -r requirements.txt
```

## Usage
The main functions of the project are provided in the src directory. Here's a basic example of how you can use the SAT solver:

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
For more usage examples, please see the examples directory.
```


## Testing
You can run the test suite with the following command:

```python
python -m unittest discover tests
```

## Contributing
We welcome contributions to this project! Please see the CONTRIBUTING.md file for more information.

## License
This project is licensed under the terms of [the Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0)

## Contact
- Zeyd Boukhers: [zeyd.boukhers@fit.fraunhofer.de](mailto:zeyd.boukhers@fit.fraunhofer.de)
