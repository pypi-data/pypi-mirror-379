"""
@author: T. Guallart
@author: J.M. Algarín

@summary: increase the pulse width and plot the peak value of the signal received 
@status: under development
@todo:

"""
import os
import sys

from marge.marge_utils import utils

#*****************************************************************************
# Get the directory of the current script
main_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(main_directory)
parent_directory = os.path.dirname(parent_directory)

# Define the subdirectories you want to add to sys.path
subdirs = ['MaRGE', 'marcos_client']

# Add the subdirectories to sys.path
for subdir in subdirs:
    full_path = os.path.join(parent_directory, subdir)
    sys.path.append(full_path)
#*****************************************************************************
import marge.marcos.marcos_client.experiment
import numpy as np
import marge.seq.mriBlankSeq as blankSeq  # Import the mriBlankSequence for any new sequence.
import scipy.signal as sig
import marge.configs.hw_config as hw


class RabiFlops(blankSeq.MRIBLANKSEQ):
    def __init__(self):
        super(RabiFlops, self).__init__()
        # Input the parameters
        self.discriminator = None
        self.cal_method = None
        self.addParameter(key='seqName', string='RabiFlopsInfo', val='RabiFlops')
        self.addParameter(key='toMaRGE', val=True)
        self.addParameter(key='nScans', string='Number of scans', val=1, field='SEQ')
        self.addParameter(key='larmorFreq', string='Larmor frequency (MHz)', val=3.06, field='RF')
        self.addParameter(key='rfExAmp', string='RF excitation amplitude (a.u.)', val=0.3, field='RF')
        self.addParameter(key='rfReAmp', string='RF refocusing amplitude (a.u.)', val=0.3, field='RF')
        self.addParameter(key='rfReTime', string='RF refocusing time (us)', val=0.0, field='RF')
        self.addParameter(key='echoTime', string='Echo time (ms)', val=10.0, field='SEQ')
        self.addParameter(key='repetitionTime', string='Repetition time (ms)', val=500., field='SEQ')
        self.addParameter(key='nPoints', string='nPoints', val=60, field='IM')
        self.addParameter(key='acqTime', string='Acquisition time (ms)', val=4.0, field='SEQ')
        self.addParameter(key='shimming', string='Shimming', val=[-12.5, -12.5, 7.5], field='OTH')
        self.addParameter(key='rfExTime0', string='Rf pulse time, Start (us)', val=5.0, field='RF')
        self.addParameter(key='rfExTime1', string='RF pulse time, End (us)', val=100.0, field='RF')
        self.addParameter(key='nSteps', string='Number of steps', val=20, field='RF')
        self.addParameter(key='deadTime', string='Dead time (us)', val=60, field='SEQ')
        self.addParameter(key='rfRefPhase', string='Refocusing phase (degrees)', val=0.0, field='RF')
        self.addParameter(key='method', string='Rephasing method: 0->Amp, 1->Time', val=0, field='RF')
        self.addParameter(key='dummyPulses', string='Dummy pulses', val=0, field='SEQ')
        self.addParameter(key='cal_method', string='Calibration method', val='FID', tip='FID or ECHO', field='OTH')
        self.addParameter(key='discriminator', string='Calibration point', val='min', field='OTH',
                          tip="'max' to use maximum for 90º or 'min' to use zero-crossing for 180º")

    def sequenceInfo(self):
        print("Rabi Flops")
        print("Author: Dr. J.M. Algarín")
        print("Contact: josalggui@i3m.upv.es")
        print("mriLab @ i3M, CSIC, Spain")
        print("Rabi Flops with different methods")
        print("Notes:")
        print("Set RF refocusing amplitude to 0.0 to get single excitation behavior")
        print("Set RF refocusing time to 0.0 to auto set the RF refocusing time:")
        print("-If Rephasing method = 0, refocusing amplitude is twice the excitation amplitude")
        print("-If Rephasing method = 1, refocusing time is twice the excitation time\n")
        

    def sequenceTime(self):
        nScans = self.mapVals['nScans']
        nSteps = self.mapVals['nSteps']
        dummyPulses = self.mapVals['dummyPulses']
        repetitionTime = self.mapVals['repetitionTime'] * 1e-3
        return (repetitionTime * nScans * nSteps * (dummyPulses + 1) / 60)  # minutes, scanTime

    def sequenceRun(self, plotSeq=0, demo=False):
        init_gpa = False  # Starts the gpa
        self.demo = demo

        # I do not understand why I cannot create the input parameters automatically
        seqName = self.mapVals['seqName']
        nScans = self.mapVals['nScans']
        larmorFreq = self.mapVals['larmorFreq']
        rfExAmp = self.mapVals['rfExAmp']
        rfReAmp = self.mapVals['rfReAmp']
        echoTime = self.mapVals['echoTime']
        repetitionTime = self.mapVals['repetitionTime']
        nPoints = self.mapVals['nPoints']
        acqTime = self.mapVals['acqTime']
        shimming = np.array(self.mapVals['shimming'])
        rfExTime0 = self.mapVals['rfExTime0']
        rfExTime1 = self.mapVals['rfExTime1']
        nSteps = self.mapVals['nSteps']
        deadTime = self.mapVals['deadTime']
        rfRefPhase = self.mapVals['rfRefPhase']
        method = self.mapVals['method']
        rfReTime = self.mapVals['rfReTime']
        dummyPulses = self.mapVals['dummyPulses']

        # Time variables in us and MHz
        larmorFreq *= 1e-6
        echoTime *= 1e3
        repetitionTime *= 1e3
        acqTime *= 1e3
        shimming = shimming * 1e-4

        # Rf excitation time vector
        rfTime = np.linspace(rfExTime0, rfExTime1, num=nSteps, endpoint=True)  # us
        self.mapVals['rfTime'] = rfTime * 1e-6  # s

        def createSequence():
            # Set shimming
            self.iniSequence(20, shimming)

            tEx = 1000  # First excitation at 1 ms
            for scan in range(nScans):
                for step in range(nSteps):
                    for pulse in range(dummyPulses + 1):
                        # Excitation pulse
                        t0 = tEx - hw.blkTime - rfTime[step] / 2
                        self.rfRecPulse(t0, rfTime[step], rfExAmp, 0)

                        # Rx gate for FID
                        if pulse == dummyPulses:
                            t0 = tEx + rfTime[step] / 2 + deadTime
                            self.ttlOffRecPulse(t0, acqTime)
                            self.rxGate(t0, acqTime)

                        # Refocusing pulse
                        if method:  # time
                            if rfReTime == 0.0:
                                t0 = tEx + echoTime / 2 - hw.blkTime - rfTime[step]
                                self.rfRecPulse(t0, rfTime[step] * 2, rfReAmp, rfRefPhase * np.pi / 180.0)
                            else:
                                t0 = tEx + echoTime / 2 - hw.blkTime - rfReTime / 2
                                self.rfRecPulse(t0, rfReTime, rfReAmp, rfRefPhase * np.pi / 180.0)
                        else:  # amplitude
                            if rfReTime == 0.0:
                                t0 = tEx + echoTime / 2 - hw.blkTime - rfTime[step] / 2
                                self.rfRecPulse(t0, rfTime[step], rfExAmp * 2, rfRefPhase * np.pi / 180.0)
                            else:
                                t0 = tEx + echoTime / 2 - hw.blkTime - rfReTime
                                self.rfRecPulse(t0, rfReTime, rfExAmp * 2, rfRefPhase * np.pi / 180.0)

                        # Rx gate for Echo
                        if pulse == dummyPulses:
                            t0 = tEx + echoTime - acqTime / 2
                            self.ttlOffRecPulse(t0, acqTime)
                            self.rxGate(t0, acqTime)

                        # Update excitation time for next repetition
                        tEx += repetitionTime

            # Turn off the gradients after the end of the batch
            self.endSequence(repetitionTime * nSteps * nScans * (dummyPulses + 1))

        # Create experiment
        bw = nPoints / acqTime * hw.oversamplingFactor  # MHz
        samplingPeriod = 1 / bw
        if not self.demo:
            self.expt = ex.Experiment(lo_freq=larmorFreq * 1e6,
                                      rx_t=samplingPeriod,
                                      init_gpa=init_gpa,
                                      gpa_fhdo_offset_time=(1 / 0.2 / 3.1),
                                      print_infos=False,
                                      )
            samplingPeriod = self.expt.get_rx_ts()[0]
        self.mapVals['samplingPeriod'] = samplingPeriod
        bw = 1 / samplingPeriod / hw.oversamplingFactor
        self.mapVals['bw'] = bw * 1e6
        acqTime = nPoints / bw

        # Execute the experiment
        createSequence()
        if self.floDict2Exp():
            print("Sequence waveforms loaded successfully")
            pass
        else:
            print("ERROR: sequence waveforms out of hardware bounds")
            return False
        if not plotSeq:
            if not self.demo:
                rxd, msgs = self.expt.run()
                self.expt.__del__()
                print(msgs)
            else:
                rxd = {'rx0': np.random.randn(2 * self.nPoints * self.nSteps * hw.oversamplingFactor) +
                              1j * np.random.randn(2 * self.nPoints * self.nSteps * hw.oversamplingFactor)}
            rxd['rx0'] = rxd['rx0'] * hw.adcFactor  # Here I normalize to get the result in mV
            self.mapVals['dataOversampled'] = rxd['rx0']
        return True

if __name__ == '__main__':
    seq = RabiFlops()
    seq.sequenceAtributes()
    seq.sequenceRun(demo=True)
    seq.sequenceAnalysis(mode='Standalone')
