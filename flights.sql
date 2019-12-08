
CREATE TABLE IF NOT EXISTS Flights(id INTEGER PRIMARY KEY AUTO_INCREMENT, airline VARCHAR(100) NOT NULL, origin VARCHAR(100) NOT NULL, oricode VARCHAR(3), destination VARCHAR(100) NOT NULL, descode VARCHAR(3), duration VARCHAR(50), type VARCHAR(100), depdate DATE, economy INTEGER, business INTEGER);

-- --------------------------------------------------------------------------------------------------------------------------

INSERT INTO Flights(airline, origin, oricode, destination, descode, duration, type, depdate, economy, business) VALUES
("Air India", "Mumbai", "BOM", "Delhi", "DEL", "02h 05m", "Domestic", "2019-09-23", 2350, 4350),
("IndiGo", "Bangalore", "BLR", "Mumbai", "BOM", "01h 30m", "Domestic", "2019-10-1", 3250, 7350),
("JetLite", "Chennai", "MAA", "Mumbai", "BOM", "02h 00m", "Domestic", "2019-09-23", 2270, 6425),
("SpiceJet", "Goa", "GOI", "Kolkata", "CCU", "04h 30m", "Domestic", "2019-10-2", 2464, 4675),
("Air Asia", "Jaipur", "JAI", "Pune", "PNQ", "01h 40m", "Domestic", "2019-11-10", 3420, 6843),
("Lufthansa", "Mumbai", "BOM", "Paris", "CDG", "11h 55m", "International", "2019-11-30", 15430, 18250),
("Kuwait Airways", "Dubai", "DXB", "New York", "JFK", "18h 00m", "International", "2019-12-05", 12320, 18990),
("Emirates", "Zurich", "ZRH", "Dubai", "DXB", "06h 10m", "International", "2019-10-20", 16550, 20990),
("Oman Air", "Amsterdam", "AMS", "Bangalore", "BLR", "23h 20m", "International", "2020-02-14", 13560, 16780),
("Vistara", "Goa", "GOI", "Delhi", "DEL", "02h 40m", "Domestic", "2019-09-29", 4380, 7860),
("Air Asia", "Mumbai", "BOM", "Singapore", "SIN", "08h 40m", "International", "2019-10-18", 13653, 17850),
("Cathay Pacific", "Hyderabad", "HYD", "Toronto", "YYZ", "28h 30m", "International", "2020-08-10", 18970, 22870),
("SpiceJet", "Bangalore", "BLR", "London", "LHR", "25h 50m", "International", "2020-03-06", 18956, 23420),
("IndiGo", "Patna", "PAT", "Cochin", "COK", "06h 20m", "Domestic", "2020-01-05", 3270, 5640),
("Vistara", "Pune", "PNQ", "Goa", "GOI", "04h 20m", "Domestic", "2020-02-20", 4329, 7650),
("Gulf Air", "Mumbai", "BOM", "Frankfurt", "FRA", "15h 50m", "International", "2020-04-08", 15640, 19850),
("American Airlines", "Chicago", "ORD", "Sydney", "SYD", "21h 50m", "International", "2020-03-15", 76250, 78990),
("Quantas Airways", "Delhi", "DEL", "Wellington", "WLG", "34h 50m", "International", "2020-04-10", 80150, 82550),
("American Airlines", "Chicago", "ORD", "Sydney", "SYD", "21h 50m", "International", "2020-03-15", 56500, 60990),
("Vistara", "Jammu", "IXJ", "Chennai", "MAA","7h 50m", "Domestic", "2019-12-30", 5680, 10350),
("Air India", "Bangalore", "BLR", "Hyderabad", "HYD", "01h 00m", "Domestic", "2019-11-25", 8250, 10950);
