import json
base_datos = [
  "Nombre,Apellido,Edad",
  "Emiliano Alejandro,Billi,43",
  "Peter,Fonda,102",
  "Mirtha,Legrand,98",
  "Cesar,Billi,11"
  ]

keys = base_datos[0].split(",")

dict_db = []
i = 1
while i < len(base_datos):
  values = base_datos[i]
  values = values.split(",")
  d = {keys[0] : values[0],
       keys[1] : values[1],
       keys[2] : values[2]
       }
  print(d)
  dict_db.append(d)
  d
  i = i + 1
print(dict_db)
json_db = json.dumps(dict_db)
