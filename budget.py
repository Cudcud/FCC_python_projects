from math import fsum, floor

class Category:
  
  def __init__(self, category = ''):
    self.category = category
    self.ledger = []
    
  def __repr__(self) :
    budget_category = self.category.center(30,'*')
    #list comprehension
    d_list = [x['description'] for x in self.ledger]
    a_list = [x['amount'] for x in self.ledger]
    #runs through amounts and descriptions lists
    #29 characters  = 30 max + 1 ' '
    #max 23 and max 7 characters are given in the task
    #a_list is sometimes an int, sometimes a float, format makes it a string with extra decimals
    for i in range(len(d_list)) :
      budget_category = budget_category + '\n' + d_list[i][:23] + ' ' + '{:.2f}'.format(a_list[i])[:7].rjust(29-len(d_list[i]))
    budget_category = budget_category + '\n' + 'Total: ' + '{:.2f}'.format(self.get_balance())
    return budget_category

  def deposit(self, d_amount, description= '') :
    #ledger is a list that's filled with 2 item dictionraries
    self.ledger.append({'amount': d_amount, 'description': description})

  def get_balance(self) :
    #makes a list of all values (in ledger list) attatched to "amount" key and then sums them
    balance = sum([x['amount'] for x in self.ledger])
    return balance
  
  def check_funds(self, c_amount) :
    if c_amount > self.get_balance() :
      return False
    if c_amount <= self.get_balance() :
      return True

  def withdraw(self, w_amount, description = '') :
    if self.check_funds(w_amount) :
      self.ledger.append({'amount': -w_amount, 'description': description})
      return True
    else :
      return False
  
  def transfer(self, t_amount, other) :
    if self.check_funds(t_amount) :
      self.withdraw(t_amount, 'Transfer to {}'.format(other.category))
      other.deposit(t_amount, 'Transfer from {}'.format(self.category))
      return True
    else :
      return False

  
def create_spend_chart(categories):

  spent_result = 'Percentage spent by category\n'
  w_totals = []
  w_percentages = []
  percentages = list(range(100,-1,-10))
  cat_names = []

  for i in range(len(categories)) :
    cat_names.append(categories[i].category)

  #why does this equal to 76.0399999.. instead of 76.04 with sum()? Floating-point arithmetic 
  for i in range(len(categories)) :
    w_totals.append(fsum(x['amount'] for x in categories[i].ledger if x['amount']<0))

  #floor is used intstead of round, because it's needed to be rounded down
  #floor only takes one argument, so first I round it down to decimals, then multiply by 10 to get a rounded down percentege
  for i in range(len(w_totals)):
    w_percentages.append((floor(w_totals[i]/sum(w_totals)*10)*10))
  
  for i in range(len(percentages)) :
    #string formatter, {} is where the variable will be pasted, :3 specifies how many spaces it's supposed to tak
    #it by default starts at 0 and fills the empty spaces with whitespace
    spent_result += '{:3}|'.format(percentages[i])
    for n in range(len(w_percentages)) :
      if w_percentages[n] >= percentages[i] -5:
        spent_result += ' o '
      else :
        spent_result += '   '
    spent_result += ' \n'

  spent_result += ' '*4 + '-'*10
  
  #key=len specifies the built in len() function
  #max(cat_names, key=len) returns Clothing string (the longest in the list)
  for i in range(len(max(cat_names, key=len))) :
    spent_result += '\n' + ' '*5
    for n in range(len(cat_names)):
      if len(cat_names[n]) > i :
        spent_result += cat_names[n][i] + '  '
      else :
        spent_result += '   '

  return spent_result