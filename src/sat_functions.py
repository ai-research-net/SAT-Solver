from pysat.solvers import Solver
from pysat.formula import CNF
import random
from itertools import combinations
from tqdm import tqdm
from functools import lru_cache
from src.utils import remove_short_lists, get_first_longest_valid_list

def read_cnf(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Filter out comment lines and problem line
    lines = [line.strip() for line in lines if line[0] not in 'cp']

    # Split each line into a list of integers (excluding the trailing '0')
    # and convert each number from DIMACS to 0-based index format
    clauses = [[int(num) for num in line.split()[:-1]] for line in lines]
    clauses = [clause for clause in clauses if clause]

    return clauses


def write_clauses_to_cnf(clauses, filename):
    with open(filename, 'w') as f:
        # Write the problem line (p cnf #vars #clauses)
        f.write('p cnf {} {}\n'.format(max(max(clause) for clause in clauses), len(clauses)))
        
        # Write each clause
        for clause in clauses:
            clause_str = ' '.join(map(str, clause)) + ' 0\n'
            f.write(clause_str)


def check_satisfiability(clauses, indices):
    # Create a new Solver instance
    s = Solver()
    
    # Add the clauses specified by the indices to the solver
    for index in indices:
        s.add_clause(clauses[index])
    
    # Check and return satisfiability
    return s.solve()

@lru_cache(maxsize=None)
def check_satisfiability_cached(clauses,indices):
    # Wrap your satisfiability checking function with caching
    return check_satisfiability(list(clauses), list(indices))


# val is the random value that decides whether add or remove 
def modify_subset(clauses_tuple, subset, N=5, val=None, stabilize = False):
    if val is None:
        val = random.random()
    # Copy the subset to avoid modifying the input
    subset = subset.copy()

    # Randomly decide whether to add or remove a clause
    if len(subset) == 0 or val < 0.5:
        # Add a clause
        available_indices = set(range(len(clauses_tuple))) - set(subset)
        if available_indices:
            new_clause_index = random.choice(list(available_indices))

            # Check if the subset remains satisfiable after adding the new clause
            #if check_satisfiability(clauses, subset + [new_clause_index]):
            if check_satisfiability_cached(clauses_tuple, tuple(sorted(subset + [new_clause_index]))):
                # If yes, add the clause
                subset.append(new_clause_index)
            elif not stabilize:
                subsubset_indices = list(set(subset))
                # Form N unique subsubsets
                N = min(N, len(subsubset_indices))  # replace 10 with desired N value
                subsubsets = [sorted([new_clause_index]+ list(i)) for i in combinations(subsubset_indices, N)]
                satisfiable_count = sum(check_satisfiability_cached(clauses_tuple, tuple(sorted(subsubset))) for subsubset in subsubsets)
                if  satisfiable_count / N > random.random():
                    subset.append(new_clause_index)

    else:
        
        # Remove a clause
        remove_clause_index = random.choice(subset)
        remaining_indices = list(set(subset) - {remove_clause_index})
        tem_subset = subset[:remove_clause_index] + subset[remove_clause_index+1:]
        
        check1 = check_satisfiability_cached(clauses_tuple, tuple(sorted(tem_subset)))
        check2 = check_satisfiability_cached(clauses_tuple, tuple(sorted(subset)))
        
        if check1 and not check2:
            subset.remove(remove_clause_index) 
            #print ('remove with confidence')
        elif check1 and check2 and not stabilize:
            #print ('remove although both true')
            if (len(subset)/len(clauses_tuple)) > random.random():
                subset.remove(remove_clause_index)
        elif not stabilize:
            #print ('remove with both false')
            # Form N unique subsubsets
            N = min(N, len(remaining_indices))  
            subsubsets = [sorted([remove_clause_index] + list(i)) for i in combinations(remaining_indices, N)]
            satisfiable_count = sum(check_satisfiability_cached(clauses_tuple, tuple(sorted(subsubset))) for subsubset in subsubsets)
            if (N - satisfiable_count) / N > random.random():
                subset.remove(remove_clause_index)
    return subset


def sat_solver (clauses,num_particles=50, num_iterations=100):
    clauses_tuple = tuple([tuple(clause) for clause in clauses])

    #if check_satisfiability(clauses, set(range(len(clauses)))):
    if check_satisfiability_cached(clauses_tuple, tuple(sorted(set(range(len(clauses)))))):
        print ('the set is already satisfied')
        satisfied_caluses = clauses
    else:
        # Create 100 subsets using a list comprehension
        subsets = [list(range(len(clauses))) for _ in range(num_particles)]

        for iteration in tqdm(range (num_iterations)):

            if iteration == int(num_iterations * 0.4) or iteration == int(num_iterations * 0.8):
                subsets = remove_short_lists(subsets)
            stabilize = True if iteration >= int(num_iterations * 0.8) else False

            for i in range (len(subsets)):
                if iteration / num_iterations <0.2: #burn out (20%)
                    subsets[i] = modify_subset(clauses_tuple, subsets[i], N=5, val=0.6, stabilize = stabilize)
                else:
                    subsets[i] = modify_subset(clauses_tuple, subsets[i], N=5, stabilize = stabilize)

        #now get the longest list 
        # Find the longest sublist

        satisfied_clauses = get_first_longest_valid_list(clauses_tuple, subsets, check_satisfiability_cached)
    return satisfied_clauses
