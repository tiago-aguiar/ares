#!/bin/bash

ps aux |grep gunicorn |grep ares | awk '{ print $2 }' |xargs kill -HUP
