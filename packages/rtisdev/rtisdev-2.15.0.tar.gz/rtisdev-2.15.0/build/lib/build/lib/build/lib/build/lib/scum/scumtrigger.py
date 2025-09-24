import rtisdev
import scipy
import scipy.io


rtisdev.open_connection(allowDebugMode=True)

uuid_rec = rtisdev.set_recording_settings(callMinimumFrequency=20000, callMaximumFrequency=80000, microphoneSamples=131072)
rtisdev.set_processing_settings(uuid_rec, minRange=0, maxRange=0.1)

current_settings = rtisdev.get_current_settings()

# Save current_settings.adcSignal to a .mat file
# This will create a file named 'adcSignal.mat' with a variable 'adcSignal' inside.
if hasattr(current_settings, 'adcSignal'):
    scipy.io.savemat('adcSignal.mat', {'adcSignal': current_settings.adcSignal})

# To save all settings as a struct, we can convert the object to a dictionary.
# The .mat file will contain a struct named 'current_settings'.
settings_dict = vars(current_settings)
scipy.io.savemat('current_settings.mat', current_settings.__dict__)


while True:
    rtisdev.get_raw_measurement(True)
