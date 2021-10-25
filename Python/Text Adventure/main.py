import random
import time


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

    def getSuit(self):
        return self.suit

    def getVal(self):
        return self.value


class Deck(object):
    def __init__(self):
        self.__cards = []
        self.__build()

    def __build(self):
        for a in range(4):
            for s in ["Blue", "Green", "Red", "Yellow"]:
                for v in range(1, 7):
                    self.__cards.append(Card(s, v))

        # for s in ["BlueChangeDirection", "GreenChangeDirection", "RedChangeDirection", "YellowChangeDirection",
        #           "BlueSkipNextPerson", "GreenSkipNextPerson", "RedSkipNextPerson", "YellowSkipNextPerson"]:
        #     for v in range(1, 3):
        #         self.__cards.append(Card(s, 0))
        #
        # for s in ["BluePlusTwo", "GreenPlusTwo", "RedPlusTwo", "YellowPlusTwo"]:
        #     for v in range(1, 3):
        #         self.__cards.append(Card(s, 0))

        for s in ["PlusFour"]:
            for v in range(1, 4):
                self.__cards.append(Card(s, 0))

        for s in ["ChangeColor"]:
            for v in range(1, 8):
                self.__cards.append(Card(s, 0))

    def show(self):
        for c in self.__cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.__cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.__cards[i], self.__cards[r] = self.__cards[r], self.__cards[i]

    def drawCard(self):
        return self.__cards.pop(0)


class Player(object):
    def __init__(self, __name, __block):
        self.__name = __name
        self.__hand = []
        self.__block = __block

    def drawDeck(self, __deck):
        self.__hand.append(__deck.drawCard())

    def drawFromPlayer(self, __player, __card):
        __player.getHand().append(__card)

    def showHand(self):
        i = 0
        for card in self.__hand:
            print(str(i) + ": ")
            i = i + 1
            card.show()

    def discardOnBlock(self, __card):
        self.__hand.remove(__card)
        block.putCardOnBlock(__card)
        return __card

    def getName(self):
        return self.__name

    def getHand(self):
        return self.__hand

    def discardToOtherPlayer(self, __card, __aimPlayer):
        self.__hand.remove(__card)
        __aimPlayer.drawFromPlayer(__aimPlayer, __card)


class Block(object):
    def __init__(self, deck):
        self.__deck = deck
        self.__block = []

    def drawFirstCard(self):
        self.__block.append(self.__deck.drawCard())

    def showBlock(self):
        for card in self.__block:
            card.show()

    def putCardOnBlock(self, __card):
        self.__block.append(__card)

    def getBlock(self):
        return self.__block

    def getCardOnTop(self):
        return self.__block[len(self.__block) - 1]


deck = Deck()
deck.shuffle()
block = Block(deck)
block.drawFirstCard()

bob = Player("Bob", block)
jeff = Player("Jeff", block)
bill = Player("Bill", block)
player = Player("Player", block)
bot = Player("Bot", block)

numberOfHandCards = int(input("Wie viele Karten soll jeder kriegen? "))
for i in range(numberOfHandCards):
    player.drawDeck(deck)
    bot.drawDeck(deck)


def botsTurn():
    cards = bot.getHand()

    isSolved = False
    suit = block.getCardOnTop().getSuit()
    val = block.getCardOnTop().getVal()
    for card in cards:
        x = card.getSuit()
        y = card.getVal()

        if suit == x:
            # print("suit == x")
            bot.discardOnBlock(card)
            isSolved = True
            break
        elif val == y:
            # print("val == y")
            bot.discardOnBlock(card)
            isSolved = True
            break

    if not isSolved:
        for card in cards:
            y = card.getVal()
            if y == 0:
                # print("y == 0")
                specialCard(card, bot, player)
                bot.discardOnBlock(card)
                for a in cards:
                    if a.getVal() != 0:
                        color = cards[0].getSuit()
                        break

                block.putCardOnBlock(Card(color, -1))
                isSolved = True
                break

    if not isSolved:
        print("Bot not solved, draw card")
        bot.drawDeck(deck)

    if len(cards) == 1:
        print()
        print("Bot: UNO")
    if len(cards) == 0:
        print()
        print("Bot: UNO - UNO - UNO - UNO - UNO - UNO - UNO - UNO")
        print("Bot: UNO - UNO - UNO - UNO - UNO - UNO - UNO - UNO")


def specialCard(__card, __person, __aimPerson):
    cardSuit = __card.getSuit()
    cardVal = __card.getVal()

    if cardSuit in ["BluePlusTwo", "GreenPlusTwo", "RedPlusTwo", "YellowPlusTwo"]:
        for f in range(2):
            __person.discardToOtherPlayer(__card, bot)

    if cardSuit == "PlusFour":
        for s in range(4):
            __aimPerson.drawDeck(deck)
        # color = input("Auf welche Farbe wills du wechseln?")
        # block.putCardOnBlock(Card(color, 0))

    if cardSuit == "ChangeColor":
        print("Change Color")


def checkValid(__card, __blockCardOnTop, __player):
    # print("Check valid")
    blockSuit = __blockCardOnTop.getSuit()
    blockVal = __blockCardOnTop.getVal()
    cardSuit = __card.getSuit()
    cardVal = __card.getVal()
    if blockSuit == cardSuit:
        return True
    elif blockVal == cardVal:
        return True
    elif cardVal == 0:
        print("special card")
        return True
    else:
        return False


while True:
    if bot.getHand() == 0 or player.getHand() == 0:
        break
    print()
    print("Deine Karten: ")
    player.showHand()
    print("----------------------------------------")
    print("Bot Karten: ")
    bot.showHand()
    print("----------------------------------------")
    print("Block Karten: ")
    block.showBlock()
    print("----------------------------------------")
    print()

    isValid = False
    loop = 0
    while not isValid:
        cardNum = input("Welche Karte willst du auf den Block legen? ")
        if cardNum == "":
            print("Karte wird vom Deck gezogen")
            player.drawDeck(deck)
            # print("Deine Karten: ")
            # player.showHand()
            break
        cardNum = int(cardNum)
        card = player.getHand()[cardNum]
        if checkValid(card, block.getCardOnTop(), player):

            cardVal = card.getVal()
            if cardVal == 0:
                specialCard(card, player, bot)
                player.discardOnBlock(card)
                color = input("Auf welche Farbe wills du wechseln?")
                block.putCardOnBlock(Card(color, -1))

            else:
                player.discardOnBlock(card)

            isValid = True
        else:
            print("Das ist leider gegen die Spiel Regeln. Entweder die Farbe oder die Zahl müssen gleich sein. Versuche es nochmal: ")
            isValid = False

    print("Block Karten: ")
    block.showBlock()

    # print("bots turn")
    # print("Bot...")
    time.sleep(0.5)
    botsTurn()
