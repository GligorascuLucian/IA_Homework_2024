import sys
import heapq
from collections import namedtuple


State = namedtuple('State', ['path', 'current_cost'])


def uniform_cost_search(n, dist):
    pq = []
    heapq.heappush(pq, State([0], 0))

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
        for i in range(n):
            if i not in state.path:
                new_path = state.path + [i]
                heapq.heappush(pq, State(new_path, state.current_cost + dist[last_city][i]))

    return best_path, best_cost


def main():
    n = int(input("Number of cities: "))
    dist = []

    print("Distances between cities matrix:")
    for i in range(n):
        dist.append(list(map(int, input().split())))

    best_path, best_cost = uniform_cost_search(n, dist)

    print("Best path:", ' '.join(map(str, best_path)), " with cost:", best_cost)


if __name__ == "__main__":
    main()
