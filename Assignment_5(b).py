# HERE WE ARE USING POLYMORPHISM CONCEPT

class America:                                 # CLASS 1
    def play(self):                            # METHOD 1
        print("Americans Play Baseball")
        print("Americans Play Cricket")
    def watch(self):                           # METHOD 2
        print("Americans watch Baseball")
        print("Americans watch Cricket")

class India:                                   # CLASS 2
    def play(self):                            # METHOD 1
        print("India Play Baseball")
        print("India Play Cricket")
    def watch(self):                           # METHOD 2
        print("India watch Baseball")
        print("India watch Cricket")
    
obj_amr = America()
obj_ind = India()
for country in (obj_amr , obj_ind):
    print(country.play())
    print(country.watch())