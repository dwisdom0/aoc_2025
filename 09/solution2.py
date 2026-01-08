from tqdm import tqdm


def read_input(fpath: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    with open(fpath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    points = []
    for line in lines:
        points.append(tuple([int(idx) for idx in line.split(",")]))

    line_segments = []
    for next_i, point in enumerate(points, start=1):
        # needs to wrap around to connect the last point to the first point
        line_segments.append((point, points[next_i % len(points)]))

    return line_segments


def solve(data: list[tuple[int, int]]) -> int:
    # I don't even know how to figure out whether a tile is valid
    # my first thought is a signed distance function
    # but idk where to even start for that
    # or triangulate?
    # for every point I could shoot a ray in the cardinal directions
    # and if one doesn't hit any line segemnts then the point is outside

    # but that could actually be wrong too
    # if there's a pocket
    #   #--------------#
    #   |   #-------#  |
    #   |   |   ^   |  |
    #   |   |  <p>  |  |
    #   #---#   v   |  |
    #               |  |
    #               |  |
    #      #--------#  |
    #      |           |
    #      #-----------#
    #
    # then that point would say it's inside
    # even though it's not
    # so I need to do like a flood from the edges I guess
    # to find every point that has some path to the edge
    # without crossing over any line segments

    # I feel like there must be a better way
    # that doesn't require explictly modeling the whole thing

    max_area = 0
    for c0 in tqdm(data, ascii=True):
        for c1 in data:
            width = max(c0[0], c1[0]) - min(c0[0], c1[0]) + 1
            height = max(c0[1], c1[1]) - min(c0[1], c1[1]) + 1
            area = width * height
            if area > max_area:
                max_area = area

    return max_area


def main():
    data = read_input("input.txt")
    print(solve(data))


if __name__ == "__main__":
    main()
