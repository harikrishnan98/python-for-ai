class Dog:
     def __init__(self,name,breed='SomeBreed'):
        self.name = name
        self.breed = breed
     def get_dog_name(self):
         return self.name

class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color

golden_reter = Dog(name="Johnny", breed="Piledriver")

golden_reter.get_dog_name()

dog1= Dog(name="Boiye")
dog1.name
dog1.breed

dog2 = Dog("Max","Puppy")

dog2.breed

class APIConfig:
    def __init__(self,api_key,model="gpt-3.5-turbo", max_tokens=300):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens



# Create different Config:
dev_config = APIConfig("sk-dev-key",max_tokens=50)


# Using all named arguments

prod_config = APIConfig(api_key="sk-prod-key",model="gpt-4",max_tokens=1000)

print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)


class DataValidator:
    def __init__(self):
        self.errors = [] # Class Attributes
     # Class Methods
    def validate_email(self,email):
        if '@' not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True
    
    # Class Methods
    def validate_age(self,age):
        if age < 0 or age > 100:
           self.errors.append(f"Invalid age: {age}")
           return False
        return True
    
    # Class Methods
    def get_errors(self):
        return self.errors
    


# Use the Validator class

validator = DataValidator()

validator.errors # errors is the initial variable for instance set by class

validator.validate_email(email="hk@cc.co")

validator.validate_age(age=200)


validator.validate_email(email="jk.cc")

validator.get_errors()

class User:
    version = []
    is_changed = 'yes'
    def __init__(self,name):
        self.name = name

    def job_detail(self,job):
        self.job = job
    
    def display_job(self):
        return self.job


hk_user = User('Hari')

hk_user.is_changed = 'No-hk'

hk_user.job_detail("SWE")

hk_user.display_job()

ak_user = User('AK')

hk_user.version.append('hk')

ak_user.is_changed = 'Yes-ak'

ak_user.version.append('ak_kumar')

## Inheritance:

class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} Animal is eating now...")
    def sleep(self):
        print(f"{self.name} Animal is sleeping...")


class Dog(Animal): # Inheritance (Its inherits the parent class Animal)
    def bark(self):
        return f"{self.name} says woof!"
    

dog_num1 = Dog(name="Sheldon")

dog_num2 = Dog("Milli")

dog_num1.bark()
dog_num1.eat()
dog_num1.sleep()

dog_num2.bark()
dog_num2.eat()
dog_num2.sleep()


## Adding Attributes to the Parent Class

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_pet = True


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Pass name to parent's __init__
        self.breed = breed
    def describe(self):
        return f"{self.name} is a {self.breed}"
    

# Creates dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

yellow = Dog("Max", "Labor")

yellow.is_pet

golden.is_pet = False

golden.describe()

yellow.describe()


txt = 'absc-gpt-290'

class Animal_z:
    def __init__(self,name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound"
    

class Dog_z(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} barks: Woof!"
    
class Cat_z(Animal):
    def __init__(self,name):
        super().__init__(name)

    def make_sound(self):
        return f"{self.name} meows: Meow!"
    
# Different animals, different sounds
generic = Animal_z("Maxim")
generic.name
generic.make_sound()

doggie = Dog_z("Gogiee")

doggie.make_sound()

cattie = Cat_z("Lisa")
cattie.make_sound()


class GptModel:
    version = '1.0'
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}")
        self.is_loaded = True

# This is class Method
    @classmethod
    def displayInfo(cls):
        cls.version = '2.0'
        print(f"This is version: {cls.version}")

gpt_mod = GptModel("Opus-4.6")
gpt_mod.displayInfo()

class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False
    
    def load(self):
        print(f"Loading {self.model_name}")
        self.is_loaded = True

# This is class Method
    @staticmethod
    def displayInfo():
        print("This is sample DisplayInfo method")


class TextModel():
    def __init__(self,model_name,max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load() # Here we are calling Parent class method()
    # Truncate if needed
        if len(text) > self.max_length:
            text = text[:self.max_length]
        return f"Processed Text: {text}"
    
    def displayInfo_text(self):
        self.displayInfo()
    

# Use the model - with named arguments
model = TextModel(model_name="gpt-3.5-turbo", max_length=100)

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
               # Processed: Hello world
model.displayInfo_text()

base_model_1 = BaseModel("Chat-GPT")

base_model_1.displayInfo()

BaseModel.displayInfo()


# Return a self

# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text
    
    def clean(self):
        self.text = self.text.strip().lower()
        return self
    
    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self

# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text