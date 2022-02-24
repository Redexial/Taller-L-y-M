import basic
file = open('InputValido.txt', 'r')
text = file.readlines()
#result, error = basic.run(text.strip())
#print(text)
#if error: print(error.as_string())
#else: 
#    print(result)
xyalpha = ''.join([line.strip() for line in text])
result, error = basic.run(xyalpha)
for block in result:
    print(block)
#for line in text:
 #   line = line.strip()
  #  result, error = basic.run(line)
   # if error: print(error.as_string())
    #else: 
     #   print(result)