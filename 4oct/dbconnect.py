import mysql.connector
    
def connect_to_database():
  database = mysql.connector.connect(host="localhost", user="root", password="12345abc$#", database="hospital")
  return database

def close_database_connection(database):
  database.close()    

def menu():
  print("Welcome to the Hospital Management System!")
  print("1. Add patient")
  print("2. Remove patient")
  print("3. Add doctor")
  print("4. Remove doctor")
  print("5. Create appointment")
  print("6. Cancel appointment")
  print("7. Exit")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    add_patient_menu()
  elif choice == 2:
    remove_patient_menu()
  elif choice == 3:
    add_doctor_menu()
  elif choice == 4:
    remove_doctor_menu()
  elif choice == 5:
    create_appointment_menu()
  elif choice == 6:
    cancel_appointment_menu()
  elif choice == 7:
    close_database_connection(mydb)
    exit()
  else:
    print("Invalid choice!")

def add_patient_menu():
    pfname=input("Enter patient first name: ")
    plname=input("Enter patient last name: ")
    page=input("Enter patients DOB: ")
    pgender=input("Enter patient gender")
    paddress=input("Enter patient address")
    pphonenumber=input("Enter patient phone number: ")
    pmedhist=input("Enter patient mediacl history: ")
    add_patient(mydb,pfname,plname,page,pgender,paddress,pphonenumber,pmedhist)
    
def add_patient(database, pfname, plname, page, pgender, paddress, pphonenumber, pmedhist):
  cursor = database.cursor()
  cursor.execute("INSERT INTO Patient (FirstName, LastName, DateOfBirth, Gender, Addresss, PhoneNumber, MedicalHistory) VALUES (%s, %s, %s, %s, %s, %s, %s)", (pfname,plname,page,pgender,paddress,pphonenumber,pmedhist))
  database.commit()
  cursor.close()

def remove_patient_menu():
  try:
    pid=int(input("Enter patient id: "))
    remove_patient(mydb,pid)  
  except ValueError:
    print("Invalid input")  
    
def remove_patient(database, patient_id):
  cursor = database.cursor()
  cursor.execute("DELETE FROM Patient WHERE PatientID = %s", (patient_id,))
  database.commit()
  cursor.close()

def add_doctor_menu():
    dfname=input("Enter doctor's first name: ")
    dlname=input("Enter doctor's last name: ")    
    dspec=input("Enter doctor's specialization")
    ddid=int(input("Enter doctor's department id"))
    add_doctor(mydb,dfname,dlname,dspec,ddid)

def add_doctor(database, doctor_first_name,doctor_last_name, doctor_specialization, doctor_department_id):
  cursor = database.cursor()
  cursor.execute("INSERT INTO Doctor (FirstName,LastName,Specialization, DepartmentID) VALUES (%s, %s, %s, %s)", (doctor_first_name,doctor_last_name, doctor_specialization, doctor_department_id))
  database.commit()
  cursor.close()

def remove_doctor_menu():
    did=int(input("Enter doctor's id: "))
    remove_doctor(mydb,did)

def remove_doctor(database, doctor_id):
  cursor = database.cursor()
  cursor.execute("DELETE FROM Doctor WHERE DoctorID = %s", (doctor_id,))
  database.commit()
  cursor.close()

def create_appointment_menu():
    appid=int(input("Enter appointment id: "))
    pid=int(input("Enter patient's id: "))
    did=int(input("Doctor's id: "))
    appdate=input("Enter appointment date: ")
    apptime=input("Enter appointment time: ")
    rid=int(input("Enter Room ID: "))
    create_appointment(mydb,appid,pid,did,appdate,apptime,rid)

def create_appointment(database, appid,patient_id, doctor_id, appointment_date, appointment_time,rid):
  cursor = database.cursor()
  cursor.execute("INSERT INTO Appointment (AppointmentID,PatientID, DoctorID, AppointmentDate, AppointmentTime,RoomID) VALUES (%s, %s, %s, %s, %s, %s)", (appid,patient_id, doctor_id, appointment_date, appointment_time,rid))
  database.commit()
  cursor.close()

def cancel_appointment_menu():
    appid=int(input("Enter appointment id: "))
    cancel_appointment(mydb,appid)

def cancel_appointment(database, appointment_id):
  cursor = database.cursor()
  cursor.execute("DELETE FROM Appointment WHERE AppointmentID = %s", (appointment_id,))
  database.commit()
  cursor.close()
  
mydb=connect_to_database() 

while True:
    menu()