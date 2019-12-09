#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

print json.dumps({
    "_meta": {
        "hostvars": {
            "test0.na.example.net": {
                "region": "NA",
                "data_center": "FDC",
                "environment": "LAB",
                "baseline": "2019q3",
                "owning_group": "TESTGROUP1"
            },
            "test1.apac.example.net": {
                "region": "ASPAC",
                "data_center": "LAB",
                "environment": "LAB",
                "baseline": "2019q4",
                "owning_group": "TESTGROUP2"
            },
            "test2.latam.example.net": {
                "region": "LATAM",
                "data_center": "LAB",
                "environment": "LAB",
                "owning_group": "TESTGROUP3"
            },
            "test3.aus.example.net": {
                "region": "AUS",
                "data_center": "LAB",
                "environment": "LAB",
                "owning_group": "TESTGROUP3"
            }
        }
    },
    "all": {
        "hosts": ["test0.na.example.net","test1.apac.example.net","test2.latam.example.net","test3.aus.example.net"]
    }    
}, indent=4)
