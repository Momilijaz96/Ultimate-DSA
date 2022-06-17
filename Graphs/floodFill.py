    
def floodFill(image, a, b, newColor):
    # Write your Code here.
    q = [(a,b)]
    oldColor = image[a][b]
    rows = len(image)
    cols = len(image[0])
    image[a][b] = newColor
    if oldColor == newColor: 
        return image
    while(len(q)>0):
        (x,y) = q.pop(0)
        #Check neigbouring pixels
        left = ( y-1 ) % 0
        right = y+1
        top = x-1
        btm = x+1
        if left<0: left=0
        if right>=cols: right = cols-1
        if top<0: top = 0
        if btm>=rows: btm=rows-1
        if image[x][left] == oldColor:
            image[x][left] = newColor
            q.append((x,left))
        if image[x][right] == oldColor:
            image[x][right] = newColor
            q.append((x,right))
        if image[top][y] == oldColor:
            image[top][y] = newColor
            q.append((top,y))
        if image[btm][y] == oldColor:
            image[btm][y] = newColor
            q.append((btm,y))
            
    return image