import time, os, random

WIDTH = os.get_terminal_size()[0] - 1
DELAY = 0.5

FISH_ASCII = [
    "     |\    O  ",
    "|\   /__\    o ",
    "|-\ /____.\ o  ",
    "|--|_______(   ",
    "|-/ \_____/    ",
    "|/   \___/     ",
    "      |/       "
]

#determining size of shape using the most number of elements in line
FISH_HEIGHT = len(FISH_ASCII)
FISH_WIDTH = max(len(line) for line in FISH_ASCII)
FISH_PROBABILITY = 0.002  # Probability of a fish appearing

CLOUD_TEMPLATE = [
    "                                (               )_   ",
    "          ____                _(                   ) ",
    "        (        )_          (_                   )  ",
    "     (               )_           (_ __  --   _  )   ",
    "   _(                   )                            ",
    "  (_                   )                             ",
    "       (_ __  --   _  )              ____            ",
    "                                   (        ).       "
]
CLOUD_TEMPLATE_HEIGHT = len(CLOUD_TEMPLATE)
CLOUD_TEMPLATE_WIDTH = len(CLOUD_TEMPLATE[0])

CLOUD_X_REPEAT = WIDTH // CLOUD_TEMPLATE_WIDTH
next_rows = []
step = 0

try:
    while True:
        while len(next_rows) < (FISH_HEIGHT + 1):
            next_rows.append(list(CLOUD_TEMPLATE[step % CLOUD_TEMPLATE_HEIGHT] * CLOUD_X_REPEAT))
            next_rows[-1].extend(' ' * (WIDTH - len(next_rows[-1])))
            step += 1

        for x in range(WIDTH - FISH_WIDTH):
            if random.random() < FISH_PROBABILITY:
                for i, line in enumerate(FISH_ASCII):
                    for j, char in enumerate(line):
                        if char != ' ':
                            next_rows[i][x + j] = char

        row = next_rows[0]
        del next_rows[0]
        print(''.join(row))
        if step % 10 == 0:
            time.sleep(DELAY)
        
except KeyboardInterrupt:
    print("Clouds and Fish, inspired by Skulls and Hearts, Al Sweigart")


