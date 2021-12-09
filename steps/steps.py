import sys
import os
import json
import keygen

KEY_SIZE = 12

def add_instruc(dataval, maindatain, keysize, name):
    if(dataval == 1):
        nkey1 = keygen.Keygen(keysize).gen_key()
        startdata = {
            "name": name,
            "devMode": True,
            "key": nkey1,
            "data": maindatain
        }

        with open("./.stepsf/index.json", 'r') as file4:
            file5 = json.load(file4)
            file4.close()
        
        file5.append(startdata)

        with open("./.stepsf/index.json", 'w') as file6:
            file6.write(json.dumps(file5))
            
            file6.close()
        
        os.system("mkdir ./.stepsf/" + nkey1)
        for x in file5[-1]['data']:
            with open("./" + x, 'r') as file7:
                file8 = file7.read()
                file7.close()
            os.system("touch ./.stepsf/" + nkey1 + "/" + x)
            with open("./.stepsf/" + nkey1 + "/" + x, 'w') as file9:
                file9.write(file8)
                file9.close()
        
    else:
        os.system("mkdir .stepsf")
        os.system("touch .stepsf/index.json")
        startdata = [{
            "name": name,
            "devMode": True,
            "key": None,
            "keyinit": False
        }]
        tad = json.dumps(startdata)
        with open("./.stepsf/index.json", 'w') as file1:
            file1.write(tad)
            file1.close()

def rollback(val):
    for i in range(val):
        with open("./.stepsf/index.json", 'r') as file10:
            file11 = json.load(file10)
            file10.close()
        nkey2 = file11[-1]['key']
        files2 = file11[-1]['data']
        filesindir = os.listdir()
        i3 = 0
        fileshere = []
        filesnothere = []
        for d in files2:
            if(os.path.isfile(filesindir[i3]) and d in filesindir):
                fileshere.append(d)
            elif(d not in filesindir):
                filesnothere.append(d)
        for f in filesnothere:
            os.system("touch " + d)
        for d in files2:
            with open("./.stepsf/" + nkey2 + "/" + d, 'r') as file12:
                data = file12.read()
                file12.close()
            with open(d, 'w') as file13:
                file13.write(data)
                file13.close()
        file11.pop(-1)
        with open("./.stepsf/index.json", 'w') as file14:
            file14.write(json.dumps(file11))
            file14.close()
        os.system("rm -r ./.stepsf/" + nkey2)

def krel():
    os.system("rm -r ./.stepsf/")

def bkp():
    bkpf = False
    filesdir = os.listdir()
    for f in filesdir:
        if(f == '.steps_bkp'):
            bkpf = True
    if(bkpf):
        bkpfi = os.listdir("./.steps_bkp")
        largest1 = 0
        for n in bkpfi:
            if(int(n) > largest1):
                largest1 = int(n)
        largest1 += 1
        print(largest1)
    else:
        os.system("mkdir ./.steps_bkp/")

manual = '''
    Steps:
'''

try:
    command = sys.argv[1]
    # data =  sys.argv[2]

    if(command == 'init'):
        initedq = False
        dirdata = os.listdir()
        for d in dirdata:
            if(os.path.isdir(d) and d == ".stepsf"):
                initedq = True
        if(initedq):
            try:
                with open("./.stepsf/index.json", 'r') as file2:
                    file3 = json.load(file2)
                    file2.close()
                if(file3[0]['devMode']):
                    os.system('rm -r .stepsf')
                    add_instruc(0, None, KEY_SIZE, 'init')
                    print("Steps Base Face (SBF) Initialized")
            except:
                print("Error 100")
        else:
            add_instruc(0, None, KEY_SIZE, 'init')
            print("Steps Base Face (SBF) Initialized")
    elif(command == 'commit'):
        try:
            data3 = sys.argv[2]
            data4 = str(sys.argv[3])
            if(data3 == "-m"):
                ifmessage = True
        except: ifmessage = False
        initedq = False
        dirdata = os.listdir()
        for d in dirdata:
            if(os.path.isdir(d) and d == ".stepsf"):
                initedq = True
        if(initedq):
            
            with open("./.stepsf/index.json", 'r') as file2:
                file3 = json.load(file2)
                file2.close()
            if(file3[0]['devMode']):
                files1 = os.listdir()
                filesref1 = []
                for f in files1:
                    if(os.path.isfile(f)):
                        filesref1.append(f)
                if(ifmessage):
                    add_instruc(1, filesref1, KEY_SIZE, data4)
                else:
                    add_instruc(1, filesref1, KEY_SIZE, None)
        
            
        else:
            files1 = os.listdir()
            filesref1 = []
            for f in files1:
                if(os.path.isfile(f)):
                    filesref1.append(f)
            if(ifmessage):
                add_instruc(1, filesref1, KEY_SIZE, data4)
            else:
                add_instruc(1, filesref1, KEY_SIZE, None)
    elif(command == "rollback"):
        try:
            data = sys.argv[2]
            if(data == "-a"):
                try:
                    data2 = sys.argv[3]
                    rollback(int(data2))
                except:
                    print(manual)
            else:
                print(manual)
        except:
            rollback(1)
    elif(command == "krel"):
        try:
            data = sys.argv[2]
            if(data == '-y'):
                krel(   )
            else:
                print("Error 500: Permission denied; Add -y tag to confirm.\nWarning: When krel is run, all data will be removed from the steps ladder")
        except:
            print("Error 500: Permission denied; Add -y tag to confirm.\nWarning: When krel is run, all data will be removed from the steps ladder")
    #elif(command == "bkp"):
    #    bkp()
    else: print(manual)
except IndexError: print(manual)