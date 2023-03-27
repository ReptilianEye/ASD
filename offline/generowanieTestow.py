import random


def gen_tests(n_testes, n_data):
    max_v = int(10e6)
    path = r'C:\Users\piotr\Programowanie\NaukaPython\ASD\offline\dane\in'
    for i in range(n_testes):
        t = [random.randint(0, max_v) for _ in range(n_data)]
        with open(path+f"\dane{i}.txt", "w") as file:
            file.write(str(t))

#do dokonczenia
gen_tests(5, 10)
