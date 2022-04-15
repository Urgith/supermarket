''' Załóżmy, że mamy supermarket
wchodzi do niego średnio 1 osoba na 30 sekund,
zbieranie towaru z półek waha się między 30 sekundami a 25 minutami,
liczba zakupionych towarów wynosi między 1 a 50 (po 30 sekund na towar),
w sklepie mamy 1 kasjerkę i 1 kasę samoobsługową,
kasjerka jest w stanie 'skasować' przedmiot w ciągu 2 sekund,
na kasie samoobsługowej klienci 'kasują' przedmiot 3 sekundy,
u kasjerki czeka się dodatkowe 20 sekund,
w kasie samoobsługowej czekamy dodatkowe 10 sekund.

Gdy wszedłeś do sklepu 20 klientów czekało przy kasach (po 10 na każdą)
W sklepie 40 ludzi zbierało towary
Chcesz zakupić 40 przedmiotów (20 minut zbierania)

Zadecyduj, czy możesz kupić wszystkie przedmioty, jeżeli masz 25 min,
jeżeli nie, ile maksymalnie możesz ich kupić.

Dla uproszczenia załóżmy, że:
- klienci z tak samo często kupują każdą ilość dóbr
- klienci zawsze wybierają kasę z mniejszą liczbą ludzi, Ty też
  (jeżeli są takie same, wybiorą losowo)
- klienci, którzy byli w sklepie, dopiero do niego weszli
'''
import random
import zad1


def summ(queue, started_sum):
  ''' function which calculate time of all people from queue to be served
    Arguments:
      queue - choosed queue
    return: remaining time to be served
  '''
  sum = started_sum

  for i in range(queue.size()):
    number = queue.dequeue()
    queue.enqueue_second(number)
    sum += number

  return sum


class Queue(zad1.Queue_end_on_end):
  ''' class of queue, inherit from Queue_end_on_end
    Defined methods:
      __init__ - constructor of this class, it initialize empty queue and modifiers
      enqueue - method which add element to queue without modifiers
      enqueue_second - method which add element to queue without modifiers
      waiting - method which simulate 1 second of time in queue
      checking - method which check if firs element in queue is 0 (client has been served)

    Inherited methods:
      __str__ - method which returns string representation of queue
      dequeue - method which pull element from beginning of queue
      isEmpty - method which check if queue is empty
      size - method which calculate size of queue
  '''
  def __init__(self, need_time, extra_time):
    ''' constructor of the class, initialize empty queue as python list and modifiers of waiting time
      Arguments:
        need_time - time to check one item for cash
        extra_time - additional time to be served
      return: None
    '''
    self.extra_time = extra_time
    self.need_time = need_time
    self.items = []

  def enqueue(self, item):
    ''' function which append element on end of queue
      Arguments:
        item - element added on end of queue after multiplaying by multipliers of cash
      return: None
    '''
    self.items.append(item*self.need_time + self.extra_time)

  def enqueue_second(self, item):
    ''' function which append element on end of queue
      Arguments:
        item - element added on end of queue without multiplaying by multipliers of cash
      return: None
    '''
    self.items.append(item)

  def waiting(self):
    ''' function which simulate 1 second in queue, it substract 1 second from beginning of queue
      return: None
    '''
    self.items[0] -= 1

  def checking(self):
    ''' function which check if first element of queue is 0
      return: True, if first element is 0
      return: False, if first element is not 0
    '''
    return not self.items[0]


def market(enter_time=30, time_f_good=30, max_goods=50, cashier_time=2, auto_time=3, add_c_time=20,
           add_a_time=10, cashes=10, beg_people=40, you_goods=40, max_time=30):
  ''' function which check how many goods can you buy in market in limited time
    Arguments:
      enter_time - positive integer which tell us how many seconds on average a new customer enters the store
      time_f_good - positive integer which tell us how long in seconds it takes to pick one good
      max_goods - positive integer which tell us how many goods customer can buy the most
      cashier_time - non negative integer which tell us how long in seconds it takes to check one good for cashier
      auto_time - non negative integer which tell us how long in seconds it takes to check one good for us
      add_c_time - non negative integer which tell us how long in seconds it takes to pay in cashier
      add_a_time - non negative integer which tell us how long in seconds it takes to pay in auto cash
      cashes - non negative integer which tell us how many people were on cashier and auto cash on beginning
      beg_people - non negative integer which tell us how many people were in store at beginning
      you_goods - positive integer which tell us now many goods you'll buy
      max_time - non negative integer which tell us how many minutes you can spend on buying goods

    return: list with 2 values:
      1) True, if you can buy everything on time
      1) False, if you can not buy everything on time
      2) The most goods you can buy
  '''
  # exceptions
  if type(enter_time) != int:
    raise TypeError('enter_time can be only integer')
  elif enter_time <= 0:
    raise ValueError('enter_time must be positive')

  elif type(time_f_good) != int:
    raise TypeError('time_for_good can be only integer')
  elif time_f_good <= 0:
    raise ValueError('time_for_good must be positive')

  elif type(max_goods) != int:
    raise TypeError('max_goods can only be integer')
  elif max_goods <= 0:
    raise ValueError('max_goods must be positive')

  elif type(cashier_time) != int:
    raise TypeError('cashier_time can only be integer')
  elif cashier_time < 0:
    raise ValueError('cashier_time can not be negative')

  elif type(auto_time) != int:
    raise TypeError('auto_time can only be integer')
  elif auto_time < 0:
    raise ValueError('auto_time can not be negative')

  elif type(add_c_time) != int:
    raise TypeError('add_cashier_time can only be integer')
  elif add_c_time < 0:
    raise ValueError('add_cashier_time can not be negative')

  elif type(add_a_time) != int:
    raise TypeError('add_auto_time can only be integer')
  elif add_a_time < 0:
    raise ValueError('add_auto_time can not be negative')

  elif type(cashes) != int:
    raise TypeError('cashes can only be integer')
  elif cashes < 0:
    raise ValueError('cashes can not be negative')

  elif type(beg_people) != int:
    raise TypeError('beg_people can only be integer')
  elif beg_people < 0:
    raise ValueError('beg_people can not be negative')

  elif type(you_goods) != int:
    raise TypeError('you_goods can only be integer')
  elif you_goods <= 0:
    raise ValueError('you_goods must be positive')

  elif type(max_time) != int:
    raise TypeError('max_time can only be integer')
  elif max_time <= 0:
    raise ValueError('max_time must be positive')

  queue_cashier = Queue(cashier_time, add_c_time)
  queue_auto = Queue(auto_time, add_a_time)

  # how many goods client buy
  goods = [random.randint(1, max_goods) for i in range(beg_people)]
  time_to_complete = [time_f_good*good for good in goods]

  # clients on queues at beginning
  for i in range(cashes):
    queue_cashier.enqueue(random.randint(1, max_goods))
    queue_auto.enqueue(random.randint(1, max_goods))

  time = 0
  times = []  # time for all clients in queue
  while time <= you_goods*time_f_good:
    # clients are collecting items (remaining time decrese)
    time_to_complete = [t - 1 for t in time_to_complete]

    # checking if somebody entered market
    if not random.randint(0, enter_time - 1):
      rand = random.randint(1, max_goods)
      goods.append(rand)
      time_to_complete.append(time_f_good * rand)

    # serving in cashier queue
    if not queue_cashier.isEmpty():
      queue_cashier.waiting()
      if queue_cashier.checking():
        queue_cashier.dequeue()

    # serving in auto queue
    if not queue_auto.isEmpty():
      queue_auto.waiting()
      if queue_auto.checking():
        queue_auto.dequeue()

    # if new good picked
    if not time%time_f_good:
      people_cashier = queue_cashier.size()
      people_auto = queue_auto.size()

      # determining which queue we choose (shorter)
      if people_cashier > people_auto:
        times.append(summ(queue_auto, time/time_f_good*auto_time + add_a_time))
      elif people_cashier < people_auto:
        times.append(summ(queue_cashier, time/time_f_good*cashier_time + add_c_time))

      else:
        if random.randint(0, 1):
          times.append(summ(queue_auto, time/time_f_good*auto_time + add_a_time))
        else:
          times.append(summ(queue_cashier, time/time_f_good*cashier_time + add_c_time))

    # if somebody picked all goods
    for i, t in enumerate(time_to_complete):
      if t == 0:
        time_to_complete.pop(i)
        people_cashier = queue_cashier.size()
        people_auto = queue_auto.size()

        # determining which queue client choose
        if people_cashier > people_auto:
          queue_auto.enqueue(goods[i])
        elif people_cashier < people_auto:
          queue_cashier.enqueue(goods[i])

        else:
          if random.randint(0, 1):
            queue_auto.enqueue(goods[i])
          else:
            queue_cashier.enqueue(goods[i])

        goods.pop(i)

    time += 1

  # remaining times for every good picked
  remaining_time = [max_time*60 - time_f_good*goods - tim for goods, tim in enumerate(times)]

  # checking how many goods can we buy
  for goods, tim in enumerate(reversed(remaining_time)):
    if tim > 0:
      return not goods, you_goods - goods
  return False, 0


if __name__ == '__main__':
  result = market()

  if result[0]:
    print('You have enough time to buy everything.')
  else:
    print('You can buy only {} goods.'.format(result[1]))
