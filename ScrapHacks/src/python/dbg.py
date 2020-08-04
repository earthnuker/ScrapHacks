import sys
import Scrap
import quickconsole
import MissionsFuncs
import SScorer
import Menu
import sys

QC = quickconsole
MF = MissionsFuncs
last_frame = None
level = 3
initialized = 0
sys.path.append(".\\pylib\\Lib")
sys.path.append(".\\pylib\\Libs")
sys.path.append(".\\pylib")


def reload():
    sys.settrace(None)
    sys.modules['__builtin__'].reload(sys.modules[__name__])


def dgb_info():
    if me:
        try:
            dbg_text = str(SVec.Mod(me.Vel))
        except:
            dbg_text=""
    else:
        dbg_text = ""
    SScorer.SetLabelText(dbg_text, Scrap.GetTime() + 0.1)
    Scrap.DeleteScheduledFuncs("dbg.dbg_info")
    Scrap.DeleteScheduledFuncs("dbg.dbg_info")
    Scrap.AddScheduledFunc(Scrap.GetTime()+0.1, dgb_info, (), "dbg.dbg_info")


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
                    log("- "+name+":"+repr(value))
                    log("      "+value.__doc__)
                else:
                    log("- "+name+":"+repr(value))
            else:
                log("- "+name+": "+repr(value))
        log("\n")
    logfile_name = None
    print "Done!"

def enable_all_conv():
    try:
        import CharConversor
    except ImportError:
        # print("CharConversor not available")
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
    import CharConversor
    enable_all_conv()
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


def find(filt="*"):
    dummy = Scrap.StartDummySearch(filt, 1)
    while dummy:
        dummy = Scrap.NextDummySearch()
        print dummy


def getall():
    E = Scrap.GetFirst()
    me = Scrap.UsrEntity(0)
    while E:
        try:
            E.Descriptor = "HAXX!"
        except:
            pass
        E = Scrap.GetEntity(E.NextInSlot)


def god(e=None):
    if e == None:
        e = Scrap.UsrEntity(0)
        if e:
            try:
                e.IsType("Car")
            except:
                return
    if e:
        if e.IsType("Car"):
            e.Ammo00 = SWeap.GetFAmmo(0, "Max")
            e.Ammo01 = SWeap.GetFAmmo(1, "Max")
            e.Ammo02 = SWeap.GetFAmmo(2, "Max")
            e.Ammo03 = SWeap.GetFAmmo(3, "Max")
            e.WeapList = "63,63,63,63,63,63,1"
            e.MaxLife = e.MinLife
            if e.Life > e.MaxLife:
                e.Life = e.MaxLife
            e.CMStamp = 0
            e.FireStamp = 0
            e.BoostTime = 0
        elif e.IsType("WalkChar"):
            e.Energy = 1
        e.Invulnerable = 1
        e.TimeSpeed = 2.0
        e.Mass = 100
    # Scrap.SetAlarm(0.0)
    Scrap.SetAlarmGrow(-0.5)
    Scrap.DeleteScheduledFuncs("dbg.god")
    Scrap.DeleteScheduledFuncs("dbg.god")
    Scrap.AddScheduledFunc(Scrap.GetTime() + 0.01, god, (e,), "dbg.god")


def ungod():
    for _ in range(1024):
        Scrap.DeleteScheduledFuncs("dbg.god")


def ultranuke():
    nuke()
    Scrap.DeleteScheduledFuncs("dbg.ultranuke")
    Scrap.DeleteScheduledFuncs("dbg.ultranuke")
    Scrap.AddScheduledFunc(Scrap.GetTime(), ultranuke,
                           (), "dbg.ultranuke")


def freeze(_=None):
    QC.freeze()
    Scrap.DeleteScheduledFuncs("dbg.freeze")
    Scrap.DeleteScheduledFuncs("dbg.freeze")
    Scrap.AddScheduledFunc(Scrap.GetTime()+0.1, freeze, (None,), "dbg.freeze")


def unfreeze(_):
    Scrap.DeleteScheduledFuncs("dbg.freeze")
    Scrap.DeleteScheduledFuncs("dbg.freeze")
    QC.unfreeze()


def brake():
    if me:
        me.Vel = (0, 0, 0)


weaps_hacked = {
    "Laser": {
        "AmmoCost": 0,
        "TimeDelay": 0,
    },
    "Vulcan": {
        "TimeDelay": 0.01,
        "TimeDelayUPG": 0.01,
        "AmmoCost": 0
    },
    "Devastator": {
        "AmmoCost": 0,
        "RechargeTime": 0,
        "SpreadAngle": 0,
    },
    "Tesla": {
        "AmmoCost": 0,
    },
    "ATPC": {
        "AmmoCost": 0,
        "UpgradeDelay": 0,
        "Delay": 0,
    },
    "Swarm": {
        "AmmoCost1": 0,
        "AmmoCost2": 0,
        "AmmoCost3": 0,
        "AmmoCost4": 0,
        "Number1": 20,
        "Number2": 20,
        "Number3": 20,
        "Number4": 20,
        "TurnSpeed": 360000,
        "TurnSpeedUPG": 360000,
        "TimeDelay": 1.0,
    },
    "Inferno": {
        "AmmoCost": 1
    }
}


def weaphacks():
    for weapon, properties in weaps_hacked.items():
        for prop, value in properties.items():
            Scrap.Set(weapon+prop, value)


def unweaphacks():
    for weapon, properties in weaps_hacked.items():
        for prop, value in properties.items():
            Scrap.Set(weapon+prop, Scrap.Def(weapon+prop))


def test_func():
    E = Scrap.GetFirst()
    me = Scrap.UsrEntity(0)
    while E:
        if E.Name == me.Name:
            E = Scrap.GetEntity(E.NextInSlot)
        try:
            E.Money = 1024*1024*1024
            # SAI.SetStateVehicle(8,me.Name,E.Name)
        except:
            pass
        E = Scrap.GetEntity(E.NextInSlot)


for _ in range(1024):
    Scrap.DeleteScheduledFuncs("dbg.dbg_info")
    Scrap.DeleteScheduledFuncs("dbg.god")
    Scrap.DeleteScheduledFuncs("dbg_info")


for module in sys.builtin_module_names:
    if module[0] == "S":
        print "Loading "+module
    exec("import " + module)

sys.settrace(None)
notrace()
helplib()
# settrace()


def init():
    global me
    global initialized
    if initialized == 0:
        from ScrapHack import Mem, asm
        sys.modules[__name__].mem = Mem
        sys.modules[__name__].asm = asm
        me = Scrap.UsrEntity(0)
    dgb_info()
    enable_all_conv()
    god()
    Scrap.Set("debug", level)
    Scrap.Set("ShowConsoleLog", 1)
    Scrap.Set("AlwaysFlushLog", 1)
    Scrap.Set("PythonExecute", "import dbg;dbg.init()")
    Scrap.DeleteScheduledFuncs("dbg_init")
    Scrap.DeleteScheduledFuncs("dbg_init")
    Scrap.AddScheduledFunc(Scrap.GetTime()+1, init, (), "dbg_init")
    initialized = 1


exec("import QuickConsole;QuickConsole.dbg=sys.modules['dbg']")
print "Debug Module loaded use /dbg.init to initialize"
