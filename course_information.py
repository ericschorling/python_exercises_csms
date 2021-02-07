#Course Information
#Eric "Jack" Schorling
#February 15, 2021

courseName = input("What course do you want to know about: ")

roomDict = {
    "CSC101" : 3004,
    "CSC102" : 4501,
    "CSC103" : 6755,
    "NET110" : 1244,
    "COM241" : 1411 
}


roomDict = {
    "CSC101" : "8:00 a.m.",
    "CSC102" : "9:00 a.m.",
    "CSC103" : "10:00 a.m.",
    "NET110" : "11:00 a.m.",
    "COM241" : "1:00 p.m." 
}


instDict = {
    "CSC101" : "Haynes",
    "CSC102" : "Alvarado",
    "CSC103" : "Rich",
    "NET110" : "Burke",
    "COM241" : "Lee" 
}

print(instDict[courseName])