"""
The following is a description of the instance of this famous puzzle involving
n=2 eggs and a building with k=36 floors.
Suppose that we wish to know which stories in a 36-story building are safe
to drop eggs from, and which will cause the eggs to break on landing.
We make a few assumptions:

…..An egg that survives a fall can be used again.
…..A broken egg must be discarded.
…..The effect of a fall is the same for all eggs.
…..If an egg breaks when dropped, then it would break if dropped from a higher floor.
…..If an egg survives a fall then it would survive a shorter fall.
…..It is not ruled out that the first-floor windows break eggs, nor is it ruled out
   that the 36th-floor do not cause an egg to break.

If only one egg is available and we wish to be sure of obtaining the right result,
the experiment can be carried out in only one way.
Drop the egg from the first-floor window; if it survives,
drop it from the second floor window.
Continue upward until it breaks. In the worst case,
this method may require 36 droppings. Suppose 2 eggs are available.
What is the least number of egg-droppings that is guaranteed to work in all cases?
The problem is not actually to find the critical floor,
but merely to decide floors from which eggs should be dropped
so that total number of trials are minimized.

1) Optimal Substructure:
When we drop an egg from a floor x, there can be two cases
(1) The egg breaks
(2) The egg doesn’t break.

1) If the egg breaks after dropping from xth floor,
then we only need to check for floors lower than x with remaining eggs;
so the problem reduces to x-1 floors and n-1 eggs

2) If the egg doesn’t break after dropping from the xth floor,
then we only need to check for floors higher than x;
so the problem reduces to k-x floors and n eggs.

Since we need to minimize the number of trials in worst case,
we take the maximum of two cases. We consider the max of above two cases
for every floor and choose the floor which yields minimum number of trials.

  k ==> Number of floors
  n ==> Number of Eggs
  eggDrop(n, k) ==> Minimum number of trials needed to find the critical
                    floor in worst case.
  eggDrop(n, k) = 1 + min{max(eggDrop(n - 1, x - 1), eggDrop(n, k - x)):
                 x in {1, 2, ..., k}}


"""

def eggDrop_recursion_memoization(n, k, cache):
    """

    :param n: number of eggs.
    :param k: number of floors.
    :return x optimal number of attempts.
    """
    if k == 0 or k == 1:
        #You need to drop one egg only on this floor.
        return k
    if n == 1:
        #you need to drop this egg from each floor
        # starting from the bottom floor to find the correct floor.
        return k
    min = -1
    for x in range(1, k+1):
        if cache[n-1][x-1] == -1:
            cache[n-1][x-1] = eggDrop_recursion_memoization(n-1, x-1, cache)
        if cache[n][k-x] == -1:
            cache[n][k-x] = eggDrop_recursion_memoization(n, k-x, cache)
        #Consider all droppings from 1st floor to kth floor
        max_value = max(cache[n-1][x-1],
                        cache[n][k - x])
        if min == -1:
            min = max_value
        elif max_value < min:
            min = max_value
    return min + 1 #consider the egg dropped on this floor.


def eggDrop(n, k):
    cache = [[-1 for y in range(k+1)] for x in range(n+1)]
    return eggDrop_recursion_memoization(n,k,cache)

def eggDropNonRecursion(n,k):
    cache = [[-1 for y in range(k + 1)] for x in range(n + 1)]

    #fill up the case where there is one egg.
    for x in range(k+1):
        cache[0][x] = 0
        cache[1][x] = x

    #fill up the case where there is one floor.
    for x in range(n+1):
        cache[x][0]=0
        cache[x][1]=1

    #for each row (total number of eggs)
    for x in range(2, n+1):
        #for each column (total number of floors)
        for y in range(2, k+1):
            for z in range(1,y+1):
                res = 1 + max(cache[x-1][z-1], cache[x][y-z])
                if cache[x][y] == -1:
                    cache[x][y] = res
                elif res < cache[x][y]:
                    cache[x][y] = res
    return cache[n][k]

k=30
for n in range(1, 10):
    print("Minimum number of attempts needed in worst case with {} floors and {} eggs is {}."
          .format(k, n, eggDrop(n, k)))
for n in range(1, 10):
    print("Non recurse:"
          "Minimum number of attempts needed in worst case with {} floors and {} eggs is {}."
          .format(k, n, eggDropNonRecursion(n, k)))
