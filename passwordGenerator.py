#!/usr/bin/env python

import random

possibleCharacters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

maxPasswordLength = 12

generatedPassword = "".join(random.sample(possibleCharacters, maxPasswordLength))

print generatedPassword
