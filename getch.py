"""
os-independent(windows and unixoid) read character in a loop without return and output ascii-value break on #
"""
class _Getch(object):
    """this will go into the docstring. the programm reads a character from stdin (which usually is the keyboard), outputs its ascii-value and the loop is terminated by the hashsign. it will work on windows- and unixoid systems."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): 
        return self.impl()

class _GetchUnix(object):
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows(object):
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

def main():
    foo = _Getch()
    print (_Getch.__doc__)
    while True:
        char = foo.impl()
        wert = ord(char)
        print (char + " _ " + str(wert))
        if (char == "#"):
            break
    print ("programmende")
		
if __name__ == "__main__":
    main()
