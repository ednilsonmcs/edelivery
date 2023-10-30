from django.http import JsonResponse
import telebot

bot = telebot.TeleBot('6634073252:AAGjoyIB4atiANZKOrmhauQKYWCkTeeo0f4')


def sample_api(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', None)
        endereco = request.POST.get('endereco', None)
        hamburguer = request.POST.get('hamburguer', None)
        acai = request.POST.get('acai', None)
        pizza = request.POST.get('pizza', None)
        refrigerante = request.POST.get('refrigerante', None)
        agua = request.POST.get('agua', None)
        suco = request.POST.get('suco', None)
        formas_pagamento = request.POST.get('formas_pagamento', None)


        message = ''  

        if nome is not None:
            message = message + "Cliente: " + nome + "\n"
        if endereco is not None:
            message = message + "Endereço de entrega: " + endereco 
        
        message = message + "\n Itens:"

        if hamburguer is not None and hamburguer == "on":
            message = message + "\n -  Hamburguer"
        if acai is not None and acai == "on":
            message = message + "\n -  Açai"
        if pizza is not None and pizza == "on":
            message = message + "\n -  Pizza"
        if refrigerante is not None and refrigerante == "on":
            message = message + "\n -  Refrigerante"
        if agua is not None and agua == "on":
            message = message + "\n -  Água"
        if suco is not None and suco == "on":
            message = message + "\n -  Suco"
        if formas_pagamento is not None:
            message = message + "\n Forma de pagamento: " + formas_pagamento

        data = {
            'message': 'Pedido registrado: ' + message.replace("\n", "; "),
            'status': 'success'
        }
        
        chat_id = '6411110438'
              
        # Enviar a mensagem usando o bot
        bot.send_message(chat_id, message)

        return JsonResponse(data)
    else:
        data = {
            'message': 'Método não permitido',
            'status': 'error'
        }
        return JsonResponse(data, status=405)
