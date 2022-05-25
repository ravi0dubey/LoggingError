#Logging_exsample.py
import logging as log
log.basicConfig(filename='app1.log',level=log.DEBUG,format ='%(name)s-%(asctime)s-%(levelname)-%(message)s')

#Create Handler
console_log= log.StreamHandler()
console_log.setLevel(log.DEBUG)
format1=log.Formatter('%(name)s-%(asctime)s-%(levelname)-%(message)s')
console_log.setFormatter(format1)

#Create a Custom Logger
log.getLogger('').addHandler(console_log)
log.info('main log')
user1_log = log.getLogger('user1')

user2_log = log.getLogger('user2')
user3_log = log.getLogger('user3')
user4_log = log.getLogger('user4')

user1_log.info('This is from user1')
user2_log.debug('This is from user2')
user3_log.error('This is from user3')
user3_log.critical('This is from user4')
