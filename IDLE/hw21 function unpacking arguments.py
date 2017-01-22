def Health_calculator(age,apple_ate,cigs_smoke):
    answer=(100-age)+3*apple_ate-2*cigs_smoke
    print(answer)

kia_data=[24,10,0]
Health_calculator(kia_data[0],kia_data[1],kia_data[2])
Health_calculator(*kia_data)
