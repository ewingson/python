#experiment with character read for main menu
class _Getch(object):
    """read character from stdin without return"""
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

class Switcher(object):
    def main_menu(self, argument):
        """dispatch method / main menu with switch case"""
        method_name = 'fall_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "nothing to compute")
        # Call the method as we return it
        return method()
  
    def fall_1(self):
        return "January"
  
    def fall_2(self):
        return "February"
  
    def fall_3(self):
        return "March"

def main():
    foo = _Getch()
    char = "#"
    print ("----------------------------")
    print ("| 1 : compute first month  |")
    print ("| 2 : compute second month |")
    print ("| 3 : compute third month  |")
    print ("| 4 : ende                 |")
    print ("----------------------------")
    while (char != "4"):
        char = foo.impl()
        wert = ord(char)
        choice = wert - 48
        #print (char + " _ " + str(wert))
        bar = Switcher()
        output = bar.main_menu(choice)
        print (output)
    print ("programmende")
		
if __name__ == "__main__":
    main()
