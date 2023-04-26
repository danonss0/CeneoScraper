import  os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")

opinions_count = len(opinions.index)
pros_count = sum([False if len(p)==0 else True for p in opinions.pros])
cons_count = sum([False if len(c)==0 else True for c in opinions.cons])
opinions.score = opinions.score.map(lambda x: float(x.split("/")[0].replace(",",".")))
avg_score = opinions.score.mean()
print(f"Dla produktu o kodzie {product_code} dostępnych jest {opinions_count} opinii. Dla {pros_count} opinii dostępna jest lista zalet, a dla {cons_count} dostępna jest liczba wad. Średnia ocena produktu to {round(avg_score, 2)}.")

#Histogram
score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
score.plot.bar(color="hotpink")
plt.xticks(rotation=0)
plt.title("Histogram ocen")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
for index, value in enumerate(score):
    plt.text(index, value+0.5, str(value), ha="center")

#plt.show()
try:
    os.mkdir("./plots")
except FileExistsError:
    pass
plt.savefig(f"./plots/{product_code}_score.png")
plt.close()
#Udzial poszczególnych rekomendacji
recomendation = opinions["recomendation"].value_counts(dropna= False).sort_index()
print(recomendation)
recomendation.plot.pie(
    label="", 
    autopct="%1.1f%%",
    labels = ["Nie polecam", "Polecam", "Nie mam zdania"],
    colors = ["crimson","forestgreen","gray"]
    )


plt.legend(bbox_to_anchor=(0.9,1.0))
plt.savefig(f"./plots/{product_code}_recommendation.png")
plt.close()