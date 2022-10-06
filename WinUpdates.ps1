#!/usr/bin/env powershell -WinUpdates.ps1

# Script: Ops 401 Class 01 Lab Solution
# Author: Ariel D.                  
# Date of latest revision: 03OCT2022      
# Purpose: Automatic OS updates enabled
# Resources: https://www.nakivo.com/blog/automate-windows-updates-using-powershell-short-overview/

# Main

# Allow executiion processing of running scripts
set-executionpolicy -ExecutionPolicy remotesigned -scope Process -force

# Display Message
Write-Host "Automating the installation of Windows Updates on this machine"

Start-Sleep -Seconds 1

# Imports PSWindowsUpdate
Import-Module -Name PSWindowsUpdate

# Installs PSWindowsUpdate to the PC (Type A for Yes to All Option)
Install-Module -Name PSWindowsUpdate

# List available updates
Get-WindowsUpdate

# To install all available updates and wait to reboot PC at the correct time (Reboot manually after updates have completed)
Get-WUInstall -AcceptAll -IgnoreReboot

# End
