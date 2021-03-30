from utils import listAllFiles

def parseCodebase(folderPath):
    reactFiles = listAllFiles(folderPath)
    svelteFiles = []

    for reactFile in reactFiles:
        with open(reactFile, 'r') as file:
            svelteFiles.append((
                reactFile.replace(".jsx", ".svelte").replace(folderPath + "/", ""),
                reactToSvelte(file.read())))
    return svelteFiles
