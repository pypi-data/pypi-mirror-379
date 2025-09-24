import rtisdev
import matplotlib.pyplot as plt
import numpy as np
import time

# Open a connection to the RTIS Device over the default serial port.
success_connect = rtisdev.open_connection(allowDebugMode=True)
rtisdev.set_log_mode(0)
directions = 361
maxRange = 5

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="das")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="das", dmasOrder=0, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="das")
das_measurement = rtisdev.get_processed_measurement(True, configName="das")
start = time.time()
das_measurement = rtisdev.get_processed_measurement(True, configName="das")
print("DAS: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="das")

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="dascf")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="dascf", dmasOrder=0, cfEnable=True, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="dascf")
dascf_measurement = rtisdev.get_processed_measurement(True, configName="dascf")
start = time.time()
dascf_measurement = rtisdev.get_processed_measurement(True, configName="dascf")
print("DAS-CF: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="dascf")

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="dmas")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="dmas", dmasOrder=1, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="dmas")
dmas_measurement = rtisdev.get_processed_measurement(True, configName="dmas")
start = time.time()
dmas_measurement = rtisdev.get_processed_measurement(True, configName="dmas")
print("DMAS: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="dmas")

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="dmascf")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="dmascf", dmasOrder=1, cfEnable=True, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="dmascf")
dmascf_measurement = rtisdev.get_processed_measurement(True, configName="dmascf")
start = time.time()
dmascf_measurement = rtisdev.get_processed_measurement(True, configName="dmascf")
print("DMAS-CF: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="dmascf")

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="dmas2")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="dmas2", dmasOrder=2, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="dmas2")
dmas2_measurement = rtisdev.get_processed_measurement(True, configName="dmas2")
start = time.time()
dmas2_measurement = rtisdev.get_processed_measurement(True, configName="dmas2")
print("DMAS2: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="dmas2")

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="dmas2cf")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="dmas2cf", dmasOrder=2, cfEnable=True, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="dmas2cf")
dmas2cf_measurement = rtisdev.get_processed_measurement(True, configName="dmas2cf")
start = time.time()
dmas2cf_measurement = rtisdev.get_processed_measurement(True, configName="dmas2cf")
print("DMAS2-CF: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="dmas2cf")

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="dmas3")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="dmas3", dmasOrder=3, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="dmas3")
dmas3_measurement = rtisdev.get_processed_measurement(True, configName="dmas3")
start = time.time()
dmas3_measurement = rtisdev.get_processed_measurement(True, configName="dmas3")
print("DMAS3: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="dmas3")

rtisdev.set_recording_settings(microphoneSamples=163840, callMinimumFrequency=25000, callMaximumFrequency=50000, configName="dmas3cf")
success_settings_processing = rtisdev.set_processing_settings(directions=directions, maxRange=maxRange, configName="dmas3cf", dmasOrder=3, cfEnable=True, cleanEnable=False)
settings = rtisdev.get_current_settings(configName="dmas3cf")
dmas3cf_measurement = rtisdev.get_processed_measurement(True, configName="dmas3cf")
start = time.time()
dmas3cf_measurement = rtisdev.get_processed_measurement(True, configName="dmas3cf")
print("DMAS3-CF: " + "{:.3f}".format((time.time() - start)*1000) + "ms")
rtisdev.unload_processing(configName="dmas3cf")

# Plot the 2D energyscape of this processed measurement.
fig, axes = plt.subplots(2, 4, figsize=(20, 10))

measurements = [
    (das_measurement, "DAS"),
    (dascf_measurement, "DAS-CF"),
    (dmas_measurement, "DMAS"),
    (dmascf_measurement, "DMAS-CF"),
    (dmas2_measurement, "DMAS2"),
    (dmas2cf_measurement, "DMAS2-CF"),
    (dmas3_measurement, "DMAS3"),
    (dmas3cf_measurement, "DMAS3-CF")
]

for ax, (measurement, title) in zip(axes.flat, measurements):
    im = ax.imshow(np.transpose(measurement.processedData), cmap="hot", interpolation='nearest')
    ax.set_xlabel("Directions (degrees)")
    ax.set_ylabel("Range (meters)")
    indexes_x = np.arange(0, measurement.processedData.shape[0], 30)
    labels_x = np.round(np.rad2deg(settings.directions[indexes_x, 0])).astype(int)
    indexes_y = np.arange(0, measurement.processedData.shape[1], 100)
    labels_y = settings.ranges[indexes_y]
    fmt_x = lambda x: "{:.0f}°".format(x)
    fmt_y = lambda x: "{:.2f}m".format(x)
    ax.set_xticks(indexes_x)
    ax.set_xticklabels([fmt_x(i) for i in labels_x])
    ax.set_yticks(indexes_y)
    ax.set_yticklabels([fmt_y(i) for i in labels_y])
    ax.set_title(title)
    ax.invert_yaxis()
    ax.set_aspect("auto")

plt.tight_layout()
plt.show()
