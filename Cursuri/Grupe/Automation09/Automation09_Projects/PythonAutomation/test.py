masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi= []

for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        print(masini[i])
        masini_vechi.append(masini[i])
        masini[i] = 'TESLA'
print(f'Masini vechi: {masini_vechi}')
print(f'Masini noi: {masini}')