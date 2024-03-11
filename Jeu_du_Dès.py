import random
import time

print("Bienvenue dans le jeux du dès")
dice = str(input("Veut tu lancer le dès (o = Oui ; n = Non) ? "))

option_action = ['Quelle est la chose la plus embarrassante que tu aies faite en public ?', 'Quel est le mensonge le plus gros que tu aies jamais dit à tes parents ?', 'Quelle est la personne que tu ascrush secrètement en ce moment ?', 'Décris ton pire rendez-vous amoureux', 'Raconte une blague embarrassante que tu as faite à quelqu un ?', 'Quelle est la pire habitude que tu aimerais abandonner ?', 'As-tu déjà triché à un examen ou un test, Si oui, comment ?', 'Quelle est la chose la plus folle que tu aies jamais faite en secret ?', 'Quel est ton plus grand regret dans la vie jusqu à présent ?', 'Quel est le secret le plus sombre que tu n as jamais partagé avec personne ?', 'Quelle est la pire punition que tu aies jamais reçue ?', 'Quel est ton plus grand rêve que tu n as jamais osé poursuivre ?', 'Quelle est la personne que tu détestes le plus dans cette pièce et pourquoi ?', 'Quelle est la chose la plus gênante que tu aies jamais dite à quelqu un ?', 'Quelle est la dernière chose que tu as recherchée sur ton téléphone ?', 'Si tu pouvais échanger ta vie avec quelqu un d autre pour une journée, qui choisirais-tu et pourquoi ?', 'Quelle est la chose la plus folle que tu aies jamais achetée en ligne ?', 'As-tu déjà volé quelque chose ? Si oui, quoi et pourquoi ?', 'Quel est ton plus grand secret honteux ?', 'Quelle est la pire chose que tu as dite à quelqu un lors d une dispute ?']
option_verité = ['As-tu déjà menti à ton meilleur ami/amie ? Si oui, à propos de quoi ?', 'Quel est ton plus grand regret dans la vie jusqu à présent ?', 'As-tu déjà eu un coup de cœur pour un(e) professeur(e) ? Qui ?', 'Quel est ton plus grand secret que tu n as jamais osé révéler à personne ?', 'As-tu déjà triché dans une relation amoureuse ? Si oui, comment ?', 'Quelle est ta plus grande peur irrationnelle ?', 'Quel est le pire mensonge que tu aies jamais dit à tes parents ?', 'As-tu déjà eu envie de disparaître complètement de la vie de quelqu un ? Pourquoi ?', 'Quelle est la chose la plus bizarre que tu aies jamais mangée ?', 'Quel est ton pire défaut selon toi ?', 'As-tu déjà regretté de commencer une relation amoureuse avec quelqu un ? Pourquoi ?', 'Quelle est la chose la plus embarrassante que tu aies jamais faite en public ?', 'As-tu déjà eu des pensées violentes envers quelqu un ? Qui et pourquoi ?', 'Quelle est la chose la plus stupide que tu aies faite par amour ?', 'As-tu déjà eu des pensées de trahison envers un ami proche ? Pourquoi ?', 'Quelle est ta plus grande faiblesse en tant que personne ?', 'As-tu déjà eu des fantasmes inavouables ? Lesquels ?', 'Quelle est la chose que tu détestes le plus chez toi ?', 'As-tu déjà eu peur de perdre quelqu un de cher ? Qui et pourquoi ?', 'Quelle est la pire chose que tu aies jamais dite à quelqu un et que tu regrettes maintenant']  
rejouer = 'o'

while rejouer != 'n':
    
    if dice == 'o':
        resultat = random.randint(0, 6)
        print(resultat)

        if resultat%2 == 0:
            qst_action = random.choices(option_action)
            print(qst_action)

        elif resultat%2 == 1:
            qst_verité = random.choices(option_verité)
            print(qst_verité)
            
    time.sleep(5)
    rejouer = str(input("Veut tu relancer le dès ? (o = oui ; n = non) ? "))
