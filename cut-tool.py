# Cut Tool 
# Anna Leitner, June 2024 

import sys 

def main(input): 
   if (len(input.argv) < 3): 
      print("Must specify an option and a filename") 
   options = "" 
   delimiter = "\t"
   file = ""
   for i in range(len(input.argv)): 
      if input.argv[i][0:2] == "-f": 
         option = input.argv[i]
      elif input.argv[i][0:2] == "-d": 
         delimiter = input.argv[i][2:]
      else: 
         file = input.argv[i]
   # option to read from standard input
   if (file == "" or file == "-"): 
      f = sys.stdin
   else: 
      f = open(file, "r")
   if (option[0:2] == "-f"): 
      for line in f: 
         line = line.split(delimiter)
         toprint = option[2:]
         if (len(toprint)== 1): 
            print(line[int(toprint) - 1])
         else: 
            if (toprint.find(",") == -1): 
               toprint = toprint.split(" ")

            else: 
               toprint = toprint.split(",")
            i = 0
            while i < len(toprint): 
               print(line[int(toprint[i]) - 1] + delimiter + line[int(toprint[i+1]) - 1])
               i+= 2

main(sys)   
