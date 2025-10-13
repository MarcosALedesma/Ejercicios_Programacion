import d20

# tiradas 
def tirada_d20 ():
    result = d20.roll("1d20")
    return result.total

def tirada_stats():
    result = d20.roll("4d6kh3")
    return result, result.total

roll_obj, roll_total = tirada_stats()

print(f"Resultado completo: {roll_obj}. Valor total: {roll_total} ")
