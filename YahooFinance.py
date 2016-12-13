# -*- coding: utf8 -*-
import ystockquote
# print(ystockquote.get_price_book("PETR4"))
# print(ystockquote.get_bid_realtime('GOOGL'))
print ("Ola --- ooo989898")
v = ystockquote.get_all("RAPT4.sa")
p = v['price']
c = v['change']
print("Valor:")
print v
print ("Preço: %s") % (str(p))
print ("Oscilação: %s") % (str(c))
d = p + (c * -1)
print ("Preço Fechamento: %s") % (str(d))
