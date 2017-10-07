import sys
import Scrap
import quickconsole
def p_s(*args):
    msg=""
    for obj in args:
        if msg:
            msg=msg+" "+str(obj)
        else:
            msg=msg+str(obj)
    Scrap.Print(msg)

def p_e(*args):
    msg=""
    for obj in args:
        if msg:
            msg=msg+" "+str(obj)
        else:
            msg=msg+str(obj)
    Scrap.ConsoleError(msg)
sys.stdout.write=p_s
sys.stderr.write=p_e

def p(*args):
    msg=""
    for obj in args:
        if msg:
            msg=msg+" "+str(obj)
        else:
            msg=msg+str(obj)
    Scrap.Print(msg+"\n")
def e(*args):
    msg=""
    for obj in args:
        if msg:
            msg=msg+" "+str(obj)
        else:
            msg=msg+str(obj)
    Scrap.ConsoleError(msg+"\n")
#sys.modules['__builtin__'].__dict__['print']=e
sys.modules['__builtin__'].__dict__['s_write']=p
sys.modules['__builtin__'].__dict__['e_write']=e

for module in sys.builtin_module_names:
    if module[0]=="S":
        print "Loading "+module
    exec("import "+module)

sys.settrace(None)

def trace(frame,event,arg):
    if event!="call": return
    g=frame.f_globals
    l=frame.f_locals
    if frame.f_code.co_name=="godcall":
        return
    R=frame.f_code.co_filename+"."+frame.f_code.co_name+"("
    for i in range(frame.f_code.co_argcount):
        name = frame.f_code.co_varnames[i]
        R=R+name+"="+repr(frame.f_locals[name])+","
    R=R+") Consts: ["
    for const in frame.f_code.co_consts:
        R=R+repr(const)+","
    R=R+"]"
    log(R)
    return trace

def menu():
    import Menu
    Menu.DebugMenu(0,'')
    Menu.InitMenuSys(0)

def settrace():
    sys.settrace(trace)

def log(*args):
    if not args:
        open(logfile_name,"w").close()
        return
    msg=""
    for obj in args:
        if msg:
            msg=msg+" "+str(obj)
        else:
            msg=msg+str(obj)
    open(logfile_name,"a").write(msg+"\n")

def helplib():
    print "Generating helplib.txt"
    log()
    for modname,mod in sys.modules.items():
        log("======== [ "+modname+" ] ========")
        for name,value in vars(mod).items():
            if name in ("__doc__","__name__"):
                continue
            if hasattr(value,"__doc__"):
                if value.__doc__:
                    log("- "+name+":")
                    log("      "+value.__doc__)
                else:
                    log("- "+name+": ???")
            else:
                log("- "+name+": "+repr(value))
        log("\n")
    print "Done!"

def enable_all_conv():
    import CharConversor
    CharConversor.ConversionChars=list(CharConversor.ConversionChars)
    E=Scrap.GetFirst()
    while E:
        try:
            if E.ActCtrl not in CharConversor.ConversionChars:
                CharConversor.ConversionChars.append(E.ActCtrl)
        except:
            E = Scrap.GetEntity(E.NextInSlot)
            continue
        E.Invulnerable=0
        E.Life=100
        E = Scrap.GetEntity(E.NextInSlot)
    print(len(CharConversor.ConversionChars))
    print "Done!"

def become(name):
    enable_all_conv()
    import CharConversor
    me = Scrap.UsrEntity(0)
    ent = Scrap.GetEntity(name)
    if ent:
        CharConversor.Possession(me.Name,name)
    else:
        print "Entity not found"

StopMovie = 0

def movie(MovieName="Movie/Movie"):
	global StopMovie
	if LastTime==None:
		Scrap.Set( "PhysicalAspectRatio", 16.0/9.0 )
		LastTime = Scrap.GetTime()
		StopMovie = 0
	if StopMovie == 1:
		return
	Scrap.Set("DisableSkipSlot",1)
	Scrap.ProcessDVF(MovieName+".dvf",0)
	Scrap.ScreenShot(MovieName+"*")
	NextTime = LastTime+1.0/25.0
	Scrap.AddScheduledFunc(NextTime,movie,(Speed,MovieName,NextTime))

logfile_name="helplib.txt"
helplib()
logfile_name="dbg.txt"
log()
quickconsole.god()
print "Godmode active"