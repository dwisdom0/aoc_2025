from tqdm import tqdm
from copy import deepcopy
from collections import deque, defaultdict
from dataclasses import dataclass

@dataclass
class Timeline:
    cur_step: tuple[int, int]
    hit_splitters: set

def read_input(fpath: str) -> list[str]:
    with open(fpath, 'r') as f:
        lines = f.readlines()
    
    data = [line.strip() for line in lines]
    return data




def solve(manifold: list[str]) -> int:
    start_idx = manifold[0].index('S')

    beams = deque()
    beams.append((0, start_idx))

    timelines = [Timeline(cur_step=(0, start_idx), hit_splitters=set())]
    num_timelines = 0
    max_iter = 100

    for _ in tqdm(range(150)):
        print(f"{len(timelines)=}")
        if len(timelines) == 0:
            return num_timelines
        new_timelines = []
        for timeline in timelines:
            new_row = timeline.cur_step[0] + 1
            col = timeline.cur_step[1]

            # if we hit the bottom, this timeline is done
            if new_row == len(manifold) - 1:
                num_timelines += 1
                continue

            # if we hit a splitter, this beam is done
            # and we have to start two new beams
            # by copying the history of the current timeline
            # and adding on the next step
            if manifold[new_row][col] == '^':
                if (new_row, col) in timeline.hit_splitters:
                    print(f'already hit: ({new_row}, {col})')
                    continue
                timeline.hit_splitters.add((new_row, col))

                # make a copy for the right side
                timeline_r = deepcopy(timeline)
                timeline_r.cur_step = (new_row, col+1)
                new_timelines.append(timeline_r)

                # use the current timeline as the left side
                timeline.cur_step = (new_row, col-1)
                new_timelines.append(timeline)




            # if we didn't hit a splitter, continue searching downward
            else:
                timeline.cur_step = (new_row, col)
                new_timelines.append(timeline)

        timelines = deepcopy(new_timelines)
        max_iter -= 1
            
    return num_timelines










def main():
    data = read_input('input.txt')
    print(solve(data))

if __name__ == '__main__':
    main()
