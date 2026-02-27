#Connection point of centromes and Cross over possiblity

#This project is developed by a second year undergraduate student of genetic and bioenginnereering at Yeditepe University, Istanbul, Turkey.
#Due to hindrances, I have used Monte Carlo method to simulate the crossover possibility. Some therminologies may not be accurate or simplified dur to my lack of knowledge.

import random
import matplotlib.pyplot as plt

def cros_poss():
    L = 1000
    possibilities4connection = {
        'metacentric': (0.48, 0.52),
        'submetacentric': (0.35, 0.45),
        'telocentric': (0.0, 0.05),
        'acrocentric': (0.10, 0.25)
    }
    #These possibilities are randomly chosen within the given ranges. It might not reflect the real life data.
    pericentromere_zone = int(L * 0.05)

    simulations = 1000

    metacentric_p = int(random.uniform(0.48*L, 0.52*L))
    submetacentric_p = int(random.uniform(0.35*L, 0.45*L))
    telocentric_p = int(random.uniform(0.0*L, 0.05*L))
    acrocentric_p = int(random.uniform(0.10*L, 0.25*L))

    metacentric_q = L - metacentric_p
    submetacentric_q = L - submetacentric_p
    telocentric_q = L - telocentric_p
    acrocentric_q = L - acrocentric_p

    meta_centromere = metacentric_p
    submeta_centromere = submetacentric_p
    telo_centromere = telocentric_p
    acro_centromere = acrocentric_p

    forbidden_head_meta = range(meta_centromere - pericentromere_zone, meta_centromere + pericentromere_zone+1)
    forbidden_head_submeta = range(submeta_centromere - pericentromere_zone, submeta_centromere + pericentromere_zone+1)
    forbidden_head_telo = range(telo_centromere - pericentromere_zone, telo_centromere + pericentromere_zone+1)
    forbidden_head_acro = range(acro_centromere - pericentromere_zone, acro_centromere + pericentromere_zone+1)


    meta_p=0
    meta_q=0
    meta_valid=0

    for i in range(simulations):
        cross_point_meta = random.randint(1, L-1)
        if cross_point_meta in forbidden_head_meta:
            continue
        meta_valid += 1
        if cross_point_meta < meta_centromere:
            meta_p += 1
        else:
            meta_q += 1


            
    submeta_p=0
    submeta_q=0
    submeta_valid=0

    for i in range(simulations):
        cross_point_submeta = random.randint(1, L-1)
        if cross_point_submeta in forbidden_head_submeta:
            continue
        submeta_valid += 1
        if cross_point_submeta < submeta_centromere:
            submeta_p += 1
        else:
            submeta_q += 1

    telo_p=0
    telo_q=0    
    telo_valid=0
    for i in range(simulations):
        cross_point_telo = random.randint(1, L-1)
        if cross_point_telo in forbidden_head_telo:
            continue
        telo_valid += 1
        if cross_point_telo < telo_centromere:
            telo_p += 1
        else:
            telo_q += 1

    acro_p=0
    acro_q=0
    acro_valid=0
    for i in range(simulations):
        cross_point_acro = random.randint(1, L-1)
        if cross_point_acro in forbidden_head_acro:
            continue
        acro_valid += 1
        if cross_point_acro < acro_centromere:
            acro_p += 1
        else:
            acro_q += 1




        test_num=100
        meta_p_oranlari= []
        for test in range(test_num):
            metacentric_p = int(random.uniform(0.48*L, 0.52*L))
            meta_centromere= metacentric_p
            forbidden_head_meta= range(meta_centromere - pericentromere_zone, meta_centromere + pericentromere_zone+1)
            meta_p=0
            meta_valid=0
            for i in range(simulations):
                cross_point_meta = random.randint(1, L-1)
                if cross_point_meta in forbidden_head_meta:
                    continue
                meta_valid += 1
                if cross_point_meta < meta_centromere:
                    meta_p += 1
            meta_p_oranlari.append(meta_p/meta_valid)


        submeta_p_oranlari= []
        for test in range(test_num):
            submetacentric_p = int(random.uniform(0.35*L, 0.45*L))
            submeta_centromere= submetacentric_p
            forbidden_head_submeta= range(submeta_centromere - pericentromere_zone, submeta_centromere + pericentromere_zone+1)
            submeta_p=0
            submeta_valid=0
            for i in range(simulations):
                cross_point_submeta = random.randint(1, L-1)
                if cross_point_submeta in forbidden_head_submeta:
                    continue
                submeta_valid += 1
                if cross_point_submeta < submeta_centromere:
                    submeta_p += 1
            submeta_p_oranlari.append(submeta_p/submeta_valid)


        telo_p_oranlari= []
        for test in range(test_num):
            telocentric_p = int(random.uniform(0.0*L, 0.05*L))
            telo_centromere= telocentric_p
            forbidden_head_telo= range(telo_centromere - pericentromere_zone, telo_centromere + pericentromere_zone+1)
            telo_p=0
            telo_valid=0
            for i in range(simulations):
                cross_point_telo = random.randint(1, L-1)
                if cross_point_telo in forbidden_head_telo:
                    continue
                telo_valid += 1
                if cross_point_telo < telo_centromere:
                    telo_p += 1
            telo_p_oranlari.append(telo_p/telo_valid)


        acro_p_oranlari= []
        for test in range(test_num):
            acrocentric_p = int(random.uniform(0.10*L, 0.25*L))
            acro_centromere= acrocentric_p
            forbidden_head_acro= range(acro_centromere - pericentromere_zone, acro_centromere + pericentromere_zone+1)
            acro_p=0
            acro_valid=0
            for i in range(simulations):
                cross_point_acro = random.randint(1, L-1)
                if cross_point_acro in forbidden_head_acro:
                    continue
                acro_valid += 1
                if cross_point_acro < acro_centromere:
                    acro_p += 1
            acro_p_oranlari.append(acro_p/acro_valid)


 
    plt.boxplot([meta_p_oranlari, submeta_p_oranlari, telo_p_oranlari, acro_p_oranlari],
                    labels=['Metacentric', 'Submetacentric', 'Telocentric', 'Acrocentric'])
    plt.ylabel('Crossover Possibility on p arm')
    plt.title('Centromere location and Crossover Possibility (Monte Carlo Simulation)')
    plt.grid(True)
    plt.show()
    plt.savefig('centromere_crossover_possibility.png')

if __name__ == "__main__":

    cros_poss()
