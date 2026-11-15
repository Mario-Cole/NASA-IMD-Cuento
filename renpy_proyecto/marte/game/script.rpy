default preferences.text_cps = 45
$ quick_menu = False
define alex = Character("Alexander")
define chucho = Character("Chucho")
define guac = Character("Guacky")
define spir = Character("Spirit")
define opp = Character("Opportunity")

init python:
    def boton_nasa(visible):
        if renpy.emscripten:
            import emscripten
            estado = "block" if visible else "none"
            emscripten.run_script(f"var b = document.getElementById('btn-nasa'); if(b) b.style.display = '{estado}';")

label splashscreen:
    jump start

label start:
    scene black
    "Alexander y Chucho llegaron a marte en busca de su querido Guacky."

    scene marte with fade:
        xysize (1920, 1080)
    show alex espacio b with dissolve:
        zoom 0.75
        xalign 0.25
        yalign 1.5
    show chucho espacio with dissolve:
        zoom 0.55
        xalign 0.75
        yalign 0.75
    alex "¡Marte! Nunca había venido aquí."
    alex "Los colores son increíbles, y el paisaje es muy único."
    chucho "Sí, es muy bonito."
    "Alexander y Chucho comenzaron a explorar el planeta. Era seco, rocoso y polvoriento. Hasta que vieron a lo lejos lo que parecían dos objetos."
    alex "¿Qué es eso que se ve allá a lo lejos?"
    chucho "¿El qué?"
    alex "Esos dos objetos. ¿Estará Guacky por ahí?"
    "Ambos se fueron acercando poco a poco. Al llegar, se dieron cuenta que no era Guacky, sino dos robots idénticos."
    show alex espacio b with dissolve:
        zoom 0.75
        linear 0.6 xalign 0.2
    show chucho espacio with dissolve:
        zoom 0.55
        linear 0.8 xalign 0.5
    show spirit opportunity at right with dissolve:
        zoom 0.5
        yalign 0
    spir "Opportunity, ¡mira!"
    opp "¿El qué, Spirit?"
    spir "¡Mira! ¡Un perro y un humano!"
    "Alexander y Chucho se miraron entre sí, confundidos y sorprendidos por la presencia de los robots."
    opp "¿Qué hacen un humano y un perro aquí?"
    spir "No sé, ¡pero tenemos visitas!"
    spir "¡Hola! Soy Spirit, y este es mi compañero Opportunity. Somos robots exploradores de Marte."
    alex "¡Hola!"
    $ boton_nasa(True)
    spir "Somos parte de la misión Mars Exploration Rover de la NASA. Llegamos a Marte en 2004 para explorar su superficie y buscar signos de agua."
    spir "Pero yo llegué primero... y Opportunity llegó después, jeje."
    opp "Eso no cambia nada."
    spir "De todas formas... Ninguno sigue funcionando."
    opp "Sí. Spirit terminó su misión en 2010, y yo terminé la mía en 2018."
    spir "¡Pero nos alegra ver que tenemos visitantes!"
    spir "¿Qué los trae por aquí?"
    alex "Estamos buscando a nuestra amiga Guacky. Es una guacamaya que se perdió en el espacio."
    opp "¿Una guacamaya?"
    chucho "Sí, ¿la han visto?"
    spir "Hmm... No estoy seguro..."
    opp "Guacamaya... Creo que sí vi una. Se fue en dirección al monte Olimpo, allá."
    "Opportunity extendió un poco su brazo robótico en dirección al monte Olimpo."
    "Alexander y Chucho se vieron entre sí, sonriendo."
    alex "¡Perfecto! Hemos estado buscandola por todos lados. Los dejamos, ¡muchas gracias!"
    spir "¡Adiós!"
    scene black with fade
    hide alex
    hide chucho
    hide spirit opportunity
    $ boton_nasa(False)

    scene olimpo with fade:
        xysize (1920, 1080)
    show alex espacio b with dissolve:
        zoom 0.75
        xalign 0.25
        yalign 1.5
    show chucho espacio with dissolve:
        zoom 0.55
        xalign 0.75
        yalign 0.75
    alex "¡Chucho! ¡Mira! Creo que allá está Guacky."
    show alex espacio b with dissolve:
        zoom 0.75
        linear 0.6 xalign 0.2
    show chucho espacio with dissolve:
        zoom 0.55
        linear 0.8 xalign 0.5
    show guacky espacio with dissolve:
        zoom 0.5
        xalign 0.95
        yalign 0.4
    chucho "¡Guacky!"
    guac "¡Chicos, hola! ¿Qué hacen aquí?"
    alex "Te estábamos buscando. ¿Por qué estas aquí?"
    guac "Quería ver el monte Olimpo."
    guac "Es muy hermoso, ¿no creen?"
    alex "Sí... Muy hermoso."
    "Los tres quedaron viendo el monte Olimpo por unos segundos, felices de reencontrarse."
    scene black with fade
    hide alex
    hide guacky
    hide chucho
    "Se abrazaron, y juntos partieron."
pause 1

menu:
        "Regresar":
            python:
                if renpy.emscripten:
                    import emscripten
                    emscripten.run_script("window.top.location.href = '/Contenido-Español/Planetas/planetas.html';")    

$ renpy.pause(hard=True)    
