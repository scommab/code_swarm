
import datetime
import time
import uuid
import random
import string

NUM_DEV = 15
NUM_DAYS = 100
FILES_PER_CL = 10
CL_PER_DAY = 5
CODE_SECTIONS = ["docs", "src1", "src2", "src3"]
FILES_PER_SECTION = 100

header = '<?xml version="1.0"?> <file_events>'
footer = '</file_events>'
template = '<event date="%s" filename="%s" author="%s" />'

def makeEntry(date, filename, person):
  d = int(time.mktime(date.timetuple())*1000)
  return template % (d, filename, person.name)

class Developer(object):
  def __init__(self, name=None):
    self.name = name
    if not self.name:
      # pick a random name
      self.name = ''.join(random.choice(string.ascii_uppercase) for x in range(6))
    self.files = []

  def addFiles(self, files):
    self.files.extend(files)

  def randomFiles(self):
    file_count = random.randint(1, FILES_PER_CL)
    cl = set()
    for i in range(file_count):
      cl.add(random.choice(self.files))
    return cl
    

files = {}
all_files = []
for s in CODE_SECTIONS:
  files[s] = []
  for i in range(FILES_PER_SECTION):
    fn = "%s/%s" % (s, uuid.uuid4())
    files[s].append(fn)
    all_files.append(fn)

people = []
for i in range(NUM_DEV):
  p = Developer()
  for j in range((random.randint(10, 23) / 10)):
    fs = files[random.choice(CODE_SECTIONS)]
    p.addFiles(fs)
  people.append(p)


d = datetime.datetime.now()
events = []
for i in range(NUM_DAYS):
  for check_ins in range(CL_PER_DAY):
    p = random.choice(people)
    fs = p.randomFiles()
    for f in fs:
      events.append(makeEntry(d, f, p))
  d += datetime.timedelta(days=1)

print header
print "\n".join(events)
print footer
