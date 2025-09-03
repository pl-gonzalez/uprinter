print("O programa verifica se seus batimentos cardiacos por minuto (BPM) esta na faixa adequada, com base na sua idade e nos BPM medidos")

bpm = int(input("Insira o valro do BPM: \n"))
idade = int(input("Insira sua idade: \n"))

if (idade <= 2):
    if(bpm < 120):
        print("BPM ABAIXO da faixa adequada")
    
    elif (bpm < 140):
        print("BPM ACIMA da faixa adequada")

    else:
        print("BPM na faixa adequada")

elif (idade >= 8 and idade <= 17):
    if(bpm < 80):
        print("BPM ABAIXO da faixa adequada")

    elif(bpm > 100):
        print("BPM ACIMA da faixa adequada")

    else:
        print("BPM na faixa adequada")

elif ( idade > 17 and idade < 60):
    if(bpm < 70):
        print("BPM ABAIXO da faixa adequada")

    elif(bpm > 80):
        print("BPM ACIMA da faixa adequada")
        
    else:
        print("BPM na faixa adequada")

elif( idade >= 60):
    if(bpm<50):
        print("BPM ABAIXO da faixa adequada")

    elif(bpm>60):
        print("BPM ACIMA da faixa adequada")

    else:
        print("BPM na faixa adequada")

