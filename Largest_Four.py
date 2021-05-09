array = [1,2,3,-1]

def soma_maior_array(array):
    old_list = array
    new_list = [ ]
    for num in range(0, 4):
        if max(old_list) not in new_list:
            maximo = max(old_list)
            new_list.append(maximo)
            old_list.remove(maximo)
    return sum(new_list)
