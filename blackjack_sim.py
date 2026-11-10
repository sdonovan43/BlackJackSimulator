#!/usr/bin/env python3
"""
Blackjack Simulator with Real Card Graphics, AI Dealer, and Players
"""
 
import random
from enum import Enum
from typing import List, Optional
 
 
class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"
 
 
class Card:
    def __init__(self, suit: Suit, rank: str):
        self.suit = suit
        self.rank = rank
        if rank in ['J', 'Q', 'K']:
            self.value = 10
        elif rank == 'A':
            self.value = 11  # We'll handle Ace as 1 or 11 in the hand
        else:
            self.value = int(rank)
    def __str__(self):
        return f"{self.rank}{self.suit.value}"
    def __repr__(self):
        return self.__str__()
 
 
class Deck:
    def __init__(self, num_decks: int = 1):
        self.cards = []
        self.num_decks = num_decks
        self.reset()
    def reset(self):
        self.cards = []
        for _ in range(self.num_decks):
            for suit in Suit:
                for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
                    self.cards.append(Card(suit, rank))
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_card(self) -> Card:
        if len(self.cards) == 0:
            self.reset()
        return self.cards.pop()
 
 
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card: Card):
        self.cards.append(card)
    def calculate_value(self) -> int:
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
                value += 11
            else:
                value += card.value
        # Adjust for aces (use 1 instead of 11)
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        return value
    def is_busted(self) -> bool:
        return self.calculate_value() > 21
    def is_blackjack(self) -> bool:
        return len(self.cards) == 2 and self.calculate_value() == 21
    def __str__(self):
        return f"[{' '.join(str(card) for card in self.cards)}] (Value: {self.calculate_value()})"
 
 
class Player:
    def __init__(self, name: str, is_human: bool = False):
        self.name = name
        self.hand = Hand()
        self.is_human = is_human
        self.chips: float = 1000.0  # Starting chips; supports 3:2 payouts
        self.bet = 0
    def place_bet(self, amount: int) -> bool:
        if amount <= self.chips:
            self.bet = amount
            self.chips -= amount
            return True
        return False
    def clear_hand(self):
        self.hand = Hand()
    def __str__(self):
        return f"{self.name}: {self.hand} (Chips: {self.chips}, Bet: {self.bet})"
 
 
class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
        self.is_human = False
    def should_hit(self) -> bool:
        # Dealer hits until 17 or higher
        return self.hand.calculate_value() < 17
    def play_turn(self, deck: Deck):
        print(f"\n{self.name}'s turn:")
        while self.should_hit():
            card = deck.deal_card()
            self.hand.add_card(card)
            print(f"Dealer hits and draws {card}")
            print(f"Dealer's hand: {self.hand}")
            if self.hand.is_busted():
                print("Dealer busts!")
                return
        print(f"Dealer stands with {self.hand}")
 
 
class BlackjackGame:
    def __init__(self, num_ai_players: int = 3, add_manual_player: bool = True):
        self.deck = Deck(num_decks=6)  # Use 6 decks for casino-style game
        self.players: List[Player] = []
        self.dealer = Dealer()
        self.add_players(num_ai_players, add_manual_player)
        self.game_stats = {
            'games_played': 0,
            'player_wins': 0,
            'dealer_wins': 0,
            'pushes': 0
        }
    def add_players(self, num_ai_players: int, add_manual_player: bool):
        # Add AI players
        for i in range(num_ai_players):
            self.players.append(Player(f"AI Player {i+1}"))
        # Add manual player if requested
        if add_manual_player:
            self.players.append(Player("Human Player", is_human=True))
    def deal_initial_cards(self):
        # Deal 2 cards to each player and dealer
        for _ in range(2):
            for player in self.players:
                card = self.deck.deal_card()
                player.hand.add_card(card)
            # Dealer gets one card face down (we'll handle this in show_hands)
            card = self.deck.deal_card()
            self.dealer.hand.add_card(card)
    def place_bets(self):
        print("=== Betting Phase ===")
        for player in self.players:
            if player.is_human:
                while True:
                    try:
                        bet_amount = int(input(f"{player.name}, you have {player.chips} chips. How much would you like to bet? "))
                        if player.place_bet(bet_amount):
                            print(f"{player.name} bets {bet_amount} chips.")
                            break
                        else:
                            print("Insufficient chips!")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                # AI players bet 100 chips (simple AI strategy)
                player.place_bet(100)
                print(f"{player.name} bets 100 chips.")
    def show_hands(self, hide_dealer_card: bool = True):
        print("\n=== Current Hands ===")
        # Show dealer's cards
        if hide_dealer_card:
            hidden_hand = "[??] " + " ".join(str(card) for card in self.dealer.hand.cards[1:])
            print(f"Dealer: {hidden_hand} (Value: ??)")
        else:
            print(f"Dealer: {self.dealer.hand}")
        # Show player hands
        for player in self.players:
            if not player.is_human:
                print(f"{player.name}: {player.hand}")
            else:
                print(f"{player.name}: {player.hand}")
    def player_turn(self, player: Player):
        if player.is_human:
            print(f"\n{player.name}'s turn:")
            self.show_hands()
            while True:
                action = input("Would you like to (h)it or (s)tand? ").lower().strip()
                if action == 'h':
                    card = self.deck.deal_card()
                    player.hand.add_card(card)
                    print(f"You draw {card}")
                    print(f"Your hand: {player.hand}")
                    if player.hand.is_busted():
                        print("You bust!")
                        return False
                elif action == 's':
                    print("You stand.")
                    break
                else:
                    print("Please enter 'h' for hit or 's' for stand.")
        else:
            # AI player logic (simple strategy - hit until 16 or higher)
            print(f"\n{player.name}'s turn:")
            hand_value = player.hand.calculate_value()
            while hand_value < 17:
                card = self.deck.deal_card()
                player.hand.add_card(card)
                hand_value = player.hand.calculate_value()
                print(f"{player.name} hits and draws {card}")
                if player.hand.is_busted():
                    print(f"{player.name} busts!")
                    return False
            print(f"{player.name} stands.")
        return True
    def dealer_turn(self):
        self.dealer.play_turn(self.deck)
    def calculate_winnings(self, player: Player, dealer_busted: bool):
        if player.hand.is_busted():
            # Player busts, loses their bet
            return 0
        elif player.hand.is_blackjack() and not self.dealer.hand.is_blackjack():
            # Player has blackjack and dealer doesn't - 3:2 payout
            return player.bet * 2.5
        elif dealer_busted or player.hand.calculate_value() > self.dealer.hand.calculate_value():
            # Player wins
            return player.bet * 2
        elif player.hand.calculate_value() == self.dealer.hand.calculate_value():
            # Push - bet returned
            return player.bet
        else:
            # Dealer wins
            return 0
    def play_round(self):
        print("\n" + "="*50)
        print("NEW BLACKJACK ROUND")
        print("="*50)
        # Reset hands
        self.dealer.clear_hand()
        for player in self.players:
            player.clear_hand()
        # Place bets
        self.place_bets()
        # Deal initial cards
        self.deal_initial_cards()
        # Show initial hands (dealer's second card is hidden)
        self.show_hands(hide_dealer_card=True)
        # Player turns
        for player in self.players:
            if not player.hand.is_busted():
                can_continue = self.player_turn(player)
                if not can_continue:
                    player.clear_hand()
        # Dealer turn
        self.dealer_turn()
        # Check who wins
        dealer_busted = self.dealer.hand.is_busted()
        print("\n" + "="*30)
        print("FINAL RESULTS")
        print("="*30)
        self.show_hands(hide_dealer_card=False)
        # Update game statistics and distribute chips
        for player in self.players:
            winnings = self.calculate_winnings(player, dealer_busted)
            if winnings > 0:
                player.chips += winnings
                if winnings == player.bet * 2.5:  # Blackjack win
                    print(f"{player.name} wins with blackjack! (3:2 payout)")
                elif winnings == player.bet * 2:  # Normal win
                    print(f"{player.name} wins {winnings - player.bet} chips!")
                else:  # Push
                    print(f"{player.name} pushes. Bet refunded.")
            else:
                if not player.hand.is_busted():
                    print(f"{player.name} loses {player.bet} chips.")
                else:
                    print(f"{player.name} busts and loses {player.bet} chips.")
        # Update game statistics
        self.game_stats['games_played'] += 1
        print("\n" + "="*30)
        print("Game Statistics:")
        print("="*30)
        print(f"Games played: {self.game_stats['games_played']}")
        # Show chip balances after the round
        for player in self.players:
            print(f"{player.name}: {player.chips} chips")
    def show_game_stats(self):
        print("\n" + "="*30)
        print("GAME STATISTICS")
        print("="*30)
        print(f"Games played: {self.game_stats['games_played']}")
        if self.game_stats['games_played'] > 0:
            win_percentage = (self.game_stats['player_wins'] / self.game_stats['games_played']) * 100
            print(f"Player win percentage: {win_percentage:.2f}%")
    def play(self):
        print("Welcome to Blackjack Simulator!")
        print("You can choose how many AI players you want and whether you want to join as a manual player.")
        while True:
            self.play_round()
            # Ask if user wants to continue
            continue_game = input("\nWould you like to play another round? (y/n): ").lower().strip()
            if continue_game != 'y':
                break
        print("Thanks for playing!")
        self.show_game_stats()
 
 
def main():
    print("Blackjack Simulator Setup")
    print("-" * 30)
    # Get number of AI players
    while True:
        try:
            num_ai_players = int(input("How many AI players would you like? (0-5): "))
            if 0 <= num_ai_players <= 5:
                break
            else:
                print("Please enter a number between 0 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    # Ask if user wants to be a player
    add_manual_player = input("Would you like to play as a manual player? (y/n): ").lower().strip() == 'y'
    # Create and start the game
    game = BlackjackGame(num_ai_players, add_manual_player)
    game.play()
 
 
if __name__ == "__main__":
    main()