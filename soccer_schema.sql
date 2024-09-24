-- Enable foreign key support
PRAGMA foreign_keys = ON;

-- Create the Soccer Management System tables
CREATE TABLE IF NOT EXISTS Players (
    PlayerID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DateOfBirth DATE,
    Address TEXT,
    ContactInformation TEXT,
    MedicalRecords TEXT,
    RegistrationDate DATE,
    RegistrationStatus TEXT
);

CREATE TABLE IF NOT EXISTS Coaches (
    CoachID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    DateOfBirth DATE,
    Address TEXT,
    ContactInformation TEXT,
    CoachingLicenseNumber TEXT,
    EmploymentStartDate DATE,
    EmploymentEndDate DATE
);

CREATE TABLE IF NOT EXISTS TrainingSessions (
    SessionID INTEGER PRIMARY KEY,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Location TEXT NOT NULL,
    SessionType TEXT,
    Attendance INTEGER,
    CHECK (Attendance >= 0) -- Assuming attendance cannot be negative
);

CREATE TABLE IF NOT EXISTS PlayersTrainingSessions (
    PlayerID INTEGER,
    SessionID INTEGER,
    PRIMARY KEY (PlayerID, SessionID),
    FOREIGN KEY (PlayerID) REFERENCES Players (PlayerID),
    FOREIGN KEY (SessionID) REFERENCES TrainingSessions (SessionID)
);

CREATE TABLE IF NOT EXISTS Referees (
    RefereeID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    ContactInformation TEXT,
    Availability TEXT
);

CREATE TABLE IF NOT EXISTS Matches (
    MatchID INTEGER PRIMARY KEY,
    HomeTeam TEXT NOT NULL,
    AwayTeam TEXT NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    Location TEXT NOT NULL,
    RefereeID INTEGER,
    MatchResult TEXT,
    FOREIGN KEY (RefereeID) REFERENCES Referees (RefereeID)
);

CREATE TABLE IF NOT EXISTS FinancialTransactions (
    TransactionID INTEGER PRIMARY KEY,
    TransactionDate DATE NOT NULL,
    TransactionType TEXT NOT NULL,
    Amount REAL NOT NULL,
    Description TEXT,
    PlayerID INTEGER,
    SponsorshipID INTEGER,
    FOREIGN KEY (PlayerID) REFERENCES Players (PlayerID),
    FOREIGN KEY (SponsorshipID) REFERENCES Sponsors (SponsorID)
);

CREATE TABLE IF NOT EXISTS Sponsors (
    SponsorID INTEGER PRIMARY KEY,
    SponsorName TEXT NOT NULL,
    ContactInformation TEXT,
    SponsorshipAmount REAL NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS Tickets (
    TicketID INTEGER PRIMARY KEY,
    MatchID INTEGER,
    TicketType TEXT NOT NULL,
    Price REAL NOT NULL,
    SaleDate DATE NOT NULL,
    BuyerInformation TEXT,
    FOREIGN KEY (MatchID) REFERENCES Matches (MatchID)
);

CREATE TABLE IF NOT EXISTS Fans (
    FanID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    ContactInformation TEXT,
    FanEngagementStatistics TEXT
);

CREATE TABLE IF NOT EXISTS FanEngagementActivities (
    ActivityID INTEGER PRIMARY KEY,
    ActivityType TEXT NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    FanID INTEGER,
    FOREIGN KEY (FanID) REFERENCES Fans (FanID)
);

CREATE TABLE IF NOT EXISTS SoccerOrganizationDirector (
    DirectorID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    ContactInformation TEXT
);
