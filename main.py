# Author: Shubhang Srikoti svs6959@psu.psu.edu
# Collaborator: Aditya Majumdar apm6483@psu.psu.edu
# Collaborator: Manav Shah mvs6909@psu.edu
# Collaborator: Weijun Fan wmf5111@psu.edu
# Section: 4
# Breakout: 12

def run(grade):
  getLetterGrade();
  G = float(input("Enter your CMPSC 131 grade: "));
  
def getLetterGrade(grade):
  if grade >= 93.0:
    G = "A"
    print("Your letter grade for CMPSC 131 is A.")
  elif grade >= 90.0:
    G = "A-"
    print("Your letter grade for CMPSC 131 is A-.")
  elif grade >= 87.0:
    G = "B+"
    print("Your letter grade for CMPSC 131 is B+.")
  elif grade >= 83.0:
    G = "B"
    print("Your letter grade for CMPSC 131 is B.")
  elif grade >= 80.0:
    G = "B-"
    print("Your letter grade for CMPSC 131 is B-.")
  elif grade >= 77.0:
    G = "C+"
    print("Your letter grade for CMPSC 131 is C+.")
  elif grade >= 70.0:
    G = "C"
    print("Your letter grade for CMPSC 131 is C.")
  elif grade >= 60.0:
    G = "D"
    print("Your letter grade for CMPSC 131 is D.")
  else :
    G = "F"
    print("Your letter grade for CMPSC 131 is F.")
  return G;



  

if __name__ == "__main__":
  run(getLetterGrade(grade));