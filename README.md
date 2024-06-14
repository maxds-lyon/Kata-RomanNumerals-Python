# Kata des chiffres romains en Python

## Pour commencer

Cliquez sur le bouton ci-dessous pour démarrer un nouvel environnement de développement :

[![Ouvrir dans Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/maxds-lyon/Kata-RomanNumerals-Python.git)

## Aperçu

Ce dépôt contient deux exercices conçus pour améliorer vos compétences en
développement piloté par les tests.

## Instructions

Les chiffres romains sont un système numérique qui était utilisé par l'ancienne Rome. Les nombres dans 
ce système utilisent des lettres de l'alphabet latin. Actuellement, il utilise sept symboles :

| Symbole | Valeur |
|:-------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Au lieu d'écrire la même lettre quatre fois, une règle de soustraction est utilisée :
la lettre est écrite une fois, puis le prochain chiffre romain le plus grand est écrit.
Par exemple, 4 n'est pas écrit comme IIII, mais plutôt comme IV, car IV est V (5)
moins I (1).

En général, les valeurs pour 5, 50 et 500 ne sont pas soustraites.

### Exercice 1

La tâche à accomplir consiste à créer une fonction `to_roman(number: int) -> str` pour
convertir les nombres arabes ordinaires en chiffres romains, tels que :

* 4 → IV
* 7 → VII
* 9 → IX

Le plus petit nombre que vous pouvez écrire en chiffres romains est le nombre I (1). Et le
plus grand chiffre est MMMCMXCIX (3999).

### Exercice 2

Dans cette phase, l'objectif est de développer une fonction `from_roman(number: str)
-> int` qui effectue la conversion inverse, transformant les chiffres romains en
leurs chiffres arabes correspondants.

## Principes directeurs

* Si vous ne connaissez pas un algorithme existant, suivez les principes stricts
  du développement piloté par les tests (TDD) pour en dériver un.
* Réfléchissez à savoir si la séquence dans laquelle vous écrivez les tests influence la finalité
  conception de votre algorithme.
* Considérez s'il est plus bénéfique de concevoir un algorithme avant de se lancer
  sur le TDD, surtout si vous n'en connaissez pas déjà un.
* Si vous connaissez un algorithme, évaluez s'il peut être mis en œuvre en utilisant des principes stricts
  du TDD.

### Prérequis

* [Python 3.8+](https://www.python.org/)
* [pytest](https://pytest.org)