# PHSX815_Week8
contains the homework/practice code and other materials for week 8 


This code is made entirely using code from my own respositories as well as the repositories of professor Rogan
https://github.com/crogan/PHSX815_Week8
https://github.com/Stayskul/

To run homework 8:
First put the Random.py file in a folder, which you need to specifiy in the Neyman.py code.
Next, to run the Neyman.py code, simply run python3 Neyman.py -sigx 10 -Nexp 10000 -Nmeas 10 (for example).
This should generate a 2D histogram depicting the measured values of mu for the lognorm vs the actual values of mu (an example graph is provided in this repository).


Homework 9: Minimization
I mainly used code from: https://www.youtube.com/watch?v=G0yP_TM-oag
I also used my own code from previous work

To run Minimize.py:
In the Minimize.py code, first in def f(x), define your y. I just choose a simply 3rd order polynomial, but it should work with any function.
Next you want to give a guess at where the minimum is; this is x_start
Finally, just run python3 Minimize.py. 
The code should then output the x and y location of the minimum, if it exists; otherwise, it will output, "cannot find minimum".
