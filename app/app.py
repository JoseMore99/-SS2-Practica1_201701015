#Jose Carlos Moreir Paz
#201701015
import querys
import db
#./VuelosDataSet.csv
#./Vuelo.csv
datasets=""
def extraer_info():
    global datasets
    try:
        ruta= input("Ingrese la ruta del archivo:\n>>>")
        archivo = open(ruta, mode='r', encoding='utf-8', errors='replace')
        datasets=archivo.read().splitlines()
    except Exception as e:
         print(f"Descripción del error: {e}")

def cargar_info():
    global datasets
    for i in datasets[1:]:
       # try:
            try:
                fecha= None
                fila=i.split(",")      
                insert=f"""IF NOT EXISTS ( SELECT 1 FROM DimPiloto WHERE PilotName='{fila[13].replace("'","")}')
                    BEGIN
                        INSERT INTO DimPiloto (PilotName) VALUES ('{fila[13].replace("'","")}');
                    END"""
                db.query(insert)
            except:
                continue
            try:
                if "-"in fila[11]:
                    fecha = fila[11].split("-")
                else:
                    fecha= fila[11].split("/")
                insert=f"""IF NOT EXISTS ( SELECT 1 FROM DimFecha WHERE Dia={fecha[1]}
                and Mes = {fecha[0]} and Año = {fecha[2]})
                    BEGIN
                        INSERT INTO DimFecha (Dia, Mes,Año) VALUES ({fecha[1]},{fecha[0]},{fecha[2]});
                    END"""
                db.query(insert)
            except:
                continue
            try:
                insert=f"""IF NOT EXISTS (
                        SELECT 1 
                        FROM DimAeropuerto 
                        WHERE AirportName = '{fila[6]}' 
                        AND AirportCountryCode = '{fila[7]}' 
                        AND CountryName = '{fila[8]}'
                    )
                    BEGIN
                        INSERT INTO DimAeropuerto (AirportName, AirportCountryCode, CountryName, AirportContinent, ContinentName) 
                        VALUES ('{fila[6]}', '{fila[7]}', '{fila[8]}', '{fila[9]}', '{fila[10]}');
                    END;"""
                db.query(insert)
            except:
                continue
            try:
                insert=f"""IF NOT EXISTS (
                    SELECT 1 
                    FROM DimPasajero 
                    WHERE FirstName = '{fila[1]}' 
                    AND LastName = '{fila[2]}' 
                    AND Nationality = '{fila[6]}'
                )
                BEGIN
                    INSERT INTO DimPasajero (Indentificador,FirstName, LastName, Gender, Age, Nationality) 
                    VALUES ('{fila[0]}','{fila[1]}', '{fila[2]}', '{fila[3]}', {fila[4]}, '{fila[5]}');
                END;"""
                db.query(insert)
            except:
                continue
            try:
                insert=f"""EXEC InsertIntoHechosVuelos '{fila[1]}', '{fila[2]}', '{fila[3]}', {fila[4]}, '{fila[5]}', '{fila[6]}', '{fila[7]}', '{fila[8]}', '{fila[9]}', '{fila[10]}', {fecha[1]},{fecha[0]},{fecha[2]}, '{fila[12]}', '{fila[13].replace("'","")}', '{fila[14]}';
    """
                db.query(insert)
            except:
                continue
            
       #except Exception as e:
            #print(f"Descripción del error: {e}")

        

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
            db.query(querys.getProcedure())
            print("modelo creado")
        except:
            print("error al crear el modelo")
    elif c ==3:
        extraer_info()
    elif c ==4:
        cargar_info()
    elif c ==5:
        print("Consulta 1-->")
        tablas= querys.getConsulta1().split(";")
        print(f"Tabla pilotos: {db.query_retorno(tablas[0])[0]}")
        print(f"Tabla Aeropuertos: {db.query_retorno(tablas[1])[0]}")
        print(f"Tabla pasajeros: {db.query_retorno(tablas[2])[0]}")
        print(f"Tabla fechas: {db.query_retorno(tablas[3])[0]}")
        print(f"Tabla Vuelos: {db.query_retorno(tablas[4])[0]}")
        print("Consulta 2-->")
        for row in db.query_retorno_all(querys.getConsulta2()):
            print(f"Genero: {row.Gender}, Porcentaje: {row.Percentage:.2f}%")
        print("Consulta 3-->")
        for row in db.query_retorno_all(querys.getConsulta3()):
            print(row)
        print("Consultas creadas")
    print("--------------------------------")


