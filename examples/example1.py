from src.sat_functions import sat_solver, modify_subset, check_satisfiability_cached


# Give a set of clauses 
clauses = [
    [1],       # Clause 1: (x1)
    [-1, 2],   # Clause 2: (NOT x1 OR x2)
    [-2, 3],   # Clause 3: (NOT x2 OR x3)
    [-3, 4],   # Clause 4: (NOT x3 OR x4)
    [-4, 5],   # Clause 5: (NOT x4 OR x5)
    [-5, 6],   # Clause 6: (NOT x5 OR x6)
    [-6, 7],   # Clause 7: (NOT x6 OR x7)
    [-7, 8],   # Clause 8: (NOT x7 OR x8)
    [-8, 9],   # Clause 9: (NOT x8 OR x9)
    [-9, 10],  # Clause 10: (NOT x9 OR x10)
    [-10, 11], # Clause 11: (NOT x10 OR x11)
    [-11, 12], # Clause 12: (NOT x11 OR x12)
    [-12, 13], # Clause 13: (NOT x12 OR x13)
    [-13, 14], # Clause 14: (NOT x13 OR x14)
    [-14, 15], # Clause 15: (NOT x14 OR x15)
    [-15, 16], # Clause 16: (NOT x15 OR x16)
    [-16, 17], # Clause 17: (NOT x16 OR x17)
    [-17, 18], # Clause 18: (NOT x17 OR x18)
    [-18, 19], # Clause 19: (NOT x18 OR x19)
    [-19, -1]  # Clause 20: (NOT x19 OR NOT x1)
]


satisfied_clauses = sat_solver (clauses,num_particles=50, num_iterations=100)
print (satisfied_clauses)
