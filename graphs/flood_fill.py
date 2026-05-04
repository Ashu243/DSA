from collections import deque
image =  [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2


def flood_fill(image, sr, sc, color):
    # if the image has already the same as color
    if image[sr][sc] == color:
        return image
    
    original_pixel = image[sr][sc]
    
    # change the pixel 
    image[sr][sc] = color
    row = len(image)
    col = len(image[0])
    queue = deque([(sr, sc)])
    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        i, j = queue.popleft()

        for dr, dc in directions:
            nr = dr+i
            nc = dc+j

            if nr>=0 and nr < row and nc>=0 and nc<col:
                if image[nr][nc] == original_pixel:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        
    return image

print(flood_fill(image, sr, sc, color))


