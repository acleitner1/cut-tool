# Cut Tool 
# Anna Leitner, June 2024 

import sys 

def main(input): 
   if (len(input.argv) < 3): 
      print("Must specify an option and a filename") 
   options = "" 
   delimiter = "\t"
   for i in range(len(input.argv)): 
      if input.argv[i][0:2] == "-f": 
         option = input.argv[i]
      elif input.argv[i][0:2] == "-d": 
         delimiter = input.argv[i][2:]
      else: 
         file = input.argv[i]

   if (option[0:2] == "-f"): 
      f = open(file, "r")
      for line in f: 
         line = line.split(delimiter)
         print(line[int(option[2]) - 1])

main(sys)   
