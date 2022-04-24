"""
Math 260
Project 3
Spring 2022

Partner 1: Matilde Molinari Giglietti
Partner 2: Parinay Gupta
Date:
"""

# Import math and p3tests.
import math
from p3tests import *

################################################################################

"""
detectArbitrage

This function will find any arbitrage opportunity.

INPUTS
adjList: the adjacency list representing the currencies graph.
adjMat: the adjacency matrix representing the exchange rates.
tol: tolerance value set at 1e-15 as default.

OUTPUTS
A single list of vertex ranks corresponding to the negative cost cycle.
"""

## Performs Bellman Ford

def detectArbitrage(adjList, adjMat, tol=1e-15):
    
    # Set initial dist and prev attributes.
    for vertex in adjList:
        vertex.dist = math.inf
        vertex.prev = 0
    adjList[0].dist = 0     

    # Perform the |V| − 1 iterations.
    for iter in range(0, len(adjList) - 1):
        # Look at each vertex.
        for u in adjList:
            # Check each neighbor of u.
            # Update predictions and previous vertex.
            for n in u.neigh:
                # Only update if the new value is better!
                if n.dist > u.dist + adjMat[u.rank][n.rank] + tol:
                    n.dist = u.dist + adjMat[u.rank][n.rank]
                    n.prev = u

    # Perform one more bellman ford iteration to find negative cycle.
    for u in adjList:
        # Check each neighbor of u.
        # Update predictions and previous vertex.
        for n in u.neigh:
            if n.dist > u.dist + adjMat[u.rank][n.rank] + tol:
                # Negative cycle exists, print the cycle.
                negative_cycle = [n, u]
                # Trace backwards to find cycle loop, stop if complete cycle.
                while u.prev not in negative_cycle:
                        negative_cycle.append(u.prev)
                        # Keep track of vertex that got updated
                        u = u.prev
                negative_cycle.append(u.prev)

    return []

################################################################################

"""
rates2mat
Builds the adjacency matrix
"""
def rates2mat(rates):

    return [[-math.log(R) for R in row] for row in rates]

"""
Main function.
"""
if __name__ == "__main__":
    testRates()
