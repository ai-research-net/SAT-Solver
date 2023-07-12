from src.sat_functions import sat_solver, modify_subset, check_satisfiability_cached, write_clauses_to_cnf, read_cnf

#read clauses from file 
clauses = read_cnf('./sample.cnf')

#solve the set of clauses
satisfied_clauses = sat_solver (clauses,num_particles=50, num_iterations=100)

#save the solved set 
write_clauses_to_cnf(satisfied_clauses, 'result.cnf')
print ('Results is saved in result.cnf')
