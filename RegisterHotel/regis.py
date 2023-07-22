class Hotel:
    def __init__(self, first_name, last_name, age, country, day, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.day = day
        self.payment = payment

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                "First_name": self.first_name,
                "Last_name": self.last_name,
                "Age": self.age,
                "Countr": self.country,
                "Day": self.day,
                "Payment": self.payment,

            }
        return [
            self.first_name,
            self.last_name,
            self.age,
            self.country,
            self.day,
            self.payment,
        ]
