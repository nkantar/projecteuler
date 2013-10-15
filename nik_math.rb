#/usr/bin/ruby

def is_prime(number)

  ############
  # exceptions

  # negative, 0, 1 even
  if number < 2 || (number % 2 == 0 && number != 2)
    return false
  end

  # 2
  if number == 2
    return true
  end


  ###########
  # iteration

  divisor = 3
  root = Math.sqrt(number).to_i

  while divisor <= root do
    if number % divisor == 0
      return false
    end 
    divisor += 2
  end 
  return true
end
