with open('input/4.txt') as f:
    data = [x for x in f.read().splitlines()]

def search_word(grid, word):
    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # 8 directions
    occurrences = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_from_position(x, y, dx, dy):
                    occurrences.append(((x, y), (dx, dy)))
    return occurrences

print(f"Part 1: {len(search_word(data, 'XMAS'))}")
