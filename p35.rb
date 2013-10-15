#/usr/bin/ruby

require "./nik_math.rb"

max = 100
max = 1000
max = 1000000

number = 3
count = 1

def is_circular(number)
    # split digits
    digits = number.to_s.split("")

    # iterate through all permutations
    digits.length.times do |digit|
        digits = digits.push(digits[0])
        digits = digits.drop(1)
        if !is_prime(digits.join("").to_i)
            return false
        end
    end

    return true
end

while number < max
    if is_prime(number)
        if is_circular(number)
            puts number
            count += 1
        end
    end
    number += 2
end

puts "-----"
puts "Count: " + count.to_s
puts "Max: " + max.to_s
puts "-----"
