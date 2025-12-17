import math
from collections import Counter

from tqdm import tqdm


def read_input(fpath: str) -> list[tuple[int, int, int]]:
    with open(fpath, "r") as f:
        coord_lists = [line.strip().split(",") for line in f.readlines()]

    data = []
    for coord_list in coord_lists:
        coords = []
        for coord in coord_list:
            coords.append(int(coord))
        data.append(tuple(coords))

    return data


def euclid_dist(v0: tuple[int, int, int], v1: tuple[int, int, int]) -> float:
    sum_of_squares = 0
    for pair in zip(v0, v1):
        sum_of_squares += (pair[1] - pair[0]) ** 2
    return math.sqrt(sum_of_squares)


def calc_dist_mat(data: list[tuple[int, int, int]]) -> list[list[float]]:
    dist_mat = []
    for v1 in data:
        row = []
        for v2 in data:
            row.append(euclid_dist(v1, v2))
        dist_mat.append(row)

    return dist_mat


def find_smallest_unconnected(
    dist_mat: list[list[float]], connections: set[tuple]
) -> tuple[int, int]:
    global_min_dist = 1e20
    global_min_idx = None
    for i, row in enumerate(dist_mat):
        for j, dist in enumerate(row):
            # only search the upper triangle
            # not including the diagonal of 0s
            if j <= i:
                continue
            if (i, j) in connections:
                continue
            if dist < global_min_dist:
                global_min_dist = dist
                global_min_idx = (i, j)

    assert isinstance(global_min_idx, tuple)
    return global_min_idx


def solve(data: list[tuple[int, int, int]]) -> int:
    dist_mat = calc_dist_mat(data)
    connections = set()
    id_to_circuit = {i: i for i in range(len(data))}
    for _ in tqdm(range(1000)):
        proposed_con = find_smallest_unconnected(dist_mat, connections)
        c0 = id_to_circuit[proposed_con[0]]
        c1 = id_to_circuit[proposed_con[1]]
        # if they're already in the same circuit, record that we found that connection
        # so that we don't keep finding it
        if c0 == c1:
            connections.add(proposed_con)
            connections.add((proposed_con[1], proposed_con[0]))
            continue
        # add c1 to c0's circuit
        # and add everything that used to be in c1's circuit to c0's circuit
        ids_to_update = [k for k, v in id_to_circuit.items() if v == c1]
        for id_to_update in ids_to_update:
            id_to_circuit[id_to_update] = c0

        connections.add(proposed_con)
        connections.add((proposed_con[1], proposed_con[0]))

    circuit_counts = Counter([v for k, v in id_to_circuit.items()])
    top_3 = [x[1] for x in circuit_counts.most_common(3)]
    return top_3[0] * top_3[1] * top_3[2]


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
