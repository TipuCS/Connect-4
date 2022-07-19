import pygame

# CONSTANTS
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 583
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)
GREEN = (30, 180, 90)
BROWN = (64, 41, 10, 0.5)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


global sizeOfCoinX
global sizeOfCoinY
sizeOfCoinX = 50
sizeOfCoinY = 50


for i in range(6, -1, -1):
  print(i)

coin_Y = (pygame.image.load(r'yellow coin.jpg'))
coin_Y = pygame.transform.scale(coin_Y, (sizeOfCoinX, sizeOfCoinY))
coin_R = (pygame.image.load(r'red coin.jpg'))
coin_R = pygame.transform.scale(coin_R, (sizeOfCoinX, sizeOfCoinY))
coin_N = (pygame.image.load(r'neutral coin.png'))
coin_N = pygame.transform.scale(coin_N, (sizeOfCoinX, sizeOfCoinY))


# PYGAME SETUP
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Chess')

# self.boardList = [
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
# ]
#Column: 1  2  3  4  5  6  7
# Row:1 [0, 0, 0, 0, 0, 0, 0],
# Row:2 [0, 0, 0, 0, 0, 0, 0],
# Row:3 [0, 0, 0, 0, 0, 0, 0],
# Row:4 [0, 0, 0, 0, 0, 0, 0],
# Row:5 [0, 0, 0, 0, 0, 0, 0],
# Row:6 [0, 0, 0, 0, 0, 0, 0],

# 

# COLORS:
# 0: None
# 1: RED
# 2: YELLOW

global redWon
global yellowWon
yellowWon = False
redWon = False

class Board():
  def __init__(self):
    self.boardPosition = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
    self.x = 10
    self.y = 10
    self.width = 500 
    self.height = 500
    self.redTurn = False

  def update(self):
    self.isItWon()
  
  def isItWon(self):
    redWon = False
    yellowWon = False
    if (self.isItWonInStraightHorizontal("red")):
      print("RED WON")
      redWon = True
    if (self.isItWonInStraightHorizontal("yellow")):
      print("YELLOW WON")
      yellowWon = True

    if self.isItWonStraightVertical("red"):
      print("RED WON 524332")
      redWon = True
    if self.isItWonStraightVertical("yellow"):
      print("YELLOW WON")
      yellowWon = True

    if self.isItWonStraightDiagonally("red"):
      print("RED WON")
      redWon = True
    if self.isItWonStraightDiagonally("yellow"):
      print("YELLOW WON")
      yellowWon = True
    if (redWon == True):
      drawText("RED WON", 550, 100, 50, RED)
    if (yellowWon == True):
      drawText("YELLOW WON", 550, 100, 50, YELLOW)

  def isItWonInStraightHorizontal(self, color):
    if color.lower() == "red":
      colorNum = 1
    elif color.lower() == "yellow":
      colorNum = 2

    # for each row, check if there is 4 of the same color
    for row in range(0, 6):
      for i in range(0, 4):
        itIsSameColor = True
        for j in range(0, 4):
          if not (self.boardPosition[row][i + j] == colorNum):
            itIsSameColor = False
        if (itIsSameColor):
          return True
    return False
      
  def isItWonStraightVertical(self, color):
    if color.lower() == "red":
      colorNum = 1
    elif color.lower() == "yellow":
      colorNum = 2
    
    # for each row, check if there is 4 of the same color
    for column in range(0, 7):
      for i in range(0, 3):
        itIsSameColor = True
        for j in range(0, 4):
          if not (self.boardPosition[i + j][column] == colorNum):
            itIsSameColor = False
        if (itIsSameColor):
          return True
    return False

  def isItWonStraightDiagonally(self, color):
    if color.lower() == "red":
      colorNum = 1
    elif color.lower() == "yellow":
      colorNum = 2
    # checking diagonal top left to bottom right
    for row in range(0, 3):
      for column in range(0, 4):
        isItSameColor = True
        for i in range(0, 4):
          if not (self.boardPosition[row + i][column + i] == colorNum):
            isItSameColor = False
        if (isItSameColor):
          return True

    # checking diagonal top right to bottom left
    for row in range(3, 6, 1):
      for column in range(0, 4, 1):
        isItSameColor = True
        for i in range(0, 4, 1):
          if not (self.boardPosition[row - i][column + i] == colorNum):
            isItSameColor = False
        if (isItSameColor):
          return True
    return False
      
  
  def addCoinToColumn(self, column):
    if (self.redTurn):
      color = "red"
      self.redTurn = False
    else:
      color = "yellow"
      self.redTurn = True
    
    #self.redTurn = -self.redTurn
    row = self.getLowestRowInColumn(column)
    if not(row == 0):
      self.addCoinToPos(row, column, color)
  
  def addCoinToPos(self, row, column, color):
    if color.lower() == "red":
      colorNum = 1
    elif color.lower() == "yellow":
      colorNum = 2
    else:
      print("ERROR NO COLOR INPUTTED WHATTTTT")
    # set the color at the position
    self.boardPosition[row-1][column-1] = colorNum

  def getLowestRowInColumn(self, column):

    # if the top item is a coin then row is empty so return 0

    coinNum = self.boardPosition[0][column-1]
    if (coinNum == 1) or (coinNum == 2):
      return 0
    
    row = 6
    for i in range(5, -1, -1):
      coinNum = self.boardPosition[i][column-1]
      if (coinNum == 1) or (coinNum == 2):
        row = i

    return row

  def drawTurnText(self):
    if (self.redTurn):
      color = RED
    else:
      color = YELLOW
    drawBox(self.x, 510, self.width, 100, color)
  
  def drawBoard(self):
    # draw the background
    x = self.x
    y = self.y
    width = self.width
    height = self.height

    gapBetweenCoinsX = (width - (sizeOfCoinX*7))/8
    gapBetweenCoinsY = (height - (sizeOfCoinY*6))/7
    
    
    drawBox(x, y, width, height, BLUE)

    # draw Coins
    for i in range(1, 8):
      for j in range(1, 7):
        if (self.boardPosition[j-1][i-1]) == 0:
          coin = coin_N
        elif (self.boardPosition[j-1][i-1]) == 1:
          coin = coin_R
        elif (self.boardPosition[j-1][i-1]) == 2:
          coin = coin_Y
        drawCoin(coin, x + (i * sizeOfCoinX) + (i * gapBetweenCoinsX) - sizeOfCoinX, y + (j * sizeOfCoinY) + (j * gapBetweenCoinsY) - sizeOfCoinY)
      
class Button():
  def __init__(self, numberID, x, y, width, height, color):
    self.numberID = numberID
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color

class Mouse():
  def __init__(self):
    self.buttonList = []
    self.leftClickLocked = False
  
  def update(self, boardObj):
    buttonClicked = self.isAnyButtonClicked()
    if not (buttonClicked == False):
      print("a button clicked")
      boardObj.addCoinToColumn(buttonClicked.numberID)

  def addButtonToList(self, numberID, x, y, width, height, color):
    button = Button(numberID, x, y, width, height, color)
    self.buttonList.append(button)
  
  def isAnyButtonClicked(self):
    # get the button that's clicked
    for button in self.buttonList:
      # is button Clicked
      if self.isButtonClicked(button.x, button.y, button.width, button.height):
        return button
    return False
    
  def drawButtonList(self):
    for button in self.buttonList:
      drawBox(button.x, button.y, button.width, button.height, button.color)

  def isButtonClicked(self, buttonX, buttonY, buttonWidth, buttonHeight):
    
    if (pygame.mouse.get_pressed()[0] == False):
      self.leftClickLocked = False
    # LEFT CLICKED
    if (self.leftClickLocked == False):
      if pygame.mouse.get_pressed()[0] == True:
        coordPosition = pygame.mouse.get_pos()
        # IS CLICK INSIDE BOX
        if (coordPosition[0] > buttonX) and (coordPosition[0] < buttonX + buttonWidth):
          if (coordPosition[1] > buttonY) and (coordPosition[1] < buttonY + buttonHeight):
            self.leftClickLocked = True
            return True
    return False
  
def returnSmallestNumber(a, b):
  if a == b:
    return a
  elif a > b:
    return b
  else:
    return a

def drawCoin(coin, x, y):
  window.blit(coin, (x, y))

def drawBox(x, y, width, height, color):
  pygame.draw.rect(window, (color), (x, y, width, height))


def drawText(text, x, y, size, color):
  arialFont = pygame.font.SysFont('arial', size)
  textRenderer = arialFont.render(text, False, color)
  window.blit(textRenderer, (x, y))


def drawBackGround():
  drawBox(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE)


def getLetterWidth(letter, size):
  arialFont = pygame.font.SysFont('arial', size)
  textRenderer = arialFont.render(letter, False, BLACK)
  return textRenderer.get_width()


def getLetterHeight(letter, size):
  arialFont = pygame.font.SysFont('arial', size)
  textRenderer = arialFont.render(letter, False, BLACK)
  return textRenderer.get_height()

def printBoard(boardPosition):
  for line in boardPosition:
    print(line)

def makeButtonsAndAddThem(boardObj, mouseObj):  
  coin_X_difference = boardObj.width / 7
  gapBetweenCoinsX = (boardObj.width - (sizeOfCoinX*7))/8
  x = boardObj.x
  y = boardObj.y + boardObj.height -24
  width = sizeOfCoinX
  height = 20
  color = GREEN
  for i in range(1, 8):
    button = Button(i,  x + (i * sizeOfCoinX) + (i * gapBetweenCoinsX) - sizeOfCoinX, y, width, height, color)
    mouseObj.buttonList.append(button)

def drawText(text, x, y, size, color):
  arialFont = pygame.font.SysFont('arial', size)
  textRenderer = arialFont.render(text, False, color)
  window.blit(textRenderer, (x, y))
  
    # for i in range(1, 8):
    #   drawBox(x + (i * sizeOfCoinX) + (i * gapBetweenCoinsX) - sizeOfCoinX)
  #   #     drawCoin(coin, x + (i * sizeOfCoinX) + (i * gapBetweenCoinsX) - sizeOfCoinX, y + (j * sizeOfCoinY) + (j * gapBetweenCoinsY) - sizeOfCoinY)

  #   gapBetweenCoinsX = (width - (sizeOfCoinX*7))/8
  #   gapBetweenCoinsY = (height - (sizeOfCoinY*6))/7
  # x = 
  # y = 10
  # mouseObj.addButtonToList(self, 0, x, y, width, height, color)

# self.boardList = [
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
# ]
boardPosition = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]
boardPosition = [[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]]

def running():
  # run once at start
  run = True
  boardObj = Board()
  mouseObj = Mouse()
  makeButtonsAndAddThem(boardObj, mouseObj)
  boardObj.boardPosition = boardPosition
  #button = Button()
  #mouseObj.addButtonToList(self, 0, x, y, width, height, color)


  # boardObj.addCoinToPos(3, 4, "red")
  # boardObj.addCoinToPos(3, 6, "red")
  # boardObj.addCoinToPos(3, 5, "yellow")
  #boardObj.addCoinToPos(3, 6, "red")
  ##print(boardObj.getLowestRowInColumn(6))
  
  while run:
    for event in pygame.event.get():
      
      # QUITTING
      if event.type == pygame.QUIT:
        run = False    

      # PROGRAM
      drawBackGround()
      boardObj.drawBoard()
      mouseObj.drawButtonList()
      #drawCoin(coin_Y, 10, 10)
      #drawCoin(coin_R, 50, 10)
      # HDFAJKSHJFB J-= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX -= FIX 
      mouseObj.drawButtonList()
      boardObj.drawTurnText()
      mouseObj.update(boardObj)
      boardObj.update()

      #boardObj.addCoinToPos(3, 5, "red")

      print("red won state:", redWon)
      

      # drawText("RED WON", 550, 100, 50, RED)
      
      pygame.display.flip()

running()
