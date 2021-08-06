#o objetivo da aplicação é simular o rendimento de financeiro com aportes frequentes
from datetime import *
from dateutil.relativedelta import *

def Calculator(start_date, years, months, percentage, initial,monthly_income):
    counter = 0
    months += years*12
    print(f"inicio do investimento: {start_date}\naporte inicial: {initial:.2f}")
    while counter < months:
        counter += 1
        start_date = start_date + relativedelta(months=+1)
        initial *= percentage
        initial += monthly_income
        print(f"{start_date}: {initial}")
        

def convert_str_to_boolean(is_monthly):
    is_monthly
    if(is_monthly == 'sim'):
        return True
    else:
        return False

def Main():
    start = input("insira a data de inicio do rendimento: formato dd/mm/yyyy \n")
    end = input("insira a data de vencimento do rendimento: formato dd/mm/yyyy\n")
    percentage = float(input("insira o rendimento mensal em porcentagem: ex: 1% = 0.01\n"))
    first_contribution = float(input("insita o valor do primeiro aporte\n"))
    is_monthly = input("terá aportes mensais? Responda sim ou não\n").lower().strip()
    percentage +=1
    start = datetime.strptime(start,"%d/%m/%Y").date()
    end = datetime.strptime(end,"%d/%m/%Y").date()

    if(not convert_str_to_boolean(is_monthly)):
        Calculator(start,relativedelta(end,start).years,
        relativedelta(end,start).months,percentage, first_contribution,0)
    else:
        monthly_income = float(input("renda mensal prevista:\n"))

        Calculator(start,relativedelta(end,start).years,
        relativedelta(end,start).months,percentage, first_contribution,monthly_income)
    
Main()