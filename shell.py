import basic
file = open('InputValido.txt', 'r')
text = file.readlines()
for line in text:
    line = line.strip()
    result, error = basic.run(line)
    if error: print(error.as_string())
    else: 
        print(result)   
        if len(result) != 0:
            if result[1].type == basic.TT_STRING:
                if result[2].type == basic.TT_STRING:
                    print('Sintaxis Valida')
                else:
                    print('Sintaxin invalida')
            
    

            
      
       


        
        

