def parse_input():
    with open("input.txt") as fh:
        data = fh.read().split("\n\n")
        numbers = [int(number) for number in data[0].split(",")]
        boards = []
        for board_str in data[1:]:
            boards.append([
                [int(number.strip()) for number in board_row_str.split()]
                for board_row_str in board_str.split("\n")
            ])
        return numbers, boards


def check_board_won(board, board_matches):
    col_counters = {}
    sun_unmatched = 0
    won = False
    for row_idx in range(len(board)):
        row_counter = 0
        for col_idx in range(len(board[row_idx])):
            col_counters.setdefault(col_idx, 0)
            if board_matches.get(row_idx, {}).get(col_idx):
                col_counters[col_idx] += 1
                row_counter += 1
                if col_counters[col_idx] == 5:
                    won = True
            else:
                sun_unmatched += board[row_idx][col_idx]
        if row_counter == 5:
            won = True
    return won, sun_unmatched


def yield_winning_board_and_score(numbers, boards):
    board_matches = {}
    for number in numbers:
        for board_idx, board in enumerate(boards):
            board_matches.setdefault(board_idx, {})
            for row_idx, row in enumerate(board):
                board_matches[board_idx].setdefault(row_idx, {})
                for col_idx, board_number in enumerate(row):
                    board_matches[board_idx][row_idx].setdefault(col_idx, False)
                    if board_number == number:
                        board_matches[board_idx][row_idx][col_idx] = True
            won, sum_unmarked_numbers = check_board_won(board, board_matches[board_idx])
            if won:
                yield board_idx, sum_unmarked_numbers * number

def part_1(numbers, boards):
    _, score = next(yield_winning_board_and_score(numbers, boards))
    return score


def part_2(numbers, boards):
    boards_won = set()
    for board_idx, score in yield_winning_board_and_score(numbers, boards):
        boards_won.add(board_idx)
        if len(boards_won) == len(boards):
            return score


numbers, boards = parse_input()
print(f"Part 1 = {part_1(numbers, boards)}")
print(f"Part 2 = {part_2(numbers, boards)}")
