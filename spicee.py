import csv
import random

class MerchantCard:
	def __init__(self, left, right, upgrade, kind):
		self.left = left
		self.right = right
		self.upgrade = upgrade
		self.kind = kind

	def __repr__(self):
		return(self.kind+" "+self.left + "->"+ self.right+" "+str(self.upgrade))

class VPCard:
	def __init__(self, spices, points):
		self.spices = spices
		self.points = points

	def __repr__(self):
		return(self.spices+" "+self.points)


class Player:
	def __init__(self, spices, vpCards, merchantCardsUp, merchantCardsDown, bonusTokens, ordering):
		self.spices = spices
		self.vpCards = vpCards
		self.merchantCards = merchantCards
		self.bonusTokens = bonusTokens
		self.ordering = ordering

	def __repr__(self):
		return(str(self.ordering)+" "+str(self.spices))

class Spicee:
	def __init__(self, allVpCards, allMerchantCards, players):
		self.allVpCards = allVpCards
		random.shuffle(self.allVpCards)
		self.allMerchantCards = allMerchantCards
		random.shuffle(self.allMerchantCards)
		self.players = players
		self.bonusTokens = {"1": len(players)*2, "3": len(players)*2}
		self.turnNumber = 1
		self.currPlayer = 0

	def buyVpCard(self, cardNum):
		self.players[self.currPlayer].vpCards.append(self.allVpCards.pop(cardNum))

	def __repr__(self):
		return(str(self.turnNumber)+" "+str(self.currPlayer))

allMerchantCards = []
with open('merchant.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	idx = 0
	for row in spamreader:
		idx+=1
		if (idx == 1):
			continue
		upgrade = 0
		if ("Upgrade" in row[0]):
			upgrade = row[3]
		m = MerchantCard(row[1], row[2], upgrade, row[0])
		allMerchantCards.append(m)

allVpCards2 = []
with open('vp.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	idx = 0
	for row in spamreader:
		idx+=1
		if (idx == 1):
			continue
		upgrade = 0
		m = VPCard(row[0], row[1])
		allVpCards2.append(m)
players = []
for order in range(2):
	initialSpices = {}
	if (order==0):
		initialSpices["Y"] = 3
	elif (order==1):
		initialSpices["Y"] = 3
	merchantCards = allMerchantCards[0:2]
	p = Player(initialSpices, [], merchantCards, [], {}, order)
	players.append(p)

allMerchantCards = allMerchantCards[2:]
game = Spicee(allVpCards2, allMerchantCards, players)
print(game)
print(game.allVpCards)
game.buyVpCard(0)

print(game.players[0].vpCards)
print(game.allVpCards)

