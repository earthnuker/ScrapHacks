# Netplay

Game Info Packet

```
Server 'B':FZ (0/10) Ver 1.0 at 192.168.99.1:28086
[0-3] header/ID?
[4-5] port (16-bit)
[6-7] max_players (16-bit)
[8-9] curr_player (16-bit)
[10-x] server name (char*)

           0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
0019fdc0  ba ce 00 01 b6 6d 0a 00 00 00 42 00 30 fe 19 00  .....m....B.0...
0019fdd0  ff ff ff ff 27 2b b3 9b c7 3e bb 00 9c af 29 00  ....'+...>....).
0019fde0  db 69 00 00 00 00 00 00 00 00 44 65 61 74 68 4d  .i........DeathM
0019fdf0  61 74 63 68 00 00 00 00 ff ff 46 5a 00 4a 91 f0  atch......FZ.J..
0019fe00  92 8b 57 4e 7f 00 00 00 10 21 fe 38 0d ae 00 00  ..WN.....!.8....
0019fe10  f0 ce f3 36 a0 e8 0b 77 a0 e8                    ...6...w..
```


Player Join Packet

```
[0-3] header/ID?
[6-x] Player name

           0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F  0123456789ABCDEF
09c9dfe8  7f 47 00 00 00 0e 55 6e 6e 61 6d 65 64 20 50 6c  .G....Unnamed Pl
09c9dff8  61 79 65 72 06 53 42 6f 73 73 31 b9 00 07 50 5f  ayer.SBoss1...P_
09c9e008  42 65 74 74 79 06 4d 42 4f 53 53 31 06 4d 42 4f  Betty.MBOSS1.MBO
09c9e018  53 53 31 00 00 10 30 2c 31 35 2c 30 2c 30 2c 31  SS1...0,15,0,0,1
09c9e028  35 2c 31 35 2c 31 02 00 00 00                    5,15,1....
```

 Message                                  | Description                                                       
 ---------------------------------------- | ----------------------------------------------------------------- 
 `5c68625c32383230395c73637261706c616e64` | "Scrapland Server" announcement broadcast (`\hb\28209\scrapland`) 
 `7f01000007`                             | Retrieve Game info                                                
 `48423d35323932322c3235363a323830383600` | Connection Information (`HB=52922,256:28086`)                     
