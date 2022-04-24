# Arbitrage
MATH 260 Final Project
This project is centered on the use of the Bellman-Ford algorithm in detecting arbitrage opportunities among a group of currency exchanges rates. Arbitrage here corresponds to finding a cycle of currencies that, when converted between each other in a specific order, result in a net increase in value when returned to the original currency. The BellmanFord algorithm is typically used to find the shortest path between two vertices in a weighted, directed graph. However, with a clever setup, we can use this algorithm to detect arbitrage cycles.

This process is performed constantly in the market, and is the reason that exchange rates are not mis-priced. The moment that one rate becomes mis-priced by even a fraction of a penny, someone’s algorithm will detect it and take advantage of the opportunity. That trade realigns the prices and fixes the mis priced exchange rate.

This project involves writing code to implement the Bellman-Ford algorithm and uses it to detect arbitrage opportunities in several test sets of provided exchange rates.
