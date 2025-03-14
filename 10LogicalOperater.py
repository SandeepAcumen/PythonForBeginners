# input(hightincome) = 100000
# input(heightcredit) =7

# if hightincome:
#     print("elegible for loan ")

# elif heightcredit:
#     print("elegible for loan")

# else:
#     print("No Loan")

hightincome =True
heightcredit =True
if hightincome and heightcredit:
    print("Good to gooo")

hight_income =True
height_credit =False
if hight_income and height_credit:
    print("good")
else:
    print("BAddddd")

hight_income =True
height_credit =False
if hight_income or height_credit:
    print("good")
else:
    print("BAddddd")

has_good_credit =True
has_no_criminal =False

if has_good_credit and not has_no_criminal:
    print("Eligible for loan")