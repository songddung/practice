from collections import deque

direct = ((-1, 0), (1, 0), (0, -1), (0, 1))
direct_dict = {
    (-1, 0): "U A",
    (1, 0): "D A",
    (0, -1): "L A",
    (0, 1): "R A",
}


def caesar(message):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []

    for key in range(26):
        translated = ""

        for letter in message:
            if letter in uppercase:
                idx = (uppercase.index(letter) - key) % 26
                translated += uppercase[idx]
            else:
                translated += letter

        res.append(translated)

    return res


def backtrack(start, end, prev):
    path = []
    curr = end

    while curr != start:
        path.append(curr)
        curr = prev[curr[0]][curr[1]]

    path.append(start)
    path.reverse()

    return path


def bfs(ar, row, col, sy, sx, target):
    q = deque([(sy, sx)])
    v = [[False] * col for _ in range(row)]
    prev = [[None] * col for _ in range(row)]
    v[sy][sx] = True

    while q:
        y, x = q.popleft()

        for k in range(4):
            dy, dx = y + direct[k][0], x + direct[k][1]

            if 0 <= dy < row and 0 <= dx < col and not v[dy][dx]:
                if ar[dy][dx] == "G":
                    q.append((dy, dx))
                    v[dy][dx] = True
                    prev[dy][dx] = (y, x)

                    if (dy, dx) in target:
                        return backtrack((sy, sx), (dy, dx), prev)

    return False


def main():
    input_data = [10, 10, 1, 2, 0]
    input_map = [
        ["G", "G", "G", "R", "G", "G", "G", "R", "G", "X"],
        ["G", "R", "G", "G", "G", "R", "G", "G", "G", "G"],
        ["G", "R", "G", "R", "R", "G", "G", "W", "W", "G"],
        ["G", "G", "R", "T", "T", "R", "G", "W", "W", "G"],
        ["R", "G", "R", "T", "T", "R", "G", "W", "W", "G"],
        ["G", "G", "T", "T", "T", "T", "R", "R", "R", "R"],
        ["G", "R", "W", "W", "W", "T", "R", "G", "G", "G"],
        ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        ["A", "G", "G", "W", "W", "R", "R", "G", "G", "R"],
        ["G", "G", "G", "W", "W", "G", "R", "R", "G", "G"],
    ]
    input_ally = ["A", 100, "R", 1, 0]
    input_enemy = [
        ["X", 10],
    ]

    sy, sx = 0, 0
    target = []
    result = ""
    row, col = input_data[0], input_data[1]

    for i in range(row):
        for j in range(col):
            if input_map[i][j] == "A":
                sy, sx = i, j
            elif input_map[i][j] == "X":
                y, x = i, j

                for k in range(4):
                    for l in range(1, 4):
                        dy, dx = y + direct[k][0] * l, x + direct[k][1] * l

                        if 0 <= dy < row and 0 <= dx < col:
                            if input_map[dy][dx] == "G" or input_map[dy][dx] == "A":
                                target.append((dy, dx))
                            elif input_map[dy][dx] == "R" or input_map[dy][dx] == "T":
                                break

    if (sy, sx) in target:
        for k in range(4):
            for l in range(1, 4):
                dy, dx = sy + direct[k][0] * l, sx + direct[k][1] * l

                if 0 <= dy < row and 0 <= dx < col:
                    if input_map[dy][dx] == "X":
                        if k == 0:
                            result = "U F"
                        elif k == 1:
                            result = "D F"
                        elif k == 2:
                            result = "L F"
                        elif k == 3:
                            result = "R F"

                        break
    else:
        path = bfs(input_map, row, col, sy, sx, target)

        if path:
            dy, dx = path[1][0] - sy, path[1][1] - sx
            result = direct_dict.get((dy, dx), "S")

    print(result)


if __name__ == "__main__":
    main()