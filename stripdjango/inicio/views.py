from django.shortcuts import render
from django.http import JsonResponse
import stripe
import json
stripe_pub="pk_test_4kooNToaA9bwzqJOGXowMPtN00jkhDC5Sm"
stripe_private="sk_test_rI3V9src2mqi8u2QuJxsJX4Q003OF64DIJ"
stripe.api_key=stripe_private

# levantar el formulario de strike


def home(request):
    return render (request, "home.html",{"key":stripe_pub})

# este es el primer checkout que se debe mostrar para que
# devuelva todos los datos de la carga- CHARGE

def checkout(request):
    amount= 90000
    #Autenticacion del Cliente
    customer = stripe.Customer.create(
        email = request.POST['stripeEmail'],
        source = request.POST['stripeToken']
    )
    
    charge =stripe.Charge.create(
        customer = customer.id,
        amount = amount,
        currency = 'aud',
        description = "Venta de prueba en el full day codiGO"   
    )
    print("status",charge)
    # return render(request,'exito.html')
    return JsonResponse(charge)






