# How to test a simple DNA sequencer -
# Given a simple DNA sequencer that allows a researcher to run an experiment on a biological sample.
# This device takes in a prepared sample, uses its highly sensitive sensors to detect the DNA structures,
# and outputs raw data.
#
# What is your process in going about testing this device?
# Please include some example test cases and state any assumptions and/or constraints you may have.

from dnaseqclass import *

sequence = {"A", "G", "C", "T"}
samples = []
samples.append(CDnaSample("AKJSCYHFDGCYAASDWEOTAGCKSDJHJ", sequence))
samples.append(CDnaSample("WHUCUHWAGCTSIDCLIIWEISKDJCVMNSD", sequence))
sensors = { CDnaSensor("AGCT"), CDnaSensor("TACG"), CDnaSensor("GUCA"), CDnaSensor("AGTC") }
for sampl in samples:
    device = CDnaSequencer("Robert Bruce Banner", sampl, sensors)
    device.analyze()
    device.printresult()

