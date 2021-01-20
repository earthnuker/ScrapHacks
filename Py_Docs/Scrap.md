# Scrap

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


