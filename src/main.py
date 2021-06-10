import sys
from parser import parseCodebase
from generator import generateSvelteCodebase

def usage(binary: str) -> None:
    print(
"""DESCRIPTION
\tSveno is a way to transpile react components to sveno code
HOW TO USE
\t{binary} [react folder] [newly svelte created folder]
""".format(binary = binary), end="")

def argumentsHandling(argv: list) -> None:
    if len(argv) == 2 and (argv[1] == '-h' or argv[1] == '--help'):
        usage(argv[0])
        sys.exit(0)
    if len(argv) != 3:
        print("Wrong nb of arguments, run with -h to get help", file=sys.stderr)
        sys.exit(84)

def main(argv: list) -> None:
    res = ""
    argumentsHandling(argv)
    res = parseCodebase(argv[1])
    generateSvelteCodebase(argv[2], res)

if __name__ == '__main__':
    main(sys.argv)