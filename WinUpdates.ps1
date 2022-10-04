#!/usr/bin/env powershell -WinUpdates.ps1

# Script: Ops 401 Class 01 Lab Solution
# Author: Ariel D.                  
# Date of latest revision: 03OCT2022      
# Purpose: Automatic OS updates enabled
# Resources: https://www.nakivo.com/blog/automate-windows-updates-using-powershell-short-overview/

# Installs PSWindowsUpdate to the PC (Type A for Yes to All Option)
Install-Module -Name PSWindowsUpdate

# Create a PSWindowsUpdate Module within the C: Drive > Windows Folder for storage
Save-Module -Name PSWindowsUpdate -C:\Windows

# Input C:\Windows in the Path request

# Main
# List available updates
Get-WindowsUpdate

# To install all available updates and wait to reboot PC at the correct time (Reboot manually after updates have completed)
Get-WUInstall -AcceptAll -IgnoreReboot

# End