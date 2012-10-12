#/usr/bin/ruby

def go_deeper(total=0, var1=1, var2=2)
  if var2.modulo(2) == 0
    total = total + var2
  end
  temp = var2
  var2 = var1 + var2
  var1 = temp
  if var2 < 4000000
    go_deeper(total, var1, var2)
  else
    print total
  end
end

go_deeper
