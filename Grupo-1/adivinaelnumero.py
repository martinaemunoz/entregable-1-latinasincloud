import random
secret_num = random.randint(1,100)
intento = none

print("adivina el numero entre 1 y 100")
while intento != secret_num:
    intento = int(input("tu intento: "))
    if intento < secret_num:
        print("mas alto")
    elif intento > secret_num:
        print("mas bajo")
    else:
        print("¡correctooo! el número secreto es", secret_num)
