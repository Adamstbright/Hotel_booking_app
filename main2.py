import pandas
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    # Watermak is a class variable while hotel_id and name are instance variables.
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing the availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return

    # This is a class method. it is use whwnever you need a method that is not related to any
    # instace but related to the class. it can be accessed by any instance of the class.
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # This is a magic method, this is used to overwrite the building python method.
    def __eq__(self, others):
        if self.hotel_id == others.hotel_id:
            return True
        else:
            return False

# This is abstract class. This is used so as to avoid overwriting a method of a mother class by
# by inheritance class. Also every class that inherit from abstract class must have the method of the class.

class Ticket(ABC):

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        pass
    def generate(self):
        content = f"""
        Thank you for your reservation! 
        Here are your booking data: 
        Name : {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    # This is a class property, it can be used to process some data so as to not make an instance too bulky.
    # it behaves like a variable due to the decorator.
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    # This is a static method, it doesn't have any reference to the class or its instance.
    # it is most-time use for conversion
    @staticmethod
    def convert(amount):
        return amount * 1.2




hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)
print(Hotel.watermark)

print(Hotel.get_hotel_count(data=df))
print(hotel2.get_hotel_count(data=df))

ticket = ReservationTicket(customer_name="adams Oluwatobi ", hotel_object=hotel1)
print(ticket.generate())

converted = ReservationTicket.convert(10)
print(converted)