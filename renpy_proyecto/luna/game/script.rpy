default preferences.text_cps = 45
$ quick_menu = False
define alex = Character("Alexander")
define chucho = Character("Chucho")
define guac = Character("Guacky")
define eag = Character("Eagle")

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
    "Alexander y Chucho se dirigieron a la luna en búsqueda de Guacky."

    scene luna with fade:
        xysize (1920, 1080)
    show alex espacio b with dissolve:
        zoom 0.75
        xalign 0.25
        yalign 1.5
    show chucho espacio with dissolve:
        zoom 0.55
        xalign 0.75
        yalign 0.75
    alex "¡Mira Chucho! ¡Qué hermosa es la luna!"
    chucho "Muy bonita."
    "Alexander y Chucho alunizaron y vieron a todo su alrededor, era un paisaje desolado, con rocas, cráteres y polvo por doquier."
    alex "Aquí en la luna no hay nada, solo objetos extraños y rocas."
    chucho "¿Cómo esa chatarra de ahí?"
    show alex espacio b with dissolve:
        zoom 0.75
        linear 0.6 xalign 0.2
    show chucho espacio with dissolve:
        zoom 0.55
        linear 0.8 xalign 0.5
    show eagle at right with dissolve:
        zoom 0.3
        yalign 0
    eag "¿Qué dices, perro? ¿Yo una chatarra? ¡Yo soy Eagle!"
    chucho "Ni idea."
    eag "¿Eagle? ¿El módulo lunar? ¡Yo soy el módulo lunar! ¡El que llevó al hombre a la luna!"
    "Alexander y Chucho se vieron entre sí, confundidos y sorprendidos por la presencia del módulo lunar."
    "Eagle hizo un sonido de frustración."
    eag "Yo fui el módulo del Apollo 11. Yo traje a los primeros humanos a la luna."
    eag "Hace muuchos años, en 1969. Pero lo recuerdo como si fuese ayer..."

$ boton_nasa(True)

eag "Mi gran misión fue lograr que los primeros seres humanos pisaran otro mundo por primera vez y mantenerlos a salvo."
eag "Mi cabina regresó con los astronautas a la Tierra, pero mi base dorada aquí quedó para siempre en el Mar de la Tranquilidad."
eag "No tengo ruedas para pasear, pero sigo vigilando este lugar silencioso..."
alex "¡Que conmovedor!"
chucho "Si... pero, ¿de casualidad has visto a una guacamaya por aquí?"
eag "¿Qué? ¿Una guacamaya? Que raro... Me parece que no."
"Alexander y Chucho se miraron con una cara triste. No sabían que hacer. Es así, como Eagle suspiró."
eag "Ahora que lo recuerdo... Me parece que vi a una guacamaya por aquí hace un tiempo. Pero creo que se dirigía a Marte."
alex "¿A Marte? ¿Por qué se iría a Marte?"
alex "¡Pero ya escuchaste, Chucho!"
alex "¡Debemos ir a Marte!"
scene black with fade
$ boton_nasa(False)
pause 1

menu:
        "Regresar":
            python:
                if renpy.emscripten:
                    import emscripten
                    emscripten.run_script("window.top.location.href = '/Contenido-Español/Planetas/planetas.html';")    

$ renpy.pause(hard=True)    
