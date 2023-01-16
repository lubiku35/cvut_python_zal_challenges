import random

class Dealer:
  def __init__(self):
    # s - srdce / heart
    # g - gula / diamond
    # z - zalud / clubs
    # l - list / spades
    self.deck = [
      '♥A', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
      '♦A', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
      '♣A', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
      '♠A', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K'
    ]

    self.players = []

  # shuffle cards
  def shuffle(self):
    # can't use random.shuffle
    tmp = []
    for i in range(len(self.deck)):
      choice = random.choice(self.deck)
      tmp.append(choice)
      self.deck.remove(choice)
    self.deck = tmp
    return self.deck

  # take card from deck
  def deal(self, n):
    tmp = []
    if n <= len(self.deck):
      for i in range(n):
        tmp.append(self.deck[i])
      self.deck = self.deck[n:]
      return tmp
    else:
      return self.deck
  
  # add player to the list of players
  def addPlayer(self, player):
    return self.players.append(player)
      
  # remove player to the list of players
  def removePlayer(self, player):
    return self.players.remove(player)


  # start round
  def startRound(self):
    more = True                                   
    while more:
      print('--- rozdavam  ---')
      more = False      
      for player in self.players:
        if player.needsCard():                # if any of players wants card "more" becomes true and continue
          player.acceptCard(self.deal(1))
          more = True
          if len(self.deck) == 0:             # empty deck
            print('Dosli karty')
            return
    self.announceWinner()

  # bubblesort algorithm to sort winner
  def bubbleSort(self, res):
    count = len(res);
    for j in range(count - 1, 0, -1):
        swaps = False
        for i in range(j):
            if res[i]['points'] < res[i + 1]['points']:
                res[i], res[i + 1] = res[i + 1], res[i]
                swaps = True
        if not swaps:
            break
    
  def announceWinner(self):
    print('--- kolo skončilo ---')
    results = []
    for player in self.players:
        points = player.getHandValue();
        # cant have more than 21
        if points > 21:
            points = 0
        results.append({'name': player.name, 'points': points})
    self.bubbleSort(results) # sorting results
    print('Hráč', results[0]['name'], 'vyhrává so ziskom', results[0]['points'], 'bodov')
    for i in range(1, len(results)):
        if results[i]['points'] == results[0]['points']:
            print('Vyhrává také hráč', results[i]['name'], 'so ziskom', results[i]['points'], 'bodov')
        else:
            print('Hráč', results[i]['name'], 'získal', results[i]['points'], 'bodov')
    print('-----------------')
      

class Player:
  def __init__(self, name, strategy):
    self.name = name
    self.strategy = strategy
    self.hand = []

  # value of cards
  def getHandValue(self):
    points = 0
    for i in self.hand:
      if i.endswith('7'):
        points += 7
      elif i.endswith('8'):
        points += 8
      elif i.endswith('9'):
        points += 9
      elif i.endswith('10'):
        points += 10
      elif i.endswith('J') or i.endswith('Q') or i.endswith('K'):
        points += 1
      elif i.endswith('A'):
        points += 11
    return points

  def acceptCard(self, cards):
    self.hand.extend(cards)
    print(self.listCards())

  # strategies
  def needsCard(self):
    if self.strategy == 'Cautious':
      return True if self.getHandValue() <= 10 else False
    if self.strategy == 'Bold':
      return True if self.getHandValue() <= 15 else False
    if self.strategy == 'Human':
      human_input = input(f"{self.listCards()} v hodnote {self.getHandValue()}, chce ďaľšie (A/N)? : ")
      return True if human_input.upper() == 'A' else False

  # list cards on hand
  def listCards(self):
    str = self.name + ' má aktuálne karty: '
    for card in self.hand:
      str += card + ' '
    return str

# TEST GAME

newDealer = Dealer()

player1 = Player('Človek Človečí', 'Human')
player2 = Player('Vilda Vopatrný', 'Cautious')
player3 = Player('Olda Odvážny','Bold')

newDealer.addPlayer(player1)
newDealer.addPlayer(player2)
newDealer.addPlayer(player3)

newDealer.shuffle()
newDealer.startRound()

