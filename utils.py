def print_welcome():
    print("""
                     __    _                                   
                _wr""        "-q__                             
             _dP                 9m_     
           _#P                     9#_                         
          d#@                       9#m                        
         d##                         ###                       
        J###                         ###L                      
        {###K                       J###K                      
        ]####K      ___aaa___      J####F                      
    __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
 _g##############mZ_         __g##############m_               
_d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
a###""        ,Z"#####@" '######"\g          ""M##m            
J#@"          0L  "*##     ##@"  J#              *#K           
#"            `#    "_gmwgm_~    dF               `#_          
7F             "#_   ]#####F   _dK                 JE          
]                *m__ ##### __g@"                   F          
                   "PJ#####LP"                                 
`                    0######_                      '           
                   _0########_                                   
.               _d#####^#####m__              ,              
  "*w_________am#####P"   ~9#####mw_________w*"                  
      ""9@#####@M""           ""P@#####@M""                    
""")
    print("Welcome to my list of the most common SQLInjection. Enter -h for help.")

def print_help():
    print("""
    -h type             --> different types
    view union          --> outlines union injection options
    view in-band        --> outlines in-band injection options
    view error-based    --> outlines error-based injection options
    view boolean-based  --> outlines boolean based injection options
    view all            --> shows all the injections in a listed format
    exit                --> exits...obviously...      
    """)

def display_payloads(payloads):
    for i, (payload, description) in enumerate(payloads, 1):
        print(f"{i}. {payload}")
        print(f"   Description: {description}\n")
