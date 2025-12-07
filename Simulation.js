const { Battle, Dex, Teams } = require('./showdown/dist/sim');
const fs = require('fs');

// ------------------------------
// PARAMÈTRE : nombre de combats
// ------------------------------
const NUM_MATCHES = 1000; // Mets ici le nombre de combats que tu veux simuler

// ------------------------------
// ÉQUIPES DES JOUEURS 
// ------------------------------
const team1 = Teams.import(`
Dragapult @ Choice Specs  
Ability: Infiltrator  
Tera Type: Ghost  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
- Flamethrower  
- Shadow Ball  
- Draco Meteor  
- U-turn

Glimmora @ Focus Sash  
Ability: Toxic Debris  
Tera Type: Ground  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Stealth Rock  
- Mortal Spin  
- Stone Edge  
- Self-Destruct    

Landorus-Therian @ Choice Scarf  
Ability: Intimidate  
Tera Type: Ground  
EVs: 252 Atk / 4 SpA / 252 Spe  
Naive Nature  
- Earthquake  
- Hammer Arm  
- U-turn  
- Crunch  

Ogerpon-Wellspring @ Wellspring Mask  
Ability: Water Absorb  
Tera Type: Water  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Wood Hammer  
- Ivy Cudgel  
- Play Rough  
- U-turn  

Kingambit @ Black Glasses  
Ability: Supreme Overlord  
Tera Type: Dark  
EVs: 252 HP / 252 Atk / 4 SpD  
Adamant Nature  
- Sucker Punch  
- Iron Head  
- Swords Dance  
- Foul Play  

Iron Valiant @ Booster Energy  
Ability: Quark Drive  
Tera Type: Fairy  
EVs: 4 Atk / 252 SpA / 252 Spe  
Rash Nature  
- Calm Mind  
- Moonblast  
- Close Combat  
- Encore 
`);

const team2 = Teams.import(`
Dragapult @ Choice Specs  
Ability: Infiltrator  
Tera Type: Ghost  
EVs: 252 SpA / 4 SpD / 252 Spe  
Timid Nature  
- Flamethrower  
- Shadow Ball  
- Draco Meteor  
- U-turn

Glimmora @ Focus Sash  
Ability: Toxic Debris  
Tera Type: Ground  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Stealth Rock  
- Mortal Spin  
- Stone Edge  
- Self-Destruct    

Landorus-Therian @ Choice Scarf  
Ability: Intimidate  
Tera Type: Ground  
EVs: 252 Atk / 4 SpA / 252 Spe  
Naive Nature  
- Earthquake  
- Hammer Arm  
- U-turn  
- Crunch  

Ogerpon-Wellspring @ Wellspring Mask  
Ability: Water Absorb  
Tera Type: Water  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Wood Hammer  
- Ivy Cudgel  
- Play Rough  
- U-turn  

Kingambit @ Black Glasses  
Ability: Supreme Overlord  
Tera Type: Dark  
EVs: 252 HP / 252 Atk / 4 SpD  
Adamant Nature  
- Sucker Punch  
- Iron Head  
- Swords Dance  
- Foul Play  

Iron Valiant @ Booster Energy  
Ability: Quark Drive  
Tera Type: Fairy  
EVs: 4 Atk / 252 SpA / 252 Spe  
Rash Nature  
- Calm Mind  
- Moonblast  
- Close Combat  
- Encore  
`);

// ------------------------------
// BOUCLE DE SIMULATION
// ------------------------------
const allReplays = [];

for (let i = 1; i <= NUM_MATCHES; i++) {
    console.log(`\n=== Combat ${i}/${NUM_MATCHES} ===`);

    const format = Dex.formats.get('gen9ou');
    const battle = new Battle({ format });

    battle.setPlayer('p1', { name: "Player1", team: team1 });
    battle.setPlayer('p2', { name: "Player2", team: team2 });

    while (!battle.ended) {
        battle.makeChoices();
    }

    // Sauvegarde du replay
    allReplays.push({
        match: i,
        winner: battle.winner,
        log: battle.log
    });

    console.log(`→ Gagnant : ${battle.winner}`);
}

// ------------------------------
// EXPORT JSON FINAL
// ------------------------------
fs.writeFileSync('replays.json', JSON.stringify(allReplays, null, 2));

console.log(`\n${NUM_MATCHES} combats simulés !`);
console.log("Résultats enregistrés dans replays.json");
