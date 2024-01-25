#!/usr/bin/env python3
import wmi
wmi_root = wmi.WMI()

title1 = int(================PROCESADOR==================)

wmi_processor = wmi_root.Win32_Processor()
for processor in wmi_processor:
    
    print("Nombre:", processor.Name)
    print("Núcleos:", processor.NumberOfCores)
    print("Hilos:", processor.ThreadCount)

title2 = int(================MEMORIA CACHÉ==================)

wmi_cachememories = wmi_root.Win32_CacheMemory()   
for cachememory in wmi_cachememories:

    print("", cachememory.DeviceID)
    print("Cantidad:", cachememory.InstalledSize,  "MB")
    print( "", cachememory.Purpose)

title3 = int(================MEMORIA RAM==================)

wmi_physicalmemories = wmi_root.Win32_PhysicalMemory()
for physicalmemories in wmi_physicalmemories:
    capacity = int(physicalmemories.Capacity) / (1024 ** 3)

    print("", physicalmemories.Tag)
    print("Localización:", physicalmemories.DeviceLocator)
    print("Cantidad:", capacity , "GB" )
    print("Velocidad:", physicalmemories.ConfiguredClockSpeed)

title4 = int(================TARJETA GRÁFICA==================)

wmi_graphics = wmi_root.Win32_VideoController()
for graphic in wmi_graphics:

    print("ID:", graphic.DeviceID)
    print("Caption:", graphic.Caption)
    print("Resolution:", graphic.CurrentHorizontalResolution, "x", graphic.CurrentVerticalResolution, "pixels", graphic.CurrentRefreshRate, "Hz")
   
