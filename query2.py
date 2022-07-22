import json,time
def get_file_read(name):
    while True:
        with open(name) as fw:
            fr=fw.read()
            if fr!="":
                return fr
            else:
                time.sleep(0.1)

def dict_keyval(dict):
    key_1=str(dict.keys()).replace("'","").replace('"',"")[11:-2]
    return key_1,dict[key_1]
def get(dbname,key):
    dbname="bin/"+dbname+".aludb"
    fr=get_file_read(dbname)
    db_file=json.loads(str(fr).replace("'",'"'))
    for x in db_file:
        if (((dict_keyval(x)[0]).replace('"',"")).replace("'",""))==key:
            return dict_keyval(dict_keyval(x)[1])[1]

def key_exists(dbname,key):
    dbname="bin/"+dbname+".aludb"
    file=json.loads(get_file_read(dbname).replace("'",'"'))
    for x in file:
        if dict_keyval(x)[0]==key:
            return True
    return False

def append(dbname,key,val):
    if not key_exists(dbname,key):
        dbname="bin/"+dbname+".aludb"
        file=json.loads(get_file_read(dbname).replace("'",'"'))
        file.append({key:val})
        with open(dbname,'w+') as fw:
            fw.write(str(file).replace("'",'"'))
            return True
    elif key_exists(dbname,key):
        dbname="bin/"+dbname+".aludb"
        file=json.loads(get_file_read(dbname).replace("'",'"'))
        for x in file:
            if dict_keyval(x)[0]==key:
                file[file.index(x)]={key:val}
                with open(dbname,'w+') as fw:
                    fw.write(str(file).replace("'",'"'))
                return True

def custom_append(dbname,val):
    dbname="bin/"+dbname+".aludb"
    file=json.loads(get_file_read(dbname).replace("'",'"'))
    file.append(val)
    with open(dbname,'w+') as fw:
        fw.write(str(file))
        return True

def contract_append(val):
    dbname="bin/contracts.aludb"
    with open(dbname,'a') as fw:
        fw.write(str(val).replace("'",'"')+",")
        return True

def givedb(dbname):
    dbname="bin/"+dbname+".aludb"
    f=get_file_read(dbname)
    if f[0]=="~":
        f=f[1:]
        f=f[:-1]
        f="["+f+"]"
        file=json.loads(f.replace("'",'"'))
    else:
        file=json.loads(f.replace("'",'"'))
    return file

def remove(dbname,key):
    if key_exists(dbname,key):
        dbname="bin/"+dbname+".aludb"
        file=json.loads(get_file_read(dbname).replace("'",'"'))
        for x in file:
            if dict_keyval(x)[0]==key:
                file.remove(json.loads(str(x).replace("'",'"')))
                open(dbname,"w+").write(json.dumps(file))
                return True