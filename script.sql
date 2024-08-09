CREATE DATABASE DWHSS2;
GO

USE DWHSS2;
GO
--Arrival Airport

CREATE TABLE HechosVuelos (
    PassengerID INT,
    DepartureDate INT, 
    AirPortID INT,
    ArrivalAirport NVARCHAR(10),
    FlightStatus NVARCHAR(50), 
    FechaID INT,
    PilotID INT,
    PRIMARY KEY (PassengerID)
);
GO

CREATE TABLE DimPasajero (
    PassengerID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Gender NVARCHAR(10),
    Age INT,
    Nationality NVARCHAR(50)
);
GO

CREATE TABLE DimAeropuerto (
    AirPortID INT PRIMARY KEY,
    AirportName NVARCHAR(100),
    AirportCountryCode NVARCHAR(10),
    CountryName NVARCHAR(50),
    AirportContinent NVARCHAR(50),
    ContinentName NVARCHAR(50)
);
GO


CREATE TABLE DimPiloto (
    PilotID INT PRIMARY KEY,
    PilotName NVARCHAR(100) 
);
GO

CREATE TABLE DimFecha (
    FechaID INT PRIMARY KEY,
    Dia INT,
    Mes INT,
    Año INT
);
GO

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
GO
