import sys
import heapq
from collections import namedtuple

State = namedtuple('State', ['path', 'current_cost', 'heuristic_cost'])


def prim_mst_cost(remaining_cities, dist):
    if not remaining_cities:
        return 0

    n = len(dist)
    key = [float('inf')] * n
    in_mst = [False] * n
    key[remaining_cities[0]] = 0
    mst_cost = 0

    for _ in range(len(remaining_cities)):
        u = min((v for v in remaining_cities if not in_mst[v]), key=lambda x: key[x])
        in_mst[u] = True
        mst_cost += key[u]

        for v in remaining_cities:
            if not in_mst[v] and dist[u][v] < key[v]:
                key[v] = dist[u][v]

    return mst_cost


def a_star_search(n, dist):
    pq = []
    heapq.heappush(pq, State([0], 0, 0))

    best_cost = sys.maxsize
    best_path = []

    while pq:
        state = heapq.heappop(pq)

        if len(state.path) == n:
            total_cost = state.current_cost + dist[state.path[-1]][0]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = state.path + [0]
            continue

        last_city = state.path[-1]
        remaining_cities = [i for i in range(n) if i not in state.path]

        mst_cost = prim_mst_cost(remaining_cities, dist)

        for city in remaining_cities:
            new_path = state.path + [city]
            heapq.heappush(pq, State(new_path, state.current_cost + dist[last_city][city], mst_cost))

    return best_path, best_cost


def main():
    n = int(input("Number of cities: "))
    dist = []

    print("Distances between cities matrix:")
    for i in range(n):
        dist.append(list(map(int, input().split())))

    best_path, best_cost = a_star_search(n, dist)

    print("Best path:", ' '.join(map(str, best_path)), " with cost:", best_cost)


if __name__ == "__main__":
    main()
