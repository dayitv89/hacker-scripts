"""
Find someone in the facebook, I have found my childhood friends.
    $ python find_fb.py
"""
print """
If you want to search someone on facebook then enter few details
If you don't have some info like city, age then press return.
Maximum info will fetch more accurate results
"""

name = raw_input("Enter Name: ")
city = raw_input("Enter city: ")
age = raw_input("Enter age group (25-30): ")
sex = raw_input("Enter sex (m/f): ")
print "please make a cup of mocha coffee me, I'm finding..."

print name + ' ' + city + ' ' + age + ' ' + sex
