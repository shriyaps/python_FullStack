# Save this code as employee.py

# To calculate dearness allowance
def da(basic):
    '''da is 80% of basic salary'''
    da = basic*(80/100)
    print(__name__)
    return da

# To calculate house rent allowance
def hra(basic):
    '''hra is 15% of basic salary'''
    hra = basic*(15/100)
    return hra

# To calculate provident fund amount
def pf(basic):
    '''pf is 12% of basic salary'''
    pf = basic*(12/100)
    return pf

# To calculate income tax payable by employee
def itax(gross):
    '''tax is calculated at 10% on gross'''
    tax = gross*0.1
    return tax
