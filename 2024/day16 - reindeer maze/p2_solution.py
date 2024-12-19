from collections import defaultdict
from typing import Iterable, Iterator, Callable
from heapq import heappop, heappush


# Vector and PathState definitions
Vector = tuple[int, int]
PathState = tuple[Vector, Vector]

def iter_next_states(state: PathState, grid: dict):
    (r, c), (dr, dc) = state
    # Turn left
    yield 1000, ((r, c), (-dc, dr))
    # Turn right
    yield 1000, ((r, c), (dc, -dr))
    # Move forward
    next_pos = (r + dr, c + dc)  # This is a tuple
    if grid[next_pos] != '#':  # grid is a dictionary-like structure now
        yield 1, (next_pos, (dr, dc))

def parse_input(lines: Iterable[str]) -> tuple[dict, Vector, Vector]:
    """
    Parse the input and return a grid (as a defaultdict), a starting position, and an ending position.
    """
    grid = defaultdict(lambda: "#")  # grid is now a defaultdict
    start_pos, end_pos = None, None
    for r, row in enumerate(lines):
        for c, tile in enumerate(row):
            pos = (r, c)
            if tile == "S":
                start_pos = pos
            elif tile == "E":
                end_pos = pos
            grid[pos] = tile
    assert start_pos is not None and end_pos is not None
    return grid, start_pos, end_pos

def find_shortest_paths(
        start_state: PathState,
        end_pos: Vector,
        get_next_states: Callable[
            [PathState], Iterable[tuple[int, PathState]]
        ],
) -> tuple[int, Iterator[list[PathState]]]:
    """
    Find the shortest path between two points in a weighted graph using Dijkstra's algorithm.
    """
    costs: dict[PathState, int] = {}
    priority_queue: list[tuple[int, PathState]] = [(0, start_state)]
    prev_states: defaultdict[PathState, set[PathState]] = defaultdict(set)

    while priority_queue:
        cost, state = heappop(priority_queue)
        pos, *_ = state
        if pos == end_pos:
            break
        for weight, next_state in get_next_states(state, grid):
            prev_cost = costs.get(next_state, float("inf"))
            next_cost = cost + weight
            if next_cost < prev_cost:
                costs[next_state] = next_cost
                heappush(priority_queue, (next_cost, next_state))
                prev_states[next_state] = {state}
            elif next_cost == prev_cost:
                prev_states[next_state].add(state)
    else:
        raise RuntimeError("no path exists!")

    start_node, *_ = start_state
    def walk(state: PathState) -> Iterator[list[PathState]]:
        node, *_ = state
        if node == start_node:
            yield [state]
            return
        for prev_state in prev_states[state]:
            for path in walk(prev_state):
                yield path + [state]

    return cost, walk(state)


filename = 'input.txt'
with open(filename, 'r') as file:
    data = file.read().splitlines()
grid = [line.strip() for line in data]


grid, start_pos, end_pos = parse_input(grid)

# Example usage of find_shortest_paths
cost, paths = find_shortest_paths(
    start_state=(start_pos, (0, 1)),  # Starting state, facing east
    end_pos=end_pos,
    get_next_states=iter_next_states
)

# Just for the purpose of illustration, print the cost
print("Minimum cost:", cost)
# answer is 
