# Importing Base Modules
import os
import logger

import core.sound_manager as soundmanager
from core.base_functions import match, activate
from core.action_listener import begin

while True:
    active = activate()
    if active: begin()