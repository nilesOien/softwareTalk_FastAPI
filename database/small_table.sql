
CREATE TABLE IF NOT EXISTS small (
        firstName           TEXT NOT NULL,
        lastName            TEXT NOT NULL,
        numBikes            INT  NOT NULL,
	usesPiApproximation REAL NOT NULL,
	likesAurorasTooMuch INT  NOT NULL
    );

INSERT INTO small 
 (firstName, lastName, numBikes, usesPiApproximation, likesAurorasTooMuch)
VALUES
('Niles', 'Oien', 3, 3.141, 1);

INSERT INTO small 
 (firstName, lastName, numBikes, usesPiApproximation, likesAurorasTooMuch) 
VALUES 
('Noah', 'Oien', 1, 3.1415927, 0);

INSERT INTO small
 (firstName, lastName, numBikes, usesPiApproximation, likesAurorasTooMuch)
VALUES
('Amy', 'Oien', 0, 3.1, 1);

INSERT INTO small
 (firstName, lastName, numBikes, usesPiApproximation, likesAurorasTooMuch)
VALUES
('Sedona', 'Crouch', 1, 3.0, 1);

