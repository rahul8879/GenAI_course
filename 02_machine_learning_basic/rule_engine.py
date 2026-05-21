def predict(cibil_score, income):
    if cibil_score > 700 and income > 30000:
        return "Approved"
    else:
        return "Rejected"

cibil_score = int(input("Enter the CIBIL score: "))
income = int(input("Enter the income: "))
print(predict(cibil_score, income))
