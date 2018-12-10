N, M, K = [ int(x) for x in input().split(' ') ]

flights = []
all_found_passengers = list(range(1, N+1))

def construct_arrays(source, destination):
  added = False
  if len(flights) == 0:
    flights.append(sorted([source, destination]))
    all_found_passengers.remove(source)
    all_found_passengers.remove(destination)
  else:
    found_counter = 0
    previous_found_index = 0
    for index, value in enumerate(flights):
      if source in flights[index] or destination in flights[index]:
        found_counter += 1
        added = True
        if (found_counter == 1):
          flights[index] = list(set(sorted(flights[index] + [source, destination])))
          previous_found_index = index
        elif (found_counter > 1):
          flights[previous_found_index] = sorted(list(set(sorted(flights[previous_found_index] + flights[index] + [source, destination]))))
          flights.remove(flights[index])
        try:
          all_found_passengers.remove(source)
        except:
          pass
        try:
          all_found_passengers.remove(destination)
        except:
          pass #shouldn't pass silently
    if not added:
      flights.append(sorted([source, destination]))
      all_found_passengers.remove(source)
      all_found_passengers.remove(destination)

for i in range(M):
  source, destination = [ int(x) for x in input().split(' ') ]
  construct_arrays(source, destination)

gift_voucher_passenger = []
if K == 1:
  gift_voucher_passenger = all_found_passengers
counter = len(gift_voucher_passenger)
# print (flights)
# print (gift_voucher_passenger)
for flight in flights:
  try:
    gift_voucher_passenger.append(sorted(flight)[K-1])
    counter += 1
  except:
    pass #shouldn't pass silently 

print(counter)
print(sorted(gift_voucher_passenger), sep=' ', end='', flush=True)