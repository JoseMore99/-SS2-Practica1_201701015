Tablas ="""

CREATE TABLE HechosVuelos (
    VuelosID  INT IDENTITY(1,1),
    PassengerID INT,
    AirPortID INT,
    ArrivalAirport NVARCHAR(10),
    FlightStatus NVARCHAR(50), 
    FechaID INT, --DepartureDate
    PilotID INT,
    PRIMARY KEY (VuelosID)
);


CREATE TABLE DimPasajero (
    PassengerID INT IDENTITY(1,1) PRIMARY KEY,
    Indentificador  NVARCHAR(10),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Gender NVARCHAR(10),
    Age INT,
    Nationality NVARCHAR(50)
);


CREATE TABLE DimAeropuerto (
    AirPortID INT IDENTITY(1,1) PRIMARY KEY,
    AirportName NVARCHAR(100),
    AirportCountryCode NVARCHAR(10),
    CountryName NVARCHAR(50),
    AirportContinent NVARCHAR(50),
    ContinentName NVARCHAR(50)
);



CREATE TABLE DimPiloto (
    PilotID INT IDENTITY(1,1) PRIMARY KEY,
    PilotName NVARCHAR(100) 
);


CREATE TABLE DimFecha (
    FechaID INT IDENTITY(1,1) PRIMARY KEY,
    Dia INT,
    Mes INT,
    Año INT
);


ALTER TABLE HechosVuelos
ADD CONSTRAINT FK_HechosVuelos_DimPasajero
FOREIGN KEY (PassengerID) REFERENCES DimPasajero(PassengerID);


ALTER TABLE HechosVuelos
ADD CONSTRAINT FK_HechosVuelos_DimAeropuerto
FOREIGN KEY (AirPortID) REFERENCES DimAeropuerto(AirPortID);


ALTER TABLE HechosVuelos
ADD CONSTRAINT FK_HechosVuelos_DimPiloto
FOREIGN KEY (PilotID) REFERENCES DimPiloto(PilotID);


ALTER TABLE HechosVuelos
ADD CONSTRAINT FK_HechosVuelos_DimFecha
FOREIGN KEY (FechaID) REFERENCES DimFecha(FechaID);

"""
def getTablas():
    return Tablas

Procedure ="""
CREATE PROCEDURE InsertIntoHechosVuelos
    @FirstName NVARCHAR(50),
    @LastName NVARCHAR(50),
    @Gender NVARCHAR(10),
    @Age INT,
    @Nationality NVARCHAR(50),
    @AirportName NVARCHAR(100),
    @AirportCountryCode NVARCHAR(10),
    @CountryName NVARCHAR(50),
    @AirportContinent NVARCHAR(50),
    @ContinentName NVARCHAR(50),
    @Dia INT,
    @Mes INT,
    @Año INT,
    @ArrivalAirport NVARCHAR(10),
    @PilotName NVARCHAR(100),
    @FlightStatus NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @PassengerID NVARCHAR(10);
    DECLARE @AirPortID INT;
    DECLARE @FechaID INT;
    DECLARE @PilotID INT;

    -- Step 1: Get Passenger ID
    SELECT @PassengerID = PassengerID FROM DimPasajero 
    WHERE FirstName = @FirstName AND LastName = @LastName AND Gender = @Gender 
    AND Age = @Age AND Nationality = @Nationality;

    IF @PassengerID IS NULL
    BEGIN
        RAISERROR('Passenger not found', 16, 1);
        RETURN;
    END

    -- Step 2: Get Airport ID
    SELECT @AirPortID = AirPortID FROM DimAeropuerto 
    WHERE AirportName = @AirportName AND AirportCountryCode = @AirportCountryCode 
    AND CountryName = @CountryName AND AirportContinent = @AirportContinent 
    AND ContinentName = @ContinentName;

    IF @AirPortID IS NULL
    BEGIN
        RAISERROR('Airport not found', 16, 1);
        RETURN;
    END

    -- Step 3: Get Date ID
    SELECT @FechaID = FechaID FROM DimFecha 
    WHERE Dia =  @Dia AND Mes =  @Mes AND Año =  @Año;

    IF @FechaID IS NULL
    BEGIN
        RAISERROR('Date not found', 16, 1);
        RETURN;
    END

    -- Step 4: Get Pilot ID
    SELECT @PilotID = PilotID FROM DimPiloto 
    WHERE PilotName = @PilotName;

    IF @PilotID IS NULL
    BEGIN
        RAISERROR('Pilot not found', 16, 1);
        RETURN;
    END

    -- Step 5: Insert into HechosVuelos
    INSERT INTO HechosVuelos (PassengerID, AirPortID, ArrivalAirport, FlightStatus, FechaID, PilotID)
    VALUES (@PassengerID, @AirPortID, @ArrivalAirport, @FlightStatus, @FechaID, @PilotID);
END

"""
def getProcedure():
    return Procedure

Drops="""
DROP PROCEDURE InsertIntoHechosVuelos;

DROP TABLE HechosVuelos; 

DROP TABLE DimPasajero; 

DROP TABLE DimAeropuerto; 

DROP TABLE DimPiloto; 

DROP TABLE DimFecha; 

"""

def getDrops():
    return Drops

temporales = """
CREATE TABLE #HechosVuelos (
    PassengerID INT,
    AirPortID INT,
    ArrivalAirport NVARCHAR(10),
    FlightStatus NVARCHAR(50), 
    FechaID INT, --DepartureDate
    PilotID INT
);

CREATE TABLE #DimPasajero (
    PassengerID INT,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Gender NVARCHAR(10),
    Age INT,
    Nationality NVARCHAR(50)
);

CREATE TABLE #DimAeropuerto (
    AirPortID INT,
    AirportName NVARCHAR(100),
    AirportCountryCode NVARCHAR(10),
    CountryName NVARCHAR(50),
    AirportContinent NVARCHAR(50),
    ContinentName NVARCHAR(50)
);


CREATE TABLE #DimPiloto (
    PilotID INT,
    PilotName NVARCHAR(100) 
);

CREATE TABLE #DimFecha (
    FechaID INT,
    Dia INT,
    Mes INT,
    Año INT
);
"""

def gettemporales():
    return temporales


Consulta1="""
Select COUNT(*) From DimPiloto;
Select COUNT(*) From DimAeropuerto;
Select COUNT(*) From DimPasajero;
Select COUNT(*) From DimFecha;
Select COUNT(*) From HechosVuelos;
"""
def getConsulta1():
    return Consulta1

Consulta2="""SELECT 
    Gender,
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM DimPasajero) AS Percentage
FROM 
    DimPasajero
GROUP BY 
    Gender;

"""
def getConsulta2():
    return Consulta2

Consulta3="""
WITH FechaSalida AS (
    SELECT 
        p.Nationality,
        CONCAT(f.Año, '-', RIGHT('0' + CAST(f.Mes AS VARCHAR(2)), 2)) AS MesAño,
        COUNT(*) AS TotalSalidas,
        ROW_NUMBER() OVER (PARTITION BY p.Nationality ORDER BY COUNT(*) DESC) AS RowNum
    FROM 
        HechosVuelos hv
    JOIN 
        DimPasajero p ON hv.PassengerID = p.PassengerID
    JOIN 
        DimFecha f ON hv.FechaID = f.FechaID
    GROUP BY 
        p.Nationality, f.Año, f.Mes
)
SELECT 
    Nationality, 
    MesAño, 
    TotalSalidas AS CantidadVuelos
FROM 
    FechaSalida
WHERE 
    RowNum = 1
ORDER BY 
    Nationality;
"""
def getConsulta3():
    return Consulta3

Consulta4="""
"""
def getConsulta4():
    return Consulta4

Consulta5="""
"""
def getConsulta5():
    return Consulta5

Consulta6="""
"""
def getConsulta6():
    return Consulta6

Consulta7="""
"""
def getConsulta7():
    return Consulta7

Consulta8="""
"""
def getConsulta8():
    return Consulta8

Consulta9="""
"""
def getConsulta9():
    return Consulta9

Consulta10="""
"""
def getConsulta10():
    return Consulta10