from django.shortcuts import render
from .models import Cliente, Productos

def index(request):
    clientes = Cliente.objects.all()  # Cambia el nombre de la variable
    context = {"clientes": clientes}  # Utiliza un nombre diferente para el contexto
    return render(request, 'Atienda/index.html', context)

def crud(request):
    clientes = Cliente.objects.all()  # Corrección: objects en lugar de objets
    context = {"clientes": clientes}  # Corrección: nombre del contexto en minúscula
    return render(request, 'Atienda/clientes_list.html', context) 

def listadoSQL(request):
    clientes= Cliente.objects.raw('SELECT * FROM Atienda_Cliente')
    print(clientes)
    context = {"clientes": clientes}
    return render(request, 'Atienda/listadoSQL.html', context)

def ClientesAdd(request):
    if request.method is not "POST":
        clientes = Cliente.objects.all()  
        context = {"clientes": clientes}  
        return render(request, 'Atienda/clientes_list.html', context)
    
    else:
        rut=request.POST['rut']
        nombre=request.POST['nombre']
        apellidos=request.POST['apellidos']
        correo=request.POST['correo']
        celular=request.POST['celular']

        obj=Cliente.objects.create(rut=rut, 
                                   nombre=nombre, 
                                   apellidos=apellidos, 
                                   correo=correo, 
                                   celular=celular)
        obj.save()
        context={'mensaje':"Ok, datos grabados...."}
        return render(request, 'Atienda/clientes_add.html', context)
    
def clientes_del(request, pk):
    context = {}
    try:
        cliente=Cliente.objects.get(rut=pk)

        cliente.delete()
        mensaje= "Cliente eliminado"
        clientes = Cliente.objects.all()
        context = {"clientes": clientes, "mensaje": mensaje}
        return render(request, 'Atienda/clientes_list.html', context)
    except:
        mensaje= "Cliente no encontrado"
        clientes = Cliente.objects.all()
        context = {"clientes": clientes, "mensaje": mensaje}
        return render(request, 'Atienda/clientes_list.html', context)
    
# def clientesUpdate(request):
#     if request.method == "POST":
#         rut=request.POST["rut"]
#         nombre=request.POST["nombre"]
#         apellidos=request.POST["apellidos"]
#         correo=request.POST["correo"]
#         celular=request.POST["celular"]
        
#         objCliente = objCliente.objects.get(rut = rut)

#         Cliente.rut=rut
#         Cliente.nombre=nombre
#         Cliente.apellidos=apellidos
#         Cliente.correo=correo
#         Cliente.celular=celular
#         Cliente.save()
#         context = {"mensaje": "Cliente actualizado",'cliente':Cliente}
#         return render(request, 'Atienda/clientes_edit.html', context)
    
#     else:
#         Cliente = Cliente.objects.all()
#         context = {"cliente": Cliente}
#         return render(request, 'Atienda/clientes_edit.html', context)

def clientesUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        apellidos = request.POST["apellidos"]
        correo = request.POST["correo"]
        celular = request.POST["celular"]
        
        try:
            cliente = Cliente.objects.get(rut=rut)
            cliente.nombre = nombre
            cliente.apellidos = apellidos
            cliente.correo = correo
            cliente.celular = celular
            cliente.save()
            context = {"mensaje": "Cliente actualizado", 'cliente': cliente}
            return render(request, 'Atienda/clientes_edit.html', context)
        except Cliente.DoesNotExist:
            mensaje = "Cliente no encontrado"
            clientes = Cliente.objects.all()
            context = {"clientes": clientes, "mensaje": mensaje}
            return render(request, 'Atienda/clientes_list.html', context)
    
    else:
        clientes = Cliente.objects.all()
        context = {"clientes": clientes}
        return render(request, 'Atienda/clientes_edit.html', context)
    
def clientes_findEdit(request, pk):
    if pk != "":
        cliente=Cliente.objects.get(rut=pk)

        context = {"cliente": cliente}
        if cliente:
            return render(request, 'Atienda/clientes_edit.html', context)
        else:
            context = {"mensaje": "Cliente no encontrado"}
            return render(request, 'Atienda/clientes_edit.html', context)
        
def main(request):
    return render(request, 'Atienda/main.html')

def contacto(request):
     return render(request, 'Atienda/contacto.html')

def productos(request):
    objplant = Productos.objects.filter(id_tipo=1)
    macetero = Productos.objects.filter(id_tipo=2)
    tierra = Productos.objects.filter(id_tipo=3)
    decoraciones = Productos.objects.filter(id_tipo=4)
    context = {'objplant' : objplant, 'macetero' : macetero, 'tierra' : tierra, 'decoraciones' : decoraciones}
    return render(request, 'Atienda/productos.html', context)




