def categorize_age(age):
    if age < 0:
        return "Invalid age. Age cannot be negative."
    elif age <= 1:
        return  "Baby"
    elif age <= 3:
        return  "Toddler"
    elif age <= 5:
        return  "Pre-school" 
    elif age <= 12:
        return  "Child" 
    elif age <= 17:
        return  "Teenager" 
    elif age <= 21:
        return  "Young Adult" 
    elif age <= 30:
        return  "Pre-adult" 
    elif age <= 50:
        return  "Adult"
    elif age <= 70:
        return  "Pre-elderly"
    else:
        return "Elderly"
        
try:
    age_input = int(input("Enter your age: ")) 
    
    category = categorize_age(age_input)
    print("Category:", category)
except ValueError:
    print("Please enter a valid integer for age.")
