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
  if grade >= 93.00:
    G = "A"
  elif grade >= 90.00:
    G = "A-"
  elif grade >= 87.00:
    G = "B+"
  elif grade >= 83.00:
    G = "B"
  elif grade >= 80.00:
    G = "B-"
  elif grade >= 77.00:
    G = "C+"
  elif grade >= 70.00:
    G = "C"
  elif grade >= 60.00:
    G = "D"
  else :
    G = "F"
  return G;



  

if __name__ == "__main__":
  run(getLetterGrade(grade));