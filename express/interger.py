#!/usr/bin/env python3
days = int(input("Enter days: "))
days1 = days;
months = days1 // 30
days1 = days1 % 30
print("Month = {} Days = {}".format(months, days1))
print("Month = {} Days = {}".format(*divmod(days, 30)))