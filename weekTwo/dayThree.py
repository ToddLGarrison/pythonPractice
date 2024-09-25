def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("todd", "GARRison")

print(formatted_name)

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))
