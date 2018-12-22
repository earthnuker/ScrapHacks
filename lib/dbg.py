import sys
import Scrap
import quickconsole
import MissionsFuncs
import SScorer
import Menu
QC = quickconsole
MF = MissionsFuncs
last_frame = None


def reload():
    sys.settrace(None)
    sys.modules['__builtin__'].reload(sys.modules['dbg'])


def dgb_info():
    txt =`last_frame`
    SScorer.SetLabelText(txt, Scrap.GetTime()+0.1)
    Scrap.AddScheduledFunc(Scrap.GetTime()+0.1, dgb_info, (), "dbg_info")


def crazy():
    E = Scrap.GetFirst()
    me = Scrap.UsrEntity(0)
    while E:
        if E.Name == me.Name:
            E = Scrap.GetEntity(E.NextInSlot)
        try:
            E.Action = "CrazyInit"
            E.CanPhoto = 1
            E.DefLoop = "Crazy"
        except:
            pass
        E = Scrap.GetEntity(E.NextInSlot)


def decrazy():
    E = Scrap.GetFirst()
    me = Scrap.UsrEntity(0)
    while E:
        if E.Name == me.Name:
            E = Scrap.GetEntity(E.NextInSlot)
        try:
            E.Action = "CrazyEnd"
            E.CanPhoto = 0
            E.ForceDefLoop = "Relax"
        except:
            pass
        E = Scrap.GetEntity(E.NextInSlot)


def p_s(*args):
    msg = ""
    for obj in args:
        if msg:
            msg = msg+" "+str(obj)
        else:
            msg = msg+str(obj)
    Scrap.Print(msg)


def p_e(*args):
    msg = ""
    for obj in args:
        if msg:
            msg = msg+" "+str(obj)
        else:
            msg = msg+str(obj)
    Scrap.ConsoleError(msg)


sys.stdout.write = p_s
sys.stderr.write = p_e


def p(*args):
    msg = ""
    for obj in args:
        if msg:
            msg = msg+" "+str(obj)
        else:
            msg = msg+str(obj)
    Scrap.Print(msg+"\n")


def e(*args):
    msg = ""
    for obj in args:
        if msg:
            msg = msg+" "+str(obj)
        else:
            msg = msg+str(obj)
    Scrap.ConsoleError(msg+"\n")


# sys.modules['__builtin__'].__dict__['print']=e
sys.modules['__builtin__'].__dict__['s_write'] = p
sys.modules['__builtin__'].__dict__['e_write'] = e


def modhelp(Module="Scrap"):
    print "======== [ " + Module + " ] ========"
    exec("import "+Module)
    for v in dir(eval(Module)):
        if v in ("__doc__", "__name__"):
            continue
        print v + ":"
        try:
            print "      " + eval(Module + "." + v + ".__doc__")
        except:
            pass


def helpfunc(func):
    print func.__name__+":"
    print "    "+func.__doc__


for module in sys.builtin_module_names:
    if module[0] == "S":
        print "Loading "+module
    exec("import " + module)

sys.settrace(None)


def trace(frame, event, arg):
    global last_frame
    if event != "call":
        return
    g = frame.f_globals
    l = frame.f_locals
    if frame.f_code.co_name == "godcall":
        return
    if frame.f_code.co_filename == ".\\lib\\dbg.py":
        return
    R = frame.f_code.co_filename+": "+frame.f_code.co_name+"("
    for i in range(frame.f_code.co_argcount):
        name = frame.f_code.co_varnames[i]
        R = R+name+"="+repr(frame.f_locals[name])+","
    R = R+") Consts: ["
    for const in frame.f_code.co_consts:
        R = R+repr(const)+","
    R = R+"]"
    print R, "Locals:", l, "Globals:", g
    last_frame = R
    return trace


def menu():
    import Menu
    Menu.DebugMenu(1, '')
    Menu.InitMenuSys(1)


def settrace():
    sys.settrace(trace)


def notrace():
    sys.settrace(None)


def log(*args):
    if not args:
        open(logfile_name, "w").close()
        return
    msg = ""
    for obj in args:
        if msg:
            msg = msg+" "+str(obj)
        else:
            msg = msg+str(obj)
    open(logfile_name, "a").write(msg+"\n")


def helplib():
    global logfile_name
    print "Generating helplib.txt"
    logfile_name = "helplib.txt"
    log()
    for modname, mod in sys.modules.items():
        if hasattr(mod, '__file__'):
            continue
        log("======== [ "+modname+" ] ========")
        for name, value in vars(mod).items():
            if name in ("__doc__", "__name__"):
                continue
            if hasattr(value, "__doc__"):
                if value.__doc__:
                    log("- "+name+":")
                    log("      "+value.__doc__)
                else:
                    log("- "+name+": ???")
            else:
                log("- "+name+": "+repr(value))
        log("\n")
    logfile_name = None
    print "Done!"


def enable_all_conv():
    try:
        import CharConversor
    except ImportError:
        print("CharConversor not available")
        return
    CharConversor.ConversionChars = list(CharConversor.ConversionChars)
    E = Scrap.GetFirst()
    while E:
        try:
            if E.ActCtrl not in CharConversor.ConversionChars:
                CharConversor.ConversionChars.append(E.ActCtrl)
        except:
            E = Scrap.GetEntity(E.NextInSlot)
            continue
        E.Invulnerable = 0
        E.Life = 100
        E = Scrap.GetEntity(E.NextInSlot)
    print(len(CharConversor.ConversionChars))
    print "Done!"


def goto(name=None):
    if name == None:
        name = MF.currentTarget
    Scrap.UsrEntity(0).Pos = Scrap.GetEntity(name).Pos


def bring(name=None):
    if name == None:
        name = MF.currentTarget
    Scrap.GetEntity(name).Pos = Scrap.UsrEntity(0).Pos


def nuke():
    E = Scrap.GetFirst()
    me = Scrap.UsrEntity(0)
    while E:
        if E.Name == me.Name:
            E = Scrap.GetEntity(E.NextInSlot)
        try:
            E.Life = 0
            E.Invulnerable = 0
        except:
            pass
        E = Scrap.GetEntity(E.NextInSlot)


def become(name):
    enable_all_conv()
    import CharConversor
    me = Scrap.UsrEntity(0)
    ent = Scrap.GetEntity(name)
    if ent:
        CharConversor.Possession(me.Name, name)
    else:
        print "Entity not found"


StopMovie = 0


def movie(MovieName="Movie/Movie"):
    global StopMovie
    if LastTime == None:
        Scrap.Set("PhysicalAspectRatio", 16.0/9.0)
        LastTime = Scrap.GetTime()
        StopMovie = 0
    if StopMovie == 1:
        return
    Scrap.Set("DisableSkipSlot", 1)
    Scrap.ProcessDVF(MovieName+".dvf", 0)
    Scrap.ScreenShot(MovieName+"*")
    NextTime = LastTime+1.0/25.0
    Scrap.AddScheduledFunc(NextTime, movie, (Speed, MovieName, NextTime))


def park():
    me = Scrap.UsrEntity(0)


def find(filt="*"):
    Scrap.StartDummySearch(filt, 1)
    dummy = 1
    while dummy:
        dummy = Scrap.NextDummySearch()
        print dummy


def getall():
    E = Scrap.GetFirst()
    me = Scrap.UsrEntity(0)
    while E:
        try:
            E.Pos = me.Pos
        except:
            pass
        E = Scrap.GetEntity(E.NextInSlot)


def god():
    e = Scrap.UsrEntity(0)
    QC.godcall(None, (1, 1, 1, 1, 1, 1))
    Scrap.AddScheduledFunc(Scrap.GetTime()+0.1, god, (), 'dbg.god')


notrace()
helplib()
# settrace()
dgb_info()
enable_all_conv()
god()
Scrap.Set("debug", 3)
Scrap.Set("ShowConsoleLog", 1)

print "Debug Module loaded"
