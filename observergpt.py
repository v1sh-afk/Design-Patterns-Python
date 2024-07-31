import abc
import unittest

class Observer(abc.ABC):
    """The Observer interface"""
    @abc.abstractmethod
    def update(self, job_card: "JobCard"):
        pass

class JobCard:
    def __init__(self, registration_number: str, owner_details: dict, engine_number: str, service_type: str, delivery_date: str):
        self._registration_number = registration_number
        self._owner_details = owner_details
        self._engine_number = engine_number
        self._service_type = service_type
        self._delivery_date = delivery_date
        self._status = "In Progress"
        self._observers = []
        
    def attach(self, observer: Observer):
        self._observers.append(observer)
        
    def detach(self, observer: Observer):
        self._observers.remove(observer)
        
    def notify(self):
        for observer in self._observers:
            observer.update(self)
            
    def update_status(self, status: str):
        self._status = status
        self.notify()
        
    def __str__(self):
        return f"JobCard [registration_number={self._registration_number}, owner_details={self._owner_details}, engine_number={self._engine_number}, service_type={self._service_type}, delivery_date={self._delivery_date}, status={self._status}]"

class OwnerAlert(Observer):
    def update(self, job_card: JobCard):
        if job_card._status == "Completed":
            print(f"Sending alert to owner {job_card._owner_details['name']} that their vehicle with registration number {job_card._registration_number} is ready for pickup.")

class ServiceMechanic(Observer):
    def update(self, job_card: JobCard):
        print(f"Service Mechanic assigned to job with registration number {job_card._registration_number}")

# Usage
job_card = JobCard("KA-01-HH-1234", {"name": "John Doe", "phone": "1234567890"}, "X567Y890Z", "Oil Service", "2022-05-01")

owner_alert = OwnerAlert()
job_card.attach(owner_alert)

service_mechanic = ServiceMechanic()
job_card.attach(service_mechanic)

job_card.update_status("Completed")
