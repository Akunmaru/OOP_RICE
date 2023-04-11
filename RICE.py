
#Rental Income Calculator Example (RICE)
#I only put 'example' in so the acronym becomes RICE


class moneyMoos():
    def __init__(self):
        self.answer = {'Good house' : False}


    #Two plus Two is FOUR, minus 1 thats Three QUICK MAFS
    def quickMafs(self):
        replyIncome = float(input('What is your monthly income? \n\n$'))

        #EXPENSES
        costs = []
        vacancy = float(replyIncome) * .05
        costs.append(vacancy)
        propertyManager = float(replyIncome) * 0.1
        costs.append(propertyManager)

        replyTax = float(input('What is your monthly tax? \n\n$'))
        costs.append(replyTax)

        replyInsur = float(input("What is your monthly insurance payment? \n\n$"))
        costs.append(replyInsur)

        replyRepair = float(input('What will be your monthly repair cost? \n\n$'))
        costs.append(replyRepair)

        replyCapEx = float(input('What will be your monthly CapEx cost? \n\n$'))
        costs.append(replyCapEx)

        replyMortgage = float(input('What is the monthly mortgage payment?\n\n$'))
        costs.append(replyMortgage)



        expenses = sum(costs)
        cashFlow = replyIncome - expenses
        print(f'Your cash flow is ${cashFlow}')

        #INVESTMENT
        sending = []

        replyDown = float(input('What is the total downpayment? \n\n$'))
        sending.append(replyDown)

        replyClose = float(input('What is the total closing cost? \n\n$'))
        sending.append(replyClose)

        replyRehab = float(input('What is the total rehab budget? \n\n$'))
        sending.append(replyRehab)

        investment = sum(sending)

        #Calculating...
        annualCashFlow = float(cashFlow) * 12.0
        print(f'Your annual cash flow is ${annualCashFlow}')
        ROI = annualCashFlow / investment
        print(f'Your Return Of Investment (ROI) is ${ROI}')
        if ROI > .10:
            self.answer.update({'Good house' : True})
            print('That is a good deal! Dayum good deal! Because your ROI is ABOVE the average stock return!')
        elif ROI < .10:
            print('That is NOT a good deal! Your ROI is BELOW the avaerage stock return!')

moola = moneyMoos()



#This starts the function
def initialize():
    while True:
        helloCitizen = input('\nWelcome to the RENTAL INCOME CALCULTOR!\nWould you like to use my services? (Y/N) ')
        if helloCitizen.lower() == 'n':
            print('Aww thats too bad :( You made me sad now')
            break
        elif helloCitizen.lower() == 'y':
            moola.quickMafs()
        else:
            print('Try another command')

initialize()