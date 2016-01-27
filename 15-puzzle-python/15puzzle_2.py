import pprint


pp = pprint.PrettyPrinter(indent=4)


def solve_puzzle_astar(start, end):
    # initialize frontier
    frontier = [[heuristic_manhattan(start), start]]

    # initialize expanded nodes
    expanded_nodes = []
    amount_expanded_nodes = 0

    # iterate while frontier is not empty
    while frontier:
        i = 0
        for j in range(1, len(frontier)):
            if frontier[i][0] > frontier[j][0]:
                i = j
        path = frontier[i]
        frontier = frontier[:i] + frontier[i + 1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded_nodes:
            continue
        for k in moves(endnode):
            if k in expanded_nodes:
                continue
            newpath = [path[0] + heuristic_manhattan(k) - heuristic_manhattan(endnode)] + path[1:] + [k]
            frontier.append(newpath)
            expanded_nodes.append(endnode)
        amount_expanded_nodes += 1
    print "Expanded nodes:", amount_expanded_nodes
    print "Solution:"
    pp.pprint(path)


def moves(mat):
    """
    lists the possible moves
    """
    output = []

    m = eval(mat)
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0);  # blank space (zero)

    if i > 0:
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]  # move up
        output.append(str(m))
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]

    if i < 3:
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]  # move down
        output.append(str(m))
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]

    if j > 0:
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]  # move left
        output.append(str(m))
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]

    if j < 3:
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]  # move right
        output.append(str(m))
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]

    return output


def heuristic_manhattan(puzzle):
    distance = 0
    m = eval(puzzle)
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0:
                continue
            distance += abs(i - (m[i][j] / 4)) + abs(j - (m[i][j] % 4))
    return distance


puzzle = str([[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 14, 0, 10]])
end = str([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
solve_puzzle_astar(puzzle, end)
