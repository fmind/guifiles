#!/usr/bin/env python3

from splinter import Browser

browser = Browser('chrome')
browser.visit('https://www.google.com')
browser.fill('q', 'splinter doc site\n')
