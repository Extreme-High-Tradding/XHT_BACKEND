from channels import Group
from channels.sessions import channel_session
from .models import Room
import json
import re
from models import Transactions


@channel_session
def ws_connect(message):
    prefix= 'testroom'
    label = 'testroom'
    room = Room.objects.get(label='testroom')
    Group('chat-' + label).add(message.reply_channel)
    message.channel_session['room'] = 'testroom'

@channel_session
def ws_receive(message):
    label = 'testroom'
    room = Room.objects.get(label='testroom')
    data = json.loads(message['text'])
    #here goes code 1
    m = Transactions.objects.create(user_id = data['user'],
                                    opening_price = data['price'], 
                                    closing_price = data['price'],
                                    asset_id = data['asset'], 
                                    amount_assets = data['amount'],
                                    operation_type = data['operation_type'], # Compra y Venta
                                    operation_status = data['operation_status']) # Activo - cerrada
    # till here code 1
    Group('chat-'+label).send({'text': json.dumps(m.content)})
    
    """                                    
    #Classifying transaction
    if m.operation_type == False:
        Transactions.object.create(user_id = m.user_id, opening_price = m.opening_price,
                                    amount_assets = m.amount_assets,
                                    asset_id = m.asset_id)
        #Modify users balance
        user_balance = Financial.objects.get(user_id = m.user_id)
        #try:look for error type and aply try catch function
        if user_balance.asset_id == 'tesla':
            user_balance.active1_amount += m.amount_assets
            user_balance.balance -= m.opening_price

        elif user_balance.asset_id == 'petroleo':
            user_balance.active2_amount += m.amount_assets
            user_balance.balance -= m.opening_price
        
        elif user_balance.asset_id == 'bitcoin':
            user_balance.active3_amount += m.amount_assets
            user_balance.balance -= m.opening_price
        #Catch: look for error type and aply try catch function
        """
    # #code 1 {
    # if data['operation_type']== False:
    #     Transactions.object.create(user_id = data['user'],
    #                                 opening_price = data['price'],
    #                                 amount_assets = data['amount'],
    #                                 asset_id = data['asset'])
    #     #Modify users balance
    #     user_balance = Financial.objects.get(user_id = data['user'])
    #     #try:look for error type and aply try catch function
    #     if user_balance.asset_id == 'tesla':
    #         user_balance.active1_amount += data['amount']
    #         user_balance.balance -= data['price']

    #     elif user_balance.asset_id == 'petroleo':
    #         user_balance.active2_amount += data['amount']
    #         user_balance.balance -= data['price']
        
    #     elif user_balance.asset_id == 'bitcoin':
    #         user_balance.active3_amount += data['amount']
    #         user_balance.balance -= data['price']
    #     #Catch: look for error type and aply try catch function 
    # #code 1   }



@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)



#Additional functions
def average(asset_id):
    list_asset = Transactions.objects.filter(asset_id = asset_id,
                                            operation_status = True,
                                            operation_type = False)


