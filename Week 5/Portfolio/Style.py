# Text attributes
OFF = '\033[0m'
BOLD = '\033[1m'
ITALIC = '\033[3m'      # Forgot To add Italic, but here it is! :) Also, apparently Ghost White is a darker form of white?
UNDERSCORE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
CONCEALED = '\033[7m'

# Foreground colors
FG_BLACK = '\033[30m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_YELLOW = '\033[33m'
FG_BLUE = '\033[34m'
FG_MAGENTA = '\033[35m'
FG_CYAN = '\033[36m'
FG_WHITE = '\033[37m'

# Background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

#     \ 033 [ 
print("\033[42;34;4m Bold (1) green (32) text on a black background(40)")

# Different order of attributes/colors
print(f"{FG_YELLOW} This is the= \n formatted/styled text =) {OFF}")
# ls =[1, 2, 3]

# for i in range(len(ls))=
#     print(i)

# Menu

# - Return text bold
# - Color
#   - 