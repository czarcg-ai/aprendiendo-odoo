class Alumno:
    def __init__ (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        self.estado = "Cursando"

    def calificar(self):
        if self.nota >= 11:
            self.estado = "Aprobado"

        else:
            self.estado = "Reprobado"
        print(f"El alumno {self.nombre} ha sido calificado como: {self.estado}")


lista_alumnos = []

alumno1 = Alumno("Cesar", 15)
alumno2 = Alumno("Robert", 20)
alumno3 = Alumno("Vero", 5)

lista_alumnos.append(alumno1)
lista_alumnos.append(alumno2)
lista_alumnos.append(alumno3)

print ("--- INICIAMOS SISTEMA DE CALIFICACION---")

for estudiante in lista_alumnos:
    estudiante.calificar()
