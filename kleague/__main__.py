import sys
sys.path.append('kleague')
from kleague.cli import CLI
from kleague.ui import GUI

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Hello World!")

    gui = GUI()
    gui.run()

    # cli = CLI()
    # cli.run()


if __name__ == "__main__":
    main()