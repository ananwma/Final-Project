
import random

# EXAMPLE STATE MACHINE
class MantisBrain:

  def __init__(self, body):
    self.body = body
    self.state = 'idle'
    self.target = None

  def handle_event(self, message, details):

    if self.state is 'idle':

      if message == 'timer':
        # go to a random point, wake up sometime in the next 10 seconds
        world = self.body.world
        x, y = random.random()*world.width, random.random()*world.height
        self.body.go_to((x,y))
        self.body.set_alarm(1)

      elif message == 'collide' and details['what'] == 'Slug':
        # a slug bumped into us; get curious
        self.state = 'curious'
        self.body.set_alarm(1) # think about this for a sec
        self.body.stop()
        self.target = details['who']

    elif self.state == 'curious':

      if message == 'timer':
        # chase down that slug who bumped into us
        if self.target:
          if random.random() < 0.5:
            self.body.stop()
            self.state = 'idle'
          else:
            self.body.follow(self.target)
          self.body.set_alarm(1)
      elif message == 'collide' and details['what'] == 'Slug':
        # we meet again!
        slug = details['who']
        slug.amount -= 0.01 # take a tiny little bite 


    
class SlugBrain:

  def __init__(self, body):
    self.body = body
    self.state = 'idle'
    self.target = None
    self.has_resource = False

  def handle_event(self, message, details):
    # TODO: IMPLEMENT THIS METHOD
    #  (Use helper methods and classes to keep your code organized where
    #  approprioate.)
    if message == 'order' and isinstance(details, tuple):
        x, y = details
        self.body.go_to((x,y))
        self.state = 'idle'
        print "moving to (%d, %d)" %(x,y)
    elif message == 'order' and type(details) == str:
        command(self, details)
        print "This slug is", self.state

    #if self.body.amount < .5:
        #self.state = 'fleeing'
        #nearest_nest = self.body.find_nearest('Nest')
        #self.body.go_to(nearest_nest)
        #print "This slug is fleeing"
        #if message == 'collide' and details['what'] == 'Nest':
            #self.body.amount = 1
            #self.state = 'idle'

    #elif self.state is 'idle':
        #self.body.stop

    #elif self.state is 'attacking':
        #self.body.set_alarm(1)
        #if message == 'timer':
            #if self.target is None:
                #print "   Searching for mantis"
                #try: 
                    #nearest_mantis = self.body.find_nearest('Mantis')
                    #self.body.follow(nearest_mantis)
                    #self.target = nearest_mantis
                #except: 
                    #print "all mantises are dead!"
        #elif message == 'collide' and details['what'] == 'Mantis':
            #mantis = details['who']
            #mantis.amount -= 0.05
            #if mantis.amount < 0:
                #self.target = None
                #self.body.set_alarm(1)

    #elif self.state is 'building':
        #nearest_nest = self.body.find_nearest('Nest')
        #self.body.go_to(nearest_nest)
        #if message == 'collide' and details['what'] == 'Nest':
            #nest = details['who']
            #if nest.amount is not 1:
                #nest.amount += 0.01

    #elif self.state is 'harvesting':
        #if self.has_resource is True:
            #nearest_nest = self.body.find_nearest('Nest')
            #self.body.go_to(nearest_nest)
            #if message == 'collide' and details['what'] == 'Nest':
                #self.has_resource = False
        #else:
            #nearest_resource = self.body.find_nearest('Resource')
            #self.body.go_to(nearest_resource)
            #if message == 'collide' and details['what'] == 'Resource':
                #resource = details['who']
                #resource.amount -= 0.25
                #self.has_resource = True

    pass

def command(self, details):
    if details == 'i':
        self.state = 'idle'
    elif details == 'a':
        self.state = 'attacking'
    elif details == 'h':
        self.state = 'harvesting'
    elif details == 'b':
        self.state = 'building'



world_specification = {
  #'worldgen_seed': 0, # comment-out to randomize
  'nests': 1,
  'obstacles': 0,
  'resources': 0,
  'slugs': 1,
  'mantises': 5,
}

brain_classes = {
  'mantis': MantisBrain,
  'slug': SlugBrain,
}
