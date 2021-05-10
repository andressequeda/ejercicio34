usuario  =  input ( "Ingrese su usuario:" )
contrasena  =  input ( "Ingrese su contraseña:" )
usuario_predefinido  =  "admin"
contrasena_predefinida  =  "admin"
si  usuario  ==  usuario_predefinido  y  contrasena  ==  contrasena_predefinida :
    print ( "Inicio de sesión completado" )
otra cosa :
    print ( "Inicio de sesión fallido (usuario o contraseña incorrecta)." )