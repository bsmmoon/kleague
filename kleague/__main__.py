import sys
sys.path.insert(0, 'kleague')
from cli.CLI import CLI

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    print("Hello World!")

    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()