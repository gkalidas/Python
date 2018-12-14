import sys;
from collections import defaultdict

oldLibs = ["msvcm90.dll","msvcr90.dll","mfc90.dll","msvcp90.dll", "mfc90u.dll" ,"mfcm90.dll", "mfcm90u.dll",
           "msvcrt.dll", "crtdll.dll", "msvcm80.dll","msvcr80.dll","mfc80.dll", "msvcp80.dll", "mfc80u.dll" ,
           "mfcm80.dll", "mfcm80u.dll", "msvcp71.dll", "msvcr71.dll", "msvcirt.dll"]

depMap = defaultdict(list)
paths = []
leaders = set()

def reversePath(path) :
    res = ""
    for i in reversed(range(len(path))):
        res = res + path[i]
        if i != 0 : 
            res = res + " -> "
    return res

def printPaths(parentMapV2, path) : 
    curnode =  path[-1]
    if curnode in  parentMapV2:
        deps = list(parentMapV2[curnode])
        for dep in deps : 
            newPath = list(path)
            newPath.append(dep)
            printPaths(parentMapV2,  newPath)
    else : 
        res = reversePath(path)
        if not res in paths :
            paths.append(res)
    
def traverseDepChain(exe): 
    stk = [exe]
    visited = [] 
    parentMap = {}
    parentMapV2 = defaultdict(list)
    printed = False

    while len (stk) > 0 :
        dep = stk.pop() ; 
        visited.append(dep)
        if dep in oldLibs : 
            continue 

        newDeps = depMap[dep]
        for newDep in newDeps : 
            if not newDep in visited or newDep in leaders :
                stk.append(newDep)

            if not newDep in parentMapV2 :
                parentMapV2[newDep] = [dep]
            else : 
                parentMapV2[newDep].append(dep)

    for node in parentMapV2 :
        if node in oldLibs : 
             printPaths(parentMapV2, [node])
             printed = True
    
    return printed 

def libdep_main(depFile):
    with open(depFile) as fDep:
        lines = fDep.readlines()
        inDll = False;
        binaryName = ""
        for line in lines:
            isExe = line.rstrip().endswith(".exe")
            isDll = line.startswith("Dump of file") 
            if (isExe or isDll): 
                if(binaryName != ""):
                    if binaryName not in depMap :
                       depMap[binaryName] = depList
                    else :
                        for dep in depMap[binaryName]:
                            if not dep in depList :
                                depList.append(dep)
                        depMap[binaryName] = depList

                binaryName =  line.split("/")[-1].rstrip().lower()
                inDll = True
                depList = []
                continue
            
            if inDll and line.startswith(" "):
                depName = line.strip().rstrip().lower()
                depList.append(depName)

    for bin in set(depMap.keys()):
        traverseDepChain(bin)
          
    paths.sort()  
    lastRoot = ""
    for path in paths: 
        root = path.split(" -> ")[0];
        if(lastRoot != root) :
            print("")
            lastRoot = root 
        sys.stdout.write(path + "\n")

if __name__ == "__main__":
    libdep_main(sys.argv[1])