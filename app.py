from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import json


file_loader = FileSystemLoader("./template")

env = Environment(loader=file_loader)

template = env.get_template("index.html")

date_now = datetime.now().date()

# Lecture du fichier de données json
with open("template/data_cv.json", "r") as f:
    data_cv = json.load(f)
    
data_infos_personne = {
    "entreprise" : "Inetum",
    "Nom_Prenom" : "Ngoye Koumba ted",
    "Poste" : "Data ingenieur",
}

render_cv = template.render(
    nom = data_cv[0]["nom"],
    prenom = data_cv[0]["prenom"],
    poste = data_cv[0]["poste"],
    formations = data_cv[0]["formations"],
    experience_pro = data_cv[0]["experiences_professionnelles"], 
    competences_techniques = data_cv[0]["competences_techniques"],
    current_year = date_now
)

print(render_cv)

f = open("build/index.html", "w")
f.write(render_cv)
f.close()

