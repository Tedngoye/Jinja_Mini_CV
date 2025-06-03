from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader("./template")

env = Environment(loader=file_loader)

template = env.get_template("index.html")

data_entete_cv = {
    "entreprise" : "Inetum",
    "Nom_Prenom" : "Ngoye Koumba ted",
    "Poste" : "Data ingenieur"
}

html = template.render(
    entete_cv = data_entete_cv
)

print(html)

f = open("build/index.html", "w")
f.write(html)
f.close()

