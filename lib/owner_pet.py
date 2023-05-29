import ipdb

class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner= None):
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        Pet.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) > 0:
            self._name = name

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise ValueError("pet_type must be one in PET_TYPES")

        self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner  
    @owner.setter
    def owner (self, value):
        if not isinstance (value, Owner):
            raise TypeError("Owner must be an instance of the Owner Class")
        self._owner = value

        

class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be and instance pf Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda x: x.name)
    
    
  

# owner = Owner("John")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
# pet3 = Pet("Whiskers", "cat", owner)
# pet4 = Pet("Jerry", "reptile", owner)

# list = owner.get_sorted_pets()

# print(list)
    
# ipdb.set_trace()
