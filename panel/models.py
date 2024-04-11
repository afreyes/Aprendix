from django.db import models
        
        
class Cursos(models.Model):
    
    idcurso = models.IntegerField(primary_key=True)
    nombre = models.CharField (max_length=30, null= False)
    descripcion = models.CharField(max_length=20, null=False)
    duracion = models.IntegerField()
    creditos = models.CharField (max_length=30, null= False)
    class Meta:
        
        db_table ='cursos'