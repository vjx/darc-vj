#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

"""
Simple Sprite objects fall across the screen and are moved back to the top once
they hit the bottom edge.
"""

import random, time

import demo
import pi3d

# Set last value (alpha) to zero for a transparent background!
BACKGROUND = (0.0, 0.0, 0.0, 1.0)

# Setup display and initialise pi3d and a shader.
DISPLAY = pi3d.Display.create(background=BACKGROUND, frames_per_second=25)
SHADER = pi3d.Shader('uv_flat')

TEXTURE = pi3d.Texture('textures/space_invaders256x256.png')
BERRY_COUNT = 27

# Setup array of random x,y,z coords and initial rotation
RASPBERRIES = []

for b in range(BERRY_COUNT):
  # Select size as a random number 0.2 and 2.1.
  size = random.uniform(0.1, 0.9)
  rasp = pi3d.ImageSprite(texture=TEXTURE, shader=SHADER, w=size, h=size)

  # distance from the camera.
  dist = random.uniform(2.0, 9.0)
  rasp.position(random.uniform(-1.0, 1.0) * dist,
                random.uniform(0.0, 4.0) * dist,
                dist)
  rasp.rotateToZ(random.uniform(0.0, 360.0))

  RASPBERRIES.append(rasp)
  DISPLAY.add_sprites(rasp)

# Fetch key presses
KEYBOARD = pi3d.Keyboard()

while DISPLAY.loop_running():
  for b in RASPBERRIES:
    b.translateY(-0.1)
    b.rotateIncZ(1)
    if b.y() < -2 * b.z():
      b.positionX((random.uniform(0.0, 2.0) - 1) * b.z())
      b.translateY(4.0 * b.z())

  k = KEYBOARD.read()
  if k >-1:
    if k == 27:
      KEYBOARD.close()
      DISPLAY.stop()
      break
    elif k == 112:
      pi3d.screenshot('IvaderRain-2.jpg')

