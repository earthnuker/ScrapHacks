# SScorer

- *SetCursor*: `<built-in function SetCursor>`
```
SetCursor(playernumber,CursorName) : pone un item del scorer como cursor
```
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


