# knox-timestamp-workaround

Python script intended to workaround KNOX security software's tendency to replace timestamps from photos with the time they are moved into KNOX managed storage.
This script matches files moved into KNOX managed storage, matches the files by name with the originals, removes the "knoxed" files and copies the originals into the device's auxiliary storage which does not encrypt or recreate files when moved. Thus the timestamps are preserved and are available on the KNOX managed device.
