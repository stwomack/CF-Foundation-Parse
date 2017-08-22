#!/usr/local/bin/python

import json

with open('status_orig.json') as data_file:
    data = json.load(data_file)

def totals():
    total_apps=0
    total_users=0
    total_ai=0
    total_si=0
    for i in data:
        foundation = i.keys()[0]
        orgs = i[foundation]['orgs'].keys()
        total_ai_in_foundation=0
        total_apps_in_foundation=0
        total_users_in_foundation=0
        total_ai_in_foundation += i[foundation]["total_app_instances"]
        total_apps_in_foundation += i[foundation]["total_apps"]
        total_users_in_foundation += i[foundation]["total_users"]
        total_ai += total_ai_in_foundation
        total_sis_in_foundation=0
        for org in orgs:
            # if org not in ['system', 'p-spring-cloud-services']:
            spaces = i[foundation]['orgs'][org]['spaces'].keys()
            for space in spaces:
                sis = i[foundation]['orgs'][org]['spaces'][space]["service_instances"]
                si_size = len (sis)
                if si_size > 0:
                    total_sis_in_foundation += si_size
        total_apps += total_apps_in_foundation
        total_si += total_sis_in_foundation
        total_users += total_users_in_foundation
        foundation_description = foundation_desc[foundation]
        print "Total AIs " + foundation + ": " + foundation_description + ": " + str(total_ai_in_foundation)
        print "Total Apps " + foundation + ": " +foundation_description + ": " + str(total_apps_in_foundation)
        print "Total SIs " + foundation + ": " +foundation_description + ": " + str(total_sis_in_foundation)
        print "Total Users " + foundation + ": " +foundation_description + ": " + str(total_users_in_foundation)
        print ""
    print "Total AIs: " + str(total_ai)
    print "Total APPs: " + str(total_apps)
    print "Total SIs: " + str(total_si)
    print "Total Users: " + str(total_users)

def print_csv():
    for i in data:
        foundation = i.keys()[0]
        orgs = i[foundation]['orgs'].keys()
        for org in orgs:
            spaces = i[foundation]['orgs'][org]['spaces'].keys()
            for space in spaces:
                for app in i[foundation]['orgs'][org]['spaces'][space]['apps']:
                  # if org not in ['system', 'p-spring-cloud-services']:
                  print foundation + "," + org + "," + space + "," + app
    return

totals()
