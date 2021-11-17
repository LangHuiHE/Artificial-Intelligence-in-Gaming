# Team Draft
# Team Drafting
-------------

## Team building is used in many domains.  A couple of obvious ones are professional sports (see "Moneyball") and Player vs Player (PVP) gaming competitions (see "League of Legends").

## These type problems several common features.

- resource limitations (number of team members, budget, etc.)
- potential team members have individual contributions to team strength
- potential team members may have individualized resource requirements
- a utility function to measure expected team strength
- large number of possible teams (see "n choose k without replacement")

## Local search strategies allow the large state space (all possible teams) to be explored, and good team compositions to be identified, without the need to explore the state space exhaustively.


## A Sample Draft
--------------

## The Pokemon franchise recently celebrated its 25th anniversary.  Pokemon GO (POGO) is a recent mobile application, which celebrated 5th anniversary a few months ago. In one popular competition format for POGO PVP, players choose a team of 6 unique pokemon to bring to the tournament.

## In this assignment, we will choose pokemon to draft into our team of 6 that will give us a good chance in a tournament.

## Match-ups between all pairs of pokemon, call the pair (a, b), allowed in the tournament have been ranked with a score in the range [0, 1000]. 500 means a tie, < 500 means that a loses, and > 500 means that a wins.  The further the score is from 500, the more extreme the outcome.

## The team's utility will be calculated as described here:  For each pokemon allowed in the tournament, find the team member pokemon with the second best score vs the tournament pokemon.  This is the team's score vs that one pokemon.  Find the minimum of these scores.  That is the teams utility.

## Use local search (hill-climbing, simulated annealing, restart) to find the 5 best teams.

# run Search.py to start the search
# Total time allowed : 120 seconds
## l.matrix.p
### BestNext
```
team                                                                                                                            | the average of (each score - 500)
Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 | 238.38674033149172
Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 | 238.38674033149172
Magnezone Sp+WC/MrS 7/13/14 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 | 238.38674033149172
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Magnezone Sp+WC/MrS 7/13/14 Zweilous DB+BS/DP 5/13/14 | 238.38674033149172
Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 238.02762430939225
Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 | 238.02762430939225
Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 Gengar SC+ShP/SlB 8/13/12 | 238.02762430939225
Gengar SC+ShP/SlB 8/13/12 Ariados PSt+Lu/Mh 4/11/15 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 | 238.02762430939225
Gengar SC+ShP/SlB 8/13/12 Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 | 238.02762430939225
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 | 237.99447513812154
Gengar SC+ShP/SlB 8/13/12 Breloom C+SeB/DyP 5/15/10 Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Graveler (Alolan) VS+SE/RB 4/6/15 | 237.99447513812154
Zweilous DB+BS/DP 5/13/14 Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 Ariados PSt+Lu/Mh 4/11/15 Pangoro Sn+CC/NS 4/5/4 | 237.7403314917127
Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 | 237.7403314917127
Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 | 237.7403314917127
Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Magnezone Sp+WC/MrS 7/13/14 Pangoro Sn+CC/NS 4/5/4 | 237.7403314917127
Pangoro Sn+CC/NS 4/5/4 Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 | 237.7403314917127
Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 | 236.81767955801104
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Venomoth I+PF/BBu 4/6/15 | 236.81767955801104
Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 | 236.81767955801104
Gengar SC+ShP/SlB 8/13/12 Breloom C+SeB/DyP 5/15/10 Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Golem (Alolan) VS+RB/SE 4/11/12 | 236.6961325966851
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 | 236.4585635359116
Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 236.4585635359116
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 Venomoth I+PF/BBu 4/6/15 | 236.4585635359116
Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 | 236.4585635359116
Graveler (Alolan) VS+SE/RB 4/6/15 Breloom C+SeB/DyP 5/15/10 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 | 236.4585635359116
Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 | 236.4585635359116
Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 | 236.4585635359116
Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 Ariados PSt+Lu/Mh 4/11/15 Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 | 236.3314917127072
Pangoro Sn+CC/NS 4/5/4 Zapdos TS+DrlP/Tb 6/14/12 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 | 236.03867403314916
Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Haunter SC+ShP/SlB 5/14/14 | 235.30939226519337
Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 Haunter SC+ShP/SlB 5/14/14 | 235.30939226519337
Ariados PSt+Lu/Mh 4/11/15 Haunter SC+ShP/SlB 5/14/14 Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 | 234.65745856353593
Haunter SC+ShP/SlB 5/14/14 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Graveler (Alolan) VS+SE/RB 4/6/15 | 234.65745856353593
Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 234.5635359116022
Gengar SC+ShP/SlB 8/13/12 Breloom C+SeB/DyP 5/15/10 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 | 234.5635359116022
Gengar SC+ShP/SlB 8/13/12 Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 Venomoth I+PF/BBu 4/6/15 | 234.5635359116022
Golem (Alolan) VS+RB/SE 4/11/12 Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 Gengar SC+ShP/SlB 8/13/12 | 234.5635359116022
Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 Gengar SC+ShP/SlB 8/13/12 Breloom C+SeB/DyP 5/15/10 | 234.5635359116022
Golem (Alolan) VS+RB/SE 4/11/12 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Heracross C+RB/Mh 7/14/15 | 234.20994475138122
Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Heracross C+RB/Mh 7/14/15 Golem (Alolan) VS+RB/SE 4/11/12 Gengar SC+ShP/SlB 8/13/12 | 234.20994475138122
Zapdos TS+DrlP/Tb 6/14/12 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 | 234.13259668508286
Pangoro Sn+CC/NS 4/5/4 Zapdos TS+DrlP/Tb 6/14/12 Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 | 234.13259668508286
Ariados PSt+Lu/Mh 4/11/15 Haunter SC+ShP/SlB 5/14/14 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 | 234.12707182320443
Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Graveler (Alolan) VS+SE/RB 4/6/15 Haunter SC+ShP/SlB 5/14/14 Breloom C+SeB/DyP 5/15/10 | 234.12707182320443
Zweilous DB+BS/DP 5/13/14 Haunter SC+ShP/SlB 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 Ariados PSt+Lu/Mh 4/11/15 Breloom C+SeB/DyP 5/15/10 | 234.12707182320443
Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 Golem (Alolan) VS+RB/SE 4/11/12 Venomoth I+PF/BBu 4/6/15 Zapdos TS+DrlP/Tb 6/14/12 | 234.04972375690608
Pangoro Sn+CC/NS 4/5/4 Zapdos TS+DrlP/Tb 6/14/12 Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 | 234.04972375690608
Haunter SC+ShP/SlB 5/14/14 Zweilous DB+BS/DP 5/13/14 Golem (Alolan) VS+RB/SE 4/11/12 Ariados PSt+Lu/Mh 4/11/15 Heracross C+RB/Mh 7/14/15 | 233.08839779005524
Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 Golem (Alolan) VS+RB/SE 4/11/12 Haunter SC+ShP/SlB 5/14/14 Breloom C+SeB/DyP 5/15/10 | 232.87845303867402
Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Tropius AS+LB/AA 5/14/14 Heracross C+RB/Mh 7/14/15 | 232.13259668508286
Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Tropius AS+LB/AA 5/14/14 | 232.13259668508286
Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 Tropius AS+LB/AA 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 232.13259668508286
Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Gengar SC+ShP/SlB 8/13/12 Tropius AS+LB/AA 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 | 232.13259668508286
Ariados PSt+Lu/Mh 4/11/15 Graveler (Alolan) VS+SE/RB 4/6/15 Zapdos TS+DrlP/Tb 6/14/12 Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 | 232.06629834254144
Zweilous DB+BS/DP 5/13/14 Chandelure I+FmC/Ov 8/15/14 Graveler (Alolan) VS+SE/RB 4/6/15 Tropius AS+LB/AA 5/14/14 Breloom C+SeB/DyP 5/15/10 | 231.5027624309392
Chandelure I+FmC/Ov 8/15/14 Zweilous DB+BS/DP 5/13/14 Tropius AS+LB/AA 5/14/14 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 | 231.5027624309392
Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Golem (Alolan) VS+RB/SE 4/11/12 Heracross C+RB/Mh 7/14/15 Tropius AS+LB/AA 5/14/14 | 230.8950276243094
Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 Tropius AS+LB/AA 5/14/14 Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 | 230.8950276243094
Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 Haunter SC+ShP/SlB 5/14/14 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 | 229.08839779005524
Heracross C+RB/Mh 7/14/15 Haunter SC+ShP/SlB 5/14/14 Tropius AS+LB/AA 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 | 229.08839779005524
Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 228.97237569060775
Pangoro Sn+CC/NS 4/5/4 Breloom C+SeB/DyP 5/15/10 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 228.97237569060775
Gengar SC+ShP/SlB 8/13/12 Scyther FC+AA/NS 5/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 | 228.40883977900552
Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 | 227.64088397790056
Zweilous DB+BS/DP 5/13/14 Chandelure I+FmC/Ov 8/15/14 Heracross C+RB/Mh 7/14/15 Tropius AS+LB/AA 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 | 227.58011049723757
Zweilous DB+BS/DP 5/13/14 Chandelure I+FmC/Ov 8/15/14 Graveler (Alolan) VS+SE/RB 4/6/15 Tropius AS+LB/AA 5/14/14 Heracross C+RB/Mh 7/14/15 | 227.58011049723757
Heracross C+RB/Mh 7/14/15 Chandelure I+FmC/Ov 8/15/14 Tropius AS+LB/AA 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 | 227.58011049723757
Tropius AS+LB/AA 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 Chandelure I+FmC/Ov 8/15/14 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 | 227.58011049723757
Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Breloom C+SeB/DyP 5/15/10 Pangoro Sn+CC/NS 4/5/4 Golem (Alolan) VS+RB/SE 4/11/12 | 227.3977900552486
Golem (Alolan) VS+RB/SE 4/11/12 Roserade PJ+WBF/LfS 6/15/11 Ariados PSt+Lu/Mh 4/11/15 Pangoro Sn+CC/NS 4/5/4 Cofagrigus SC+SB/DP 5/15/8 | 227.0110497237569
Golem (Alolan) VS+RB/SE 4/11/12 Tropius AS+LB/AA 5/14/14 Chandelure I+FmC/Ov 8/15/14 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 | 226.5303867403315
Heracross C+RB/Mh 7/14/15 Chandelure I+FmC/Ov 8/15/14 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Golem (Alolan) VS+RB/SE 4/11/12 | 226.5303867403315
Heracross C+RB/Mh 7/14/15 Chandelure I+FmC/Ov 8/15/14 Tropius AS+LB/AA 5/14/14 Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 | 226.5303867403315
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Golem (Alolan) VS+RB/SE 4/11/12 Heracross C+RB/Mh 7/14/15 Venomoth I+PF/BBu 4/6/15 | 225.91712707182322
Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 Pangoro Sn+CC/NS 4/5/4 | 225.91712707182322
Golem (Alolan) VS+RB/SE 4/11/12 Tropius AS+LB/AA 5/14/14 Zapdos TS+DrlP/Tb 6/14/12 Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 | 225.15469613259668
Pangoro Sn+CC/NS 4/5/4 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Zapdos TS+DrlP/Tb 6/14/12 | 225.14917127071823
Obstagoon C+NS/CrC 4/13/15 Chandelure I+FmC/Ov 8/15/14 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Muk (Alolan) PJ+AS/DP 4/12/9 | 222.92265193370164
Tropius AS+LB/AA 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Honchkrow Sn+BrB/SA 6/10/15 | 221.99447513812154
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Graveler (Alolan) VS+SE/RB 4/6/15 Victreebel RL+AS/LB 5/13/11 Venomoth I+PF/BBu 4/6/15 | 221.8121546961326
Pangoro Sn+CC/NS 4/5/4 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Muk (Alolan) PJ+AS/DP 4/12/9 | 221.73480662983425
Heracross C+RB/Mh 7/14/15 Honchkrow Sn+BrB/SA 6/10/15 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Golem (Alolan) VS+RB/SE 4/11/12 | 221.58011049723757
Graveler (Alolan) VS+SE/RB 4/6/15 Breloom C+SeB/DyP 5/15/10 Beedrill PJ+AA/DR 4/14/12 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 | 221.5027624309392
Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 Vileplume RL+M/SlB 4/10/13 Venomoth I+PF/BBu 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 221.01657458563537
Graveler (Alolan) VS+SE/RB 4/6/15 Obstagoon C+NS/CrC 4/13/15 Beedrill PJ+AA/DR 4/14/12 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 | 220.87292817679557
Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 Tropius AS+LB/AA 5/14/14 Muk (Alolan) PJ+AS/DP 4/12/9 Golem (Alolan) VS+RB/SE 4/11/12 | 220.83977900552486
Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Emolga TS+AA/D 5/15/11 Ariados PSt+Lu/Mh 4/11/15 Pangoro Sn+CC/NS 4/5/4 | 220.8011049723757
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Golem (Alolan) VS+RB/SE 4/11/12 Torterra RL+FP/ST 5/14/9 Venomoth I+PF/BBu 4/6/15 | 220.61325966850828
Golem (Alolan) VS+RB/SE 4/11/12 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Ivysaur VW+SlB/PW 3/15/14 Venomoth I+PF/BBu 4/6/15 | 220.25414364640883
Golem (Alolan) VS+RB/SE 4/11/12 Vileplume RL+M/SlB 4/10/13 Venomoth I+PF/BBu 4/6/15 Pangoro Sn+CC/NS 4/5/4 Gengar SC+ShP/SlB 8/13/12 | 219.49171270718233
Ariados PSt+Lu/Mh 4/11/15 Cofagrigus SC+SB/DP 5/15/8 Graveler (Alolan) VS+SE/RB 4/6/15 Honchkrow Sn+BrB/SA 6/10/15 Pangoro Sn+CC/NS 4/5/4 | 218.95027624309392
Honchkrow Sn+BrB/SA 6/10/15 Pangoro Sn+CC/NS 4/5/4 Ariados PSt+Lu/Mh 4/11/15 Graveler (Alolan) VS+SE/RB 4/6/15 Cofagrigus SC+SB/DP 5/15/8 | 218.95027624309392
Muk (Alolan) PJ+AS/DP 4/12/9 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Tropius AS+LB/AA 5/14/14 Heracross C+RB/Mh 7/14/15 | 218.81767955801104
Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 Gloom RL+M/SlB 5/12/13 Venomoth I+PF/BBu 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 218.78453038674033
Venomoth I+PF/BBu 4/6/15 Pangoro Sn+CC/NS 4/5/4 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 Oddish RL+M/SlB 15/15/15 | 218.06629834254144
Servine VW+GK/LT 6/12/15 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 218.060773480663
Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Grotle RL+BS/EB 4/15/7 Pangoro Sn+CC/NS 4/5/4 Graveler (Alolan) VS+SE/RB 4/6/15 | 217.95027624309392
Gengar SC+ShP/SlB 8/13/12 Breloom C+SeB/DyP 5/15/10 Pangoro Sn+CC/NS 4/5/4 Roserade PJ+WBF/LfS 6/15/11 Golem (Alolan) VS+RB/SE 4/11/12 | 217.94475138121547
Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Bayleef RL+GK/AP 4/14/14 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 | 217.77348066298342
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Graveler (Alolan) VS+SE/RB 4/6/15 Bayleef RL+GK/AP 4/14/14 Venomoth I+PF/BBu 4/6/15 | 217.77348066298342
Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 Gengar SC+ShP/SlB 8/13/12 Servine VW+GK/LT 6/12/15 Pangoro Sn+CC/NS 4/5/4 | 217.34806629834253
Gengar SC+ShP/SlB 8/13/12 Golem (Alolan) VS+RB/SE 4/11/12 Venomoth I+PF/BBu 4/6/15 Pangoro Sn+CC/NS 4/5/4 Servine VW+GK/LT 6/12/15 | 217.34806629834253
Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Quilladin VW+BS/EB 5/14/13 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 | 217.24309392265192
Serperior VW+FP/AA 4/11/12 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 217.0110497237569
Pangoro Sn+CC/NS 4/5/4 Graveler (Alolan) VS+SE/RB 4/6/15 Roserade PJ+WBF/LfS 6/15/11 Breloom C+SeB/DyP 5/15/10 Haunter SC+ShP/SlB 5/14/14 | 216.45303867403314
Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 Galvantula VS+D/Lu 5/11/12 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 | 216.08287292817678
Meganium VW+FP/Eq 6/14/14 Pangoro Sn+CC/NS 4/5/4 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 | 216.02762430939225
Meganium VW+FP/Eq 6/14/14 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 Pangoro Sn+CC/NS 4/5/4 Gengar SC+ShP/SlB 8/13/12 | 216.02762430939225
Golem (Alolan) VS+RB/SE 4/11/12 Gengar SC+ShP/SlB 8/13/12 Quilladin VW+BS/EB 5/14/13 Venomoth I+PF/BBu 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 215.99447513812154
Gengar SC+ShP/SlB 8/13/12 Galvantula VS+D/Lu 5/11/12 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 Golem (Alolan) VS+RB/SE 4/11/12 | 214.74585635359117
Scraggy FA+FoP/BkB 13/15/15 Graveler (Alolan) VS+SE/RB 4/6/15 Haunter SC+ShP/SlB 5/14/14 Ariados PSt+Lu/Mh 4/11/15 Heracross C+RB/Mh 7/14/15 | 214.5745856353591
Haunter SC+ShP/SlB 5/14/14 Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 Tropius AS+LB/AA 5/14/14 Krookodile Sn+Cr/Eq 4/7/14 | 213.9281767955801
Haunter SC+ShP/SlB 5/14/14 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 Galvantula VS+D/Lu 5/11/12 Graveler (Alolan) VS+SE/RB 4/6/15 | 213.3977900552486
Gengar SC+ShP/SlB 8/13/12 Galvantula VS+D/Lu 5/11/12 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 | 212.24309392265192
Zweilous DB+BS/DP 5/13/14 Galvantula VS+D/Lu 5/11/12 Haunter SC+ShP/SlB 5/14/14 Heracross C+RB/Mh 7/14/15 Golem (Alolan) VS+RB/SE 4/11/12 | 212.0331491712707
Golem (Alolan) VS+RB/SE 4/11/12 Galvantula VS+D/Lu 5/11/12 Breloom C+SeB/DyP 5/15/10 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 | 211.353591160221
Pangoro Sn+CC/NS 4/5/4 Minun Sp+D/GK 4/14/12 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 | 210.07734806629836
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Minun Sp+D/GK 4/14/12 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 | 210.07734806629836
Zapdos TS+DrlP/Tb 6/14/12 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 Pangoro Sn+CC/NS 4/5/4 Cradily BS+SE/GK 4/10/10 | 209.67403314917127
Roserade PJ+WBF/LfS 6/15/11 Breloom C+SeB/DyP 5/15/10 Sableye SC+FoP/Re 7/15/15 Golem (Alolan) VS+RB/SE 4/11/12 Obstagoon C+NS/CrC 4/13/15 | 199.1988950276243
Roserade PJ+WBF/LfS 6/15/11 Breloom C+SeB/DyP 5/15/10 Sableye SC+FoP/Re 7/15/15 Graveler (Alolan) VS+SE/RB 4/6/15 Obstagoon C+NS/CrC 4/13/15 | 198.97790055248618
```


### Annealing
```
team                                                                                                                            | the average of (each score - 500)
Magnezone Sp+WC/MrS 7/13/14 Pangoro Sn+CC/NS 4/5/4 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 | 238.38674033149172
Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 Magnezone Sp+WC/MrS 7/13/14 Pangoro Sn+CC/NS 4/5/4 | 238.38674033149172
Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Magnezone Sp+WC/MrS 7/13/14 Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 | 238.38674033149172
Magnezone Sp+WC/MrS 7/13/14 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 | 238.38674033149172
Pangoro Sn+CC/NS 4/5/4 Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Magnezone Sp+WC/MrS 7/13/14 Venomoth I+PF/BBu 4/6/15 | 238.38674033149172
Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 Zweilous DB+BS/DP 5/13/14 | 238.38674033149172
Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 | 238.38674033149172
Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Magnezone Sp+WC/MrS 7/13/14 | 238.38674033149172
Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 | 238.38674033149172
Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 Gengar SC+ShP/SlB 8/13/12 | 238.38674033149172
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Ariados PSt+Lu/Mh 4/11/15 | 238.02762430939225
Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 | 238.02762430939225
Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 | 238.02762430939225
Gengar SC+ShP/SlB 8/13/12 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 | 237.99447513812154
Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 | 237.99447513812154
Gengar SC+ShP/SlB 8/13/12 Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 Magnezone Sp+WC/MrS 7/13/14 | 237.7403314917127
Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 Ariados PSt+Lu/Mh 4/11/15 Magnezone Sp+WC/MrS 7/13/14 | 237.7403314917127
Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 Gengar SC+ShP/SlB 8/13/12 Magnezone Sp+WC/MrS 7/13/14 | 237.7403314917127
Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 236.81767955801104
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 | 236.81767955801104
Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 236.4585635359116
Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 Gengar SC+ShP/SlB 8/13/12 | 236.4585635359116
Breloom C+SeB/DyP 5/15/10 Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 | 236.4585635359116
Breloom C+SeB/DyP 5/15/10 Zweilous DB+BS/DP 5/13/14 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 | 236.4585635359116
Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 | 236.4585635359116
Gengar SC+ShP/SlB 8/13/12 Venomoth I+PF/BBu 4/6/15 Zapdos TS+DrlP/Tb 6/14/12 Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 | 236.03867403314916
Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Zapdos TS+DrlP/Tb 6/14/12 Zweilous DB+BS/DP 5/13/14 | 236.03867403314916
Zweilous DB+BS/DP 5/13/14 Magnezone Sp+WC/MrS 7/13/14 Pangoro Sn+CC/NS 4/5/4 Ariados PSt+Lu/Mh 4/11/15 Haunter SC+ShP/SlB 5/14/14 | 235.30939226519337
Ariados PSt+Lu/Mh 4/11/15 Zweilous DB+BS/DP 5/13/14 Haunter SC+ShP/SlB 5/14/14 Heracross C+RB/Mh 7/14/15 Graveler (Alolan) VS+SE/RB 4/6/15 | 234.65745856353593
Breloom C+SeB/DyP 5/15/10 Venomoth I+PF/BBu 4/6/15 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 Golem (Alolan) VS+RB/SE 4/11/12 | 234.5635359116022
Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 | 234.5635359116022
Zapdos TS+DrlP/Tb 6/14/12 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 | 234.13259668508286
Zapdos TS+DrlP/Tb 6/14/12 Venomoth I+PF/BBu 4/6/15 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 | 234.13259668508286
Ariados PSt+Lu/Mh 4/11/15 Breloom C+SeB/DyP 5/15/10 Haunter SC+ShP/SlB 5/14/14 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 | 234.12707182320443
Pangoro Sn+CC/NS 4/5/4 Zweilous DB+BS/DP 5/13/14 Zapdos TS+DrlP/Tb 6/14/12 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 | 234.04972375690608
Zapdos TS+DrlP/Tb 6/14/12 Venomoth I+PF/BBu 4/6/15 Golem (Alolan) VS+RB/SE 4/11/12 Zweilous DB+BS/DP 5/13/14 Pangoro Sn+CC/NS 4/5/4 | 234.04972375690608
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Tropius AS+LB/AA 5/14/14 Heracross C+RB/Mh 7/14/15 | 232.13259668508286
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Heracross C+RB/Mh 7/14/15 | 232.13259668508286
Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 Golem (Alolan) VS+RB/SE 4/11/12 | 230.8950276243094
Golem (Alolan) VS+RB/SE 4/11/12 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 | 230.8950276243094
Venomoth I+PF/BBu 4/6/15 Breloom C+SeB/DyP 5/15/10 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 228.97237569060775
Scyther FC+AA/NS 5/13/12 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 Gengar SC+ShP/SlB 8/13/12 | 228.40883977900552
Venomoth I+PF/BBu 4/6/15 Heracross C+RB/Mh 7/14/15 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 227.64088397790056
Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Heracross C+RB/Mh 7/14/15 | 227.64088397790056
Venomoth I+PF/BBu 4/6/15 Jumpluff BS+AA/EB 4/10/15 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 227.14364640883977
Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Jumpluff BS+AA/EB 4/10/15 | 227.14364640883977
Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Venusaur VW+FP/SlB 7/15/15 Venomoth I+PF/BBu 4/6/15 | 223.32596685082873
Graveler (Alolan) VS+SE/RB 4/6/15 Victreebel RL+AS/LB 5/13/11 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 | 221.8121546961326
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Ivysaur VW+SlB/PW 3/15/14 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 221.76795580110496
Muk (Alolan) PJ+AS/DP 4/12/9 Tropius AS+LB/AA 5/14/14 Zweilous DB+BS/DP 5/13/14 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 221.73480662983425
Pangoro Sn+CC/NS 4/5/4 Roserade PJ+WBF/LfS 6/15/11 Haunter SC+ShP/SlB 5/14/14 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 | 221.4364640883978
Venomoth I+PF/BBu 4/6/15 Torterra RL+FP/ST 5/14/9 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 221.37016574585635
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Vileplume RL+M/SlB 4/10/13 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 221.01657458563537
Venomoth I+PF/BBu 4/6/15 Vileplume RL+M/SlB 4/10/13 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 221.01657458563537
Emolga TS+AA/D 5/15/11 Pangoro Sn+CC/NS 4/5/4 Graveler (Alolan) VS+SE/RB 4/6/15 Zweilous DB+BS/DP 5/13/14 Ariados PSt+Lu/Mh 4/11/15 | 220.8011049723757
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Gloom RL+M/SlB 5/12/13 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 218.78453038674033
Venomoth I+PF/BBu 4/6/15 Gloom RL+M/SlB 5/12/13 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 218.78453038674033
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Oddish RL+M/SlB 15/15/15 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 218.06629834254144
Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Oddish RL+M/SlB 15/15/15 | 218.06629834254144
Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Oddish RL+M/SlB 15/15/15 Pangoro Sn+CC/NS 4/5/4 | 218.06629834254144
Venomoth I+PF/BBu 4/6/15 Servine VW+GK/LT 6/12/15 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 218.060773480663
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Grotle RL+BS/EB 4/15/7 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 217.95027624309392
Venomoth I+PF/BBu 4/6/15 Grotle RL+BS/EB 4/15/7 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 217.95027624309392
Graveler (Alolan) VS+SE/RB 4/6/15 Grotle RL+BS/EB 4/15/7 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 | 217.95027624309392
Venomoth I+PF/BBu 4/6/15 Bayleef RL+GK/AP 4/14/14 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 217.77348066298342
Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Bayleef RL+GK/AP 4/14/14 | 217.77348066298342
Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 Gengar SC+ShP/SlB 8/13/12 Quilladin VW+BS/EB 5/14/13 | 217.24309392265192
Graveler (Alolan) VS+SE/RB 4/6/15 Quilladin VW+BS/EB 5/14/13 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 | 217.24309392265192
Serperior VW+FP/AA 4/11/12 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 Pangoro Sn+CC/NS 4/5/4 Gengar SC+ShP/SlB 8/13/12 | 217.0110497237569
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Serperior VW+FP/AA 4/11/12 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 217.0110497237569
Venomoth I+PF/BBu 4/6/15 Serperior VW+FP/AA 4/11/12 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 217.0110497237569
Venomoth I+PF/BBu 4/6/15 Meganium VW+FP/Eq 6/14/14 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 216.8232044198895
Graveler (Alolan) VS+SE/RB 4/6/15 Meganium VW+FP/Eq 6/14/14 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 | 216.8232044198895
Roserade PJ+WBF/LfS 6/15/11 Haunter SC+ShP/SlB 5/14/14 Pangoro Sn+CC/NS 4/5/4 Breloom C+SeB/DyP 5/15/10 Graveler (Alolan) VS+SE/RB 4/6/15 | 216.45303867403314
Gengar SC+ShP/SlB 8/13/12 Zweilous DB+BS/DP 5/13/14 Galvantula VS+D/Lu 5/11/12 Graveler (Alolan) VS+SE/RB 4/6/15 Heracross C+RB/Mh 7/14/15 | 216.08287292817678
Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Minun Sp+D/GK 4/14/12 Graveler (Alolan) VS+SE/RB 4/6/15 Venomoth I+PF/BBu 4/6/15 | 210.07734806629836
Venomoth I+PF/BBu 4/6/15 Minun Sp+D/GK 4/14/12 Gengar SC+ShP/SlB 8/13/12 Graveler (Alolan) VS+SE/RB 4/6/15 Pangoro Sn+CC/NS 4/5/4 | 210.07734806629836
Graveler (Alolan) VS+SE/RB 4/6/15 Minun Sp+D/GK 4/14/12 Gengar SC+ShP/SlB 8/13/12 Pangoro Sn+CC/NS 4/5/4 Venomoth I+PF/BBu 4/6/15 | 210.07734806629836
Minun Sp+D/GK 4/14/12 Venomoth I+PF/BBu 4/6/15 Haunter SC+ShP/SlB 5/14/14 Pangoro Sn+CC/NS 4/5/4 Golem (Alolan) VS+RB/SE 4/11/12 | 206.11602209944752
```

------
## h.matrix.p
### BestNext
```
team | the average of (each score - 500)
Wormadam (Trash) Cf+IH/BBu 4/13/13 Scrafty C+FoP/PUP 4/13/14 Golbat WA+PF/SB 4/8/14 Toxicroak C+MB/SlB 7/13/15 Umbreon Sn+FoP/LR 4/15/8 | 224.2095238095238

```
### Annealing
```
team | the average of (each score - 500)

```