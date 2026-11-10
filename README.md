# Blackjack Simulator

## Overview
A complete Python implementation of the classic Blackjack card game with advanced simulation capabilities for strategy testing and performance analysis.

## Features

### Core Gameplay
- **Standard Blackjack Rules**: Dealer hits until 17 or higher, proper Ace handling (1/11 values)
- **Chip System**: Realistic betting with chip management
- **Hand Evaluation**: Accurate card counting with bust detection
- **Win/Loss Tracking**: Complete game statistics

### Enhanced Simulation Capabilities
- **Automated Testing**: Run thousands of games without manual input
- **Comprehensive Analytics**: Track wins, losses, busts, pushes, and blackjacks  
- **Performance Insights**: Analyze strategy effectiveness through data
- **Pretty Tracking Interface**: Clear console output with progress indicators
- **Game Mode Selection**: Switch between manual and automated gameplay

### Technical Implementation
- **Object-Oriented Design**: Clean separation of Card, Deck, Hand, Player, Dealer classes
- **No External Dependencies**: Pure Python standard library implementation
- **Extensible Architecture**: Easy to add new features or strategies

## Getting Started

### Prerequisites
```bash
Python 3.6+
```

### Installation
```bash
# Clone the repository
git clone https://github.com/sdonovan43/BlackJackSimulator.git
cd BlackJackSimulator
```

## Usage

Run the game:
```bash
python blackjack_sim.py
```

### Game Modes
1. **Manual Gameplay** (Interactive): 
   - Play against AI dealers manually
   - Real-time decision making
2. **Simulation Mode**: 
   - Automated gameplay runs
   - Statistical analysis of results
   - Batch testing of strategies

### Example Workflow
```bash
How many AI players would you like? (0-5): 3
Would you like to play as a manual player? (y/n): y

Choose mode:
1. Manual gameplay (interactive)
2. Simulation mode (automated)

Select mode (1 or 2): 2
How many simulation rounds would you like to run? 1000
```

## Code Structure

### Core Classes
- **Card**: Individual playing cards with suit/rank/value representation  
- **Deck**: Card management with shuffling and deal functionality
- **Hand**: Card collections with value calculations and bust detection
- **Player**: Base class for all game participants 
- **Dealer**: AI dealer implementing standard rules
- **BlackjackGame**: Main game controller managing flow and state

### Enhanced Classes  
- **SimulationStats**: Comprehensive tracking of game outcomes
- **SimulationRunner**: Automated gameplay execution engine
- **Enhanced Player/Dealer**: Extended functionality for simulation mode

## Game Rules

- 6-deck standard Blackjack
- Dealer hits until 17 or higher
- Natural Blackjacks pay 3:2 payout
- All other wins pay 2:1 
- Busts lose the entire bet
- Dealer busts win for remaining players

## Example Output

### Interactive Mode
```
NEW ROUND
==================================================
=== Betting Phase ===
AI Player 1 bets 100 chips
AI Player 2 bets 100 chips  
Human Player bets 100 chips
Dealer: 7♠ ? (Hidden cards)
AI Player 1: [Q♥ 8♦] (Value: 18)
AI Player 2: [A♠ 5♣] (Value: 16) 
Human Player: [9♥ 3♠ A♠ 3♦ Q♠] (Value: 26)
You bust!
```

### Simulation Mode
```
Running Simulation Mode...
------------------------------
How many simulation rounds would you like to run? 1000
Completed 100 rounds...
Completed 200 rounds...
==================================================
Simulation Completed!
==================================================
SIMULATION RESULTS SUMMARY
==================================================
Total games played: 1000
Player wins: 442 (44.20%)
Dealer wins: 453 
Pushes: 105
Player busts: 298
Dealer busts: 192
Blackjacks: 78

Thanks for playing!
==============================
GAME STATISTICS
==============================
Games played: 1000
Player win percentage: 44.20%
```

## Contributing

This project serves as an educational demo for Python object-oriented programming concepts and game development. Enhancements are welcome including:

- Additional AI betting strategies
- Card counting system implementation  
- Advanced statistical analysis tools
- Web-based user interface

## License

MIT License - feel free to use, modify, and distribute for educational purposes.

---

Now you can copy this content into your `README.md` file in the project directory. This format is clean, professional, and follows GitHub best practices for documentation while maintaining all the key information about your enhanced Blackjack Simulator!