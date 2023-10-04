
CREATE TABLE Patient (
  PatientID INT NOT NULL AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  DateOfBirth DATE NOT NULL,
  Gender VARCHAR(255) NOT NULL,
  Addresss VARCHAR(255) NOT NULL,
  PhoneNumber VARCHAR(255) NOT NULL,
  MedicalHistory TEXT,
  PRIMARY KEY (PatientID)
);

CREATE TABLE Department (
  DepartmentID INT NOT NULL AUTO_INCREMENT,
  DepartmentName VARCHAR(255) NOT NULL,
  PRIMARY KEY (DepartmentID)
);

CREATE TABLE Doctor (
  DoctorID INT NOT NULL AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Specialization VARCHAR(255) NOT NULL,
  DepartmentID INT NOT NULL,
  PRIMARY KEY (DoctorID),
  FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

CREATE TABLE Staff (
  StaffID INT NOT NULL AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  JobTitle VARCHAR(255) NOT NULL,
  DepartmentID INT NOT NULL,
  PRIMARY KEY (StaffID),
  FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);


CREATE TABLE Room (
  RoomID INT NOT NULL AUTO_INCREMENT,
  RoomType VARCHAR(255) NOT NULL,
  DepartmentID INT NOT NULL,
  PRIMARY KEY (RoomID),
  FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

CREATE TABLE Appointment (
  AppointmentID INT NOT NULL AUTO_INCREMENT,
  PatientID INT NOT NULL,
  DoctorID INT NOT NULL,
  AppointmentDate DATE NOT NULL,
  AppointmentTime TIME NOT NULL,
  RoomID INT NOT NULL,
  PRIMARY KEY (AppointmentID),
  FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY (DoctorID) REFERENCES Doctor(DoctorID),
  FOREIGN KEY (RoomID) REFERENCES Room(RoomID)
);

CREATE TABLE Medicine (
  MedicineID INT NOT NULL AUTO_INCREMENT,
  MedicineName VARCHAR(255) NOT NULL,
  Quantity INT NOT NULL,
  PRIMARY KEY (MedicineID)
);

CREATE TABLE Equipment (
  EquipmentID INT NOT NULL AUTO_INCREMENT,
  EquipmentName VARCHAR(255) NOT NULL,
  Quantity INT NOT NULL,
  PRIMARY KEY (EquipmentID)
);

CREATE TABLE Bill (
  BillID INT NOT NULL AUTO_INCREMENT,
  AppointmentID INT NOT NULL,
  TotalAmount DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (BillID),
  FOREIGN KEY (AppointmentID) REFERENCES Appointment(AppointmentID)
);

INSERT INTO Patient (FirstName, LastName, DateOfBirth, Gender, Addresss, PhoneNumber, MedicalHistory)
VALUES
('Nimal', 'Perera', '1990-01-01', 'Male', '123 Main Street, Colombo, Sri Lanka', '+94 11 2345678', 'No known medical history'),
('Dilhani', 'Silva', '1991-02-02', 'Female', '456 Elm Street, Kandy, Sri Lanka', '+94 81 4567890', 'No known medical history'),
('Kamal', 'Rajapaksa', '1992-03-03', 'Male', '789 Oak Street, Galle, Sri Lanka', '+94 71 6789012', 'No known medical history'),
('Priya', 'Fernando', '1993-04-04', 'Female', '1011 Maple Street, Matara, Sri Lanka', '+94 41 8901234', 'No known medical history'),
('Dinesh', 'Gunesekera', '1994-05-05', 'Male', '1234 Pine Street, Negombo, Sri Lanka', '+94 31 0123456', 'No known medical history'),
('Shani', 'Mendis', '1995-06-06', 'Female', '567 Birch Street, Kurunegala, Sri Lanka', '+94 55 2345678', 'No known medical history'),
('Anura', 'Herath', '1996-07-07', 'Male', '890 Cedar Street, Anuradhapura, Sri Lanka', '+94 25 4567890', 'No known medical history'),
('Priyanka', 'Jayawardena', '1997-08-08', 'Female', '1122 Elm Street, Polonnaruwa, Sri Lanka', '+94 65 6789012', 'No known medical history'),
('Malith', 'Bandara', '1998-09-09', 'Male', '1356 Oak Street, Sigiriya, Sri Lanka', '+94 75 8901234', 'No known medical history'),
('Tharaka', 'Wijesinghe', '1999-10-10', 'Female', '1589 Maple Street, Dambulla, Sri Lanka', '+94 85 0123456', 'No known medical history'),
('Kushan', 'Perera', '2000-11-11', 'Male', '1822 Pine Street, Trincomalee, Sri Lanka', '+94 95 2345678', 'No known medical history'),
('Nayomi', 'Silva', '2001-12-12', 'Female', '2055 Birch Street, Anuradhapura, Sri Lanka', '+94 25 4567890', 'No known medical history'),
('Nishan', 'Rajapaksa', '2002-01-01', 'Male', '2288 Cedar Street, Polonnaruwa, Sri Lanka', '+94 65 6789012', 'No known medical history'),
('Roshani', 'Fernando', '2003-02-02', 'Female', '2521 Elm Street, Sigiriya, Sri Lanka', '+94 75 8901234', 'No known medical history'),
('Chanaka', 'Gunesekera', '2004-03-03', 'Male', '2754 Oak Street, Dambulla, Sri Lanka', '+94 85 0123456');

INSERT INTO Department (DepartmentName)
VALUES ('Cardiology'),
('Orthopedics'),
('Pediatrics'),
('Dermatology'),
('Neurology'),
('General Surgery'),
('Ophthalmology');

INSERT INTO Doctor (FirstName, LastName, Specialization, DepartmentID)
VALUES ('Rahul', 'Gupta', 'Cardiology', 1);
INSERT INTO Doctor (FirstName, LastName, Specialization, DepartmentID)
VALUES ('Aisha', 'Khan', 'Orthopedics', 2);
INSERT INTO Doctor (FirstName, LastName, Specialization, DepartmentID)
VALUES ('Arvind', 'Kumar', 'Pediatrics', 3);
INSERT INTO Doctor (FirstName, LastName, Specialization, DepartmentID)
VALUES ('Bhavna', 'Patel', 'Dermatology', 4);
INSERT INTO Doctor (FirstName, LastName, Specialization, DepartmentID)
VALUES ('Chandan', 'Singh', 'Neurology', 5);
INSERT INTO Doctor (FirstName, LastName, Specialization, DepartmentID)
VALUES ('Deepika', 'Verma', 'General Surgery', 6);
INSERT INTO Doctor (FirstName, LastName, Specialization, DepartmentID)
VALUES ('Eshaan', 'Jain', 'Ophthalmology', 7);


INSERT INTO Staff (FirstName, LastName, JobTitle, DepartmentID)
VALUES
('Mohammad', 'Ali', 'Nurse', 1),
('Sohel', 'Ahmed', 'Lab Technician', 3),
('Nusrat', 'Jahan', 'Pharmacist', 4),
('Kamal', 'Hossain', 'Receptionist', 5),
('Priya', 'Das', 'Ward Clerk', 6),
('Rasel', 'Ahmed', 'Accountant', 7),
('Sharmin', 'Akter', 'HR Manager', 8),
('Rahim', 'Sheikh', 'IT Manager', 9),
('Jannat', 'Alam', 'Maintenance Manager', 10);

INSERT INTO Room (RoomType, DepartmentID)
VALUES
('General Ward', 1),
('ICU', 1),
('CCU', 1),
('Pediatric Ward', 2),
('NICU', 2),
('PICU', 2),
('Maternity Ward', 3),
('Labor and Delivery Room', 3),
('Operating Room', 4),
('Recovery Room', 4);


INSERT INTO Appointment (PatientID, DoctorID, AppointmentDate, AppointmentTime, RoomID)
VALUES
(1, 1, '2023-08-08', '10:00 AM', 1),
(2, 2, '2023-08-08', '11:00 AM', 2),
(3, 3, '2023-08-08', '12:00 PM', 3),
(4, 4, '2023-08-09', '10:00 AM', 4),
(5, 5, '2023-08-09', '11:00 AM', 5),
(6, 6, '2023-08-09', '12:00 PM', 6),
(7, 7, '2023-08-10', '10:00 AM', 7);

INSERT INTO Medicine (MedicineName, Quantity)
VALUES
('Paracetamol', 100),
('Ibuprofen', 50),
('Azithromycin', 20),
('Amoxicillin', 20),
('Metformin', 10),
('Glipizide', 10),
('Insulin', 10),
('Atenolol', 10),
('Amlodipine', 10),
('Lisinopril', 10),
('Fluticasone', 10),
('Salbutamol', 10),
('Montelukast', 10),
('Ciprofloxacin', 10),
('Ofloxacin', 10),
('Levofloxacin', 10);

INSERT INTO Equipment (EquipmentName, Quantity)
VALUES
('Stethoscope', 10),
('Sphygmomanometer', 10),
('Glucometer', 10),
('Thermometer', 10),
('Pulse oximeter', 10),
('Defibrillator', 5),
('Ventilator', 5),
('Anesthesia machine', 5),
('Surgical microscope', 5),
('X-ray machine', 2),
('CT scanner', 2),
('MRI scanner', 2),
('Ultrasound machine', 2),
('Dialysis machine', 2),
('Lithotripter', 1),
('Linear accelerator', 1);

INSERT INTO Bill (PatientID, DoctorID, AppointmentID, Date, TotalAmount)
VALUES
(1, 1, 1, '2023-08-08', 1000),
(2, 2, 2, '2023-08-08', 1200),
(3, 3, 3, '2023-08-08', 1500),
(4, 4, 4, '2023-08-09', 1800),
(5, 5, 5, '2023-08-09', 2100),
(6, 6, 6, '2023-08-09', 2400),
(7, 7, 7, '2023-08-10', 2700);

