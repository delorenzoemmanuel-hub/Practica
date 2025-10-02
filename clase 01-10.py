import json
base_datos = [
    "Nombre,Apellido,Edad,Nacionalidad,estado_civil",
    "Emiliano Alejandro,Billi,43,Argentino,Casado",
    "Peter,Fonda,102",
    "Mirtha,Legrand,98",
    "Cesar,Billi,11",
    "Emmanuel,Delorenzo,36",
    "pepe,pepito,88",
    "pepe,argento,54"
]

keys = base_datos[0].split(",")

dict_db = []
i = 1
while i < len(base_datos):
  values = base_datos[i]
  values = values.split(",")
  d = {
    keys[0] : values[0],
    keys[1] : values[1],
    keys[2] : values[2]
  }
  print(d)
  dict_db.append(d)
  i = i + 1
print(dict_db)
json_db = json.dumps(dict_db)