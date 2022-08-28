def arithmetic_arranger(problems, solution = False) :

  if len(problems )> 5 :
    return "Error: Too many problems."

  top = ""
  bottom = ""
  lines = ""
  results = ""
  arranged_problems = ""

  for problem in range(0,len(problems)) :
    
    topnum = problems[problem].split()[0]
    operator = problems[problem].split()[1]
    botnum = problems[problem].split()[2]

    if operator != "+" and operator != "-" :
      return "Error: Operator must be '+' or '-'."  
    if topnum.isdigit() == False or botnum.isdigit() == False:
      return "Error: Numbers must only contain digits."  
    if len(topnum) > 4 or len(botnum) > 4 :
      return "Error: Numbers cannot be more than four digits."

    max_len = max(len(topnum), len(botnum))
    line_len = max_len + 2

    line = '-'*line_len
    topline = topnum.rjust(line_len,' ')
    botline = operator+botnum.rjust(line_len-1,' ')
    

    #makes sure there is no extra spaces after the last problem
    if problem < len(problems)-1 :
      top = top + topline + '    '
      bottom = bottom + botline + '    '
      lines = lines + line + '    '
    else :
      top = top + topline
      bottom = bottom + botline
      lines = lines + line

    #only looks at solution when asked
    if solution :
      result = str(eval(problems[problem]))
      resultline = result.rjust(line_len,' ')
      if problem < len(problems)-1 :
        results = results + resultline + '    '
      else :
        results = results + resultline    
    
  arranged_problems = top + '\n' + bottom + '\n' + lines
    
  if solution : 
     arranged_problems = arranged_problems + '\n' + results

  return arranged_problems