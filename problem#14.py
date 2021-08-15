from itertools import permutations

def solution(n, weak, dist):
    if len(weak) == 1:
        return 1
    
    dist.sort(reverse = True)
    
    for i in range(1, len(dist) + 1):
        for dist_per in list(permutations(dist[:i], i)):
            for start_index in range(len(weak)):
                search_list = weak[start_index:] + [n + x for x in weak[:start_index]]
                turn = 0
                while turn < i and search_list:
                    a = search_list[0]
                    b = dist_per[turn]
                    turn += 1
                    target = a + b
                    while search_list[0] <= target:
                        del search_list[0]
                        if len(search_list) == 0:
                            return i      
    return -1