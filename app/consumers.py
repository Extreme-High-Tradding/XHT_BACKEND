from channels import Group
from channels.sessions import channel_session
from .models import Room
import json
import re
from .models import Transactions,Financial
from django.contrib.auth.models import User
from django.core import serializers
from decimal import *



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


    user_balance = Financial.objects.get(user_id_id=int(data['user_id']))# produccion get(user_id=data[user_id])
    #if user does not have enough credit, user can not buy assets
    if(data['operation_type'] == 'False') and (user_balance.balance >= float(data['price'])):
        buy()
        transaction = serializers.serialize('json', [ m, ])
        balance = serializers.serialize('json', [ user_balance, ])
        Group('chat-'+label).send({'text': transaction })
        Group('chat-'+label).send({'text': balance })
    elif(data['operation_type']== 'True') and (data['operation_status'] == 'False'):
        opening_sell()
        transaction = serializers.serialize('json', [ m, ])
        balance = serializers.serialize('json', [ user_balance, ])
        Group('chat-'+label).send({'text': transaction })
        Group('chat-'+label).send({'text': balance })
    elif (data['operation_type']== 'True') and (data['operation_status'] == 'True'):
        closing_sell()
        transaction = serializers.serialize('json', [ open_transaction, ])
        balance = serializers.serialize('json', [ user_balance, ])
        Group('chat-'+label).send({'text': transaction })
        Group('chat-'+label).send({'text': balance })

        #creating transaction row
    # # user_striped = data['user'].strip("'")
    # #here goes code 1
    # user = Financial.objects.get_or_create(user_id_id=int(data['user_id']))

    # m = Transactions.objects.create(user_id = user[0],
    #                                 opening_price = float(data['price']), 
    #                                 closing_price = float(data['price']),
    #                                 asset_id = data['asset_id'],#1,2,3
    #                                 amount_assets = float(data['amount_assets']),
    #                                 operation_type = (data['operation_type'] != 'False'),      #data['operation_type'],  False= = 'Buy', True = 'Sell' 
    #                                 operation_status = (data['operation_status'] != 'False'))   #data['operation_status'])  False = open , True = 'close'
    # m.save()
    # # till here code 1
    # serialized_obj = serializers.serialize('json', [ m, ])
    # Group('chat-'+label).send({'text': serialized_obj })
    
                                       
# """     #Classifying transaction
#     if m.operation_type == False:
#         Transactions.object.create(user_id = m.user_id, opening_price = m.opening_price,
#                                     amount_assets = m.amount_assets,
#                                     asset_id = m.asset_id)
#         #Modify users balance
#         user_balance = Financial.objects.get(user_id = m.user_id)
#         #try:look for error type and aply try catch function
#         if user_balance.asset_id == 'tesla':
#             user_balance.active1_amount += m.amount_assets
#             user_balance.balance -= m.opening_price

#         elif user_balance.asset_id == 'petroleo':
#             user_balance.active2_amount += m.amount_assets
#             user_balance.balance -= m.opening_price
        
#         elif user_balance.asset_id == 'bitcoin':
#             user_balance.active3_amount += m.amount_assets
#             user_balance.balance -= m.opening_price
#         #Catch: look for error type and aply try catch function
#       """  
# #***************************************************************************************
# #*****************************************************************************************
# #*******************************************************************************************

#     #code 1 {
#     # Buy operation ¡¡¡¡¡¡¡¡¡¡¡¡¡¡Works 100%!!!!!!!!!!!!!!!!!!
#     user_balance = Financial.objects.get(user_id_id=int(data['user_id']))# produccion get(user_id=data[user_id])
#     #if user does not have enough credit, user can not buy assets
#     if(data['operation_type'] == 'False') and (user_balance.balance >= float(data['price'])):
#         #creating transaction row
#         m = Transactions.objects.create(user_id_id = int(data['user_id']),
#                                     opening_price = float(data['price']),#float()
#                                     amount_assets = int(data['amount_assets']),
#                                     operation_type = False,
#                                     asset_id = str(data['asset_id']))
#         m.save()
#         #Modify users balance
#         #try:look for error type and aply try catch function
#         if '1' == data['asset_id']:
#             user_balance.active1_amount += int(data['amount_assets'])
#             user_balance.balance -= Decimal(data['price'])

#         elif '2' == data['asset_id']:
#             user_balance.active2_amount += int(data['amount_assets'])
#             user_balance.balance -= Decimal(data['price'])
        
#         elif '3' == data['asset_id']:
#             user_balance.active3_amount += int(data['amount_assets'])
#             user_balance.balance -= Decimal(data['price'])

#         user_balance.save()
#         print("""         _nnnn_                      
#         dGGGGMMb     ,"""""""""""""".
#        @p~qp~~qMb    | Linux Rules! |
#        M|@||@\) M|   _;..............'
#        @,----.JM| -'
#       JS^\__/  qKL
#      dZP        qKRb
#     dZP          qKKb
#    fZP            SMMb
#    HZM            MMMM
#    FqM            MMMM
#  __| ".        |\dS"qML
#  |    `.       | `' \Zq
# _\)      \.___.,|     .'
# \____   \)MMMMMM|   .'
#      `-'       `--' hjm""")
#         print(user_balance.balance)
#         transaction = serializers.serialize('json', [ m, ])
#         balance = serializers.serialize('json', [ user_balance, ])
#         Group('chat-'+label).send({'text': transaction })
#         Group('chat-'+label).send({'text': balance })
#         #¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡works 1000%!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         #return print('User does not have enough credit or asset does not exist')#raise



#     # Sell function, open transaction
#     #if user does not have enough assets, user can not open a sell movement. with the following lines
#     #we avoid than user sell assets before of buy enough
#     elif(data['operation_type']== 'True') and (data['operation_status'] == 'False'):
#         #creating transaction row
#         amount_check = Financial.objects.get(user_id_id=int(data['user_id']))
#         if ((amount_check.active1_amount > 0 and amount_check.active1_amount >= int(data['amount_assets']))
#             or (amount_check.active2_amount > 0 and amount_check.active2_amount >= int(data['amount_assets']))
#             or (amount_check.active3_amount > 0 and amount_check.active3_amount >= int(data['amount_assets']))):
#             m = Transactions.objects.create(user_id_id = int(data['user_id']),
#                                     opening_price = float(data['price']),
#                                     amount_assets = int(data['amount_assets']),
#                                     operation_type = True,
#                                     operation_status = False,
#                                     asset_id = str(data['asset_id']))
#                   #get the transaction_id and return it with the average
#             #Returning average price
#             m.save()
#             user_balance.save()
#             print("""         _nnnn_                      
#         dGGGGMMb     ,"""""""""""""".
#        @p~qp~~qMb    | Linux Rules! |
#        M|@||@\) M|   _;..............'
#        @,----.JM| -'
#       JS^\__/  qKL
#      dZP        qKRb
#     dZP          qKKb
#    fZP            SMMb
#    HZM            MMMM
#    FqM            MMMM
#  __| ".        |\dS"qML
#  |    `.       | `' \Zq
# _\)      \.___.,|     .'
# \____   \)MMMMMM|   .'
#      `-'       `--' hjm""")
#             print(user_balance.balance)
#             print(m.id)
#             transaction = serializers.serialize('json', [ m, ])
#             balance = serializers.serialize('json', [ user_balance, ])
#             Group('chat-'+label).send({'text': transaction })
#             Group('chat-'+label).send({'text': balance })
#             #average()
#         else:
#             return print('the user does not have enough assets for transaction' )

        
#     # Sell function, closed transaction
#     elif (data['operation_type']== 'True') and (data['operation_status'] == 'True'):
#         #check for variable¡¡¡¡¡¡IMPORTANTE!!!!temporal para pruebas id=41 o 40
#         open_transaction = Transactions.objects.get(id = 45)
#         #check for variable¡¡¡¡¡¡IMPORTANT!!!!temporal para pruebas id=41 o 40
#         #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#         #check for variable ¡¡¡¡¡IMPORTANT!!!!!data['closing_price '] 
#         # I am changing this  ------> Decimal(data['closing_price']) correct
#         # for this Decimal(100) to test  
#         open_transaction.closing_price = Decimal(100)
#         #check for variable ¡¡¡¡¡IMPORTANT!!!!!data['closing_price '] 
#         # I am changing this  ------> Decimal(data['closing_price']) correct
#         # for this Decimal(100) to test
#         open_transaction.operation_status = True
#         #save()
#         #Modify users balance
#         user_balance = Financial.objects.get(user_id_id=int(data['user_id']))
#         #try:look for error type and aply try catch function
#         if '1' == open_transaction.asset_id:
#             user_balance.active1_amount -= open_transaction.amount_assets
#             user_balance.balance += Decimal(100)

#         elif '2' == open_transaction.asset_id:
#             user_balance.active2_amount -= open_transaction.amount_assets
#             user_balance.balance += Decimal(100)
        
#         elif '3' == open_transaction.asset_id:
#             user_balance.active3_amount -= open_transaction.amount_assets
#             user_balance.balance += Decimal(100)

#         open_transaction.save()
#         user_balance.save()
#         print("""         _nnnn_                      
#         dGGGGMMb     ,"""""""""""""".
#        @p~qp~~qMb    | Linux Rules! |
#        M|@||@\) M|   _;..............'
#        @,----.JM| -'
#       JS^\__/  qKL
#      dZP        qKRb
#     dZP          qKKb
#    fZP            SMMb
#    HZM            MMMM
#    FqM            MMMM
#  __| ".        |\dS"qML
#  |    `.       | `' \Zq
# _\)      \.___.,|     .'
# \____   \)MMMMMM|   .'
#      `-'       `--' hjm""")
#         print(user_balance.balance)
#         #average()
#         # en lugar de return raise
#         #raise #leyenda del error 
#         transaction = serializers.serialize('json', [ open_transaction, ])
#         balance = serializers.serialize('json', [ user_balance, ])
#         Group('chat-'+label).send({'text': transaction })
#         Group('chat-'+label).send({'text': balance })
#         #Catch: look for error type and aply try catch function 
#     # #code 1   }
# #***********************************************************************************
# #**************************************************************************************
# #***************************************************************************************

@channel_session
def ws_disconnect(message):
    label = message.channel_session['room']
    Group('chat-'+label).discard(message.reply_channel)



#Additional functions
def average(asset_id):
    list_asset = Transactions.objects.filter(asset_id = asset_id,
                                            operation_status = True,
                                            operation_type = True)


def buy():
    m = Transactions.objects.create(user_id_id = int(data['user_id']),
                                    opening_price = float(data['price']),#float()
                                    amount_assets = int(data['amount_assets']),
                                    operation_type = False,
                                    asset_id = str(data['asset_id']))
        m.save()
        #Modify users balance
        #try:look for error type and aply try catch function
        if '1' == data['asset_id']:
            user_balance.active1_amount += int(data['amount_assets'])
            user_balance.balance -= Decimal(data['price'])

        elif '2' == data['asset_id']:
            user_balance.active2_amount += int(data['amount_assets'])
            user_balance.balance -= Decimal(data['price'])
        
        elif '3' == data['asset_id']:
            user_balance.active3_amount += int(data['amount_assets'])
            user_balance.balance -= Decimal(data['price'])

        user_balance.save()
        print("""         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux Rules! |
       M|@||@\) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_\)      \.___.,|     .'
\____   \)MMMMMM|   .'
     `-'       `--' hjm""")
        print(user_balance.balance)
        transaction = serializers.serialize('json', [ m, ])
        balance = serializers.serialize('json', [ user_balance, ])
        Group('chat-'+label).send({'text': transaction })
        Group('chat-'+label).send({'text': balance })
        #¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡works 1000%!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #return print('User does not have enough credit or asset does not exist')#raise


def opening_sell():
    amount_check = Financial.objects.get(user_id_id=int(data['user_id']))
        if ((amount_check.active1_amount > 0 and amount_check.active1_amount >= int(data['amount_assets']))
            or (amount_check.active2_amount > 0 and amount_check.active2_amount >= int(data['amount_assets']))
            or (amount_check.active3_amount > 0 and amount_check.active3_amount >= int(data['amount_assets']))):
            m = Transactions.objects.create(user_id_id = int(data['user_id']),
                                    opening_price = float(data['price']),
                                    amount_assets = int(data['amount_assets']),
                                    operation_type = True,
                                    operation_status = False,
                                    asset_id = str(data['asset_id']))
                  #get the transaction_id and return it with the average
            #Returning average price
            m.save()
            user_balance.save()
            print("""         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux Rules! |
       M|@||@\) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_\)      \.___.,|     .'
\____   \)MMMMMM|   .'
     `-'       `--' hjm""")
            print(user_balance.balance)
            print(m.id)
            transaction = serializers.serialize('json', [ m, ])
            balance = serializers.serialize('json', [ user_balance, ])
            Group('chat-'+label).send({'text': transaction })
            Group('chat-'+label).send({'text': balance })
            #average()
        else:
            return print('the user does not have enough assets for transaction' )


def closing_sell():
        # Sell function, closed transaction
        #check for variable¡¡¡¡¡¡IMPORTANTE!!!!temporal para pruebas id=41 o 40
    open_transaction = Transactions.objects.get(id = 45)
        #check for variable¡¡¡¡¡¡IMPORTANT!!!!temporal para pruebas id=41 o 40
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #check for variable ¡¡¡¡¡IMPORTANT!!!!!data['closing_price '] 
        # I am changing this  ------> Decimal(data['closing_price']) correct
        # for this Decimal(100) to test  
    open_transaction.closing_price = Decimal(100)
        #check for variable ¡¡¡¡¡IMPORTANT!!!!!data['closing_price '] 
        # I am changing this  ------> Decimal(data['closing_price']) correct
        # for this Decimal(100) to test
    open_transaction.operation_status = True
        #save()
        #Modify users balance
    user_balance = Financial.objects.get(user_id_id=int(data['user_id']))
        #try:look for error type and aply try catch function
    if '1' == open_transaction.asset_id:
        user_balance.active1_amount -= open_transaction.amount_assets
        user_balance.balance += Decimal(100)

    elif '2' == open_transaction.asset_id:
        user_balance.active2_amount -= open_transaction.amount_assets
        user_balance.balance += Decimal(100)
        
    elif '3' == open_transaction.asset_id:
        user_balance.active3_amount -= open_transaction.amount_assets
        user_balance.balance += Decimal(100)

    open_transaction.save()
    user_balance.save()
    print("""         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Linux Rules! |
       M|@||@\) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_\)      \.___.,|     .'
\____   \)MMMMMM|   .'
     `-'       `--' hjm""")
    print(user_balance.balance)
        #average()
        # en lugar de return raise
        #raise #leyenda del error 
    transaction = serializers.serialize('json', [ open_transaction, ])
    balance = serializers.serialize('json', [ user_balance, ])
    Group('chat-'+label).send({'text': transaction })
    Group('chat-'+label).send({'text': balance })
        #Catch: look for error type and aply try catch function 
    # #code 1   }
