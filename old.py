def calculate_age(year_of_birth, current_year): 
        age = (current_year - year_of_birth)
        if age >= 2:
              return  f"You are {age} years old."
        elif age == 1:
            return f"You are {age} year old."
        elif age <= -2:
            a = abs(age)
            return f"You will be born in {a} years."
        elif age == -1:
            a = abs(age)
            return f"You will be born in {a} year."
        else:
            return f"You were born this very year!"