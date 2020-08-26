import sys

f = open(sys.argv[1], 'r')
contents = f.read()
data = contents.split("\n")
print(data)

def read_input(data):
  for s in data:
      literals = s.split()
      for lit in literals:
          sign = (lit[0] != '-')
          variable = lit.strip('-')
  return variable
def propagate(variable):
    for h in variable:
        clause = h.split.strip('-')
    return clause
    
def pure_elim(variable):
    for a in variable:
      if (a != F):
          new_clause = a.strip('-')
          variable.append(new_clause)
    return variable
    
def solve(variable):
    new_var = propagate(variable)
    solution = pure_elim(variable)
    if (solution = False):
       print ("Not Satisfied")
    else:
      print ("Satisfied")
      print(solution)

solve(data)
        
                