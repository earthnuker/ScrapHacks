# SInput

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


