#!/usr/bin/
seq = [9,6,12,27,39,99,3,2,4,3,11,4,4,16,10,20,2,1,9,22,2,0,1,5,7,0]
reg1 = 0
reg2 = 0
insp = 0

def start():
  global seq, reg1, reg2, insp
  cyc = 1 
  while True:
    if seq[insp] == 0:
      return
    elif seq[insp] == 1:
      reg1 = seq[insp+1]
      insp += 2
    elif seq[insp] == 2:
      reg2 = seq[insp+1]
      insp += 2
    elif seq[insp] == 3:
      reg1 = seq[seq[insp+1]]
      insp += 2
    elif seq[insp] == 4:
      reg2 = seq[seq[insp+1]]
      insp += 2
    elif seq[insp] == 5:
      reg1 = reg2
      insp += 1
    elif seq[insp] == 6:
      reg1 = seq[reg2]
      insp += 1
    elif seq[insp] == 7:
      seq[reg1] = reg2
      insp += 1
    elif seq[insp] == 8:
      seq[seq[insp+1]] = reg1
      insp += 2
    elif seq[insp] == 9:  #jump
      insp = seq[insp+1]
    elif seq[insp] == 10: #jne
      if reg1 == 0:
        insp += 2
      else:
        insp = [insp+1]
    elif seq[insp] == 11:
      reg1 += reg2
      insp += 1
    elif seq[insp] == 12:
      reg1 -= reg2
      insp += 1
    elif seq[insp] == 13:
      reg1 *= reg2
      insp += 1
    elif seq[insp] == 14: #beware of integer division
      reg1 //= reg2
      insp += 1
    elif seq[insp] == 15:
      reg1 *= -1
      insp += 1
    elif seq[insp] == 16: #TODO: simplify
      if reg1-reg2 == 0:
        reg1 = 0
      else:
        reg1 = abs(reg1-reg2)/(reg1-reg2)
      insp += 1
    print("Cycle #"+ str(cyc))
    cyc += 1

def main():
  start()
  print("Register1: "+ str(reg1) + "\nRegister2: " + str(reg2) + "\nInstruction Pointer: " + str(insp))

main()
