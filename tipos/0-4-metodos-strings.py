animal = "  vaca loca es muy feliz  "
print(animal.upper())  # Poner mayus
print(animal.lower())  # Poner minuscula
print(animal.capitalize())  # Coloca a la primera en mayus
print(animal.title())  # Coloca a la primera letra de cada palabra en mayus
print(animal.strip())  # Remover todos los espacios de la drecha e izquda
# Elimina los espacios y pone la primera letra de cada palabra en mayus
print(animal.strip().capitalize())
print(animal.lstrip())  # Sacar los espacios de la izquierda
print(animal.rstrip())  # Sacar los espacios de la derecha
# Encuentra en una cadena de caracteres y nos devuelve el indice
print(animal.find("va"))
# Remplaza una cadena de caracteres por otros
print(animal.replace("vaca", "toro").replace("a", "o"))
# Da un boolean sobre SI SE encuentra en una cadena de caracteres
print("aca" in animal)
print("aca" not in animal)  # Para saber si NO SE ENCUENTRA
