
# Программа для рассчета замены расходников на автомобиле по километражу, что менять на ближайшем ТО

probeg_now = int(input("Текущий пробег: "))

maslo = 165000 + 8000   # Пробег при последней замене масла + интервал замены в км
maslo_MKPP = 165000 + 60000
cvechi = 165000 + 30000
remen_GRM = 138713 + 50000
tormoz = 148000 + 60000
antifriz = 138690 + 80000
jitkost_GUR = 148000 + 80000

dict = {}
print('Ближайшие замены:')

if maslo > probeg_now:
    maslo_TO = maslo - probeg_now
    dict["Масло"] = maslo_TO
    if maslo_TO < 8000:
        print("Масло надо заменить через", maslo - probeg_now, "км")
else:
    print("Замени масло")

if maslo_MKPP > probeg_now:
    maslo_MKPP_TO = maslo_MKPP - probeg_now
    dict["Масло_МКПП"] = maslo_MKPP_TO
    if maslo_MKPP - probeg_now < 8000:
        print("Масло МКПП надо заменить через", maslo_MKPP - probeg_now, "км")
else:
    print("Замени масло МКПП")

if cvechi > probeg_now:
    cvechi_TO = cvechi - probeg_now
    dict["Свечи"] = cvechi_TO
    if cvechi_TO < 8000:
        print("Свечи надо заменить через", cvechi - probeg_now, "км")
else:
    print("Замени свечи")

if remen_GRM > probeg_now:
    remen_GRM_TO = remen_GRM - probeg_now
    dict["Ремень_ГРМ"] = remen_GRM_TO
    if remen_GRM_TO < 8000:
        print("Ремень ГРМ надо заменить через", remen_GRM - probeg_now, "км")
else:
    print("Замени ремень ГРМ")

if tormoz > probeg_now:
    tormoz_TO = tormoz - probeg_now
    dict["Тормозная_жидкость"] = tormoz_TO
    if tormoz_TO < 8000:
        print("Тормозную жидкость надо заменить через", tormoz - probeg_now, "км")
else:
    print("Замени Тормозную жидкость")

if antifriz > probeg_now:
    antifriz_TO = antifriz - probeg_now
    dict["Антифриз"] = antifriz_TO
    if antifriz_TO < 8000:
        print("Антифриз надо заменить через", antifriz - probeg_now, "км")
else:
    print("Замени Антифриз")

if jitkost_GUR > probeg_now:
    jitkost_GUR_TO = jitkost_GUR - probeg_now
    dict["Жидкость_ГУРа"] = jitkost_GUR_TO
    if jitkost_GUR_TO < 8000:
        print("Жидкость ГУРа надо заменить через", jitkost_GUR - probeg_now, "км")
else:
    print("Замени Жидкость ГУРа")

print("Замены по пробегу, через 'n' км:", dict)
