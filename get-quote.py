import random
def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = [line.strip() for line in f.readlines()]
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd1 = random.randint(0, last)
  print((rnd+1), quotes[rnd])   
  print((rnd1+1), quotes[rnd1])

def addlines():
  str1 = str(input("Enter the line to append to file: "))
  #s = str(str1)
  f=open("quotes.txt", "a+")
  f.write(str1 + "\n")
  f.close()
  #print("Your new line: ", str1)


if __name__== "__main__":
  addlines()
  main()
