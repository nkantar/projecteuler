#/usr/bin/ruby

def is_prime(number)
  divisor = 2 
  root = Math.sqrt(number).to_i
  while divisor <= root do
    if number % divisor == 0
      return false
    end 
    divisor += 1
  end 
  return true
end
