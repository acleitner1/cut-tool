# Cut Tool 
# Anna Leitner, June 2024 
# Implements Unix Cut Tool 
# To Run: Call "python3 cut-tool.py" followed by option flag (-f) and optionally, delimiter (-d) and filename

import sys 

def main(input): 
   if (len(input.argv) < 3): 
      print("Must specify an option") 
   options = "" 
   delimiter = "\t"
   file = ""

   # Assign option, delimter, and file from intput
   for i in range(len(input.argv)): 
      if input.argv[i][0:2] == "-f": 
         option = input.argv[i]
      elif input.argv[i][0:2] == "-d": 
         delimiter = input.argv[i][2:]
      else: 
         file = input.argv[i]

   # If no file specified, 
   if (file == "" or file == "-"): 
      f = sys.stdin
   else: 
      f = open(file, "r")

   # Ensures that option is specified
   if (option[0:2] == "-f"): 
      for line in f: 
         line = line.split(delimiter)
         toprint = option[2:]

         # Print each option specified 
         if (len(toprint)== 1): 
            print(line[int(toprint) - 1])
         else: 
            if (toprint.find(",") == -1): 
               toprint = toprint.split(" ")

            else: 
               toprint = toprint.split(",")
            i = 0

            # Print in File Format with specified delimeter 
            while i < len(toprint): 
               print(line[int(toprint[i]) - 1] + delimiter + line[int(toprint[i+1]) - 1])
               i+= 2
   else: 
      print("Must include an -f option")

main(sys)   
