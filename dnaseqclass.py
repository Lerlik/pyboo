# Design a class for a simple DNA sequencer -
# Given: A simple sequencer that a researcher could run an experiment
# on a biological sample and get raw data from.
# It takes in a prepared biological sample input,
# analyzes it using its sensors, and outputs raw data from the sensors.
# You can make up any values and data types for the purpose of this question.
#
# Question: Conceptually, how would you model this device using a class?
# Please clearly state any assumptions and/or constraints about your design.
# You may use pseudocode or code using any OO language/script.

class CDnaSample:
    def __init__(self, psampleid, pseq):
        self.m_id = psampleid
        self.m_seq = pseq

class CDnaSensor:
    def __init__(self, psensorid):
        self.m_id = psensorid

    def featuresdetected(self, psample):
        if psample == 42:
            return [" !!Hulk has been born!!"]
        else:
            return [" normal "]

    def analyzesample(self, psample):
        sensorresult = "[" + str(self.m_id) + "] Raw: " + str(psample)
        sensorresult += str(self.featuresdetected(psample))
        return [sensorresult]


class CDnaSequencer:
    def __init__(self, puser, psample, psensors):
        self.m_user = puser
        self.m_sample = psample
        self.m_sensors = psensors
        self.m_results = []

    def analyze(self):
        for sens in self.m_sensors:
            self.m_results.append(sens.analyzesample(self.m_sample))

    def printresult(self):
        for res in self.m_results:
            print(res)





