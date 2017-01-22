def get_gender(sex="unknown"):
    if sex==('M'):
        sex="Male"
    if sex==('F'):
        sex="Female"
    print(sex)

get_gender('M')
get_gender('F')
get_gender()
