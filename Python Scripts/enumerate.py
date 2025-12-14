def enumerator (num):

    units = ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
    altTens = ["", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
    tens = ["", "ده", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
    hundreds = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]
    scales = ["", "هزار", "میلیون", "میلیارد", "تریلیون", "کوادریلیون"]

    answer = []
    finalString = ""

    def thousends (n1000, n): #Calculating the string for each three digits
        if n1000 > 100:
            h = n1000 // 100
            n1000 %= 100

            t = n1000 // 10
            n1000 %= 10

            u = n1000
            
            if t == 1 and u != 0:
                return f"{hundreds[h]} و {altTens[u]} {scales[n]}"    
            return f"{hundreds[h]} و {tens[t]} و {units[u]} {scales[n]}"
        
        elif n1000 > 10:
            t = n1000 // 10
            n1000 %= 10

            u = n1000
            if t == 1 and u != 0:
                return f"{altTens[u]} {scales[n]}"    
            return f"{tens[t]} و {units[u]} {scales[n]} "
        
        else:
            return f"{units[n1000]} {scales[n]}"
    
    for n in range(len(str(num)) // 3 + 1):
        if num % 1000 != 0:
            answer.insert(0, thousends(num % 1000, n))
        num //= 1000
    

    for i in answer: #Creating the final string
        finalString += i
        if i != answer[-1]: finalString += " و " 

    return finalString

number = int(input())
print(enumerator(number))
