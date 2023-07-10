from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE, ImageField, PositiveIntegerField, DateField, PROTECT, BooleanField  
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

class ModeloProducto(Model):
    nombre = CharField(max_length=30, null=False, unique=True)
    precio = IntegerField(validators=[MinValueValidator(200000),  MaxValueValidator(1000000)], null= False )
    cantidad = IntegerField(validators=[MinValueValidator(1),  MaxValueValidator(30)], null= True )
    foto = ImageField(upload_to= 'productos', null = True)
    usuario = ForeignKey(User, on_delete = CASCADE )

class Boleta(Model):
    fecha_venta = DateField(auto_now = True)
    total = PositiveIntegerField(default = 0)
    usuario = ForeignKey(User
     , on_delete = CASCADE)
    estado = BooleanField()


class Detalle_boleta(Model):
    cantidad = IntegerField()
    precio = IntegerField()
    boleta = ForeignKey(Boleta, on_delete= PROTECT)
    producto = ForeignKey(ModeloProducto, on_delete=PROTECT )
