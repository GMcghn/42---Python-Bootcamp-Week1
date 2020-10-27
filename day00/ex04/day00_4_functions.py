def multiple_operations(a,b):
    import sys
    """Apply mathematical operations sum, soustraction, product, division and modulo to two integers and print the results."""

    try:
            
        c = int(a)
        d = int(b)
        
    except ValueError:       
        print("InputError: only numbers" +"\n" + "Usage: python operations.py <number1> <number2>"  \
              + "\n" + "Example:" + "\n" +"\t" + "python operations.py 10 3")
        sys.exit(1)
        
    if d == 0:
        print("Sum:"+ "\t"*2+ str(c+d) +"\n"+
              "Difference: "+"\t"+str(c-d) +"\n"+
              "Product: "+"\t"+str(c*d) +"\n"+
              "Quotient: "+"\t"+ "ERROR (div by zero)" +"\n"+
              "Remainder: " + "\t"+"ERROR (modulo by zero)"
             )
    else:

        print("Sum:"+ "\t"*2+ str(c+d) +"\n"+
              "Difference: "+"\t"+str(c-d) +"\n"+
              "Product: "+"\t"+str(c*d) +"\n"+
              "Quotient: "+"\t"+str(c/d) +"\n"+
              "Remainder: " + "\t"+str(c%d)
             )
