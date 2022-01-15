#Differential Equation Solver
#By: alex4371
#This program was written to solvebasic ODEs
#Created: Dec 32, 2021
#Last Modified: Dec 23, 2021
#Running on :Python 3.7.4


"""**********Imports**********"""

import numpy as np
import math

"""**********Classes**********"""
#Class to handle polynomials of any variable - base
class Polynomial:

    def __init__ (self, coefficients = [0], var = 'x'):
        coefficients.reverse()
        self.coefs = coefficients
        self.var = var

    def derivative(self, order = 1):
        polynomial = self.coefs
        for j in range(order):
            try:
                deriv = [0 for i in range(len(polynomial) - 1)]
                deriv[0] = 0                                    #Force an error if the polynomial is a consant
                for i in range(len(polynomial) - 1):
                    deriv[i] = polynomial[i + 1] * (i + 1)
                polynomial = deriv
            except:
                polynomial = [0]

        polynomial.reverse()
        return polynomial

    def getEquation(self):
        equation = ''
        for i in range(len(self.coefs) - 1,1,-1):
            if self.coefs[i] is 0:
                continue
            elif self.coefs[i] is 1:
                equation += self.var + "^" + str(i) + " + "
            elif self.coefs[i] is -1:
                equation = equation[:-2]
                equation += "- " + self.var + "^" + str(i) + " + "
            else:
                equation += str(self.coefs[i]) + self.var + "^" + str(i) + " + "
                
        if self.coefs[1] not in [-1,0,1]:
            equation += str(self.coefs[i]) + self.var + " + "   #No need for powers
        elif self.coefs[1] is 1:
            equation += self.var + " + "
        elif self.coefs[1] is -1:
            equation = equation[:-2]
            equation += "- " + self.var + " + "
            
        if self.coefs[0] is not 0:
            if self.coefs[0] < 0:
                equation = equation[:-2]
            equation += str(self.coefs[0])
            return equation
        else:
            return equation[:-3]    #Remove the unecessary last three charachters " + "


#Class to handle exponentials of any variable - base
class Exponential:

    def __init__ (self, r, k, var = 'x'):
        self.r = r
        self.k = k
        self.var = var
        print(self.r)
        print(self.k)

    def derivative(self, order = 1):
        return [self.r * self.k ** order, self.k]

    def getEquation(self):
        equation = ''
        if self.r is 0:
            return '0'
        elif self.k is 0:
            return str(self.r)
        
        equation += str(self.r)
        
        if self.r in [-1,1]:
            equation = equation[:-1]
            
        equation += "e^" + str(self.k)
        
        if self.k in [-1,1]:
            equation = equation[:-1]
            
        equation += self.var
            
        return equation


#Class to handle polynomials of any variable - base
class Sinusoidal:

    def __init__ (self, amplitudes, frequency, var = 'x'):
        self.amplitudes = amplitudes
        self.frequency = frequency
        self.var = var
        
    def derivative(self, order = 1):
        amplitudes = self.amplitudes
        for i in range(order):
            amplitudes.reverse()
            amplitudes[0] = -amplitudes[0] * self.frequency
            amplitudes[1] = amplitudes[1] * self.frequency
        return amplitudes, self.frequency

    def getEquation(self):
        equation = ''
        #sin
        if self.amplitudes[0] is not 0 and self.frequency[0] is not 0:
            equation += str(self.amplitudes[0])
            if self.amplitudes[0] in [-1,1]:
                equation = equation[:-1]
            equation += "sin(" + str(self.frequency[0])
            if self.frequency[0] in [-1,1]:
                equation = equation[:-1]
            equation += str(self.var) + ") + "

        #cos
        if self.amplitudes[1] is not 0:
            if self.amplitudes[1] < 0 and equation is not "":
                equation = equation[:-2]
            equation += str(self.amplitudes[1])
            if self.frequency[1] is not 0:
                if self.amplitudes[1] in [-1,1]:
                    equation = equation[:-1]
                if self.frequency[1] is not 0:
                    equation += "cos(" + str(self.frequency[1])
                if self.frequency[0] in [-1,1]:
                    equation = equation[:-1]
                equation += str(self.var) + ")"
        elif equation is "":
            equation = "0"
        else:
            equation = equation[:-3]    #Trim the plus if there is no cosine
        return equation
            


#Master class to handle entire equations which contains instances of Polynomials, Exponentials, and Sinusoidals
class Equation(Polynomial, Exponential, Sinusoidal):
    
    def __init__(self, equation, var = 'x'):
        #FIXME - Code to generate key variables from the equation as a series of 

        polys = []
        expos = []
        sins = []

        #Generate Polynomial objects and save them in an array
        for i in range(len(polyCoefs)):
            polys[i] = Polynomial(polyCoefs[i], var)
            self.polynomials = polys
        
        #Generate Exponential objects and save them in an array
        for i in range(len(polyCoefs)):
            expos[i] = Exponential(expoRs[i], expoTaus[i], var)
            self.polynomials = expos
            
        #Generate Sinusiodal objects and save them in an array
        for i in range(len(sinusoidalsCoefs)):
            sins[i] = Sinusoidal(sinusoidalsCoefs[i], sinusoidalsFreq[i], var)
            self.sinusoidals = sins

        #Take the derivative of all components of the equation
        def Derivative(self, order = 1):
            return 0    #FIXME - Iterate through all objects


"""**********Methods**********"""
#Clean up the string to remove unneded charachters
def CleanEqn(diffEqn):
    diffCleaned = diffEqn.replace(" ", "")
    return diffCleaned


#Extracting the charachteristic equation from a ODE
def GetCharEqn(diffEqn):
    poly = [0]
    primeCounter = 0
    numbCat = ''
    sign = 1
    for i in range(len(diffEqn)):

        if diffEqn[i] is "=":
            break
        
        if diffEqn[i].isdigit():
            numbCat= numbCat + diffEqn[i]                   #Collect the Digits
            continue
        
        if diffEqn[i] is "y":
            #print("It's a Y")
            primeCounter = 0
            for j in range(1,len(diffEqn)-i):
                #print(j)
                #print(diffEqn[i+j])
                if diffEqn[i+j] is "'":
                    primeCounter += 1
                    #print(primeCounter)                     #Put the digits in the right orders
                else:
                    break
                
            try:
                poly[primeCounter] = sign * int(numbCat)
                numbCat = ''

            except:
                for j in range(primeCounter):
                    poly.append(0)
                poly[primeCounter] = sign
                numbCat = ''
        
        elif  diffEqn[i] is "+":
            sign = 1
            continue
        
        elif diffEqn[i] is "-":
            sign = -1                                       #Check for negatives
            continue
        
    poly.reverse()
    return poly


#Get the roots from the charachteristic equation
def GetCharRoots(polyArray):
    return(np.roots(polyArray))


def GenerateHomoEqn(roots):
    equation = "y = "
    constant = 67
    usedRoots = []
    for i in roots:
        print(i)
        print(usedRoots)
        if -i in usedRoots and np.imag(i) > 0.0001:
            print("skip")
            continue
        
        equation += chr(constant)
        constant += 1
        
        if i in usedRoots:
            equation += "x"
            if usedRoots.count(i) > 1:
                equation += "^" + str(usedRoots.count(i))
            
        if abs(i) < 0.0001:
            pass        #DO NOT REMOVE - Not a placeholder
        elif abs(np.real(i)) < 0.0001:
            function = Sinusoidal([1,1], [np.imag(i), np.imag(i)])
            equation += "(" + function.getEquation() + ")" 
        elif abs(np.imag(i)) < 0.0001:
            function = Exponential(1, np.real(i))
            equation += function.getEquation()
        else:
            realFun = Exponential(1, np.real(i))
            imagFun = Sinusoidal([1,1], [np.imag(i), np.imag(i)])
            equation += realFun.getEquation() + "(" + imagFun.getEquation() + ")"

        equation += " + "
        usedRoots.append(i)

        #print(equation)
        if equation in "y = ":
            equation += "0   "

    return equation[:-3]
            

"""**********Core Code**********"""

print("""               Differential Equation Solver
                        By: alex4371

This program solves basic ODEs with the form L[y] = g(x) into y = f(x)

Currently Solves:
Linear Homogeneous ODEs

-----------------------------------------------------------------------
""")

while True:
    diffEqnIn = input("Enter Differential Equation in Standard Form using Prime Notation: ")

    cleanDiffEqn = CleanEqn(diffEqnIn)
    #print(cleanDiffEqn)
    try:
        #print(GetCharEqn(cleanDiffEqn))
        print(GetCharRoots(GetCharEqn(cleanDiffEqn)))
        print(GenerateHomoEqn(GetCharRoots(GetCharEqn(cleanDiffEqn))))

    except:
        print("Equation Failed. Please Try Again,\n")
        continue

    break

