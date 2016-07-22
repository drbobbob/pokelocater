import random

def get_fake_pokemon_result(location, count=1):
    loc_parts = location.split(',')
    result = []
    for i in range(count):
        lat = float(loc_parts[0].strip()) + (random.random() * 0.002) - 0.001
        lon = float(loc_parts[1].strip()) + (random.random() * 0.002) - 0.001
        i = random.randint(1,151)
        grey = bool(random.randint(0,1))
        if grey:
            i_str = "%d_grey" % i
        else:
            i_str = str(i)

        result.append({"id":i_str,"name":"foo","latitude":lat,"longitude":lon,"time_left":100,"distance":10,"direction":"N"})

    return result
