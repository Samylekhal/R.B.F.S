const { Battle, Dex, Teams } = require('./showdown/dist/sim');

// Format OU
const format = Dex.formats.get('gen9ou');
const battle = new Battle({ format });

// Fournir des équipes manuelles pour OU
battle.setPlayer('p1', { team: Teams.import(`
Pikachu
Ability: Static
Level: 50
- Thunderbolt
- Quick Attack
- Iron Tail
- Thunder
`) });

battle.setPlayer('p2', { team: Teams.import(`
Bulbasaur
Ability: Overgrow
Level: 50
- Vine Whip
- Tackle
- Razor Leaf
- Leech Seed
`) });

// Combat automatique
while (!battle.ended) {
    battle.makeChoices();
}

console.log("WINNER:", battle.winner);
