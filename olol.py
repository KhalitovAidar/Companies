# {name, value, count, price, dollarCourse}
from django.db import models
'''

class TestDomain:
    @staticmethod
    def can_create(param):
        if param.count * param.dollarCourse != param.price:
            raise Exception('pnh')
        return param


class DataBase:
    _model: models.Model

    def __init__(self, model: models.Model):
        self._model = model
#        readOne, listMany, update, delete. create

    def create(self, param):
        return self._model(param)


class TestService:

    # Need to create condition, price = count * dollarCourse'
    def create(self, param):
        toCreate = TestDomain.can_create(param);
        return self'''