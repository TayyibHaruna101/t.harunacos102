girls_name = ["Evelyn", "Jessics", "Somto", "Edith", "Liza", "Mandonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_age = ["17", "16", "17", "18", "16", "18", "17", "20", "19", "17"]
girls_height = ["5.5", "6.0", "5.4", "5.9", "5.6", "5.5", "6.1", "6.0", "5.7", "5.5"]
girls_scores = ["80", "85", "70", "60", "76", "66", "87", "95", "50", "49"]

boys_name = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Weslesy"]
boys_age = ["19", "16", "18", "17", "20", "19", "16", "18", "17", "19"]
boys_height = ["5.7", "5.9", "5.8", "6.1", "5.9", "5.5", "6.1", "5.4", "5.8", "5.7"]
boys_scores = ["74", "87", "75", "68", "66", "78", "87", "98", "54", "60"]

print("                          GIRL'S LIST")
print("NAME        |AGE         |HEIGHT         |SCORE")

for i in range(10):
    print(f"{girls_name[i]}           |{girls_age[i]}               |{girls_height[i]}                    |{girls_scores[i]}")

print("                          BOY'S LIST")
print("NAME        |AGE         |HEIGHT         |SCORE")

for i in range(10):
  print(f"{boys_name[i]}           |{boys_age[i]}               |{boys_height[i]}                    |{boys_scores[i]}")