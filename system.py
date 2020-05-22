#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	return (du.total / 100) < 20
	#print(du)

	amount = du.total / du.free
	return (amount / 100) < 20

print(check_disk_usage("/"))

def check_cpu_usage():
	pu = psutil.cpu_percent(1.0)
	return pu < 50.0

if not check_disk_usage("/") and not check_cpu_usage():
	print("Error!!!")
else:
	print("Alles OK - Rechner läuft rund")
