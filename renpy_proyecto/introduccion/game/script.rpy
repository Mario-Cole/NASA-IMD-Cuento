define alex = Character("Alexander")
define perro = Character("Chucho")
define guac = Character("Guacky")

label splashscreen:
    jump start

label start:

    scene cuarto:
        xysize (1920, 1080)

    "Era una mañana como cualquier otra, el sol brillaba, los pájaros y gallos cantaban. Alexander recién se despertaba."

    show alex espacio at left with fade:
        zoom 0.45

    menu:
        "¿Qué debería hacer Alexander?"
        "Seguir durmiendo":
            jump dormir
        "Levantarse":
            jump levantarse

label dormir:
    alex "Ay... 5 minutos más."
        
    return
