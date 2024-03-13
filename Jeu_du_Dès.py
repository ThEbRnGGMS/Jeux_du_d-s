import random
import time

print("Bienvenue sur le jeux du dès")

player1 = input("Nom du player 1: ")
player2 = input("Nom du player 2: ")

action_options = [
    "La chose la plus embarrassante que j'aie faite en public :",
     "Le plus gros mensonge jamais dit à tes parents:",
     "La personne sur qui tu as actuellement un béguin secret:",
     "La pire date:",
     "Blague embarrassante sur quelqu'un:",
     "Pire habitude à abandonner:",
     "Avez-vous déjà triché à un examen ou un test ? Si oui, comment ?:",
     "La chose la plus folle que vous ayez jamais faite en secret:",
     "Secret le plus sombre:",
     "Punition la pire que vous ayez jamais reçue:",
     "Plus grand rêve non poursuivi: ",
     "Personne la plus détestée dans la pièce et pourquoi ?: ",
     "La chose la plus embarrassante que vous ayez jamais dite à quelqu'un:",
     "La dernière chose que vous avez cherchée sur votre téléphone:",
     "Avez-vous déjà volé quelque chose ? Si oui, quoi et pourquoi ?:",
     "La pire chose que vous ayez jamais dite à quelqu'un lors d'une dispute :",
]

truth_options = [
    "Avez-vous déjà menti à votre meilleur ami ? Si oui, à propos de quoi ?",
     "Quel est ton plus grand regret dans la vie jusqu'à présent ?",
     "Avez-vous déjà eu le béguin pour un professeur ? Qui ?",
     "Quel est ton plus grand secret que tu n'as jamais osé révéler à personne ?",
     "Avez-vous déjà triché dans une relation amoureuse ? Si oui, comment ?",
     "Quelle est votre plus grande peur irrationnelle ?",
     "Quel est le pire mensonge que vous ayez jamais dit à vos parents ?",
     "Avez-vous déjà voulu disparaître complètement de la vie de quelqu'un ? Pourquoi ?",
     "Quelle est la chose la plus étrange que vous ayez jamais mangée ?",
     "Selon vous, quelle est votre pire qualité ?",
     "Avez-vous déjà regretté d'avoir commencé une relation amoureuse avec quelqu'un ? Pourquoi ?",
     "Quelle est la pire chose que vous ayez jamais dite à quelqu'un et que vous regrettez maintenant ?"
]

replay = 'y'

time.sleep(0)


def roll_dice():
    return random.randint(0, 6)


def choose_question(options):
    return random.choice(options)


player1_answers = []
player2_answers = []
is_player1_turn = True

game_duration = int(input("Combien de minutes veut-tu jouer ??? "))

start_time = time.time()
end_time = start_time + (60 * game_duration)

while time.time() < end_time:
    if is_player1_turn:
        current_player = player1
        other_player = player2
    else:
        current_player = player2
        other_player = player1

    print(f"C'est le tour de [{current_player}]")
    time.sleep(1)

    roll_dice_input = input(f"{current_player}, Veut tu faire rouler le dès? (o = oui; n = non): ")

    if roll_dice_input == 'o':
        result = roll_dice()
        print(result)

        if result % 2 == 0:
            action_question = choose_question(action_options)
            print(action_question)
            answer = input("Ta réponse: ")
            player1_answers.append(answer) if is_player1_turn else player2_answers.append(answer)
        else:
            truth_question = choose_question(truth_options)
            print(truth_question)
            answer = input("Ta réponse: ")

            player1_answers.append(answer) if is_player1_turn else player2_answers.append(answer)

    time.sleep(0)

    if len(player1_answers) == len(player2_answers):
        replay = input("Veut tu relancer le dès? (o = oui; n = non): ")
    else:
        replay = 'n'
        print("Tourne ton tour. Au joueur suivant")

    is_player1_turn = not is_player1_turn

print("\nFin du jeux!")
print(f"Les questions de {player1}")
for i, answer in enumerate(player1_answers):
    print(f"Question {i + 1}: {answer}")

print("\n")

print(f"Les question de {player2}:")
for i, answer in enumerate(player2_answers):
    print(f"Question {i + 1}: {answer}")
