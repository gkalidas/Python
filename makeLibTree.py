import os, sys, io 
import subprocess
import threading
import multiprocessing

DEFAULT_NUM_THREADS = 4 
NUM_THREADS = DEFAULT_NUM_THREADS

try:
    NUM_THREADS =  multiprocessing.cpu_count()
except NotImplementedError :
    pass

def split_list(alist, wanted_parts):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def which(file):
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, file)):
                return os.path.join(path, file)
    return None

def doJobFast(lst , dumpbin_exe, results, idx):
    for bin in lst : 
        p = subprocess.Popen([dumpbin_exe,"/dependents", bin], stdout = subprocess.PIPE)
        (results[idx]).append(bin.replace("\\","/").rstrip())
        for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):
            if ".dll" in line : 
                results[idx].append(line.replace("\\","/").rstrip())

def makeLibTreeMTFast(q, dumpbin_exe):
    lists = split_list(q, NUM_THREADS)
    threads = []
    results = [[] for _ in range(NUM_THREADS)]
    for i  in range(NUM_THREADS):
        t = threading.Thread(target=doJobFast, args = (lists[i], dumpbin_exe, results, i))
        t.start()
        threads.append(t)
    for thr in threads: 
        thr.join()
    for res in results : 
        for line in res :
            print (line)

def makeBinListFast(rootPath):
    q = [] 
    for root, dirs, files in os.walk(rootPath):
        for file in files :
            ext = os.path.splitext(file)[1] 
            if (ext == ".dll" or ext == ".exe"):
                q.append(os.path.join(root,file))
    return q

if __name__ == "__main__":
    if(len (sys.argv) == 2) :
        db_bin = which("dumpbin.exe")
        if(not db_bin):
            db_env = os.environ.get('DUMPBIN_BIN')
            if(db_env and os.path.exists(db_env)):
                db_bin = db_env
        if(db_bin):
            makeLibTreeMTFast(makeBinListFast(sys.argv[1]), db_bin)
        else:
            print ("dumpbin not found, setsys or setenv DUMPBIN_BIN <dumpbin path>")
    else:
        print ("\nUsage: %s <CD Image root path>\n" % sys.argv[0])