import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render, redirect
from django.contrib import messages
import json
import os  # 👈 Para leer variables de entorno

def index(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        fecha = request.POST.get('fecha')
        cajera = request.POST.get('cajera')
        remision = request.POST.get('remision')
        factura = request.POST.get('factura')
        efectivo = request.POST.get('efectivo')
        tarjeta = request.POST.get('tarjeta')
        anulada = request.POST.get('anulada')
        ch_posfechado = request.POST.get('ch_posfechado')
        saldo_a_favor = request.POST.get('saldo_a_favor')
        pago_qr = request.POST.get('pago_qr')
        observaciones = request.POST.get('observaciones')

        # Conectar con Google Sheets usando credenciales desde variables de entorno
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"
        ]

        # 👉 Leer las credenciales desde una variable de entorno
        credentials_json = os.environ.get("GOOGLE_CREDENTIALS")
        creds_dict = json.loads(credentials_json)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)

        # Abrir hoja y pestaña
        sheet = client.open("pagos-django-html").sheet1  # o .worksheet("Nombre de pestaña")

        # Insertar datos en la fila 2 (debajo del encabezado)
        sheet.insert_row([
            fecha, cajera, remision, factura, efectivo, tarjeta, anulada,
            ch_posfechado, saldo_a_favor, pago_qr, observaciones
        ], index=2)

        messages.success(request, "✅ Pago registrado correctamente.")
        return redirect('index')

    return render(request, 'payment_register/index.html')
