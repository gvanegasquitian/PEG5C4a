from modelos.Candidato import Candidato
class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")
    def index(self):
        print("Listar todos los candidatos")
        cnt={
            "numeroResolucion":"R-0123456789",
            "cedula":"R-0123456789",
            "nombre":"Giovani",
            "apellido":"Vanegas Quitian",
            "partido":"Liberal"
        }
        return [cnt]
    def create(self,infoCandidato):
        print("Crear un candidato")
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__
    def show(self,id):
        print("Mostrando un candidato con id ",id)
        elCandidato = {
            "numeroResolucion": id,
            "cedula":"123456789",
            "nombre":"Giovani",
            "apellido":"Vanegas Quitian",
            "partido":"Liberal"
        }
        return elCandidato
    def update(self,id,infoCandidato):
        print("Actualizando candidato con id ",id)
        elCandidato = Candidato(infoCandidato)
        return elCandidato.__dict__
    def delete(self,id):
        print("Elimiando candidato con id ",id)
        return {"deleted_count":1}