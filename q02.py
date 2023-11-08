print("-"*28)
print("        員工薪資輸入        ")
print("    若姓名處未輸入則代表結束")
print("-"*28)
memberlist = None
while True:
    a = input("請輸入姓名:")
    if a == "":
        break
    else:
        member ={"eName":a,"eSalary":""}
        member["eSalary"] = input("請輸入薪資:")
        print("")
        if memberlist is None:
            memberlist = []
    memberlist.append(member)
print("-"*28)
if memberlist is not None:
    for person in memberlist:
        print(f'員工{person["eName"]:<6}的薪資為{int(person["eSalary"]):>7,}')
print("-"*28)
if memberlist is not None:
    total=0
    for person in memberlist:
        total+=int(person["eSalary"])
    avg = round(total / len(memberlist),2)
    print(f"合計薪資：{total:>15,}")
    print(f"平均薪資：{avg:>18,.2f}")
    print("="*28)
else:
    total = 0
    avg = 0
    print(f"合計薪資：{total:>15}")
    print(f"平均薪資：{avg:>18.2f}")
    print("="*28)