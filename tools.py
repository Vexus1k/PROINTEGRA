from random import shuffle


class Tools:
    @staticmethod
    def random_color() -> str:
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange', 'brown', 'black',
                  'white', 'gray', 'gold', 'silver', 'navy blue', 'sky blue', 'lime green', 'teal', 'indigo',
                  'magenta', 'violet', 'khaki', 'salmon', 'crimson', 'lavender', 'plum', 'blue violet', 'olive',
                  'cyan', 'maroon', 'beige', 'turquoise']
        shuffle(colors)
        return colors[0]
