from nada_dsl import *

def compute_mean(my_int1, my_int2):

    return (my_int1 + my_int2) /Integer(2)

def markov_inequality(mean, a):
    # Compute the upper bound probability according to Markov's inequality
    return mean / a

def nada_main():
    party1 = Party(name="Party1")
    
    # Secure inputs
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    mean = compute_mean(my_int1, my_int2)
    a = Integer(10)

    upper_bound_probability = markov_inequality(mean, a)

    return [Output(upper_bound_probability, "upper_bound_probability", party1)]
