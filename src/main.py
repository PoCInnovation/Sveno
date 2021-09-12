from utils import listAllFiles, pathResolver
import sys
from parseReact import parseCodebase
from generator import createTree, generateSvelteCodebase
# from fileDependencies import resolveFileDependencies

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
    return pathResolver(argv[1]), pathResolver(argv[2])

def main(argv: list) -> None:
    oldFolder, newFolder = argumentsHandling(argv)
    files = listAllFiles(oldFolder)
    createTree(oldFolder, newFolder, files)
    res = parseCodebase(files)
    # res = resolveFileDependencies(res)
    generateSvelteCodebase(oldFolder, newFolder, res)
    print("Done !")

if __name__ == '__main__':
    main(sys.argv)