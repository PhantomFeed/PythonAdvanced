# Ошибки в mod3 task4 #

## Ошибка №1: ##
### Тест "test_can_get_age_correct_in_mod3_task4" выдал ошибку "20 != -20" ###

    def get_age(self):
       now = datetime.datetime.now()
       return self.yob - now.year

### Ошибка заключается в неправильной постановке now.year и self.yob, возвращается отрицательное число, так что их нужно поменять местами ###

        def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.yob

## Ошибка №2: ##
### Тест "test_can_set_name_correctly_in_mod3_task4" выдал ошибку "Владислав != Данила" ###

    def set_name(self, name):
       self.name = self.name

### Ошибка заключается в присваивании полю самого же себя, а нужно присваивать аргумент ###

    def set_name(self, name):
        self.name = name

## Ошибка №3: ##
### Тест "test_can_set_address_correctly_in_mod3_task4" выдал ошибку " != Have" ###

    def set_address(self, address):
       self.address == address

### Ошибка заключается в том, что использовано сравнение, а не присваивание ###

    def set_address(self, address):
        self.address = address

## Ошибка №4: ##
### Тест "test_can_return_homeless_person_in_mod3_task4" выдал ошибку ###

    def is_homeless(self):
       '''
       returns True if address is not set, false in other case
       '''
       return address is None

### Ошибка заключается в том, что нужно обращаться к полю self.address, а не к переменной. Также, если адрес не задается, по умолчанию self.address должен быть '' ###

    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return self.address == ''