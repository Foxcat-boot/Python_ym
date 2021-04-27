# -*- coding:utf-8 -*-

# For EA Class1

from time import time, localtime, strftime

print("\n")
a = localtime(time())
d = strftime("%A", a)
print(d)


def Monday():
    print("8:20-9:20\t Writing\t Classroom6")
    print("9:25-10:15\t Review\t\t Classroom4")
    print("10:30-11:20\t Vocabulary\t Classroom4")
    print("11:25-12:15\t Bible\t\t Classroom5")
    print("12:20-1:10\t Grammar\t Classroom3")
    print("13:40-14:30\t Reading\t Classroom6")
    print("14:45-15:35\t Photography\t Classroom1")
    print("15:45-16:45\t Study Hall\t Classroom5")


def Wednesday():
    print("8:20-9:20\t Writing\t Classroom6")
    print("9:25-10:15\t Review\t\t Classroom4")
    print("10:30-11:20\t Vocabulary\t Classroom4")
    print("11:25-12:15\t Bible\t\t Classroom5")
    print("12:20-1:10\t Grammar\t Classroom3")
    print("13:40-14:30\t Reading\t Classroom6")
    print("14:45-15:35\t Chapel\t\t Classroom1")
    print("15:45-16:45\t Study Hall\t Classroom5")


def Tuesday():
    print("8:20-9:20\t Writing\t Classroom6")
    print("9:25-10:15\t Review\t\t Classroom4")
    print("10:30-11:20\t Vocabulary\t Classroom4")
    print("11:25-12:15\t Bible\t\t Classroom5")
    print("12:20-1:10\t Grammar\t Classroom3")
    print("13:40-14:30\t PE\t\t Classroom6")
    print("14:45-15:35\t ChineseCooking\t Kitchen")
    print("15:45-16:45\t Study Hall\t Classroom5")


def Thursday():
    print("8:20-9:20\t Writing\t Classroom6")
    print("9:25-10:15\t Review\t\t Classroom4")
    print("10:30-11:20\t Vocabulary\t Classroom4")
    print("11:25-12:15\t Bible\t\t Classroom5")
    print("12:20-1:10\t Grammar\t Classroom3")
    print("13:40-14:30\t PE\t\t Classroom6")
    print("14:45-15:35\t EnglishPron\t Classroom1")
    print("15:45-16:45\t Study Hall\t Classroom5")


def Friday():
    print("8:20-9:20\t Writing\t\t Classroom6")
    print("9:25-10:15\t Review\t\t Classroom4")
    print("10:30-11:20\t Vocabulary\t Classroom4")
    print("11:25-12:15\t Bible\t\t Classroom5")
    print("12:20-1:10\t Grammar\t\t Classroom3")
    print("13:40-14:30\t Reading\t\t Classroom6")
    print("14:45-15:35\t Hiking\t\t FromClassroom1")


def Saturday():
    print("Clubs ;)")
    print("19：00-??:??\t FilmNight\t Classroom1")


def Sunday():
    print("9:30-??:??\t *****\t\t Classroom1")
    print("Clubs")


if d == "Sunday":
    Sunday()
elif d == "Monday":
    Monday()
elif d == "Tuesday":
    Tuesday()
elif d == "Wednesday":
    Wednesday()
elif d == "Thursday":
    Thursday()
elif d == "Friday":
    Friday()
elif d == "Saturday":
    Saturday()

print("\n")
