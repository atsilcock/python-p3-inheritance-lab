#!/usr/bin/env python

from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Initial knowledge"]

    def teach(self, learned_information=None):
        if learned_information is None:
            learned_information = "Deault Knowledge"
        self.knowledge.append(learned_information)
        return learned_information
        