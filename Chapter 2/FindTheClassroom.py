classRooms={
    "Biology":211,
    "Computing":401,
    "Electronics":75 
}
studentInput=input("Type your name and subject:")
inputList=list(studentInput.split())
studentName=inputList[0]
studentSubject=inputList[1]
if classRooms.keys().__contains__(studentSubject):
    print(f"Hi {studentName}, go to room {classRooms[studentSubject]} for {studentSubject}.")
else:
    print(f"I don't know which room that class is in.")