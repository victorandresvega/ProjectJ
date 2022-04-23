import copy
import time 
import hashlib
class Appointment:
    def __init__(self,doctor_name,doctor_image,phone,address,specialty, appointment_id, doctor_id):
        """
        Initializes Event object
        :param doctor_name: Name of doctor
        :param doctor_image: Profile image URL for doctor
        :param address: ID of appointment associated with event
        :param specialty: specialty of doctor
        :param appointment_id: appointment id created when an appointment is scheduled
        :param doctor_id: ID of doctor associated with event
        :param phone: Phone to contact doctor's office
        """

        self.name=self.set_doctor_name(doctor_name)
        self.appointment_id = self.generate_appointment_id(appointment_id)
        self.doctor_id = self.set_doctor_id(doctor_id)
        self.doctor_image=self.set_doctor_image(doctor_image)
        self.address=self.set_doctor_address(address)
        self.specialty=self.set_doctor_specialty(specialty)
        self.phone=self.set_doctor_phone(phone)

    # Setters
    
    def set_doctor_id(self, doctor_id):
        if type(doctor_id) != str:
            raise TypeError("doctor_id must be a string")
        self.appointment_id = doctor_id
    def set_doctor_specialty(self, specialty):
        if type(specialty) != str:
            raise TypeError("specialty must be a string")
        self.doctor_id = specialty
    def set_doctor_address(self, address):
        if type(address) != str:
            raise TypeError("address must be a string")
        self.doctor_id = address
    def set_doctor_image(self, doctor_image):
        if type(doctor_image) != str:
            raise TypeError("doctor_image must be a string")
        self.doctor_id = doctor_image
    def set_doctor_name(self, doctor_name):
        if type(doctor_name) != str:
            raise TypeError("doctor_name must be a string")
        self.name = doctor_name
    def set_doctor_phone(self, doctor_phone):
        if type(doctor_phone) != str:
            raise TypeError("doctor_phone must be a string")
        self.name = doctor_phone
    @staticmethod
    def get_available_time_slots(doc_id,day,database,time_slots):
        collection = database.db.events
        # result=time_slots
        result=copy.deepcopy(time_slots)
        time_slots_filled=collection.find({"$and":[ {"doctor_id":doc_id}, {"date":day}]})
        for i in time_slots_filled:
            result.remove(i["start_time"])
        return result
    def to_json(self):
        return {'username': self.username, 'ratings': self.ratings , 'raters_amount': self.raters_amount, 'user_items': self.user_items, 'profile_image': self.profile_image}
    @staticmethod
    def generate_appointment_id():
        # Generate unique user ID
        cur_time = str(time.time())
        hashed_time = hashlib.sha1()
        hashed_time.update(cur_time.encode("utf8"))
        return hashed_time.hexdigest()