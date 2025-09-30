import re
from datetime import datetime,timedelta
import locale

#Crear Formulario con Validacion

now = datetime.now()

salida = True

print("Bienvenidos al Formulario")
    
while salida:
        
        #Validacion de Nombre
        name = input("Ingrese su Nombre:")
        
        def validar_nombre (nombre):
            nombre = nombre
    
            new_nombre = re.sub(r"\s","_",nombre)
            
            condicion = r"^[A-Za-z_]+$"
            validacion = re.search(condicion,new_nombre)
                        
            if validacion:
               return validacion.group()
            else:
                while validacion == False:
                    print("¡Error!\nColoque su Nombre Correctamente")
                    nombre = input("Ingrese su Nombre:")
                    new_nombre = re.sub(r"\s","_",nombre)
                    condicion = r"^[A-Za-z_]+$"
                    validacion = re.search(condicion,new_nombre)
            
            return validacion.group()
                    
        
        resultado_nombre = validar_nombre(name)
        print(resultado_nombre)
        
        #Validacion de Apellido
        lastname = input("Ingrese su Apellido:")
        
        def validar_apellido (apellido):
            apellido = apellido
            espacio_condicion = re.sub(r"\s", "_",apellido)
            condicion = r"^[A-Za-z_]+$"
            validacion = re.search(condicion,espacio_condicion)
            
            if validacion:
               return validacion.group()
            else:
               while validacion == False:
                    print("¡Error!\nColoque su Nombre Correctamente")
                    apellido = input("Ingrese su Apellido:")
                    espacio_condicion = re.sub(r"\s", "_",apellido)
                    condicion = r"^[A-Za-z_]+$"
                    validacion = re.search(condicion,espacio_condicion)
                    
                
            return validacion.group()
        
        resultado_apellido = validar_apellido(lastname)
        print(resultado_apellido)
        
        #Validar Numero de Telefono
        
        phone_number = input("Ingrese su Numero de Telefono:")
        
        def validar_numero_de_tel (tel):
            tel = tel
            espacio = re.sub(r"\s","-",tel)
            condicion_mas = r"\+\d{2,3}-\d{10}"
            verificar_mas = re.fullmatch(condicion_mas,espacio)
            
            
            
            if verificar_mas is None:
                while verificar_mas == False:
                    print("Debes ingresar un + y su Numero para Verificar tu Zona de Numero")
                    tel = input("Ingrese su Numero de Telefono:")
                    espacio = re.sub(r"\s","-",tel)
                    condicion_mas = r"\+\d{2,3}-\d{10}"
                    verificar_mas = re.fullmatch(condicion_mas,espacio)
            else:
                return verificar_mas.group()
            
        resultado_tel = validar_numero_de_tel(phone_number)
        print(resultado_tel)
        
        #Validar Email
        
        mail = input("Ingrese su Email:")
        
        def validar_email(email):
            email = email
            espacio = r"\s"
            validar_email = re.findall(espacio,email)
            
            if validar_email:
                while validar_email:
                    print("¡Error!\nEl Email no puede contener Espacios")
                    email = input("Ingrese su Email:")
                    espacio = r"\s"
                    validar_email = re.findall(espacio,email)
        
            condicion = r"[A-Za-z\d]+\@gmail?\.com"
            verificar = re.fullmatch(condicion,email)
            
            if verificar:
                return verificar.group()
            else:
                while verificar == False:
                    print("¡Error!\nDebes Ingresar el Formato correcto del Email")
                    
                    email = input("Ingrese su Email:")
                    condicion = r"[A-Za-z0-9]+\@(gmail|hotmail|outlook)\.com(ar|org)?"
                    verificar = re.fullmatch(condicion,email)
                    
            return verificar.group()
        
        
        resultado_mail = validar_email(mail)
        print(resultado_mail)
        
        #Validar Fecha de Nacimiento
        try:
            day = int(input("Ingrese el Dia de su Nacimiento:"))
            if day < 0 or day > 31:
                while day < 0 or day > 31:
                    print("Ingresa un Dia Valido")
                    day = int(input("Ingrese el Dia de su Nacimiento:"))
                    
            month = int(input("Ingrese el Mes de su Nacimiento:"))
            if month < 0 or month > 12:
                while month < 0 or month > 12:
                    print("Ingresa un Mes Valido")
                    month = int(input("Ingrese el Mes de su Nacimiento:"))
                    
            year = int(input("Ingrese el Año de su Nacimiento:"))
            if year < 0 or year > 2025:
                while year < 0 or year > 2025:
                    print("Ingresa un Año Valido")
                    month = int(input("Ingrese el Año de su Nacimiento:"))
        except TypeError as error:
            print("¡Error!\nDebes Ingresar Numeros")
            print(error)
            
        import locale
        locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")            
        fecha_de_nacimiento = datetime(year,month,day)
        reformatada = fecha_de_nacimiento.strftime("%A - %B - %Y")
        
        print(reformatada)
        
        salida = False
        
print("\n-----------------Datos Personales Completos-----------------")
print(f"-Nombre:{resultado_nombre}\n-Apellido:{resultado_apellido}\n-Fecha de Nacimiento:{reformatada}\n-Correo Electronico:{resultado_mail}\n-N°Telefono:{resultado_tel}\n")

print(now)