#!/usr/bin/env python
# coding: utf-8

from sympy import * # To use symbolic manipulation
import itertools # To use product of iterators

# # Example of Quiz Generator
# Yo do not need to change this filename. If you do,
# it is necessary to change it the template file.

fout=open('chunks-moodle.tex','w');
fout.write("\\begin{quiz}{NameOfTheQuestionBank}\n") 

var('x,a,b,c,t') # Define the symbolic variables required

# Definition of the functions that we will integrate
f1=exp(a*x)+cos(b*x)**2 
f2=x**2+c


for a0,b0,c0 in itertools.product(range(2,4),range(1,4),range(1,4)):
    
    vals_example={a:a0,b:b0,c:c0} 
    
    # Each element in the quiz has the 'NameofCategory' and a specific number
    # The numbering contains the parameters a,b,c so one has to be careful if
    # using floats. Otherwise you can replace it by a counter. 
    fout.write(r"\begin{multi}{NameofCategory-"+'-'.join(map(str,vals_example.values()))+r'}')
    fout.write("\n")           

    # Write the statment of the problem with the specific integral 
    # once the values are substituted. 
    statement=r"Given the following function defined by an integral:"
    fun=r"$$F(x)= \int_{0}^{"+latex(f2.subs(vals_example))+r"}\left("
    fun+=latex(f1.subs(vals_example).subs({x:t}))+r'\right) dt .$$'
    fun+=r"Which of the following answers corresponds to the value of $F(0)+F'(0)$?"
    
    # Find the correct answer
    res_der=integrate(f1.subs(vals_example),(x,0,f2.subs(vals_example))).diff(x).subs({x:0})
    res_val=integrate(f1.subs(vals_example),(x,0,f2.subs(vals_example).subs({x:0})))
    result1=latex((res_der+res_val).simplify())
    # Compute some wrong answers
    result2=latex((res_der+res_val+1).simplify())
    result3=latex(res_der)
    result4=latex(res_val)

    fout.write(statement+fun)
    fout.write("\n")                       
    fout.write('\\item* $'+result1+'$\n'); # This is the correct answer
    fout.write('\\item $' +result2+'$\n'); # This is not the correct answer
    fout.write('\\item $' +result3+'$\n'); # This is not the correct answer
    fout.write('\\item $' +result4+'$\n'); # This is not the correct answer
    fout.write('\\item None of the above\n'); # Just in case...
    fout.write('\\end{multi}\n\n');

    
fout.write('\\end{quiz}\n');
fout.close()
