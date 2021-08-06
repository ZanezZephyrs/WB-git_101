#o objetivo da aplicação é simular o rendimento de financeiro com aportes frequentes
from datetime import *

def Simple(start, end, percentage):
    
    return
        
def complex(start, end, percentage, monthly_income):
    return

def Main():
    start = input("insira a data de inicio do rendimento: formato dd/mm/yy")
    end = input("insira a data de vencimento do rendimento: formato dd/mm/yy")
    percentage = input("insira o rendimento mensal em porcentagem: ex: 1% = 0.01")
    first_contribution = float(input("insita o valor do primeiro aporte"))
    is_monthly = float(input("terá aportes mensais ?"))

    start = datetime.strptime(start,'%d/%m/Y').date()
    end = datetime.strptime(end,'%d/%m/Y').date()
    percentage = float(percentage)

    if(not is_monthly):
        Simple(start,end,percentage)
    else:
        monthly_income = float(input("renda mensal prevista"))
        complex(start,end,percentage,monthly_income)
    
    return
    
