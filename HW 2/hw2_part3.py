def reverse(number):
    hundreds = number/100
    tens = (number%100)/10
    ones = number%10
    reverse = ones * 100 + tens * 10 + hundreds
    return reverse

number = raw_input('Enter a value ==> ')
print number + "\n"
number = int(number)

first_answer = (reverse(number)-number)
final_answer = first_answer + reverse(first_answer)

print "Here is the computation:"
print reverse(number),"-",number,"=", first_answer
print first_answer,"+", reverse(first_answer), "=", final_answer

if final_answer == 1089:
    print "You see, I told you."
else:
    print "Are you sure your input is valid?"





