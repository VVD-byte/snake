DISPLAY_SIZE = (640, 480)
COLOR = {
    'white':(255, 255, 255),
    'black':(0, 0, 0),
    0:(255, 255, 255),
    1:(125, 125, 125),
    2:(255, 0, 0),
}
BACKGROUNG_COLOR = COLOR['black']
BLOCK_SIZE = 50
MARGIN = 0
START_X = DISPLAY_SIZE[0] - (BLOCK_SIZE + 2) * (DISPLAY_SIZE[0]//(BLOCK_SIZE + MARGIN))
START_Y = DISPLAY_SIZE[1] - (BLOCK_SIZE + 2) * (DISPLAY_SIZE[1]//(BLOCK_SIZE + MARGIN))
SNAKE_SPEED = 3
