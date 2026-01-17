print("PASSWORD STRENGTH CHECKER")

username = input("Enter your username: ")
password = input("Enter your password: ")



def check(username,password):
    #initialize the variable
    score = 0
    #listing the characters
    special = "!@#$%^&*"


    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in special for ch in password)

   
    if has_upper:
        score += 1
    else:
        score -= 1
  
    if has_lower:
        score += 1
    else:
        score -= 1
    
    if has_digit:
        score += 1
    else:
        score -= 1
   
    if has_special:
        score += 1
    else:
        score -= 1
  

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        score -= 2

    d = {}
    for i in password:
        if password.count(i)>1:
            d[i] = password.count(i)
    score -= len(d)
    if len(d) == 0:
        score += 2
    
    
    if username.lower() in password.lower():
        score -= 2

    messages = []
    if len(d) != 0:
        messages.append("Your password has repeated characters. Please try not to use them more than once")
        messages.append(d)
    if username.lower() in password.lower():
        messages.append("Your password includes the username. Please remove the username from your password")
    if len(password)<8:
        messages.append("Your password length is small. Please increase your password length")
    if not has_upper:
        messages.append("❌ Password must contain at least one uppercase letter")

    if not has_lower:
        messages.append("❌ Password must contain at least one lowercase letter")

    if not has_digit:
        messages.append("❌ Password must contain at least one digit")

    if not has_special:
        messages.append("❌ Password must contain at least one special character")
        
    for msg in messages:
        print(msg)

    print(f"\nYour password strength score is {score}")
    if score <= 2:
        print("Strength: Very Weak ❌")
    elif score <= 4:
        print("Strength: Weak ⚠️")
    elif score <= 6:
        print("Strength: Medium 🟡")
    else:
        print("Strength: Strong ✅")


check(username,password)
