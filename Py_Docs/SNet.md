# SNet

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


