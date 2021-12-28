# reads files from openflights, spits out dictionary of flights: origin to destination
import sys
import json

ifile = sys.argv[1]

flights = {}

with open(ifile,'r') as f:
  for line in f.readlines():
    tokens = line.strip().split(',')
    origin = tokens[2]
    destination = tokens[4]
    if origin not in flights:
      flights[origin] = set()
    flights[origin].add(destination)
flights = {key: list(value) for key, value in flights.items()}

print(flights)
