default preferences.text_cps = 45
$ quick_menu = False
define alex = Character("Alexander")
define chucho = Character("Chucho")
define guac = Character("Guacky")


label splashscreen:
    jump start

label start:

    scene cuarto:
        xysize (1920, 1080)

    "Era una mañana como cualquier otra, el sol brillaba, los pájaros y gallos cantaban. Alexander recién se despertaba."

    show alex normal at center with dissolve:
        zoom 0.75
    pause 1

   
    menu:
        "¿Qué debería hacer Alexander?"
        "Seguir durmiendo":
            alex "Ay... 5 minutos más."
            hide alex with dissolve
            "Alexander se acurruca en su cama y sigue durmiendo."
            "Pero el gallo sigue cantando y no puede dormir más."
        "Levantarse":
            alex "Es hora de levantarse."
    
    hide alex with dissolve
    "El muchacho decide irse a lavar los dientes y luego a buscar algo de comer."

    scene sala with fade:
        xysize (1920, 1080)
    "Al llegar a la sala, se encuentra con su perro, a quien cariñosamente llama Chucho, sentado en el sofá, leyendo el periódico."
    pause 0.35
    show alex normal with dissolve:
        zoom 0.75
        xalign 0.25
        yalign 1.5
    show chucho normal with dissolve:
        zoom 0.55
        xalign 0.75
        yalign 0.75 
    alex "¿Y vos qué haces, Chucho? ¿Por qué estás leyendo el periódico?"
    
    alex "¿Quién lee el periódico en 2026?"
    chucho "Pues yo lo hago."
    "Alex ve a Chucho de forma incrédula."
    pause 0.35
    alex "Que perro tan raro."
    "Alexander decide dejar a Chucho leer su periódico tranquilamente y se dirige al baño para poder cepillar sus dientes."

    scene baño with fade:
        xysize (1920, 1080)
    
    "Al entrar al baño, el muchacho esperó escuchar la bienvenida de su guacamaya. No obstante, fue recibido por silencio y soledad."

    show alex normal with dissolve:
        zoom 0.75
        xalign 0.25
        yalign 1.5
    alex "¿Guacky? ¿Dónde estás?"
    show guacky normal with dissolve:
        zoom 0.55
        xalign 0.75
        yalign 0.75
    pause 0.5
    scene sala with fade:
        xysize (1920, 1080)
    
    show alex normal with dissolve:
        zoom 0.75
        xalign 0.25
        yalign 1.5
    show chucho normal with dissolve:
        zoom 0.55
        xalign 0.75
        yalign 0.75
    alex "Vos Chucho, ¿no has visto a Guacky?"
    chucho "¿La guacamaya? No, no la he visto. ¿Por qué?"
    alex "No estaba en el baño cuando entré. Y no la escuché cantar."
    "Alex vio de un lado a otro. De repente, se dio cuenta que el casco espacial de Guacky no estaba..."
    alex "Chucho... Agarra tu casco. Iremos al espacio."

    scene black with fade 
    
    $ renpy.pause(hard=True)
    return
