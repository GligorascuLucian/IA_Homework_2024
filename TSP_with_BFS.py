from collections import deque
import sys


def bfs_tsp(n, dist):
    queue = deque()
    queue.append((0, [0], 0))

    best_cost = sys.maxsize
    best_path = []

    while queue:
        current_city, path, current_cost = queue.popleft()

        if len(path) == n:
            total_cost = current_cost + dist[current_city][0]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = path + [0]
            continue

        for next_city in range(n):
            if next_city not in path:
                new_path = path + [next_city]
                new_cost = current_cost + dist[current_city][next_city]
                queue.append((next_city, new_path, new_cost))

    return best_path, best_cost


def main():
    n = int(input("Number of cities: "))
    dist = []

    print("Distances between cities matrix:")
    for i in range(n):
        dist.append(list(map(int, input().split())))

    best_path, best_cost = bfs_tsp(n, dist)

    print("Best path:", ' '.join(map(str, best_path)), " with cost:", best_cost)


if __name__ == "__main__":
    main()
