Tablas ="""

CREATE TABLE HechosVuelos (
    PassengerID  INT IDENTITY(1,1),
    AirPortID INT,
    ArrivalAirport NVARCHAR(10),
    FlightStatus NVARCHAR(50), 
    FechaID INT, --DepartureDate
    PilotID INT,
    PRIMARY KEY (PassengerID)
);


CREATE TABLE DimPasajero (
    PassengerID INT IDENTITY(1,1) PRIMARY KEY,
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

Drops="""
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

