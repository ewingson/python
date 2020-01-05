"""
experiment with a main menu and switch / case construction
"""
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
        """dispatch method / main menu with switch case / three tasks"""
        method_name = 'fall_' + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "nothing to compute")
        # Call the method as we return it
        return method()
  
    def fall_1(self):
        #emulate slow progress
        from time import sleep
        import sys
        i=0
        for i in range (12):
            sleep (0.5)
            sys.stdout.write (".")
            sys.stdout.flush()
        print("")   
        return "January"
  
    def fall_2(self):
        #output Switcher dictionary
        print (Switcher.__dict__)
        return "February"
  
    def fall_3(self):
        #return given string
        query = input ("gimme a string: ")
        return query

def main():
    foo = _Getch()
    char = "#"
    while (ord(char) != 52):
        print ("----------------------------")
        print ("| 1 : menu point one       |")
        print ("| 2 : menu point two       |")
        print ("| 3 : menu point three     |")
        print ("| 4 : ende                 |")
        print ("----------------------------")
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
