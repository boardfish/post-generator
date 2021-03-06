from textwrap import dedent
import datetime
import sys
import subprocess
import os
import re  # as reeeeeeeee


def to_kebab_case(string):
    string = re.sub(r'[^\w\s]', '', string)
    string = re.sub('\s+', '-', string)
    return string.lower()


def create_announcement_file(post):
    post_header = """---
layout: post
title: %s
summary: %s
prompt: Learn More
image: %s
image_description: %s
games: %s
categories: %s
event:
  date: %s %s
  location: %s
  facebook_link: %s
  ticket_link: %s
---

%s
        """ % (
        post['title'],
        post['summary'],
        post['image'],
        post['image_description'],
        post['games'],
        ' '.join(post['categories'].split()),
        post['event']['date'].strftime("%Y-%m-%d"),
        post['event']['date'].strftime("%H:%M"),
        post['event']['location'],
        post['event']['facebook_link'],
        post['event']['ticket_link'],
        post['content']
    )
    post_header = dedent(post_header)
    filename = '../{}/_posts/{}-{}.html'.format(
        'website',
        datetime.datetime.now().strftime("%Y-%m-%d"),
        to_kebab_case(post['title'])
    )
    md_file = open(filename, 'w')
    md_file.write(post_header)
    md_file.close()
    build = subprocess.Popen('make build'.split(), cwd='../website')
    build.wait()
