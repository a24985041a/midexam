from pkg.modu import triangle_zhonxin as tr

print("請輸入三角形的 3 個頂點坐標")
print("-"*30)
a = tuple((input("請輸入頂點 a 的坐標：").split(",")))
b = tuple((input("請輸入頂點 b 的坐標：").split(",")))
c = tuple((input("請輸入頂點 c 的坐標：").split(",")))
z = (tr(a,b,c))
print("-"*30)
print(f"此三角形的重心為：{z}")