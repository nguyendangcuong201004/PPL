a,b,c=0,1,4
def sub2(b,c,f):
  return (f(c)-f(b))*2
def sub1(a):
  def sub3(b):
    return b*c+a
  global b
  b=sub2(1,2,sub3)  
sub1(3)
print(b)