# Cut Tool 
# Anna Leitner, June 2024 

import sys 

def main(input): 
   if (len(input.argv) < 3): 
      print("Must specify an option and a filename") 
   option = input.argv[1]    
   file = input.argv[2]
   if (option[0:2] == "-f"): 
      f = open(file, "r")
      for line in f: 
         line = line.split("\t")
         print(line[int(option[2])])

main(sys)   
