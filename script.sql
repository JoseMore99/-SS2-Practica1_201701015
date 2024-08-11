CREATE DATABASE DWHSS2;
GO

USE DWHSS2;
GO
--Arrival Airport


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

ALTER TABLE HechosVuelos
ADD CONSTRAINT FK_HechosVuelos_DimFecha
FOREIGN KEY (FechaID) REFERENCES DimFecha(FechaID);
GO

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
    @DepartureDate DATE,
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
    WHERE Dia = DAY(@DepartureDate) AND Mes = MONTH(@DepartureDate) AND Año = YEAR(@DepartureDate);

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
