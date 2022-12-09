class Folder:
    def __init__(self, name, parent):
        self.size = "NaN"
        self.name = name
        self.parent = parent
        self.files = {}
        self.folders = {}

    def calcFolderSize(self):
        global allFolders
        self.size = sum(self.files.values())
        for f in self.folders.values():
            self.size += f.calcFolderSize()

        allFolders[self.name] = self.size

        return self.size

    def solvePart1(self):
        ans1 = 0
        for folder in self.folders.values():
            ans1 += folder.size if folder.size <= 100000 else 0
            ans1 += folder.solvePart1()
        return ans1

    # Returns the smallest folder that meets the target
    def solvePart2(self, target):
        ans2 = 70000000

        for folder in self.folders.values():
            if folder.size >= target:
                if folder.size < ans2:
                    ans2 = folder.size
            subsizes = folder.solvePart2(target)
            if subsizes < ans2:
                ans2 = subsizes
        return ans2



def createTree():
    file = open('2022/Day 7/input.txt').readlines()
    instructions = [x.strip().split() for x in file]

    homefolder = Folder('/', '')
    currentdirectory = homefolder

    for i in instructions[1:]:
        if i[0] == '$':
            if i[1] == 'cd':
                if i[2] == '/':
                    currentdirectory = homefolder
                elif i[2] == '..':
                    currentdirectory = currentdirectory.parent
                else:
                    # print(currentdirectory.folders)
                    currentdirectory = currentdirectory.folders[i[2]]
            elif i[1] == 'ls':
                pass
        else:
            if i[0] == 'dir':
                currentdirectory.folders[i[1]] = Folder(i[1], currentdirectory)
            else:
                currentdirectory.files[i[1]] = int(i[0])

    return homefolder


allFolders = {}
homefolder = createTree()
TOTALSPACE = 70000000
NEEDEDSPACE = 30000000
TARGETSIZE = TOTALSPACE - NEEDEDSPACE

used = homefolder.calcFolderSize()
toremove = used - TARGETSIZE
smallest = TOTALSPACE
for folder in allFolders:
    if allFolders[folder] >= toremove:
        if allFolders[folder] < smallest:
            smallest = allFolders[folder]

print('The answer to part 1: ', homefolder.solvePart1())
print('The answer to part 2: ', homefolder.solvePart2(toremove))
