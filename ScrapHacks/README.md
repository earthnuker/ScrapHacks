## Usage

`.\Injector.exe dll .\ScrapHack.dll <PATH_TO_SCRAP.exe>`
e.g:
`.\Injector.exe dll .\ScrapHack.dll "D:\Games\Deep Silver\Scrapland\Bin\Scrap.exe"`

or inject into a running instance of the game using your DLL-Injector of choise like so:

`.\Injector.exe dll .\ScrapHack.dll <PID>`


Currently the Injected DLL creates a thread that waits for you to press F12 and then writes something to the ingame console