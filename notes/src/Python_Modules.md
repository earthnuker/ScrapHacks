# Python API

## SScorer

- *SetCursor*: `<built-in function SetCursor>`

SetCursor(playernumber,CursorName) : pone un item del scorer como cursor

- *Show*: `<built-in function Show>`
```
Show(playernumber) : Activa el scorer.
```
- *GetTextArea*: `<built-in function GetTextArea>`
```
(width, height) GetTextArea(fontType, text) : obtiene la anchura y la altura de un texto dado el texto y el tipo de fuente
```
- *AddModel*: `<built-in function AddModel>`
```
AddModel(playernumber,Name,ModelFile,numanim,Radius) : Pre carga un modelo para usarse en el scorer.
```
- *SetOnPrev*: `<built-in function SetOnPrev>`
```
SetOnPrev(playernumber,CancelEvent) : Define la funcion que se ejecutara en el caso del pagina abajo.
```
- *AddChatMsg*: `<built-in function AddChatMsg>`
```
AddChatMsg(string,red,gree,blue) : Agrega un mensaje a la lista de chat.
```
- *GetOnCancel*: `<built-in function GetOnCancel>`
```
(CancelEvent)GetOnCancel(playernumber) : Devuelve la funcion que se ejecutara en el caso del escape.
```
- *GetDefault*: `<built-in function GetDefault>`
```
DefaultItemName GetDefault(playernumber) Obtiene el nombre del item por defecto
```
- *SetOnSpecialHint*: `<built-in function SetOnSpecialHint>`
```
SetOnSpecialHint(playernumber,SpecialHintTestFunc,SpecialHint) : Define la funcion que decide si se muestra un hint especial
```
- *SetConsole*: `<built-in function SetConsole>`
```
SetConsole(show) : oculta/ muestra la consola de pantalla completa
```
- *Get2DPos*: `<built-in function Get2DPos>`
```
(x,y) Get2DPos(vector3d) : obtiene en cordenadas de pantalla una posicion del escenario
```
- *GetActual*: `<built-in function GetActual>`
```
ActualItem GetActual(playernumber) Obtiene el item actual
```
- *SetOnNext*: `<built-in function SetOnNext>`
```
SetOnNext(playernumber,CancelEvent) : Define la funcion que se ejecutara en el caso del pagina abajo.
```
- *SetMPFunc*: `<built-in function SetMPFunc>`
```
SetMPFunc(playernumber,Callback) : Callback(id,showmpscorer) (muestra oculta el scorer multiplayer)
```
- *Set*: `<built-in function Set>`
```
Set(playernumber,itemname,varname,value) :  Modifica el valor de una variable de un item
```
- *SetSpeechCallback*: `<built-in function SetSpeechCallback>`
```
SetSpeechCallback(Callback) : Especifica la funcion callback que será llamada
```
- *Get*: `<built-in function Get>`
```
Get(playernumber,itemname,varname) :  Obtiene el valor de una variable de un item
```
- *GetMenuAccept*: `<built-in function GetMenuAccept>`
```
GetMenuAccept(id) : Devuelve el estado de la acción de menu aceptar.
```
- *SetDefault*: `<built-in function SetDefault>`
```
SetDefault(playernumber,DefaultItemName) : pone un item del scorer 'por defecto'
```
- *CancelSpeech*: `<built-in function CancelSpeech>`
```
CancelSpeech(time) : cancela un mensaje remoto
```
- *SetHeadMonitor*: `<built-in function SetHeadMonitor>`
```
SetHeadMonitor(Head,Msg,anm) : Especifica la cabeza que será usada en el monitor y el mensaje.
```
- *Add*: `<built-in function Add>`
```
Add(playernumber,itemname,itemtype,AtEnd) : Agrega un item al scorer.
```
- *SetMarkerSprite*: `<built-in function SetMarkerSprite>`
```
SetMarkerSprite(id,SpriteName) : pone un sprite como marcador
```
- *PreloadTexture*: `<built-in function PreloadTexture>`
```
PreloadTexture(filename) : Precarga una textura
```
- *SetMsgText*: `<built-in function SetMsgText>`
```
SetMsgText(text,time) : Muestra un mensaje de sistema y lo desactiva en el tiempo de mundo time
```
- *Fade*: `<built-in function Fade>`
```
Fade(id,(r,g,b,a),(r,g,b,a),time) : Realiza un fade de rgba a rgba.
```
- *Clear*: `<built-in function Clear>`
```
Clear(playernumber) : Limpia el scorer completamente.
```
- *SetCinema*: `<built-in function SetCinema>`
```
SetCinema(id,status,time) : Activa el modo escena de cine.
```
- *SetSpeechText*: `<built-in function SetSpeechText>`
```
SetSpeechText(text,time,r,g,b) : activa el texto de una conversacion que durará un tiempo espeficico
```
- *SetOnCancel*: `<built-in function SetOnCancel>`
```
SetOnCancel(playernumber,CancelEvent) : Define la funcion que se ejecutara en el caso del escape.
```
- *Hide*: `<built-in function Hide>`
```
Hide(playernumber) : Desactiva el scorer.
```
- *SetLabelText*: `<built-in function SetLabelText>`
```
SetLabelText(text,time) : Muestra un rotulo de sistema y lo desactiva en el tiempo de mundo time
```


## _locale

- *strcoll*: `<built-in function strcoll>`
```
string,string -> int. Compares two strings according to the locale.
```
- *LC_TIME*: `5`
- *Error*: `'locale.Error'`
- *LC_ALL*: `0`
- *LC_CTYPE*: `2`
- *strxfrm*: `<built-in function strxfrm>`
```
string -> string. Returns a string that behaves for cmp locale-aware.
```
- *localeconv*: `<built-in function localeconv>`
```
() -> dict. Returns numeric and monetary locale-specific parameters.
```
- *LC_MONETARY*: `3`
- *setlocale*: `<built-in function setlocale>`
```
(integer,string=None) -> string. Activates/queries locale processing.
```
- *LC_COLLATE*: `1`
- *CHAR_MAX*: `127`
- *LC_NUMERIC*: `4`


## marshal

- *loads*: `<built-in function loads>`
- *dump*: `<built-in function dump>`
- *dumps*: `<built-in function dumps>`
- *load*: `<built-in function load>`


## sys

- *hexversion*: `17105648`
- *last_value*: `'a'`
- *setcheckinterval*: `<built-in function setcheckinterval>`
```
setcheckinterval(n)

Tell the Python interpreter to check for asynchronous events every
n instructions.  This also affects how often thread switches occur.
```
- *exc_info*: `<built-in function exc_info>`
```
exc_info() -> (type, value, traceback)

Return information about the exception that is currently being handled.
This should be called from inside an except clause only.
```
- *stderr*: `<__main__.ConsoleErrorOutput instance at d1d421c>`
- *exit*: `<built-in function exit>`
```
exit([status])

Exit the interpreter by raising SystemExit(status).
If the status is omitted or None, it defaults to zero (i.e., success).
If the status numeric, it will be used as the system exit status.
If it is another kind of object, it will be printed and the system
exit status will be one (i.e., failure).
```
- *version*: `'1.5.2 (#0, Oct 13 2004, 11:28:15) [MSC 32 bit (Intel)]'`
- *platform*: `'win32'`
- *last_type*: `'NameError'`
- *modules*: `{'EnginesTab': <module 'EnginesTab' from 'PACK: ShipEdit/EnginesTab.pyc'>, 'Cloud': <module 'Cloud' from 'PACK: Weapons/Cloud.pyc'>, 'Mayor': <module 'Mayor' from 'PACK: Chars/Mayor.pyc'>, 'InPolice': <module 'InPolice' from 'PACK: Missions/InPolice.pyc'>, 'MapSnd': <module 'MapSnd' from 'PACK: MapSnd.pyc'>, 'BankDirectorSound': <module 'BankDirectorSound' from 'PACK: Sound/BankDirectorSound.pyc'>, 'Human': <module 'Human' from 'PACK: Chars/Human.pyc'>, 'SScorer': <module 'SScorer' (built-in)>, 'DesktopSound': <module 'DesktopSound' from 'PACK: Sound/DesktopSound.pyc'>, 'Bureaucracy': <module 'Bureaucracy' from 'PACK: Chars/Bureaucracy.pyc'>, 'Scene': <module 'Scene' from 'PACK: Missions/Scene.pyc'>, 'RacerScorer': <module 'RacerScorer' from 'PACK: Scorer/RacerScorer.pyc'>, '_locale': <module '_locale' (built-in)>, 'CharConversor': <module 'CharConversor' from 'PACK: Missions/CharConversor.pyc'>, 'CharScorer': <module 'CharScorer' from 'PACK: Scorer/CharScorer.pyc'>, 'PhoneCab': <module 'PhoneCab' from 'PACK: Missions/PhoneCab.pyc'>, 'marshal': <module 'marshal' (built-in)>, 'Functionary': <module 'Functionary' from 'PACK: Chars/Functionary.pyc'>, 'RaceMaker': <module 'RaceMaker' from 'PACK: Missions/RaceMaker.pyc'>, 'sys': <module 'sys' (built-in)>, 'ShipMaker': <module 'ShipMaker' from 'PACK: Vehicles/ShipMaker.pyc'>, 'Alarm': <module 'Alarm' from 'PACK: Missions/Alarm.pyc'>, 'Items': <module 'Items' from 'PACK: Items.pyc'>, 'QuickConsole': <module 'QuickConsole' from '.\lib\QuickConsole.pyc'>, 'Metro': <module 'Metro' from 'PACK: Missions/Metro.pyc'>, 'CrazyWing': <module 'CrazyWing' from 'PACK: Missions/CrazyWing.pyc'>, 'BankMasterSound': <module 'BankMasterSound' from 'PACK: Sound/BankMasterSound.pyc'>, 'SLogic': <module 'SLogic' (built-in)>, 'Teleport': <module 'Teleport' from 'PACK: Missions/Teleport.pyc'>, 'OutPolice': <module 'OutPolice' from 'PACK: Missions/OutPolice.pyc'>, 'math': <module 'math' (built-in)>, 'HumanSound': <module 'HumanSound' from 'PACK: Sound/HumanSound.pyc'>, 'new': <module 'new' (built-in)>, 'MayorSound': <module 'MayorSound' from 'PACK: Sound/MayorSound.pyc'>, 'Vulcan': <module 'Vulcan' from 'PACK: Weapons/Vulcan.pyc'>, 'SNet': <module 'SNet' (built-in)>, 'SputnikSound': <module 'SputnikSound' from 'PACK: Sound/SputnikSound.pyc'>, 'Chars': <module 'Chars' from 'PACK: Chars/Chars.pyc'>, 'PoliceBossSound': <module 'PoliceBossSound' from 'PACK: Sound/PoliceBossSound.pyc'>, 'GateKeeper': <module 'GateKeeper' from 'PACK: Chars/GateKeeper.pyc'>, 'FunctionarySound': <module 'FunctionarySound' from 'PACK: Sound/FunctionarySound.pyc'>, 'strop': <module 'strop' (built-in)>, 'errno': <module 'errno' (built-in)>, 'Map': <module 'Map' from 'PACK: Map.pyc'>, 'WeaponsTab': <module 'WeaponsTab' from 'PACK: ShipEdit/WeaponsTab.pyc'>, 'Net': <module 'Net' from 'PACK: Net/Net.pyc'>, 'SentinelSound': <module 'SentinelSound' from 'PACK: Sound/SentinelSound.pyc'>, '__main__': <module '__main__' (built-in)>, 'Doors': <module 'Doors' from 'PACK: Missions/Doors.pyc'>, 'SputnikInterface': <module 'SputnikInterface' from 'PACK: ShipEdit/SputnikInterface.pyc'>, 'Gear': <module 'Gear' from 'PACK: Chars/Gear.pyc'>, 'CharsNPC': <module 'CharsNPC' from 'PACK: Chars/CharsNPC.pyc'>, 'Init': <module 'Init' from 'PACK: Init.pyc'>, 'SAct': <module 'SAct' (built-in)>, 'Weapons': <module 'Weapons' from 'PACK: Weapons/Weapons.pyc'>, 'GearSound': <module 'GearSound' from 'PACK: Sound/GearSound.pyc'>, 'Elevator': <module 'Elevator' from 'PACK: Missions/Elevator.pyc'>, 'EMI': <module 'EMI' from 'PACK: Weapons/EMI.pyc'>, 'MissionsFuncs': <module 'MissionsFuncs' from 'PACK: Missions/MissionsFuncs.pyc'>, 'Scrap': <module 'Scrap' (built-in)>, 'Devastator': <module 'Devastator' from 'PACK: Weapons/Devastator.pyc'>, 'quickconsole': <module 'quickconsole' from '.\lib\quickconsole.pyc'>, 'Police': <module 'Police' from 'PACK: Chars/Police.pyc'>, 'BishopSound': <module 'BishopSound' from 'PACK: Sound/BishopSound.pyc'>, 'HangarTab': <module 'HangarTab' from 'PACK: ShipEdit/HangarTab.pyc'>, 'Nurse': <module 'Nurse' from 'PACK: Chars/Nurse.pyc'>, 'Bishop': <module 'Bishop' from 'PACK: Chars/Bishop.pyc'>, 'Dtritus': <module 'Dtritus' from 'PACK: Chars/Dtritus.pyc'>, 'Sentinel': <module 'Sentinel' from 'PACK: Chars/Sentinel.pyc'>, 'Parking': <module 'Parking' from 'PACK: Vehicles/Parking.pyc'>, 'SWeap': <module 'SWeap' (built-in)>, 'InMap': <module 'InMap' from 'PACK: Chars/InMap.pyc'>, 'signal': <module 'signal' (built-in)>, 'Tesla': <module 'Tesla' from 'PACK: Weapons/Tesla.pyc'>, 'SFX': <module 'SFX' (built-in)>, 'OutMap': <module 'OutMap' from 'PACK: Vehicles/OutMap.pyc'>, 'SVec': <module 'SVec' (built-in)>, 'InTraffic': <module 'InTraffic' from 'PACK: Vehicles/InTraffic.pyc'>, 'PCMenu': <module 'PCMenu' from 'PACK: Scorer/PCMenu.pyc'>, 'ShipEdit': <module 'ShipEdit' from 'PACK: ShipEdit/ShipEdit.pyc'>, 'Berto': <module 'Berto' from 'PACK: Chars/Berto.pyc'>, 'SSound': <module 'SSound' (built-in)>, 'Betty': <module 'Betty' from 'PACK: Chars/Betty.pyc'>, 'Accelerator': <module 'Accelerator' from 'PACK: Vehicles/Accelerator.pyc'>, 'Menu': <module 'Menu' from 'PACK: Scorer/Menu.pyc'>, 'Messenger': <module 'Messenger' from 'PACK: Chars/Messenger.pyc'>, 'SaveGame': <module 'SaveGame' from 'PACK: SaveGame.pyc'>, 'PoliceSound': <module 'PoliceSound' from 'PACK: Sound/PoliceSound.pyc'>, 'Vehicles': <module 'Vehicles' from 'PACK: Vehicles/Vehicles.pyc'>, 'Challenge': <module 'Challenge' from 'PACK: Missions/Challenge.pyc'>, 'VehiclesNPC': <module 'VehiclesNPC' from 'PACK: Vehicles/VehiclesNPC.pyc'>, 'string': <module 'string' from 'PACK: Python/string.pyc'>, 'Laser': <module 'Laser' from 'PACK: Weapons/Laser.pyc'>, 'imp': <module 'imp' (built-in)>, 'Sound': <module 'Sound' from 'PACK: Sound/Sound.pyc'>, 'BettySound': <module 'BettySound' from 'PACK: Sound/BettySound.pyc'>, 'GateKeeperSound': <module 'GateKeeperSound' from 'PACK: Sound/GateKeeperSound.pyc'>, 'HumphreySound': <module 'HumphreySound' from 'PACK: Sound/HumphreySound.pyc'>, 'ATPC': <module 'ATPC' from 'PACK: Weapons/ATPC.pyc'>, 'Scorer': <module 'Scorer' from 'PACK: Scorer/Scorer.pyc'>, 'Traffic': <module 'Traffic' from 'PACK: Missions/Traffic.pyc'>, 'SInput': <module 'SInput' (built-in)>, 'MakeChar': <module 'MakeChar' from 'PACK: Chars/MakeChar.pyc'>, 'OutSound': <module 'OutSound' from 'PACK: Sound/OutSound.pyc'>, 'CharAct': <module 'CharAct' from 'PACK: Chars/CharAct.pyc'>, 'NurseSound': <module 'NurseSound' from 'PACK: Sound/NurseSound.pyc'>, 'HullTab': <module 'HullTab' from 'PACK: ShipEdit/HullTab.pyc'>, 'DoorSound': <module 'DoorSound' from 'PACK: Sound/DoorSound.pyc'>, 'Humphrey': <module 'Humphrey' from 'PACK: Chars/Humphrey.pyc'>, 'Fx': <module 'Fx' from 'PACK: FX/Fx.pyc'>, 'MisItems': <module 'MisItems' from 'PACK: Missions/MisItems.pyc'>, 'SAI': <module 'SAI' (built-in)>, 'Sonic': <module 'Sonic' from 'PACK: Weapons/Sonic.pyc'>, 'regex': <module 'regex' (built-in)>, 'PoliceBoss': <module 'PoliceBoss' from 'PACK: Chars/PoliceBoss.pyc'>, 'Inferno': <module 'Inferno' from 'PACK: Weapons/Inferno.pyc'>, 'BankMaster': <module 'BankMaster' from 'PACK: Chars/BankMaster.pyc'>, 'Speech': <module 'Speech' from 'PACK: Chars/Speech.pyc'>, 'Sputnik': <module 'Sputnik' from 'PACK: Chars/Sputnik.pyc'>, 'BankDirector': <module 'BankDirector' from 'PACK: Chars/BankDirector.pyc'>, 'Swarm': <module 'Swarm' from 'PACK: Weapons/Swarm.pyc'>, 'BertoSound': <module 'BertoSound' from 'PACK: Sound/BertoSound.pyc'>, '__builtin__': <module '__builtin__' (built-in)>, 'dbg': <module 'dbg' from '.\lib\dbg.py'>, 'DtritusSound': <module 'DtritusSound' from 'PACK: Sound/DtritusSound.pyc'>, 'DTritusDesktop': <module 'DTritusDesktop' from 'PACK: Missions/DTritusDesktop.pyc'>, 'MessengerSound': <module 'MessengerSound' from 'PACK: Sound/MessengerSound.pyc'>, 'Desktop': <module 'Desktop' from 'PACK: Chars/Desktop.pyc'>, 'NewsPanel': <module 'NewsPanel' from 'PACK: Missions/NewsPanel.pyc'>}`
- *stdin*: `<open file '<stdin>', mode 'r' at d1db030>`
- *exec_prefix*: `''`
- *copyright*: `'Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam'`
- *__stderr__*: `<open file '<stderr>', mode 'w' at d1db0a0>`
- *executable*: `'D:\\Games\\Deep Silver\\Scrapland\\Bin\\Scrap.exe'`
- *builtin_module_names*: `('SAI', 'SAct', 'SFX', 'SInput', 'SLogic', 'SNet', 'SScorer', 'SSound', 'SVec', 'SWeap', 'Scrap', '__builtin__', '__main__', '_locale', 'errno', 'imp', 'marshal', 'math', 'new', 'regex', 'signal', 'strop', 'sys')`
- *__stdin__*: `<open file '<stdin>', mode 'r' at d1db030>`
- *path*: `['D:\\devel\\pythonpath', '.\\DLLs', '.\\lib', '.\\lib\\plat-win', '.\\lib\\lib-tk', 'D:\\Games\\Deep Silver\\Scrapland\\Bin', 'Scripts', 'Scripts/Scorer', 'Scripts/ShipEdit', 'Scripts/Python', 'Scripts/Weapons', 'Scripts/Vehicles', 'Scripts/Net', 'Scripts/FX', 'Scripts/Sound', 'Scripts/Chars', 'Scripts/Missions', 'Scripts/SuperDeals', 'Scripts/Split', 'Levels/Menu/Scripts', '.\\pylib\\Lib', '.\\pylib\\Libs', '.\\pylib', '.\\pylib\\Lib', '.\\pylib\\Libs', '.\\pylib', '.\\pylib\\Lib', '.\\pylib\\Libs', '.\\pylib', '.\\pylib\\Lib', '.\\pylib\\Libs', '.\\pylib']`
- *maxint*: `2147483647`
- *prefix*: `''`
- *__stdout__*: `<open file '<stdout>', mode 'w' at d1db068>`
- *setprofile*: `<built-in function setprofile>`
```
setprofile(function)

Set the profiling function.  It will be called on each function call
and return.  See the profiler chapter in the library manual.
```
- *settrace*: `<built-in function settrace>`
```
settrace(function)

Set the global debug tracing function.  It will be called on each
function call.  See the debugger chapter in the library manual.
```
- *last_traceback*: `<traceback object at d70a6a8>`
- *stdout*: `<__main__.ConsoleOutput instance at d1d3b6c>`
- *getrefcount*: `<built-in function getrefcount>`
```
getrefcount(object) -> integer

Return the current reference count for the object.  This includes the
temporary reference in the argument list, so it is at least 2.
```


## SLogic

- *IsEnemyActive*: `<built-in function IsEnemyActive>`
```
int IsEnemyActive() : Indica si hay un enemigo activo, mirando el contenido de la lista de enemigos y en el tráfico.
```
- *ChangeZoneState*: `<built-in function ChangeZoneState>`
```
void ChangeZoneState(zoneId, state): Pone el estado de una zona de dominación
```
- *SetOnFloor*: `<built-in function SetOnFloor>`
```
void SetOnFloor(Entity) : Pone una entidad en el suelo
```
- *ChangeBatonState*: `<built-in function ChangeBatonState>`
```
void ChangeBatonState(pos, state): Actualiza el estado del testigo en el modo dominación
```
- *SetShipToRegenerate*: `<built-in function SetShipToRegenerate>`
```
void SetShipToRegenerate(shipName, regSpeed,regEndSpeed): Pone una nave a regenerarse
```
- *SetDominationZones*: `<built-in function SetDominationZones>`
```
void SetDominationZones(zonesList): Establece la lista de posiciones de las zonas de dominación en la super apuesta de dominación
```
- *Flash*: `<built-in function Flash>`
```
void Flash((x,y,z),radius) : Pone una entidad en el suelo
```
- *GetNearestShip*: `<built-in function GetNearestShip>`
```
Name GetNearestShip(pos) : Cicla por varias listas y devuelve la nave más cercana a la posición indicada
```
- *SendSentinelToWatch*: `<built-in function SendSentinelToWatch>`
```
void SendSentinelToWatch(Pos) : Envia a un centinela a inspeccionar una posicion
```
- *UpdateTauntEndTime*: `<built-in function UpdateTauntEndTime>`
```
void UpdateTauntEndTime(time): Tiempo final del taunt
```
- *GearAttack*: `<built-in function GearAttack>`
```
void GearAttack(Entity) : Envia a un Gear a atacar a una entidad
```
- *SetCharState*: `<built-in function SetCharState>`
```
void SetCharState(entityName, state, entityTargetName) : Pone a una entidad en un estado de logica y un target determinados
```


## math

- *fmod*: `<built-in function fmod>`
```
fmod(x,y)

Return x % y.
```
- *log10*: `<built-in function log10>`
```
log10(x)

Return the base-10 logarithm of x.
```
- *pi*: `3.14159274101`
- *acos*: `<built-in function acos>`
```
acos(x)

Return the arc cosine of x.
```
- *sqrt*: `<built-in function sqrt>`
```
sqrt(x)

Return the square root of x.
```
- *modf*: `<built-in function modf>`
```
modf(x)

Return the fractional and integer parts of x. Both results carry the sign
of x.  The integer part is returned as a real.
```
- *sin*: `<built-in function sin>`
```
sin(x)

Return the sine of x.
```
- *atan2*: `<built-in function atan2>`
```
atan2(y, x)

Return atan(y/x).
```
- *frexp*: `<built-in function frexp>`
```
frexp(x)

Return the matissa and exponent for x. The mantissa is positive.
```
- *exp*: `<built-in function exp>`
```
exp(x)

Return e raised to the power of x.
```
- *asin*: `<built-in function asin>`
```
asin(x)

Return the arc sine of x.
```
- *floor*: `<built-in function floor>`
```
floor(x)

Return the floor of x as a real.
```
- *fabs*: `<built-in function fabs>`
```
fabs(x)

Return the absolute value of the real x.
```
- *log*: `<built-in function log>`
```
log(x)

Return the natural logarithm of x.
```
- *e*: `2.71828174591`
- *cos*: `<built-in function cos>`
```
cos(x)

Return the cosine of x.
```
- *pow*: `<built-in function pow>`
```
pow(x,y)

Return x**y.
```
- *tanh*: `<built-in function tanh>`
```
tanh(x)

Return the hyperbolic tangent of x.
```
- *tan*: `<built-in function tan>`
```
tan(x)

Return the tangent of x.
```
- *sinh*: `<built-in function sinh>`
```
sinh(x)

Return the hyperbolic sine of x.
```
- *hypot*: `<built-in function hypot>`
```
hypot(x,y)

Return the Euclidean distance, sqrt(x*x + y*y).
```
- *ldexp*: `<built-in function ldexp>`
```
ldexp_doc(x, i)

Return x * (2**i).
```
- *cosh*: `<built-in function cosh>`
```
cosh(x)

Return the hyperbolic cosine of x.
```
- *ceil*: `<built-in function ceil>`
```
ceil(x)

Return the ceiling of x as a real.
```
- *atan*: `<built-in function atan>`
```
atan(x)

Return the arc tangent of x.
```


## new

- *module*: `<built-in function module>`
```
Create a module object from (NAME).
```
- *classobj*: `<built-in function classobj>`
```
Create a class object from (NAME, BASE_CLASSES, DICT).
```
- *instancemethod*: `<built-in function instancemethod>`
```
Create a instance method object from (FUNCTION, INSTANCE, CLASS).
```
- *code*: `<built-in function code>`
```
Create a code object from (ARGCOUNT, NLOCALS, STACKSIZE, FLAGS, CODESTRING, CONSTANTS, NAMES, VARNAMES, FILENAME, NAME, FIRSTLINENO, LNOTAB).
```
- *instance*: `<built-in function instance>`
```
Create an instance object from (CLASS, DICT) without calling its __init__().
```
- *function*: `<built-in function function>`
```
Create a function object from (CODE, GLOBALS, [NAME, ARGDEFS]).
```


## SNet

- *SendUsrString*: `<built-in function SendUsrString>`
```
SendUsrString(id,string) : -1 significa a todo el mundo en modo servidor, para cliente id se ignora
```
- *InitServer*: `<built-in function InitServer>`
```
InitServer(LevelPath,MaxPlayers,ipport) : Intenta inicializar el servidor.
```
- *GetBotName*: `<built-in function GetBotName>`
```
GetBotName() : Obtiene un nombre valido de entidad jugador manejada por el servidor (bot o jugador local)
```
- *CloseServer*: `<built-in function CloseServer>`
```
CloseServer(LevelPath) : Acaba el servidor y carga un nivel.
```
- *IsClient*: `<built-in function IsClient>`
```
IsClient() : 1 si esta activado el sistema cliente 
NOTA: Scrap.GetNetFlags() tiene el flag cliente activado 
si la coneccion se hizo efectiva
```
- *ServerChangeLevel*: `<built-in function ServerChangeLevel>`
```
ServerChangeLevel(resource name) : carga el siguiente nivel.
```
- *DoneBrowser*: `<built-in function DoneBrowser>`
```
DoneBrowser() : Cierra el browser de red local.
```
- *InitClient*: `<built-in function InitClient>`
```
InitClient(ipAddress,ipport) : Inicia el proceso de coneccion con el servidor.
```
- *CloseClient*: `<built-in function CloseClient>`
```
CloseClient(LevelPath) : Acaba el cliente y carga un nivel.
```
- *IsServer*: `<built-in function IsServer>`
```
IsServer() : 1 si esta activado el sistema servidor 
 NOTA: es para depuracion, mejor use Scrap.GetNetFlags()
```
- *GetObjName*: `<built-in function GetObjName>`
```
GetObjName() : Obtiene un nombre valido de Objeto cualesquiera.
```
- *GetMyClientShip*: `<built-in function GetMyClientShip>`
```
GetMyClientShip() : retorna el nombre de su nave.
```
- *ModifyUsrData*: `<built-in function ModifyUsrData>`
```
ModifyUsrData(ClientId) : 
 modifica desde el servidor los datos locales.
```
- *AddResource*: `<built-in function AddResource>`
```
resourceid AddResource(resource name) : intenta agregar un recurso si este no existe. -1 si el pool esta lleno
```
- *SendChatString*: `<built-in function SendChatString>`
```
SendChatString(id,string) : -1 significa a todo el mundo en modo servidor, para cliente id se ignora
```
- *GetClientData*: `<built-in function GetClientData>`
```
GetClientData() : Obtiene la tupla (ipaddress,ipport)
```
- *InitBrowser*: `<built-in function InitBrowser>`
```
InitBrowser(port) : Inicializa el browser de red local.
```
- *SendMasterString*: `<built-in function SendMasterString>`
```
SendMasterString(string) : envia una cadena al master. Si retorna cero no hay master.
```
- *PingInetSvrs*: `<built-in function PingInetSvrs>`
```
PingInetSvrs() : 1 exitoso. revisa el estado de los servidores en internet. Se realiza despues de browse.
```
- *IsMaster*: `<built-in function IsMaster>`
```
IsMaster() : 1 si esta activado el sistema cliente 
NOTA: Scrap.GetNetFlags() tiene el flag cliente activado 
si la coneccion se hizo efectiva
```
- *GetServerData*: `<built-in function GetServerData>`
```
GetServerData() : Obtiene la tupla (Hostname,ipaddress,ipport)
```


## strop

- *translate*: `<built-in function translate>`
```
translate(s,table [,deletechars]) -> string

Return a copy of the string s, where all characters occurring
in the optional argument deletechars are removed, and the
remaining characters have been mapped through the given
translation table, which must be a string of length 256.
```
- *rstrip*: `<built-in function rstrip>`
```
rstrip(s) -> string

Return a copy of the string s with trailing whitespace removed.
```
- *maketrans*: `<built-in function maketrans>`
```
maketrans(frm, to) -> string

Return a translation table (a string of 256 bytes long)
suitable for use in string.translate.  The strings frm and to
must be of the same length.
```
- *splitfields*: `<built-in function splitfields>`
```
split(str [,sep [,maxsplit]]) -> list of strings
splitfields(str [,sep [,maxsplit]]) -> list of strings

Return a list of the words in the string s, using sep as the
delimiter string.  If maxsplit is nonzero, splits into at most
maxsplit words If sep is not specified, any whitespace string
is a separator.  Maxsplit defaults to 0.

(split and splitfields are synonymous)
```
- *split*: `<built-in function split>`
```
split(str [,sep [,maxsplit]]) -> list of strings
splitfields(str [,sep [,maxsplit]]) -> list of strings

Return a list of the words in the string s, using sep as the
delimiter string.  If maxsplit is nonzero, splits into at most
maxsplit words If sep is not specified, any whitespace string
is a separator.  Maxsplit defaults to 0.

(split and splitfields are synonymous)
```
- *rfind*: `<built-in function rfind>`
```
rfind(s, sub [,start [,end]]) -> int

Return the highest index in s where substring sub is found,
such that sub is contained within s[start,end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
```
- *expandtabs*: `<built-in function expandtabs>`
```
expandtabs(string, [tabsize]) -> string

Expand tabs in a string, i.e. replace them by one or more spaces,
depending on the current column and the given tab size (default 8).
The column number is reset to zero after each newline occurring in the
string.  This doesn't understand other non-printing characters.
```
- *atof*: `<built-in function atof>`
```
atof(s) -> float

Return the floating point number represented by the string s.
```
- *join*: `<built-in function join>`
```
join(list [,sep]) -> string
joinfields(list [,sep]) -> string

Return a string composed of the words in list, with
intervening occurences of sep.  Sep defaults to a single
space.

(join and joinfields are synonymous)
```
- *lower*: `<built-in function lower>`
```
lower(s) -> string

Return a copy of the string s converted to lowercase.
```
- *count*: `<built-in function count>`
```
count(s, sub[, start[, end]]) -> int

Return the number of occurrences of substring sub in string
s[start:end].  Optional arguments start and end are
interpreted as in slice notation.
```
- *find*: `<built-in function find>`
```
find(s, sub [,start [,end]]) -> in

Return the lowest index in s where substring sub is found,
such that sub is contained within s[start,end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
```
- *capitalize*: `<built-in function capitalize>`
```
capitalize(s) -> string

Return a copy of the string s with only its first character
capitalized.
```
- *strip*: `<built-in function strip>`
```
strip(s) -> string

Return a copy of the string s with leading and trailing
whitespace removed.
```
- *atol*: `<built-in function atol>`
```
atol(s [,base]) -> long

Return the long integer represented by the string s in the
given base, which defaults to 10.  The string s must consist
of one or more digits, possibly preceded by a sign.  If base
is 0, it is chosen from the leading characters of s, 0 for
octal, 0x or 0X for hexadecimal.  If base is 16, a preceding
0x or 0X is accepted.  A trailing L or l is not accepted,
unless base is 0.
```
- *lowercase*: `'abcdefghijklmnopqrstuvwxyz'`
- *atoi*: `<built-in function atoi>`
```
atoi(s [,base]) -> int

Return the integer represented by the string s in the given
base, which defaults to 10.  The string s must consist of one
or more digits, possibly preceded by a sign.  If base is 0, it
is chosen from the leading characters of s, 0 for octal, 0x or
0X for hexadecimal.  If base is 16, a preceding 0x or 0X is
accepted.
```
- *replace*: `<built-in function replace>`
```
replace (str, old, new[, maxsplit]) -> string

Return a copy of string str with all occurrences of substring
old replaced by new. If the optional argument maxsplit is
given, only the first maxsplit occurrences are replaced.
```
- *swapcase*: `<built-in function swapcase>`
```
swapcase(s) -> string

Return a copy of the string s with upper case characters
converted to lowercase and vice versa.
```
- *uppercase*: `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
- *lstrip*: `<built-in function lstrip>`
```
lstrip(s) -> string

Return a copy of the string s with leading whitespace removed.
```
- *joinfields*: `<built-in function joinfields>`
```
join(list [,sep]) -> string
joinfields(list [,sep]) -> string

Return a string composed of the words in list, with
intervening occurences of sep.  Sep defaults to a single
space.

(join and joinfields are synonymous)
```
- *whitespace*: `'\011\012\013\014\015 '`
- *upper*: `<built-in function upper>`
```
upper(s) -> string

Return a copy of the string s converted to uppercase.
```


## errno

- *ENODEV*: `19`
- *EHOSTUNREACH*: `10065`
- *EUSERS*: `10068`
- *WSAENETDOWN*: `10050`
- *WSAEAFNOSUPPORT*: `10047`
- *WSAEHOSTUNREACH*: `10065`
- *WSAELOOP*: `10062`
- *WSAESTALE*: `10070`
- *ENOSYS*: `40`
- *EINVAL*: `22`
- *WSAEINTR*: `10004`
- *WSAEUSERS*: `10068`
- *EINTR*: `4`
- *WSANOTINITIALISED*: `10093`
- *EPROTOTYPE*: `10041`
- *ENOBUFS*: `10055`
- *WSAENOPROTOOPT*: `10042`
- *EREMOTE*: `10071`
- *WSAEFAULT*: `10014`
- *ECHILD*: `10`
- *ELOOP*: `10062`
- *EXDEV*: `18`
- *EPROTONOSUPPORT*: `10043`
- *ESRCH*: `3`
- *WSAENOTSOCK*: `10038`
- *EAFNOSUPPORT*: `10047`
- *WSAEPROCLIM*: `10067`
- *EHOSTDOWN*: `10064`
- *EPFNOSUPPORT*: `10046`
- *ENOPROTOOPT*: `10042`
- *EBUSY*: `16`
- *errorcode*: `{29: 'ESPIPE', 20: 'ENOTDIR', 1: 'EPERM', 40: 'ENOSYS', 16: 'EBUSY', 25: 'ENOTTY', 10101: 'WSAEDISCON', 10093: 'WSANOTINITIALISED', 10092: 'WSAVERNOTSUPPORTED', 10091: 'WSASYSNOTREADY', 10071: 'WSAEREMOTE', 10070: 'WSAESTALE', 10069: 'WSAEDQUOT', 10068: 'WSAEUSERS', 10067: 'WSAEPROCLIM', 10066: 'WSAENOTEMPTY', 10065: 'WSAEHOSTUNREACH', 10064: 'WSAEHOSTDOWN', 10063: 'WSAENAMETOOLONG', 10062: 'WSAELOOP', 10061: 'WSAECONNREFUSED', 10060: 'WSAETIMEDOUT', 10059: 'WSAETOOMANYREFS', 10058: 'WSAESHUTDOWN', 10057: 'WSAENOTCONN', 10056: 'WSAEISCONN', 10055: 'WSAENOBUFS', 10054: 'WSAECONNRESET', 10053: 'WSAECONNABORTED', 10052: 'WSAENETRESET', 10051: 'WSAENETUNREACH', 10050: 'WSAENETDOWN', 10049: 'WSAEADDRNOTAVAIL', 10048: 'WSAEADDRINUSE', 10047: 'WSAEAFNOSUPPORT', 10046: 'WSAEPFNOSUPPORT', 10045: 'WSAEOPNOTSUPP', 10044: 'WSAESOCKTNOSUPPORT', 10043: 'WSAEPROTONOSUPPORT', 10042: 'WSAENOPROTOOPT', 10041: 'WSAEPROTOTYPE', 10040: 'WSAEMSGSIZE', 10039: 'WSAEDESTADDRREQ', 10038: 'WSAENOTSOCK', 10037: 'WSAEALREADY', 10036: 'WSAEINPROGRESS', 10035: 'WSAEWOULDBLOCK', 42: 'EILSEQ', 41: 'ENOTEMPTY', 10024: 'WSAEMFILE', 39: 'ENOLCK', 10022: 'WSAEINVAL', 36: 'EDEADLOCK', 34: 'ERANGE', 33: 'EDOM', 32: 'EPIPE', 31: 'EMLINK', 10014: 'WSAEFAULT', 10013: 'WSAEACCES', 28: 'ENOSPC', 27: 'EFBIG', 10009: 'WSAEBADF', 24: 'EMFILE', 23: 'ENFILE', 22: 'EINVAL', 21: 'EISDIR', 10004: 'WSAEINTR', 19: 'ENODEV', 18: 'EXDEV', 17: 'EEXIST', 10000: 'WSABASEERR', 14: 'EFAULT', 13: 'EACCES', 12: 'ENOMEM', 11: 'EAGAIN', 10: 'ECHILD', 9: 'EBADF', 8: 'ENOEXEC', 7: 'E2BIG', 6: 'ENXIO', 5: 'EIO', 38: 'ENAMETOOLONG', 3: 'ESRCH', 2: 'ENOENT', 30: 'EROFS', 4: 'EINTR'}`
- *ESTALE*: `10070`
- *WSAEREMOTE*: `10071`
- *ERANGE*: `34`
- *ESPIPE*: `29`
- *WSAEHOSTDOWN*: `10064`
- *EWOULDBLOCK*: `10035`
- *WSAETOOMANYREFS*: `10059`
- *EBADF*: `9`
- *EISCONN*: `10056`
- *EIO*: `5`
- *ETIMEDOUT*: `10060`
- *ENOSPC*: `28`
- *WSAEBADF*: `10009`
- *ENETUNREACH*: `10051`
- *EALREADY*: `10037`
- *ENETDOWN*: `10050`
- *WSAECONNRESET*: `10054`
- *EACCES*: `13`
- *WSAENAMETOOLONG*: `10063`
- *EDOM*: `33`
- *EILSEQ*: `42`
- *WSAETIMEDOUT*: `10060`
- *ENOTDIR*: `20`
- *WSAECONNABORTED*: `10053`
- *WSAEACCES*: `10013`
- *EPERM*: `1`
- *WSAENOBUFS*: `10055`
- *ENETRESET*: `10052`
- *ENOTEMPTY*: `41`
- *ECONNREFUSED*: `10061`
- *EISDIR*: `21`
- *WSAEDISCON*: `10101`
- *EROFS*: `30`
- *WSABASEERR*: `10000`
- *EADDRNOTAVAIL*: `10049`
- *EDESTADDRREQ*: `10039`
- *WSAEMSGSIZE*: `10040`
- *WSAENOTEMPTY*: `10066`
- *WSAEPROTOTYPE*: `10041`
- *WSAEDESTADDRREQ*: `10039`
- *WSAEADDRINUSE*: `10048`
- *WSAEADDRNOTAVAIL*: `10049`
- *WSAEALREADY*: `10037`
- *WSAEPROTONOSUPPORT*: `10043`
- *WSASYSNOTREADY*: `10091`
- *WSAESHUTDOWN*: `10058`
- *ENFILE*: `23`
- *ESHUTDOWN*: `10058`
- *EMSGSIZE*: `10040`
- *ENOENT*: `2`
- *EEXIST*: `17`
- *EDQUOT*: `10069`
- *WSAEPFNOSUPPORT*: `10046`
- *WSAEOPNOTSUPP*: `10045`
- *WSAEISCONN*: `10056`
- *WSAEDQUOT*: `10069`
- *WSAEWOULDBLOCK*: `10035`
- *WSAENETUNREACH*: `10051`
- *EFAULT*: `14`
- *EFBIG*: `27`
- *EDEADLK*: `36`
- *ENOTCONN*: `10057`
- *WSAENETRESET*: `10052`
- *WSAENOTCONN*: `10057`
- *ENOLCK*: `39`
- *ECONNABORTED*: `10053`
- *WSAEINVAL*: `10022`
- *WSAEINPROGRESS*: `10036`
- *ENOMEM*: `12`
- *ENOTSOCK*: `10038`
- *WSAEMFILE*: `10024`
- *ENOEXEC*: `8`
- *EMLINK*: `31`
- *ECONNRESET*: `10054`
- *WSAESOCKTNOSUPPORT*: `10044`
- *EADDRINUSE*: `10048`
- *WSAVERNOTSUPPORTED*: `10092`
- *EAGAIN*: `11`
- *ENAMETOOLONG*: `38`
- *ENOTTY*: `25`
- *EOPNOTSUPP*: `10045`
- *ESOCKTNOSUPPORT*: `10044`
- *EDEADLOCK*: `36`
- *ETOOMANYREFS*: `10059`
- *WSAECONNREFUSED*: `10061`
- *EMFILE*: `24`
- *EPIPE*: `32`
- *EINPROGRESS*: `10036`
- *ENXIO*: `6`
- *E2BIG*: `7`


## __main__

- *SVec*: `<module 'SVec' (built-in)>`
- *SFX*: `<module 'SFX' (built-in)>`
- *SSound*: `<module 'SSound' (built-in)>`
- *ConsoleErrorOutput*: `<class __main__.ConsoleErrorOutput at d1ec00c>`
- *dbg*: `<module 'dbg' from '.\lib\dbg.py'>`
- *SScorer*: `<module 'SScorer' (built-in)>`
- *SInput*: `<module 'SInput' (built-in)>`
- *Init*: `<module 'Init' from 'PACK: Init.pyc'>`
- *SWeap*: `<module 'SWeap' (built-in)>`
- *SNet*: `<module 'SNet' (built-in)>`
- *SAct*: `<module 'SAct' (built-in)>`
- *ConsoleOutput*: `<class __main__.ConsoleOutput at d1ebfec>`
- *Scrap*: `<module 'Scrap' (built-in)>`
- *__builtins__*: `<module '__builtin__' (built-in)>`
```
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
```
- *sys*: `<module 'sys' (built-in)>`
```
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules
exitfunc -- you may set this to a function to be called when Python exits

stdin -- standard input file object; used by raw_input() and input()
stdout -- standard output file object; used by the print statement
stderr -- standard error object; used for error messages
  By assigning another file object (or an object that behaves like a file)
  to one of these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

exc_type -- type of exception currently being handled
exc_value -- value of exception currently being handled
exc_traceback -- traceback of exception currently being handled
  The function exc_info() should be used instead of these three,
  because it is thread-safe.

Static objects:

maxint -- the largest supported integer (the smallest is -maxint-1)
builtin_module_names -- tuple of module names built into this intepreter
version -- the version of this interpreter
copyright -- copyright notice pertaining to this interpreter
platform -- platform identifier
executable -- pathname of this Python interpreter
prefix -- prefix used to find the Python library
exec_prefix -- prefix used to find the machine-specific Python library
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
__stdin__ -- the original stdin; don't use!
__stdout__ -- the original stdout; don't use!
__stderr__ -- the original stderr; don't use!

Functions:

exc_info() -- return thread-safe information about the current exception
exit() -- exit the interpreter by raising SystemExit
getrefcount() -- return the reference count for an object (plus one :-)
setcheckinterval() -- control how often the interpreter checks for events
setprofile() -- set the global profiling function
settrace() -- set the global debug tracing function

```
- *SAI*: `<module 'SAI' (built-in)>`
- *SLogic*: `<module 'SLogic' (built-in)>`


## SAct

- *CreateClass*: `<built-in function CreateClass>`
```
CreateClass(classname) : Crea una clase de objeto animado
```
- *CreateAction*: `<built-in function CreateAction>`
```
CreateAction(varname) :  Crea una accion en la clase actual.
```
- *DelClass*: `<built-in function DelClass>`
```
DelClass(classname) : Crea una clase de objeto animado
```
- *SetCls*: `<built-in function SetCls>`
```
SetCls(varname,value) :  Modifica el valor de una variable de una clase objeto animado
```
- *GetCls*: `<built-in function GetCls>`
```
GetCls(varname) :  Obtiene el valor de una variable de una clase objeto animado
```
- *GetClass*: `<built-in function GetClass>`
```
GetClass(classname) : Activa una clase de objeto animado
```
- *SetAct*: `<built-in function SetAct>`
```
SetAct(varname,value) :  Modifica el valor de una variable de la accion de una clase objeto animado
```
- *GetAct*: `<built-in function GetAct>`
```
GetAct(varname) :  Obtiene el valor de una variable de la accion de una clase objeto animado
```
- *GetAction*: `<built-in function GetAction>`
```
GetAction(varname) :  Obtiene una accion de la clase actual.
```


## Scrap

- *DropDebris*: `<built-in function DropDebris>`
```
DropDebris(name,size) : Lanza un objeto que cae y rebota hasta que desaparece
```
- *ShowGVars*: `<built-in function ShowGVars>`
```
ShowGVars() :  Muestra una lista de todas las variables globales
```
- *GetNewLevelPath*: `<built-in function GetNewLevelPath>`
```
levelpath GetNewLevelPath() :  Obtiene el path del próximo nivel
```
- *SetTime*: `<built-in function SetTime>`
```
SetTime(Time) :  Cambia el tiempo del mundo en segundos
```
- *SetCam*: `<built-in function SetCam>`
```
SetCam(i,name) :  Activa una camara
```
- *PreloadAnm*: `<built-in function PreloadAnm>`
```
PreloadAnm(ObjFilename,AnmFilename) :  Precarga una animacion
```
- *GetCam*: `<built-in function GetCam>`
```
name GetCam(i) :  Obtiene el nombre de una entidad camara
```
- *GetLockAlarm*: `<built-in function GetLockAlarm>`
```
Scrap.GetLockAlarm() : verdadero si la alarma esta bloqueada
```
- *AddItem*: `<built-in function AddItem>`
```
Scrap.AddItem(Life, string name, int life) : Add Item Life.
 Scrap.AddItem(Ammo, string name, int typeAmmo, int ammo) : Add Item Ammo.
```
- *Verbose*: `<built-in function Verbose>`
```
Verbose(string name) :  Muestra un mensaje de parloteo por la consola
```
- *StartDummySearch*: `<built-in function StartDummySearch>`
```
StartDummySearch(name,usewildcards) : Inicia la busqueda de dummies en el mapa
```
- *OpenPack*: `<built-in function OpenPack>`
```
OpenPack(string PackPath) :  Abre un archivo *.packed
```
- *LaunchDashboard*: `<built-in function LaunchDashboard>`
```
int Scrap.LaunchDashboard() : sale del juego y ejecuta el dashboard.
```
- *SaveGameVars*: `<built-in function SaveGameVars>`
```
Scrap.SaveGameVars(str, str) : Salva un juego en un archivo, con un nombre opcional
```
- *SphereCall*: `<built-in function SphereCall>`
```
Scrap.SphereCall(x,y,z,radius,´strmask´,´callback´,[IgnoreGeometry=1]) : testea una esfera y llama a ´callback´ por cada entidad que colisiona
```
- *SetTimeSpeed*: `<built-in function SetTimeSpeed>`
```
SetTimeSpeed(TimeSpeed) :  Cambia la velocidad del tiempo del mundo.
```
- *Preload3DObject*: `<built-in function Preload3DObject>`
```
Preload3DObject(filename,scalex,scaley,scalez) :  Precarga un objeto 3D
```
- *TestLine*: `<built-in function TestLine>`
```
((x,y,z),s) TestLine((x,y,z),(fz,fy,fz),'strmask') : testea una linea y devuelve el nombre de la entidad y punto de colision  o '' si es el mapa o None
```
- *GetFreeBlocks*: `<built-in function GetFreeBlocks>`
```
int Scrap.GetFreeBlocks() : obtiene los bloques libres en el disco duro.
```
- *IncSaveVar*: `<built-in function IncSaveVar>`
```
int Scrap.IncSaveVar(str[,value]) : incrementa un contador de estadisticas
```
- *DeselectProfile*: `<built-in function DeselectProfile>`
```
Scrap.DeselectProfile() : deselecciona el profile actual.
```
- *GetMoney*: `<built-in function GetMoney>`
```
money Scrap.GetMoney() : Devuelve el liquido disponible.
```
- *CreateElements*: `<built-in function CreateElements>`
```
CreateElements() :  Crea una lista de elementos estaticos que pertenecen al mapa.
```
- *NextDummySearch*: `<built-in function NextDummySearch>`
```
(s(ddd)(dd)i) NextDummySearch() : Obtiene el proximo dummy, sino None
```
- *CreateEntity*: `<built-in function CreateEntity>`
```
CreateEntity(name,x,y,z,type) :  Crea una una entidad
```
- *LoadLevel*: `<built-in function LoadLevel>`
```
LoadLevel(string name) :  Carga un nivel en el siguiente frame
```
- *DebugInput*: `<built-in function DebugInput>`
```
string DebugInput() :  Detiene todo para iniciar la depuracion
```
- *GetLangStr*: `<built-in function GetLangStr>`
```
str Scrap.GetLangStr(Name) : Obtiene una cadena de lenguaje. '' si no existe.
```
- *Get*: `<built-in function Get>`
```
Get('GlobalVar') :  Obtiene el valor de una variable global
```
- *SetAlarmChar*: `<built-in function SetAlarmChar>`
```
Scrap.SetAlarmChar(El_que_se_busca) : Modifica el personaje que se busca.
```
- *GetEntity*: `<built-in function GetEntity>`
```
GetEntity(string name) :  Retorna una entidad
```
- *GetLanguage*: `<built-in function GetLanguage>`
```
lang Scrap.GetLanguage() : Obtiene la lengua actual. None si no fue inicializada.
```
- *Print*: `<built-in function Print>`
```
Print(string name) :  Muestra un mensaje por la consola siempre
```
- *SwitchMissionArrows*: `<built-in function SwitchMissionArrows>`
```
SwitchMissionArrows(MainMissionFile,TargetMissionFile) : Cambia las flechas de mision primaria y secundaria (Modelos)
```
- *GetFarestParked*: `<built-in function GetFarestParked>`
```
Entity,Pos =  Scrap.GetFarestParked([isparked[,fromPos]]) : Obtiene la nave aparcada mas lejana.
```
- *CreateSaveProfile*: `<built-in function CreateSaveProfile>`
```
int Scrap.CreateSaveProfile(str) : Crea un Save profile para X-Box y pone como actual.
```
- *ExtractPack*: `<built-in function ExtractPack>`
```
ExtractPack(string PackPath) :  Extrae un archivo *.packed
```
- *SetLockAlarm*: `<built-in function SetLockAlarm>`
```
Scrap.SetLockAlarm(1/0) : Bloquea/desbloquea la alarma
```
- *SetSaveVar*: `<built-in function SetSaveVar>`
```
bool Scrap.SetSaveVar(Name,DefValue) : Modifica una variable (si puede)
```
- *ListModels*: `<built-in function ListModels>`
```
ListModels() : Muestra una lista de modelos y escenas
```
- *ConsoleOut*: `<built-in function ConsoleOut>`
```
ConsoleOut(string name) :  Muestra un mensaje pyton por la consola
```
- *ScreenShot*: `<built-in function ScreenShot>`
```
ScreenShot(filename) : Screenshot of the current frame
```
- *SetMoney*: `<built-in function SetMoney>`
```
Scrap.SetMoney(money) : Determina el liquido disponible
```
- *GetFirst*: `<built-in function GetFirst>`
```
GetFirst() :  Retorna la primera entuidad de la lista o none
```
- *LoadGameVars*: `<built-in function LoadGameVars>`
```
Scrap.LoadGameVars(str) : Carga un juego en un archivo
```
- *GetTime*: `<built-in function GetTime>`
```
GetTime() :  Obtiene el tiempo del mundo en segundos
```
- *GetAlarmChars*: `<built-in function GetAlarmChars>`
```
(Actual, El_que_se_busca) Scrap.GetAlarmChars() : Obtiene los tipos de personaje que se buscan.
```
- *SetVideoCurrentMode*: `<built-in function SetVideoCurrentMode>`
```
SetVideoCurrentMode() : Set Video Current Mode Index
```
- *AddScheduledFunc*: `<built-in function AddScheduledFunc>`
```
AddScheduledFunc(time,func,params[,name]) : Ejecuta un codigo en python en un instante de tiempo.
```
- *ClosePack*: `<built-in function ClosePack>`
```
ClosePack() :  Abre un archivo *.packed
```
- *CreateEntityList*: `<built-in function CreateEntityList>`
```
CreateEntityList(listName) :  Crea una lista de entidades
```
- *ProcessDVF*: `<built-in function ProcessDVF>`
```
ProcessDVF(filename,command) : send a dvf command
```
- *SetAlarm*: `<built-in function SetAlarm>`
```
Scrap.SetAlarm(dialpos) : pone la alarma en una posicion (0 desactiva, 1 activa).
```
- *GetNearestParked*: `<built-in function GetNearestParked>`
```
Entity,Pos = Scrap.GetNearestParked([isparked[,fromPos]]) : Obtiene la nave aparcada mas cercana.
```
- *Set*: `<built-in function Set>`
```
Set('GlobalVar',val) :  Modifica el valor de una variable global
```
- *PythonCompileAll*: `<built-in function PythonCompileAll>`
```
PythonCompileAll() :  compila recursivamente los archivos .py
```
- *Rand*: `<built-in function Rand>`
```
Rand(min,max) :  Obtiene un numero seudo-aleatorio entre (min,max)
```
- *Def*: `<built-in function Def>`
```
Def('GlobalVar') :  Obtiene el valor por defecto de una variable global
```
- *Round*: `<built-in function Round>`
```
Round(num) : Redondea un numero real al entero más cercano.
```
- *ModelInfo*: `<built-in function ModelInfo>`
```
ModelInfo(name) : Muestra información sobre la jerarquía de nodos del modelo
```
- *UsrEntity*: `<built-in function UsrEntity>`
```
UsrEntity(ictr) :  Retorna una entidad controlada por usario (personaje o nave)
```
- *GetAlarm*: `<built-in function GetAlarm>`
```
(active,dialpos,growcode) Scrap.GetAlarm() : Obtiene informacion de la alarma.
```
- *SetDebrisValue*: `<built-in function SetDebrisValue>`
```
SetDebrisValue(id,x,y,z) : id = 0:Posicion, 1:Angulos, 2:Velocidad, 3:Velocidad de rotacion
```
- *MusicPlayer*: `<built-in function MusicPlayer>`
```
MusicPlayer(filename[,command,param1]) : play music file
```
- *Des*: `<built-in function Des>`
```
Des('GlobalVar') :  Obtiene el descriptor de una variable global
```
- *SetCallFunc*: `<built-in function SetCallFunc>`
```
Scrap.SetCallFunc('!funcname') : Especifica la funcion callback (c++) a llamar. (1 si existe)
```
- *SetDebrisSys*: `<built-in function SetDebrisSys>`
```
SetDebrisSys(name,initialnumber,MaxDist,Friction,Scale,Grav,bounce)  crea/modifica un sistema de debris
```
- *Execute*: `<built-in function Execute>`
```
Scrap.Execute() : Ejecuta una funcion callback (c++).
```
- *AddParamf*: `<built-in function AddParamf>`
```
Scrap.AddParamf(Float) : Incluye un parametro a una funcion callback (c++).
```
- *PreloadLibrary*: `<built-in function PreloadLibrary>`
```
PreloadLibrary(LibraryName,CompiledFile) :  Precarga una libreria de un archivo empaquetado
```
- *GetVideoCurrentMode*: `<built-in function GetVideoCurrentMode>`
```
GetVideoCurrentMode() : Get Video Current Mode Index
```
- *InitLoading*: `<built-in function InitLoading>`
```
InitLoading() Inicia la pantalla de carga rapida.
```
- *CallElements*: `<built-in function CallElements>`
```
CallElements('Function') :  llama una funcion Function(Name,x,y,z,angx,angy)
```
- *GetTimeSpeed*: `<built-in function GetTimeSpeed>`
```
GetTimeSpeed() :  Obtiene la velocidad del tiempo del mundo.
```
- *CreateSaveVar*: `<built-in function CreateSaveVar>`
```
bool Scrap.CreateSaveVar(Name,DefValue) : Crea una nueva variable (si puede)
```
- *EntityListGet*: `<built-in function EntityListGet>`
```
(value)Scrap.EntityListGet(listName, varName) :  Obtiene el valor de una variable de una lista de entidades
```
- *DeleteProfile*: `<built-in function DeleteProfile>`
```
int Scrap.DeleteProfile(str) : Borra un profile de X-Box.
```
- *AddParami*: `<built-in function AddParami>`
```
Scrap.AddParami(int) : Incluye un parametro a una funcion callback (c++).
```
- *VideoPlayer*: `<built-in function VideoPlayer>`
```
VideoPlayer(filename[,command]) : play video file
```
- *SetLanguage*: `<built-in function SetLanguage>`
```
res Scrap.SetLanguage(Name[,forcetoreload]) : Modifica la lengua actual. false si ya es la lengua la selecionada
```
- *AddParams*: `<built-in function AddParams>`
```
Scrap.AddParams(string) : Incluye un parametro a una funcion callback (c++).
```
- *GetVideoModes*: `<built-in function GetVideoModes>`
```
GetVideoModes(NumMode) : Get Video Mode Info
```
- *GetSaveGamesList*: `<built-in function GetSaveGamesList>`
```
 [(fecha, slot)] Scrap.GetSaveGamesList() : Devuelve una lista de tuplas donde para cada tupla el primer elemento indica el nombre (fecha) del archivo y el segundo elemento indica el slot del que se leerá la partida. La lista está ordenada por la fecha, de la más reciente a la más antigua.
```
- *GetLevelPath*: `<built-in function GetLevelPath>`
```
levelpath GetLevelPath() :  Obtiene el path del nivel actual
```
- *BuildFont*: `<built-in function BuildFont>`
```
BuildFont(name,size) : Construye un archivo de fuente de letras a partir de un .TGA dado
```
- *DeleteScheduledFuncs*: `<built-in function DeleteScheduledFuncs>`
```
DeleteScheduledFuncs(name) : Borra las scheduled funcs creadas con un nombre dado.
```
- *GetNetFlags*: `<built-in function GetNetFlags>`
```
GetNetFlags() :  Obtiene la tupla de flags : client, server, dedicated
```
- *GetSaveVar*: `<built-in function GetSaveVar>`
```
value Scrap.GetSaveVar(Name) : obtiene una variable o devuelve none
```
- *GetLangEntries*: `<built-in function GetLangEntries>`
```
[str] Scrap.GetLangEntries(Name) : Obtiene un subconjunto de entradas de la tabla de lenguaje que empiecen por 'Name'.
```
- *FileExist*: `<built-in function FileExist>`
```
FileExist() check for file existence.
```
- *GetMinCamDist*: `<built-in function GetMinCamDist>`
```
GetMinCamDist(x,y,z) :  Obtiene la distancia de un punto a la camara
```
- *EntityListSet*: `<built-in function EntityListSet>`
```
EntityListSet(listName, varName, value) :  Modifica el valor de una variable de una lista de entidades
```
- *SetAlarmGrow*: `<built-in function SetAlarmGrow>`
```
Scrap.SetAlarmGrow(growcode) : -1 baja, 0 se mantiene, 1 sube.
```
- *Exit*: `<built-in function Exit>`
```
Exit() sale del juego.
```
- *DelSaveVars*: `<built-in function DelSaveVars>`
```
Scrap.DelSaveVars(str) : Elimina las <str>* variables
```
- *SaveConfig*: `<built-in function SaveConfig>`
```
res Scrap.SaveConfig() : Guarda el fichero de configuración
```
- *SetSaveProfile*: `<built-in function SetSaveProfile>`
```
int Scrap.SetSaveProfile(path,name) : Carga un profile de jugador.
```
- *GetSavedProfilesList*: `<built-in function GetSavedProfilesList>`
```
[(Directorio, nombre)] Scrap.GetSavedProfilesList() : Devuelve una lista de tuplas donde para cada tupla el primer elemento indica el directorio del profile y el segundo elemento indica el nombre del profile. La lista está ordenada por el criterio de microsoft 
```
- *SetGrid*: `<built-in function SetGrid>`
```
SetGrid(x,y,z) :  Modifica las dimensiones del grid de colision
```
- *TestSphere*: `<built-in function TestSphere>`
```
Scrap.TestSphere(x,y,z,radius,´strmask´) : testea una esfera y devuelve el nombre de la entidad o '' si es el mapa o None
```
- *EndLoading*: `<built-in function EndLoading>`
```
EndLoading() Inicia la pantalla de carga rapida.
```
- *Ver*: `<built-in function Ver>`
```
Ver() Obtiene la version del juego.
```
- *ConsoleError*: `<built-in function ConsoleError>`
```
ConsoleError(string name) :  Muestra un mensaje de error por la consola
```
- *GetFloor*: `<built-in function GetFloor>`
```
i GetFloor(y) :  Obtiene el numero de piso en el que esta.
```
- *AddParkingZone*: `<built-in function AddParkingZone>`
```
Scrap.AddParkingZone(occupied,pos,name) : Agrega un sitio de parking.
```


## SWeap

- *SetSWeap*: `<built-in function SetSWeap>`
```
SetSWeap(numammo,svar,svalue) : Pone un valor cadena de las municiones
```
- *FillPriority*: `<built-in function FillPriority>`
```
FillPriority() : Inizializa las prioridades de las armas
```
- *GetSAmmo*: `<built-in function GetSAmmo>`
```
GetSAmmo(numammo,svar) : Obtiene un valor cadena de las municiones
```
- *SetFAmmo*: `<built-in function SetFAmmo>`
```
GetFAmmo(numammo,svar,fvalue) : Pone un valor numerico de las municiones
```
- *InitWeap*: `<built-in function InitWeap>`
```
InitWeap(num) : Inicializa las armas num es el numero de armas
```
- *GetNWeap*: `<built-in function GetNWeap>`
```
GetNWeap() : Obtiene el numero de armas en el juego
```
- *GetFAmmo*: `<built-in function GetFAmmo>`
```
GetFAmmo(numammo,svar) : Obtiene un valor numerico de las municiones
```
- *GetFirstiWeap*: `<built-in function GetFirstiWeap>`
```
GetFirstiWeap() : Obtiene el arma primera y por defecto
```
- *GetSWeap*: `<built-in function GetSWeap>`
```
GetSWeap(numWeap,svar) : Obtiene un valor cadena de las municiones
```
- *GetFWeap*: `<built-in function GetFWeap>`
```
GetFWeap(numWeap,svar) : Obtiene un valor numerico de las municiones
```
- *GetNAmmo*: `<built-in function GetNAmmo>`
```
GetNAmmo() : Obtiene el numero de municiones en el juego
```
- *NetExec*: `<built-in function NetExec>`
```
NetExec() : Rutinas de red de los misiles
```
- *SetFWeap*: `<built-in function SetFWeap>`
```
GetFWeap(numWeap,svar,fvalue) : Pone un valor numerico de las municiones
```
- *InitAmmo*: `<built-in function InitAmmo>`
```
InitAmmo(num) : Inicializa las municiones del juego
```
- *SetSAmmo*: `<built-in function SetSAmmo>`
```
SetSAmmo(numammo,svar,svalue) : Pone un valor cadena de las municiones
```


## signal

- *default_int_handler*: `<built-in function default_int_handler>`
```
default_int_handler(...)

The default handler for SIGINT instated by Python.
It raises KeyboardInterrupt.
```
- *SIGABRT*: `22`
- *SIGTERM*: `15`
- *SIGILL*: `4`
- *getsignal*: `<built-in function getsignal>`
```
getsignal(sig) -> action

Return the current action for the given signal.  The return value can be:
SIG_IGN -- if the signal is being ignored
SIG_DFL -- if the default action for the signal is in effect
None -- if an unknown handler is in effect
anything else -- the callable Python object used as a handler

```
- *SIGINT*: `2`
- *signal*: `<built-in function signal>`
```
signal(sig, action) -> action

Set the action for the given signal.  The action can be SIG_DFL,
SIG_IGN, or a callable Python object.  The previous action is
returned.  See getsignal() for possible return values.

*** IMPORTANT NOTICE ***
A signal handler function is called with two arguments:
the first is the signal number, the second is the interrupted stack frame.
```
- *SIGFPE*: `8`
- *SIG_IGN*: `1`
- *NSIG*: `23`
- *SIGSEGV*: `11`
- *SIG_DFL*: `0`


## SFX

- *CharacterConversor*: `<built-in function CharacterConversor>`
```
FXCharacterConversor(CharacterName, ConversorName, phase) : Conversor de Personajes.
```
- *BishopSellLife*: `<built-in function BishopSellLife>`
```
FXBishopSellLife(AttackerName, AttackedName) : Efecto de dar vida (de Attacker [Bishop ó NULL] a Attacked[Usuario]).
```
- *CharacterConversion*: `<built-in function CharacterConversion>`
```
FXCharacterConversion(AttackerName, AttackedName, time) : Conversión de Personajes.
```
- *EmbeddedSet*: `<built-in function EmbeddedSet>`
```
FXEmbeddedSet(EntityName, FXType) : Asigna el controlador de efectos embedidos.
```
- *ShipExplosion*: `<built-in function ShipExplosion>`
```
ShipExplosion(V3D Pos, V3D Vel, float scale, float time, float nflames, bool bcolision) : Explosión de la nave.
```
- *MoneyTransfer*: `<built-in function MoneyTransfer>`
```
FXMoneyTransfer(EntityFrom, EntityTo, Time) : Transferencia de dinero
```


## SVec

- *Mod*: `<built-in function Mod>`
```
res Mod(v1) : Devuelve el modulo de un vector
```
- *Norm*: `<built-in function Norm>`
```
res Norm(v1) : Normaliza un vector
```
- *Prod*: `<built-in function Prod>`
```
res Prod(v1,f) : multiplica un vector por un numero
```
- *ModSqr*: `<built-in function ModSqr>`
```
res ModSqr(v1) : Devuelve el modulo (al cuadrado) de un vector
```
- *DProd*: `<built-in function DProd>`
```
res DProd(v1,v2) : Calcula el producto escalar de dos vectores
```
- *Add*: `<built-in function Add>`
```
res Add(v1,v2) : suma dos vectores 3D
```
- *CProd*: `<built-in function CProd>`
```
vRes CProd(v1,v2) : Calcula el producto vectorial de dos vectores
```
- *NormAng*: `<built-in function NormAng>`
```
rAng NormAng(Ang) : Normaliza un angulo
```
- *Sub*: `<built-in function Sub>`
```
res Sub(v1,v2) : Resta dos vectores 3D
```
- *GetRotAng*: `<built-in function GetRotAng>`
```
AngX,AngY GetRotAng(vec) : Obtiene la rotacion de un vector
```
- *Rotate3D*: `<built-in function Rotate3D>`
```
res Rotate3D(src,rot) : Rota un vector
```
- *GetAngle*: `<built-in function GetAngle>`
```
Ang GetAngle(vec) : Obtiene el ángulo entre dos vectores
```


## SSound

- *StopVoice*: `<built-in function StopVoice>`
```
StopVoice(channel) : stop a voice on the specified channel.
```
- *Play*: `<built-in function Play>`
```
Play('soundname'[,vol,pan]) : ejecuta un sonido con el volumen deseado.
```
- *PlaySound*: `<built-in function PlaySound>`
```
PlaySound((x,y,z),'soundname',vol[,AttenIni,AttenEnd,Doppler]) : ejecuta un sonido en la posicion dada con el volumen deseado.
```
- *SetMusic*: `<built-in function SetMusic>`
```
SetMusic('soundname'[,vol]) : set the file of the background music.
```
- *LoadSound*: `<built-in function LoadSound>`
```
LoadSound(soundfile) : carga un sonido desde un archivo empaquetado.
```
- *OpenVoice*: `<built-in function OpenVoice>`
```
OpenVoice(name,channel) : Preload a voice on a channel.
```
- *StopAllSounds*: `<built-in function StopAllSounds>`
```
SCRAP_StopAllSounds() : para todos los sonidos.
```
- *SetMusicVolume*: `<built-in function SetMusicVolume>`
```
SetMusicVolume(vel) : set the volume of the background music.
```
- *UsePS*: `<built-in function UsePS>`
```
UsePS(Name) : Crea un nuevo sonido posicional
```
- *SetVoiceString*: `<built-in function SetVoiceString>`
```
SetVoiceString(channel,volume) : set string user data of a voice.
```
- *VoiceRemain*: `<built-in function VoiceRemain>`
```
VoiceRemain(channel,time) : return the remaining time of a voice.
```
- *CreatePS*: `<built-in function CreatePS>`
```
CreatePS(Name) : Crea un nuevo sonido posicional
```
- *SetPS*: `<built-in function SetPS>`
```
SetPS(name,varname,value) :  Modifica el valor de una variable de un sonido posicional
```
- *PlayVoice*: `<built-in function PlayVoice>`
```
PlayVoice(channel) : play a voice loaded on the specified channel.
```
- *DeleteAllSounds*: `<built-in function DeleteAllSounds>`
```
SCRAP_DeleteAllSounds() : elimina todos los sonidos.
```
- *GetPS*: `<built-in function GetPS>`
```
GetPS(name,varname) :  Obtiene el valor de una variable de un sonido posicional
```
- *SetVoiceVolume*: `<built-in function SetVoiceVolume>`
```
SetVoiceVolume(channel,volume) : set the volume of a voice.
```


## imp

- *C_BUILTIN*: `6`
- *C_EXTENSION*: `3`
- *init_frozen*: `<built-in function init_frozen>`
- *SEARCH_ERROR*: `0`
- *load_module*: `<built-in function load_module>`
```
load_module(name, file, filename, (suffix, mode, type)) -> module
Load a module, given information returned by find_module().
The module name must include the full package name, if any.
```
- *new_module*: `<built-in function new_module>`
```
new_module(name) -> module
Create a new module.  Do not enter it in sys.modules.
The module name must include the full package name, if any.
```
- *is_frozen*: `<built-in function is_frozen>`
- *find_module*: `<built-in function find_module>`
```
find_module(name, [path]) -> (file, filename, (suffix, mode, type))
Search for a module.  If path is omitted or None, search for a
built-in, frozen or special module and continue search in sys.path.
The module name cannot contain '.'; to search for a submodule of a
package, pass the submodule name and the package's __path__.
```
- *load_compiled*: `<built-in function load_compiled>`
- *PY_FROZEN*: `7`
- *is_builtin*: `<built-in function is_builtin>`
- *get_magic*: `<built-in function get_magic>`
```
get_magic() -> string
Return the magic number for .pyc or .pyo files.
```
- *PKG_DIRECTORY*: `5`
- *load_package*: `<built-in function load_package>`
- *init_builtin*: `<built-in function init_builtin>`
- *PY_CODERESOURCE*: `8`
- *PY_RESOURCE*: `4`
- *load_dynamic*: `<built-in function load_dynamic>`
- *get_suffixes*: `<built-in function get_suffixes>`
```
get_suffixes() -> [(suffix, mode, type), ...]
Return a list of (suffix, mode, type) tuples describing the files
that find_module() looks for.
```
- *load_source*: `<built-in function load_source>`
- *PY_COMPILED*: `2`
- *get_frozen_object*: `<built-in function get_frozen_object>`
- *PY_SOURCE*: `1`


## SInput

- *Rumble*: `<built-in function Rumble>`
```
Rumble(iPlayer,Left,Right,Time) : Inicializa el rumble de un pad.
```
- *GetActionSet*: `<built-in function GetActionSet>`
```
string GetActionSet() :  Obtiene el set de acciones Actual...
```
- *SetInputFunc*: `<built-in function SetInputFunc>`
```
SetInputFunc(iPlayer,modfunc) : agrega la funcion callback de entrada modfunc(iPlayer,string)
```
- *GetCursorChar*: `<built-in function GetCursorChar>`
```
GetCursorChar(iPlayer) : Obtiene el (x,y,caracter) que indican el estado del cursor.
```
- *GetDefinedEntry*: `<built-in function GetDefinedEntry>`
```
value GetDefinedEntry(iPlayer,ActionSet,Action,Device) : obtiene una cadena con la primera definicion del control que encuentre
```
- *AbortListenToDefine*: `<built-in function AbortListenToDefine>`
```
AbortListenToDefine() : Aborta la redefinicion en curso
```
- *ResetToDefault*: `<built-in function ResetToDefault>`
```
ResetToDefault(iPlayer,ActionSet,Action) : Pone todas las entradas de los controles a valores por defecto.
```
- *ResetToSplit*: `<built-in function ResetToSplit>`
```
ResetToSplit() : Resetea el sistema de entrada de datos para iniciar el modo split screen.
```
- *GetDefinedList*: `<built-in function GetDefinedList>`
```
GetDefinedList(iPlayer,ActionSet,Action) : obtiene una cadena con la definicion de controles
```
- *AssingEntry*: `<built-in function AssingEntry>`
```
int AssingEntry(Device,Entry,Player,ActionSet,Action) :  Asigna una entrada... retorna 0 o el Nro de parametro erroneo
```
- *CheckPadButton*: `<built-in function CheckPadButton>`
```
CheckPadButton() : Chequea el estado de un determinado botón del pad.
```
- *ListenToDefine*: `<built-in function ListenToDefine>`
```
ListenToDefine(iPlayer,ActionSet,Action,LaFunction) : Espera a que el usuario mueva un control y lo redefine
```
- *SetString*: `<built-in function SetString>`
```
SetString(iPlayer,String) : Modifica la cadena de entrada de texto.
```
- *Bind*: `<built-in function Bind>`
```
Bind(iPlayer,ActionSet,Action) : obtiene una cadena con la definicion de controles
```
- *GetEntry*: `<built-in function GetEntry>`
```
(Player,Action) GetEntry(Device,Entry,ActionSet) :  Obtiene una entrada, (0,) si vacia
```
- *GetVirtualKeyboard*: `<built-in function GetVirtualKeyboard>`
```
GetVirtualKeyboard() : Obtiene el (W,H,Board) que son datos del keyboard virtual.
```
- *GetString*: `<built-in function GetString>`
```
GetString(iPlayer) : Obtiene la cadena de entrada de texto.
```
- *SetVirtualKeyboard*: `<built-in function SetVirtualKeyboard>`
```
SetVirtualKeyboard(tipo de teclado) : Cambia el teclado virtual
```
- *SetActionSet*: `<built-in function SetActionSet>`
```
SetActionSet(string name) :  Pone el set de acciones requerido...
```
- *ClearDefinedList*: `<built-in function ClearDefinedList>`
```
ClearDefinedList(iPlayer,ActionSet,Action) : Elimina todas las entradas de un control.
```


## SAI

- *GetStateChar*: `<built-in function GetStateChar>`
```
GetStateChar(string nameEntity) : Devuelve el estado de la IA del personaje.

```
- *AddVehicleRace*: `<built-in function AddVehicleRace>`
```
bool AddVehicleRace(cWithLifeEntity *entidad) : Asigna entidad como perteneciente a carrera.
```
- *SetStateVehicle*: `<built-in function SetStateVehicle>`
```
SetStateVehicle(0, string nameAgent) : Estado sin movimiento ni disparo.
 SetStateVehicle(1, float posObjX, float posObjY, float posObjZ, radiusObj, string nameAgent) : Estado alcanzar posición.
 SetStateVehicle(2, string nameObjectiveDin, string nameAgent) : Estado persecución enemigo.
 SetStateVehicle(3, string nameAgent) : Estado en ruta.
 SetStateVehicle(4, string nameAgent) : Estado tráfico.
 SetStateVehicle(5, string nameAgent, float distStop) : Estado huída con parada.
 SetStateVehicle(6, float posObjX, float posObjY, float posObjZ, radiusObj, string nameAgent) : Estado alcanzar meta en carrera.
 SetStateVehicle(7, string nameObjectiveDin, string nameAgent) : Estado persecución.
 SetStateVehicle(8, string nameObjectiveDin, string nameAgent) : Estado persecución enemigo con uso de hook.

```
- *EnableAIChar*: `<built-in function EnableAIChar>`
```
EnableAIChar(string nameEntity, int enable, int stupidPathfinding) : Habilita la IA del personaje indicando características asociadas al movimiento).
```
- *BuildGraph*: `<built-in function BuildGraph>`
```
BuildGraph(int numNodesRadius, float sizeNodeX, float sizeNodeY, float sizeNodeZ) : Crea el Grafo asociado al Pathfinding
```
- *AnalizeMap*: `<built-in function AnalizeMap>`
```
AnalizeMap(float sizeNode) : Analiza características mapa.
```
- *SetStateChar*: `<built-in function SetStateChar>`
```
SetStateChar(0, string nameAgent) : Estado sin movimiento ni disparo.
 SetStateChar(1, string nameAgent, float vel, int withStopTemp) : Estado en ruta.
 SetStateChar(2, string nameAgent, string nameObjective, float vel) : Estado en persecución objetivo con acción.
 SetStateChar(3, string nameAgent, string nameObjective, float vel) : Estado en persecución objetivo sin acción.
 SetStateChar(4, string nameAgent, float posObjX, float posObjY, float posObjZ, float orientX, float orientY, float orientZ, float radiusObj, float velObj) : Estado ir a un punto con orientación final.
 SetStateChar(5, string nameAgent, string nameObjective, float vel) : Estado huída de otro personaje.
 SetStateChar(6, string nameAgent, float centerPatrolZone.x, float centerPatrolZone.y, float centerPatrolZone.z, float radiusPatrolZone, float vel, int withStopTemp) : Estado patrulla de zona.
 SetStateChar(7, string nameAgent, string nameObjective, float vel) : Estado en persecución objetivo con acción.
```
- *AnalizeGraph2D*: `<built-in function AnalizeGraph2D>`
```
AnalizeGraph2D() : Analiza características grafo 2D.
```
- *GetNextRacePoint*: `<built-in function GetNextRacePoint>`
```
(point) GetNextRacePoint(initialPoint, minDist, maxDist) : A partir de un punto inicial 'initialPoint', una distancia mínima 'minDist' y una distancia máxima 'maxDist', devuelve un punto aleatorio a partir del grafo 3D de la IA en el interior actual.
```
- *GetOD*: `<built-in function GetOD>`
- *SetRotStaticObj*: `<built-in function SetRotStaticObj>`
```
bool SetRotStaticObj(float maxVelRot, float limIncVelRot) : Asigna rotaciones para movimiento hacia objetivo estático.
```
- *IniAI*: `<built-in function IniAI>`
```
IniAI(levelPath) : Inicializa AI para un nivel.
```
- *GetStateVehicle*: `<built-in function GetStateVehicle>`
```
GetStateVehicle(string nameEntity) : Devuelve el estado de la IA del vehículo.
 0 : Estado sin movimiento ni disparo.
 1 : Estado alcanzar posición.
 2 : Estado persecución enemigo.
 3 : Estado en ruta.
 4 : Estado tráfico.
 5 : Estado huída con parada.
 6 : Estado alcanzar meta en carrera.
 7 : Estado persecución.
 8 : Estado persecución enemigo con uso de hook.
 9 : Estado sin movimiento ni disparo por estar objetivo en posición inválida.

```
- *BuildGraph2D*: `<built-in function BuildGraph2D>`
```
BuildGraph2D(int numNodesRadius, float sizeNodeX, float sizeNodeY, float sizeNodeZ) : Crea el Grafo asociado al Pathfinding 2D
```
- *AnalizeTraffic*: `<built-in function AnalizeTraffic>`
```
AnalizeTraffic() : Analiza características tráfico.
```
- *SetInertia*: `<built-in function SetInertia>`
```
void SetInertia(bool inertia) : Indica si la nave tiene inercia.
```
- *InitVehicleRace*: `<built-in function InitVehicleRace>`
```
InitVehicleRace() : Inicializa carrera de vehículos.
```
- *GetNearestItemLife*: `<built-in function GetNearestItemLife>`
```
(itemName) GetNearestItemLife(vehicleName)) : Devuelve el item de vida más cercano a una nave dada.
```
- *EnableAIVehicle*: `<built-in function EnableAIVehicle>`
```
EnableAIVehicle(string nameEntity, int enable, int controlStrafe, int controlBrake, int stupidPathfinding) : Habilita la IA del vehículo indicando características asociadas al movimiento).
```
- *AnalizeGraph*: `<built-in function AnalizeGraph>`
```
AnalizeGraph() : Analiza características grafo.
```
- *GetRandomVisibilityPoint*: `<built-in function GetRandomVisibilityPoint>`
```
(point) GetRandomVisibilityPoint() : Devuelve un punto aleatorio del grafo de puntos de visibilidad.
```
- *GetReposCharPos*: `<built-in function GetReposCharPos>`
```
(x,y,z) GetReposCharPos((x,y,z) ,EntityClass,[,EntityName]) : Obtiene un punto de reposicion de personaje (si entidad, se asigna).
 Retorna (None) si falla
```


## regex

- *match*: `<built-in function match>`
- *symcomp*: `<built-in function symcomp>`
- *get_syntax*: `<built-in function get_syntax>`
- *error*: `'regex.error'`
- *set_syntax*: `<built-in function set_syntax>`
- *search*: `<built-in function search>`
- *casefold*: `'\000\001\002\003\004\005\006\007\010\011\012\013\014\015\016\017\020\021\022\023\024\025\026\027\030\031\032\033\034\035\036\037 !"#$%&\'()*+,-./0123456789:;<=>?@abcdefghijklmnopqrstuvwxyz[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\177\200\201\202\203\204\205\206\207\210\211\212\213\214\215\216\217\220\221\222\223\224\225\226\227\230\231\232\233\234\235\236\237\240\241\242\243\244\245\246\247\250\251\252\253\254\255\256\257\260\261\262\263\264\265\266\267\270\271\272\273\274\275\276\277\300\301\302\303\304\305\306\307\310\311\312\313\314\315\316\317\320\321\322\323\324\325\326\327\330\331\332\333\334\335\336\337\340\341\342\343\344\345\346\347\350\351\352\353\354\355\356\357\360\361\362\363\364\365\366\367\370\371\372\373\374\375\376\377'`
- *compile*: `<built-in function compile>`


## __builtin__

- *OverflowError*: `'OverflowError'`
- *AttributeError*: `'AttributeError'`
- *NotImplementedError*: `'NotImplementedError'`
- *range*: `<built-in function range>`
```
range([start,] stop[, step]) -> list of integers

Return a list containing an arithmetic progression of integers.
range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
When step is given, it specifies the increment (or decrement).
For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
These are exactly the valid indices for a list of 4 elements.
```
- *filter*: `<built-in function filter>`
```
filter(function, sequence) -> list

Return a list containing those items of sequence for which function(item)
is true.  If function is None, return a list of items that are true.
```
- *KeyboardInterrupt*: `'KeyboardInterrupt'`
- *TypeError*: `'TypeError'`
- *AssertionError*: `'AssertionError'`
- *apply*: `<built-in function apply>`
```
apply(function, args[, kwargs]) -> value

Call a function with positional arguments taken from the tuple args,
and keyword arguments taken from the optional dictionary kwargs.
```
- *_*: `2`
- *__debug__*: `1`
- *ord*: `<built-in function ord>`
```
ord(c) -> integer

Return the integer ordinal of a one character string.
```
- *eval*: `<built-in function eval>`
```
eval(source[, globals[, locals]]) -> value

Evaluate the source in the context of globals and locals.
The source may be a string representing a Python expression
or a code object as returned by compile().
The globals and locals are dictionaries, defaulting to the current
globals and locals.  If only globals is given, locals defaults to it.
```
- *ZeroDivisionError*: `'ZeroDivisionError'`
- *callable*: `<built-in function callable>`
```
callable(object) -> Boolean

Return whether the object is callable (i.e., some kind of function).
Note that classes are callable, as are instances with a __call__() method.
```
- *len*: `<built-in function len>`
```
len(object) -> integer

Return the number of items of a sequence or mapping.
```
- *max*: `<built-in function max>`
```
max(sequence) -> value
max(a, b, c, ...) -> value

With a single sequence argument, return its largest item.
With two or more arguments, return the largest argument.
```
- *buffer*: `<built-in function buffer>`
```
buffer(object [, offset[, size]) -> object

Creates a new buffer object which references the given object.
The buffer will reference a slice of the target object from the
start of the object (or at the specified offset). The slice will
extend to the end of the target object (or with the specified size).
```
- *hash*: `<built-in function hash>`
```
hash(object) -> integer

Return a hash value for the object.  Two objects with the same value have
the same hash value.  The reverse is not necessarily true, but likely.
```
- *None*: `None`
- *map*: `<built-in function map>`
```
map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence).
```
- *ValueError*: `'ValueError'`
- *slice*: `<built-in function slice>`
```
slice([start,] step[, stop]) -> slice object

Create a slice object.  This is used for slicing by the Numeric extensions.
```
- *abs*: `<built-in function abs>`
```
abs(number) -> number

Return the absolute value of the argument.
```
- *getattr*: `<built-in function getattr>`
```
getattr(object, name[, default]) -> value

Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
When a default argument is given, it is returned when the attribute doesn't
exist; without it, an exception is raised in that case.
```
- *reduce*: `<built-in function reduce>`
```
reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.
```
- *complex*: `<built-in function complex>`
```
complex(real[, imag]) -> complex number

Create a complex number from a real part and an optional imaginary part.
This is equivalent to (real + imag*1j) where imag defaults to 0.
```
- *execfile*: `<built-in function execfile>`
```
execfile(filename[, globals[, locals]])

Read and execute a Python script from a file.
The globals and locals are dictionaries, defaulting to the current
globals and locals.  If only globals is given, locals defaults to it.
```
- *FloatingPointError*: `'FloatingPointError'`
- *min*: `<built-in function min>`
```
min(sequence) -> value
min(a, b, c, ...) -> value

With a single sequence argument, return its smallest item.
With two or more arguments, return the smallest argument.
```
- *OSError*: `'OSError'`
- *RuntimeError*: `'RuntimeError'`
- *locals*: `<built-in function locals>`
```
locals() -> dictionary

Return the dictionary containing the current scope's local variables.
```
- *id*: `<built-in function id>`
```
id(object) -> integer

Return the identity of an object.  This is guaranteed to be unique among
simultaneously existing objects.  (Hint: it's the object's memory address.)
```
- *EnvironmentError*: `('IOError', 'OSError')`
- *issubclass*: `<built-in function issubclass>`
```
issubclass(C, B) -> Boolean

Return whether class C is a subclass (i.e., a derived class) of class B.
```
- *intern*: `<built-in function intern>`
```
intern(string) -> string

``Intern'' the given string.  This enters the string in the (global)
table of interned strings whose purpose is to speed up dictionary lookups.
Return the string itself or the previously interned string object with the
same value.
```
- *coerce*: `<built-in function coerce>`
```
coerce(x, y) -> None or (x1, y1)

When x and y can be coerced to values of the same type, return a tuple
containing the coerced values.  When they can't be coerced, return None.
```
- *KeyError*: `'KeyError'`
- *EOFError*: `'EOFError'`
- *__import__*: `<built-in function __import__>`
```
__import__(name, globals, locals, fromlist) -> module

Import a module.  The globals are only used to determine the context;
they are not modified.  The locals are currently unused.  The fromlist
should be a list of names to emulate ``from name import ...'', or an
empty list to emulate ``import name''.
When importing a module from a package, note that __import__('A.B', ...)
returns package A when fromlist is empty, but its submodule B when
fromlist is not empty.
```
- *ImportError*: `'ImportError'`
- *oct*: `<built-in function oct>`
```
oct(number) -> string

Return the octal representation of an integer or long integer.
```
- *MemoryError*: `'MemoryError'`
- *cmp*: `<built-in function cmp>`
```
cmp(x, y) -> integer

Return negative if x<y, zero if x==y, positive if x>y.
```
- *dir*: `<built-in function dir>`
```
dir([object]) -> list of strings

Return an alphabetized list of names comprising (some of) the attributes
of the given object.  Without an argument, the names in the current scope
are listed.  With an instance argument, only the instance attributes are
returned.  With a class argument, attributes of the base class are not
returned.  For other types or arguments, this may list members or methods.
```
- *round*: `<built-in function round>`
```
round(number[, ndigits]) -> floating point number

Round a number to a given precision in decimal digits (default 0 digits).
This always returns a floating point number.  Precision may be negative.
```
- *str*: `<built-in function str>`
```
str(object) -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.
```
- *reload*: `<built-in function reload>`
```
reload(module) -> module

Reload the module.  The module must have been successfully imported before.
```
- *compile*: `<built-in function compile>`
```
compile(source, filename, mode) -> code object

Compile the source string (a Python module, statement or expression)
into a code object that can be executed by the exec statement or eval().
The filename will be used for run-time error messages.
The mode must be 'exec' to compile a module, 'single' to compile a
single (interactive) statement, or 'eval' to compile an expression.
```
- *list*: `<built-in function list>`
```
list(sequence) -> list

Return a new list whose items are the same as those of the argument sequence.
```
- *raw_input*: `<built-in function raw_input>`
```
raw_input([prompt]) -> string

Read a string from standard input.  The trailing newline is stripped.
If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
On Unix, GNU readline is used if enabled.  The prompt string, if given,
is printed without a trailing newline before reading.
```
- *setattr*: `<built-in function setattr>`
```
setattr(object, name, value)

Set a named attribute on an object; setattr(x, 'y', v) is equivalent to
``x.y = v''.
```
- *IndexError*: `'IndexError'`
- *delattr*: `<built-in function delattr>`
```
delattr(object, name)

Delete a named attribute on an object; delattr(x, 'y') is equivalent to
``del x.y''.
```
- *hasattr*: `<built-in function hasattr>`
```
hasattr(object, name) -> Boolean

Return whether the object has an attribute with the given name.
(This is done by calling getattr(object, name) and catching exceptions.)
```
- *ArithmeticError*: `('OverflowError', 'ZeroDivisionError', 'FloatingPointError')`
- *xrange*: `<built-in function xrange>`
```
xrange([start,] stop[, step]) -> xrange object

Like range(), but instead of returning a list, returns an object that
generates the numbers in the range on demand.  This is slightly slower
than range() but more memory efficient.
```
- *repr*: `<built-in function repr>`
```
repr(object) -> string

Return the canonical string representation of the object.
For most object types, eval(repr(object)) == object.
```
- *tuple*: `<built-in function tuple>`
```
tuple(sequence) -> list

Return a tuple whose items are the same as those of the argument sequence.
If the argument is a tuple, the return value is the same object.
```
- *StandardError*: `(('OverflowError', 'ZeroDivisionError', 'FloatingPointError'), ('IndexError', 'KeyError'), 'AssertionError', 'AttributeError', 'EOFError', 'FloatingPointError', ('IOError', 'OSError'), 'IOError', 'OSError', 'ImportError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'MemoryError', 'NameError', 'OverflowError', 'RuntimeError', 'NotImplementedError', 'SyntaxError', 'SystemError', 'TypeError', 'ValueError', 'ZeroDivisionError')`
- *isinstance*: `<built-in function isinstance>`
```
isinstance(object, class-or-type) -> Boolean

Return whether an object is an instance of a class or of a subclass thereof.
With a type as second argument, return whether that is the object's type.
```
- *Exception*: `('SystemExit', (('OverflowError', 'ZeroDivisionError', 'FloatingPointError'), ('IndexError', 'KeyError'), 'AssertionError', 'AttributeError', 'EOFError', 'FloatingPointError', ('IOError', 'OSError'), 'IOError', 'OSError', 'ImportError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'MemoryError', 'NameError', 'OverflowError', 'RuntimeError', 'NotImplementedError', 'SyntaxError', 'SystemError', 'TypeError', 'ValueError', 'ZeroDivisionError'))`
- *SystemExit*: `'SystemExit'`
- *type*: `<built-in function type>`
```
type(object) -> type object

Return the type of the object.
```
- *input*: `<built-in function input>`
```
input([prompt]) -> value

Equivalent to eval(raw_input(prompt)).
```
- *IOError*: `'IOError'`
- *chr*: `<built-in function chr>`
```
chr(i) -> character

Return a string of one character with ordinal i; 0 <= i < 256.
```
- *NameError*: `'NameError'`
- *long*: `<built-in function long>`
```
long(x) -> long integer

Convert a string or number to a long integer, if possible.
A floating point argument will be truncated towards zero.
```
- *hex*: `<built-in function hex>`
```
hex(number) -> string

Return the hexadecimal representation of an integer or long integer.
```
- *e_write*: `<function e at d71c630>`
- *SystemError*: `'SystemError'`
- *open*: `<built-in function open>`
```
open(filename[, mode[, buffering]]) -> file object

Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
writing or appending.  The file will be created if it doesn't exist
when opened for writing or appending; it will be truncated when
opened for writing.  Add a 'b' to the mode for binary files.
Add a '+' to the mode to allow simultaneous reading and writing.
If the buffering argument is given, 0 means unbuffered, 1 means line
buffered, and larger numbers specify the buffer size.
```
- *LookupError*: `('IndexError', 'KeyError')`
- *Ellipsis*: `Ellipsis`
- *divmod*: `<built-in function divmod>`
```
divmod(x, y) -> (div, mod)

Return the tuple ((x-x%y)/y, x%y).  Invariant: div*y + mod == x.
```
- *globals*: `<built-in function globals>`
```
globals() -> dictionary

Return the dictionary containing the current scope's global variables.
```
- *int*: `<built-in function int>`
```
int(x) -> integer

Convert a string or number to an integer, if possible.
A floating point argument will be truncated towards zero.
```
- *float*: `<built-in function float>`
```
float(x) -> floating point number

Convert a string or number to a floating point number, if possible.
```
- *SyntaxError*: `'SyntaxError'`
- *pow*: `<built-in function pow>`
```
pow(x, y[, z]) -> number

With two arguments, equivalent to x**y.  With three arguments,
equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
```
- *s_write*: `<function p at d700d88>`
- *vars*: `<built-in function vars>`
```
vars([object]) -> dictionary

Without arguments, equivalent to locals().
With an argument, equivalent to object.__dict__.
```


