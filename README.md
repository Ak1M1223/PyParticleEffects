# PyParticleEffects
Ver 0.1. Simple particle generator for pygame

class particle:

surface, x, y, israndom, spread, ptype, grav, drag, image, color = [0,255,255]
  -SURFACE py blit surface output
  -x of particle
  -y of particle
  -israndom, are random calculations are used? Basically if there will be a spread or a trail.
  -ptype, particle types: 0 pixel, 1 line, 2 pixel with gradient to the black, 3 line with gradient to the black.
  -grav, gravity of the object, pixels of down movement per parmove() called.
  -drag, drag, horizontal and vertical per parmove() called.
  -image, NOT IMPLEMENTED YET.
  -color, self explainatory.

parmove(self):
  Method that should be called every frame for every object. It makes calculations for the object and draws them on the -surface output.
  returns blit surface output.
  
  
  TO DO:
  image support? or animation support.
  optimalization.
  
