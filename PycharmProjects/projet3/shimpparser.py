import csv
import itertools


class ShimpData:
    t = []
    head_velocity = []
    eye_velocity = []


class ShimpParser:

    def parse(self, filename):
        with open(filename, 'r') as file:
            start = self.__parse_lateral_start(file)
            stop = self.__parse_lateral_stop(file, start)
            return self.__parse_lateral(filename, start, stop)

    def __parse_lateral(self, filename, start, stop):
        with open(filename, 'r') as file:
            cr = csv.reader(file, delimiter=';')
            data = ShimpData()
            for row in itertools.islice(cr, start, stop):
                t = int(row[0])
                head_velocity = float(row[3].replace(',', '.'))
                eye_velocity = float(row[4].replace(',', '.'))
                data.t.append(t)
                data.head_velocity.append(head_velocity)
                data.eye_velocity.append(eye_velocity)
            return data

    def __parse_lateral_start(self, file):
        start = 0
        while file:
            line = file.readline()
            if '<TestType>HI - Lateral</TestType>' in line:
                return start + 1
            start = start + 1
        return False

    def __parse_lateral_stop(self, file, start):
        stop = start
        while file:
            line = file.readline()
            if '<TestType>' in line:
                return stop
            stop = stop + 1
        return stop