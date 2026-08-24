comp=int(input("Comprimento:"))
larg=int(input("Largura:"))
preco_m2=float(input("Preço do m2:"))
area_m2=comp*larg
preco_total = preco_m2 * area_m2
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")