#!/usr/bin/env powershell -acctcreation.ps1

# Script: Ops 401 Lab 04 Solution
# Author: Ariel D.                  
# Date of latest revision: 06OCT2022      
# Purpose: Enables GPO Password Complexity Requirements

# Main

# Enable Password Complexity Requirements
secedit /export /cfg c:\secpol.cfg
(GC C:\secpol.cfg) -Replace "PasswordComplexity = 0","PasswordComplexity = 1" | Out-File C:\secpol.cfg
secedit /configure /db c:\windows\security\local.sdb /cfg c:\secpol.cfg /areas SECURITYPOLICY
Remove-Item C:\secpol.cfg -Force

# End