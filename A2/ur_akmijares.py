#!/usr/bin/env python3

# OPS435 Assignment 2 - Winter 2019
# Program: ur_akmijares.py
# Author: "Antonio Karlo Mijares"
# The python code in this file ur_akmijares.py is original work written by
# Antonio Karlo Mijares. No code in this file is copied from any other source
# including any person, textbook, or on-line resource except those provided
# by the course instructor. I have not shared this python file with anyone
# or anything except for submission for grading.
# I understand that the Academic Honesty Policy will be enforced and violators
# will be reported and appropriate action will be taken.

'''
   authorship declaration

   __author__ Antonio Karlo Mijares
   __date__ March 2019
   __version__ 1.0

   Calculate user usage for the day, week or month
'''

import sys
import os
import argparse
import time


def read_login_rec(filelist):
    ''' docstring for this function
    get records from given filelist
    open and read each file from the filelist
    filter out the unwanted records
    add filtered record to list (login_recs)'''
    # os1 = "pts"
    try:
        fileopen = open(filelist, 'r')
        login_rec = fileopen.read()
        return login_rec
    except FileNotFoundError:
        print("File not found")
        sys.exit()


def cal_daily_usage(subject, login_recs):
    ''' docstring for this function
    generate daily usage report for the given
    subject (user or remote host)'''
    fileopen = open(login_recs, 'r')
    login_recs = fileopen.read()

    if subject.isdigit():
        if subject in login_recs:
            line = login_recs.readline()
            print(line)
    else:
        if subject in login_recs:
            line = login_recs.readline()
            print(line)


# return daily_usage


def cal_weekly_usage(subject, login_recs):
    ''' docstring for this function
    generate weekly usage report for the given
    subject (user or remote host)'''


# return weekly_usage


def cal_monthly_usage(subject, login_recs):
    ''' docstring for this function
    generate monthly usage report fro the given
    subject (user or remote host)'''


# return monthly_usage


# Checks for arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(
        description="Usage report based on the last command")
    parser.add_argument("F",
                        action='store',
                        help="list of files to be processed")
    parser.add_argument("-l", "--list", choices=['user', 'host'],
                        help="generate user name or remote host IP from the given files")
    parser.add_argument("-r", "--rhost",
                        help="usage report for the given remote host IP",
                        action='store',
                        type=str)
    parser.add_argument("-t", "--type",
                        choices=['daily', 'weekly', 'monthly'],
                        help="type of report: daily, weekly and monthly")
    parser.add_argument("-u", "--user",
                        help="usage report for the given user name",
                        action='store',
                        type=str)
    parser.add_argument("-v", "--verbose", help="turn on output verbosity")
    args = parser.parse_args()

    if args.list:
        if args.list == 'user':
            print('1')
        elif args.list == 'host':
            print('2')

    elif args.user:
        if args.type:
            if args.type == 'daily':
                cal_daily_usage(args.type, args.F)
            elif args.type == 'weekly':
                cal_weekly_usage(args.type, args.F)
            elif args.type == 'monthly':
                cal_monthly_usage(args.type, args.F)
    elif args.rhost:
        if args.type:
            if args.type == 'daily':
                cal_daily_usage(args.type, args.F)
            elif args.type == 'weekly':
                cal_weekly_usage(args.type, args.F)
            elif args.type == 'monthly':
                cal_monthly_usage(args.type, args.F)
