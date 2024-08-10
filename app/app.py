#Jose Carlos Moreir Paz
#201701015
import querys
import db
#./VuelosDataSet.csv
datasets=""
def extraer_info():
    global datasets
    try:
        ruta= input("Ingrese la ruta del archivo:\n>>>")
        archivo = open(ruta, mode='r', encoding='utf-8', errors='replace')
        datasets=archivo.read().splitlines()
        #for i in datasets[1:]:
            #fila=i.split(",")
           
    except Exception as e:
         print(f"Descripción del error: {e}")

while True:
    print("SS2 PRACTICA 1")
    print("1. Borrar Modelo")
    print("2. Crear Modelo")
    print("3. Extraer informacion")
    print("4. Cargar informacion")
    print("5. Realizar Consultas")
    print("6. Salir")

    c = int(input(">>> "))

    if c == 6:
        break
    elif c ==1:
        try:
            db.query(querys.getDrops())
            print("modelo eliminado")
        except:
            print("error al borrar el modelo")

    elif c ==2:
        try:
            db.query(querys.getTablas())
            print("modelo creado")
        except:
            print("error al crear el modelo")
    elif c ==3:
        extraer_info()
    print("--------------------------------")


