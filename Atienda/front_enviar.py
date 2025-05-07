from django.shortcuts import render
import requests

def webpay_form_view(request):
  if request.method == "POST":
    buy_order = request.POST.get("buy_order")
    session_id = request.POST.get("session_id")
    amount = request.POST.get("amount")
    return_url = request.build_absolute_uri("/webpay/retorno/")

    # Llamada a tu API interna
    response = requests.post("http://localhost:8000/api/webpay/iniciar/", json={
      "buy_order": buy_order,
      "session_id": session_id,
      "amount": amount,
      "return_url": return_url
    })

    if response.status_code == 200:
      data = response.json()
      # Redirige al formulario de Webpay con token
      return render(request, "front/verificar.html", {
        "url": data["url"],
        "token": data["token"]
      })

    return render(request, "front/form.html", {"error": "Error al iniciar transacción"})

  return render(request, "front/form.html")
