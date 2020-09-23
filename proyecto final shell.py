#PROYECTO VERSION FINAL SHELL
import time
import random


palabras= ["hermoso",                                 "lleno",                                                      "moderno",                                               "amanecer",                                   "enorme",                                                        "frio",                                                               "limpio",                                 "facil",                                                                  "veloz",                                                                "inteligente",                             "urbano"]
sin=[["bello","precioso","bonito","guapo","apolineo"],["repleto","pleno","repleto","colmado","atestado","completo"], ["reciente","actual","reciente","nuevo", "vanguardista"],["alba", "esclarecer","alborear"],            ["grande","gigantesco","desmesurado","colosal","amplio","alto"], ["gelido","helado","congelado","fresco","glacial"],                  ["aseado","pulcro"],                      ["sencillo","simple","hacedero","factible"],                             ["rapido","kuchau","rapido","pronto","presuroso","acelerado","apresurado"], ["astuto","brillante","listo"],           ["metropolitano","ciudad","metropoli"]]
ant=[["feo","horrendo","horripilante","antiestetico"],["vacio", "desocupado","deshabitado","desierto","hueco"],      ["anticuado","viejo","antiguo","obsoleto","arcaico"    ],["anochecer","atardecer","oscurecer","ocaso"],["pequeño","chico","reducido","diminuto","minusculo","bajo"],    ["caliente","caluroso","calido","ardiente","candenete","fogoso"],    ["sucio","cochino","marrano","impulcro"], ["dificil","complicado","arduo","trabajoso","intrincado","embrollado"],  ["lento","lento","tardo","tardio","pausado"],                              ["tonto","torpe","mentecato","simple"],   ["rural","rustico","agrario"]]
#Estas son las opciones dadas, la idea es meterlas en una caja cuando haga el programa grafico
sinbox=["bello","precioso","bonito","guapo","apolineo","repleto","pleno","repleto","colmado","atestado","completo","reciente","actual","reciente","nuevo","vanguardista","alba","esclarecer","alborear","grande","gigantesco","desmesurado","colosal","amplio","alto","gelido","helado","congelado","fresco","glacial","aseado","pulcro","sencillo","simple","hacedero","factible","veloz","kuchau","rapido","pronto","presuroso","acelerado","apresurado","astuto","brillante","listo","metropolitano","ciudad","metropoli"]
antbox=["feo","horrendo","horripilante","antiestetico","vacio","desocupado","deshabitado","desierto","hueco","anticuado","viejo","antiguo","obsoleto","arcaico","anochecer","atardecer","oscurecer","ocaso","pequeño","chico","reducido","diminuto","minusculo","bajo","caliente","caluroso","calido","ardiente","candenete","fogoso","sucio","cochino","marrano","impulcro","dificil","complicado","arduo","trabajoso","intrincado","embrollado","lento","lento","tardo","tardio","pausado","tonto","torpe","mentecato","simple","rural","rustico","agrario"]
antbox.reverse()

def instr ():
    print("Se te mostrara una palabra al azar")
    time.sleep(3)
    print("Cuando se te indique, ingresa un sinonimo de la palabra que te mostraron")
    time.sleep(3)
    print("Luego se te pedira que ingreses un antonimo de la misma palabra ")
    time.sleep(3)
    print("Si es correcta, recibiras cinco puntos y  se te dará una palabra nueva")
    time.sleep(3)
    print("Por cada incorrecta con cinco puntos menos")
    time.sleep(3)
    print("Si tu puntaje es mayor a 85, recibiras una sorpresa")
    
def scoreboard():
    print("El puntaje actual es: " +str (score))
    #este si es funcion por que lo uso seguido
        
def remplazo (x):
    x=x.lower()
    x=x.replace("á","a")
    x=x.replace("é","e")
    x=x.replace("í","i")
    x=x.replace("ó","o")
    x=x.replace("ú","u")
    return(x)

def shrek():
    if score>=85:
        print("""
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
""")
def madeBy():
    print("""
  __  __           _        _              _                  _____  __              
 |  \/  |         | |      | |            | |                |  __ \/_/              
 | \  / | __ _  __| | ___  | |__  _   _   | |     ___  ___   | |__) |__ _ __ ___ ____
 | |\/| |/ _` |/ _` |/ _ \ | '_ \| | | |  | |    / _ \/ _ \  |  ___/ _ \ '__/ _ \_  /
 | |  | | (_| | (_| |  __/ | |_) | |_| |  | |___|  __/ (_) | | |  |  __/ | |  __// / 
 |_|  |_|\__,_|\__,_|\___| |_.__/ \__, |  |______\___|\___/  |_|   \___|_|  \___/___|
                                   __/ |                                            
                                  |___/                                            
                                

""")
    time.sleep(2)
    print("""
            _____           _   _ _         _          _______                    _   __        _                   
          |_   _|         | | (_) |       | |        |__   __|                  | | /_/       (_)                  
            | |  _ __  ___| |_ _| |_ _   _| |_ ___      | | ___  ___ _ __   ___ | | ___   __ _ _  ___ ___          
            | | | '_ \/ __| __| | __| | | | __/ _ \     | |/ _ \/ __| '_ \ / _ \| |/ _ \ / _` | |/ __/ _ \         
           _| |_| | | \__ \ |_| | |_| |_| | || (_) |    | |  __/ (__| | | | (_) | | (_) | (_| | | (_| (_) |        
          |_____|_| |_|___/\__|_|\__|\__,_|\__\___/     |_|\___|\___|_| |_|\___/|_|\___/ \__, |_|\___\___/         
                          \ \   / /     | |                | |           | (_)            __/ |                    
                           \ \_/ /    __| | ___    ___  ___| |_ _   _  __| |_  ___  ___  |___/                     
                            \   /    / _` |/ _ \  / _ \/ __| __| | | |/ _` | |/ _ \/ __|                           
                             | |    | (_| |  __/ |  __/\__ \ |_| |_| | (_| | | (_) \__ \                           
                             |_|     \__,_|\___|  \___||___/\__|\__,_|\__,_|_|\___/|___/                           
   _____                       _                           _        __  __             _                           
  / ____|                     (_)                         | |      |  \/  |           | |                          
 | (___  _   _ _ __   ___ _ __ _  ___  _ __ ___  ___    __| | ___  | \  / | ___  _ __ | |_ ___ _ __ _ __ ___ _   _ 
  \___ \| | | | '_ \ / _ \ '__| |/ _ \| '__/ _ \/ __|  / _` |/ _ \ | |\/| |/ _ \| '_ \| __/ _ \ '__| '__/ _ \ | | |
  ____) | |_| | |_) |  __/ |  | | (_) | | |  __/\__ \ | (_| |  __/ | |  | | (_) | | | | ||  __/ |  | | |  __/ |_| |
 |_____/ \__,_| .__/ \___|_|  |_|\___/|_|  \___||___/  \__,_|\___| |_|  |_|\___/|_| |_|\__\___|_|  |_|  \___|\__, |
              | |                                                                                             __/ |
              |_|                                                                                            |___/            
""")
    time.sleep(3)
    print("""
              
                          `.-::/+oooo+/::-.                           
                    `-/oyddmmmmmmmdodmmmmmmddso:.`                    
                 .+ydmmmmmmmmmmmmmo .ymmmmmmymmmmds/.                 
              .ohmmmmmmmmmmmmmmmmy.  .dmmmmy`:dmmmmmmy+.              
           `/ymmmmmmmmmmmmmmmmmms`   .dmmmy`  ommmmmmmmdy:            
          +hmmmmmmmmmmmmmmmmmms-    `smmd+`   ommmmmmmmmmmh/          
        :hmmmmmmmmmmmmmmmmmms-     :hmds`    :dmdmmmmmmmmmmmh:        
      .smmmmmmmmmmmmmmmmmds.     :ymdo.    `+mms.ymmmmmmmmmmmmo`      
     -hmmmmmmmmmmmmmmmmds.    `:ymd+`    `+dmh/  ommmmmdsmmmmmmy-     
    :mmmmmmmmmmmmmmmmds.     :hmd+`    `+hmdo`   smmmmh. hmmmmmmd-    
   :dmmmmmmmmmmmmmmmo.     :hmd+`    `+dmdo.    /dmmd/`  ymmmmmmmd-   
  .dmmmmmmmmmmmmmd+`     +hmd+`    `+dmm+`    `smmd+`   .dmmmmmmmmh`  
  ymmmmmmmmmmmmdo`    `/hmh/`    `+dmd+`    `odmh+`    -hmmmmmmmmmms  
 :dmmmmmmmmmmmy`    `/dmh:`    `+dmh+`    .odmh/`    `+mmmmmmmmmmmmd- 
 ommmmmmmmmmd+`   `/dmh:`    `odmh/`    .odmd/`    `+dmdhmmmmmmmmmmmo 
.hmmmmmmmmmmo    -hmd/`    .odmh/`    .odmh/`    `odmdo`+mmmmmmmmmmms`
-dmmmmmmmmmm.   /dmh.    .odmh/`    .odmh:`    .odmdo`  ommmmmmmmmmmh.
-dmmmmmmmmmd.  -dmh.   `ommh/`    .sdmh/     .smmd/`   .hmmmmmmmmmmmd-
-dmmmmmmmmmm:  smd/   :dmd+`    -ymmh:     .ommh/`    -dmmmmmmmmmmmmy.
`ymmmmmmmmmmd- ymd-  /dmd.    .smmh:     -smmy:`    .sdmmmmmmmmmmmmms`
 ommmmmmmmmmmd/+mm+ :mmh-   `/dmd+`    -ymmy:     -sdmmmmmmmmmmmmmmm+ 
 .dmmmmmmmmmmmmhmmd/hmm/   `smmd:    .sdmm+`    -smmmmmmmmmmmmmmmmmd` 
  +mmmmmmmmmmmmmmmmmmmd`  `smmm+    :dmmd/    -ymmmmmmmmmmmmmmmmmmm/  
  `ymmmmmmmmmmmmmmmmmmd`  +mmmd:   ommmmo   `smmmmmmmmmmmmmmmmmmmms`  
   .ymmmmmmmmmmmmmmmmmm/ `ymmmm+  :mmmmm-  :dmmmmmmmmmmmmmmmmmmmmy`   
    `hmmmmmmmmmmmmmmmmmh:`ymmmmm/`ymmmmm/ /mmmmmmmmmmmmmmmmmmmmmy`    
     `ommmmmmmmmmmmmmmmmmshmmmmmdsdmmmmmd+dmmmmmmmmmmmmmmmmmmmdo`     
       /dmmmmmmmdhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdmmmmmmmh:       
        `ommmmmmh:                                  /hmmmmmm+`        
          `odmmmmmh+`                            .+hmmmmmdo`          
            `+ymmmmmmho:.                   `.:ohmmmmmmy/`            
               -+hmmmmmmmdhso+:        :+oshdmmmmmmdy+.               
                  ./shdmmmmmmmy       `ymmmmmmmdho:.                  
                      `-/oshdds       `yddyso:-`
""")

madeBy()
time.sleep(2.5)
nombre=input("Ingresa tu nombre: ")
nombre=nombre.lower()#pasa todo el nombre a minusculas
nombre=nombre.capitalize()#hace mayuscula la primera letra
time.sleep(1)
print("Hola " +str(nombre) +", bienvenido al juego. Pon atención a las intrucciones siguientes: ")
time.sleep(3)
instr()
print("¿estas listo?")
time.sleep(4)
print("")
print("Algunas opciones de sinonimos y antonimos podrian ser :")
time.sleep(2)
for randoooom in range (0,random.randint(5,20)):
    randsin=random.randint(0, len(sinbox)-1)
    randant=random.randint(0,len(antbox)-1)
    sb=sinbox[randsin]
    ab=antbox[randant]
    print(" ", sb," ", ab," ", end=(""))

    sinbox.remove(sb)
    antbox.remove(ab)
time.sleep(3)  
score=0
while len(palabras)>0: #esto es para que dure mientras haya palabras
    index=random.randint(0,len(palabras)-1)
    p=palabras[index]
    s=sin[index]
    a=ant[index]
    print('\n la palabra es: "' +str(p)+'"')
    rs=input("Ingresa el sinonimo: ")
    time.sleep(1)
    ra=input("Ingresa el antonimo: ")
    rs=remplazo(rs)
    ra=remplazo(ra)
    
    for n in range (index,index+1):
        
        if rs in (sin[n]):
            print("El sinonimo es correcto")
            score=score+5
            time.sleep(1)
        else:
            print("El sinonimo es incorrecto")
            score=score-5
            time.sleep(1)
    for n in range (index, index+1):
        if ra in (ant[n]):
            print("El antonimo es correcto")
            score=score+5
            time.sleep(1)
        else:
            print("El antonimo es incorrecto")
            score=score-5
            time.sleep(1)
    time.sleep(1)
    scoreboard()
    
    palabras.remove(p)
    sin.remove(s)
    ant.remove(a)
    
print("Tu puntaje fué: " + str(score) )
if score>=95:
    print("Tu puntaje fue muy bueno, felicitaciones")
    shrek()
    









"""
 I would love to change the world, but they won't give me the source code

                                     .:/osydmNNMMMMMMMMNNmdyso/:.                                    
                              `:+ydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+:`                              
                          `/sdNMMMMMMMmdyso//:--------::/osydmMMMMMMMNds/.                          
                       -odNMMMMMmhs/-``                      ``-/shNMMMMMNdo-                       
                    -omNMMMMmy+.`                                  `.+ymMMMMNmo-                    
                 `/dNMMMMdo+ymdd:  :/.///-.:++o/.                      `-odMMMMNd/`                 
               .omMMMMMNho+oyNNMNyss::dMs`NMNNmMNmy                       `.odMMMMmo.               
             .oNMMMMMMMhsdNNdyyNMhsymNMMNhh/..:hMMMy.                        `:yMMMMNo.             
           `+mMMMMMMMMMmhdMMMMMMMMMNho:yh+-:-oyhms:-                         -/yMMMMMMm+`           
          :dMMMMMMMMMMMmdmMMMMMMMd/.   ``oNNNm.-+.                     `.`  -mMMMMMmNMMMd:          
        `oNMMMMMMMMMMMMMMMMMMMMMMd:-.  `.yMMMMmNM+                   `.hN+   .yhdMd::NMMMNo`        
       .hMMMMMMMMMMMMMMMMMMm+mMMMMMNm`/dmMMMMMMMMNh`                .dmyyNo.-ossyNhyyNMMMMMh.       
      -mMMMMMMMMMMMMMMMMMMMNdNMNNMMMMhNMMMMmohmdhms`                ./--ydmyNMMMMMMMMMMMMMMMm-      
     :NMMMNMMMMMMMMMMMMMMMMMMMy/+ydMNMMMMMdo+.:`ohh/                    -mNMMMMMMNNMMMMMMMMMMN:     
    :NMMMMMMMMMMMMMMMMMMMMMMMM+sMsydhMMNd/-+.o/`  .`                `:+++dMMmNddMo-+dMMMMMNMMMN:    
   -NMMMMMMMMMMMMMMMMMMMMMMMMMdMmsmmdd+.                            sMMMMMNo..``/yhs.mMNsMhdMMMN-   
  `dMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMN+`                              /mNNNm/..... +hd :h+ ymmNMMMm`  
  sMMMN/mNMMMMMMMMMMMMMMMMMMMMMMMNm/                                -ohhhhmmNNMM. `   ``  --:NMMMs  
 -MMMM/ `oMhNMMMMMMMMMMMMMMMMMMNs-                                 /MMMMMMMMMMMMhyo/-ohdy:```oMMMM- 
 yMMMd   +MoyMMMMMMMMNh+/////dM/                                 `-hMMMMMMMMMMMMMMMMMNMMMMNmmNMMMMy 
.MMMM:   .dMsyMMMMMMh`       -+:                               .+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.
+MMMm     `sh.+MMMMm`    ``                                   :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo
hMMMy         /MMMMN.``/hN-                                   `oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh
NMMM+          :ydNMmNMMMmo/                                  `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN
MMMM:              ` :shmMMM.    `:.`                         .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMM:                    +mM/.` /mMMMh::oy:                    +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMM:                     `+osyNMMMMMMMMMMMo`                   `sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
NMMM+                          NMMMMMMMMMMMMMMMo                  -ssoooo- `+sydMMMMMMMMMMMMMMMMMMMN
hMMMy                       `+dMMMMMMMMMMMMMMMMM`                              sMMMMMMMMMMMMMMMMMMMh
oMMMm                       :MMMMMMMMMMMMMMMMMMMmy+////-                       yMMMMMMMMMMMMMMMMMMM+
.MMMM:                      oMMMMMMMMMMMMMMMMMMMMMMMMMMN+-`                    `hMMMMMMMMMMMMMMMMMM.
 hMMMd                      .hMMMMMMMMMMMMMMMMMMMMMMMMMMMN.                     `yMMMMMMMMMMMMMMMMy 
 -MMMM/                      `/NMMMMMMMMMMMMMMMMMMMMMMMMd:                       `mMMMMMMMMMMMMMMM- 
  sMMMN.                       .NMMMMMMMMMMMMMMMMMMMMMMN`                        sMMMMMMMMMMMMMMMo  
  `dMMMh`                       .-odMMMMMMMMMMMMMMMMMMMd                        .MMMMMMMMMMMMMMMd`  
   -NMMMy                          `hMMMMMMMMMMMMMMMMMMs                         /NMMMMMMMMMMMMN-   
    :NMMMs`                         yMMMMMMMMMMMMMNyhh+`                          dMMMMMMMMMMMN:    
     :NMMMh`                        yMMMMMMMMMMMMM+                               sMMMMMMMMMMN:     
      -mMMMd-                       yMMMMMMMMMMMMMy                               `+MMMMMMMMm-      
       .dMMMN+`                     -NMMMMMMMMMMMh-                                 MMMMMMMh.       
        `sNMMMd-                    .MMMMMMMMMMN+`                                  sMMMMNo`        
          :dMMMNy.                  `hMMMMMMMNd:                                  -yNMMMd:          
           `+mMMMNs-                 `NMMMmo:.                                  -yNMMMm+`           
             .oNMMMNy:`               NMMMN/                                 `:yNMMMNo.             
               .omMMMMdo.`            yMMMNy:                             `.odMMMMmo.               
                 `/dNMMMMdo-`          oNMMM-                          `-odMMMMNh/`                 
                    -omNMMMMmy/.`       -yNMd+                     `.+ymMMMMNdo-                    
                       -odNMMMMMmhs/-``   .---               ``-/shmMMMMMNdo-                       
                          ./sdMMMMMMMMmdyso//:--------://osydmMMMMMMMNds:`                          
                              `:+ydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdy+:`                              
                                    .:/osydmNNMMMMMMMMNNddyso/-.                                    
"""