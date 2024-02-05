# -*- coding: utf-8 -*-
from banks import Banks,Slinea_Banks

bank1 = Banks('Sam')                 
print(bank1.bank_title())  
bank1.save_money(500)                 
bank1.get_balance()                    
bank = Slinea_Banks()            
print(bank.bank_title())  
