from enum import Enum

class Education(Enum):
    high_school     = 1
    some_college    = 2
    bachelor        = 3
    master          = 4
    phd             = 5
    dont_care       = 99

class Employment(Enum):
    unemployment    = 1
    employed        = 2
    self_employed   = 3
    retired         = 4
    student         = 5
    part_time       = 6
    dont_care       = 99