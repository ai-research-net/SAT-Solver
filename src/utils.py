from pysat.solvers import Solver
from pysat.formula import CNF
import random
from itertools import combinations
from tqdm import tqdm
from functools import lru_cache


def remove_short_lists (list_of_lists):
    # calculate the lengths of the lists
    lengths = [len(lst) for lst in list_of_lists]

    # calculate mean and standard deviation of the lengths
    mean_len = sum(lengths) / len(lengths)
    std_dev_len = (sum((x - mean_len) ** 2 for x in lengths) / len(lengths)) ** 0.5

    # split the lists into short and long based on mean
    short_lists = [lst for lst in list_of_lists if len(lst) < mean_len]
    long_lists = [lst for lst in list_of_lists if len(lst) - mean_len > std_dev_len]

    # for every deleted short list, duplicate a long one
    for i in range(len(short_lists)-1):
        long_lists.append(random.choice(long_lists))

    # the result is the non-short lists + duplicated long lists
    result = [lst for lst in list_of_lists if len(lst) >= mean_len] + long_lists
    return result



def get_first_longest_valid_list(clauses_tuple, subsets, check_satisfiability_cached):
    sorted_subsets = sorted(subsets, key=len, reverse=True)
    for subset in sorted_subsets:
        #if check_satisfiability(clauses, subset):
        if check_satisfiability_cached(clauses_tuple, tuple(sorted(subset))):
            sorted_longest_subset = sorted(subset)
            satisfied_clauses = [clauses_tuple[x] for x in sorted_longest_subset]
            return satisfied_clauses
    return []
