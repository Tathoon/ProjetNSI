import pygame
import pyscroll
import pytmx
from Map import MapManager
from Animation import AnimateSprite
from Evenement import evenement

class monde_reve:
    def __init__(self, mainScreen, path):
        # generer un joueur 
        self.player = Player("Wizard", path)                       # creer un objet de la classe "player" appelé "player" avec une position de départ de (640, 607) sur l'écran
        self.map_manager = MapManager(mainScreen, self.player, path) # creer un objet de la classe "MapManager" appelé "map_manager" avec l'écran principal du jeu et l'objet du joueur comme arguments

    def handle_input(self):
        # touche pour deplacement du joueur
        pressed = pygame.key.get_pressed() 

        if pressed[pygame.K_z]:   # verifie la touche enfoncée
            self.player.move_up() 
            self.player.change_animations('up')    # cela appelle la méthode "move_up" de l'objet "player" pour déplacer le personnage vers le haut, et la méthode "change_animation" pour changer l'animation du personnage vers le haut
        elif pressed[pygame.K_s]: # verifie la touche enfoncée
            self.player.move_down()
            self.player.change_animations('down')  # cela appelle la méthode "move_down" de l'objet "player" pour déplacer le personnage vers le bas, et la méthode "change_animation" pour changer l'animation du personnage vers le bas
        elif pressed[pygame.K_q]: # verifie la touche enfoncée
            self.player.move_left() 
            self.player.change_animations('left')  # cela appelle la méthode "move_left" de l'objet "player" pour déplacer le personnage vers la gauche, et la méthode "change_animation" pour changer l'animation du personnage vers la gauche
        elif pressed[pygame.K_d]: # verifie la touche enfoncée
            self.player.move_right()
            self.player.change_animations('right') # cela appelle la méthode "move_right" de l'objet "player" pour déplacer le personnage vers la droite, et la méthode "change_animation" pour changer l'animation du personnage vers la droite

    def update(self, quete3, menu_quetes, accueil, pnj, evenement, soundDesign): # définit une nouvelle méthode appelée "update" qui met à jour l'état du jeu
        self.map_manager.update(self, quete3, menu_quetes, accueil, pnj, evenement, soundDesign)

    def run(self, running, quete3, menu_quetes, accueil, pnj, evenement, soundDesign):

        # boucle principale du jeu
            
        self.player.save_location() # save la location du joueur si jamais obstacle
        self.handle_input()         # appelle la methode handle_input qui verifie la touche appuyée par le joueur
        self.update(quete3, menu_quetes, accueil, pnj, evenement, soundDesign)               # update le jeu
        self.map_manager.draw()     # dessine le jeu à l'écran
        pygame.display.flip()       # update l'affichage (fonction Pygame)

        for event in pygame.event.get(): # verifie si le joueur quite le jeu et si oui on arrete la boucle
            if event.type == pygame.QUIT:
                evenement.gerer_quitter(self, event, running)

class Entity(AnimateSprite): # définit une nouvelle classe appelée "player_reve" qui hérite de la classe "pygame.sprite.Sprite"

    def __init__(self, name, x , y, path):
        super().__init__(name, path)                   # appelle la méthode "init()" de la classe mère "pygame.sprite.Sprite", cela permet d'initialiser l'objet comme un sprite pygame
        self.image = self.get_image(0, 0)    # appelle la méthode "get_image()" de l'objet avec les coordonnées x=0 et y=0 pour obtenir une sous-image de l'attribut "sprite_sheet" et l'assigne à l'attribut "image" de l'objet
        self.image.set_colorkey([0, 0, 0])   # définit la couleur transparente de l'attribut "image" en utilisant la valeur RVB [0, 0, 0], qui représente le noir, cela permet de rendre le fond noir de l'image transparent, de sorte que seule la partie du joueur sera visible
        self.rect = self.image.get_rect()    # creer un objet Rect (rectangle) à partir de l'attribut "image" de l'objet et l'assigne à l'attribut "rect" de l'objet, le rectangle est utilisé pour représenter la position et la taille du joueur dans le jeu
        self.position = [x, y]               # initialise l'attribut "position" de l'objet avec les coordonnées x et y passées en paramètres du constructeur
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12) # creer un autre objet Rect appelé "feet" (pieds) qui représente la position et la taille des pieds du joueur dans le jeu. Il est initialisé avec des valeurs basées sur la largeur et la hauteur du rectangle "rect" de l'objet, ainsi qu'une hauteur de 12 pixels et une largeur égale à la moitié de la largeur du rectangle "rect". Cet objet "feet" sera utilisé pour détecter les collisions avec le sol dans le jeu
        self.old_position = self.position.copy()                 # initialise l'attribut "old_position" de l'objet avec la copie de la valeur actuelle de l'attribut "position". Cela permettra de sauvegarder la position précédente du joueur avant de déplacer celui-ci, afin de pouvoir le faire revenir à cette position en cas de besoin (collisions)
        self.speed = 1                                           # initialise l'attribut "speed" de l'objet avec la valeur 1, qui représente la vitesse de déplacement du joueur dans le jeu

    def save_location(self): self.old_position = self.position.copy() # définit une méthode appelée "save_location()" qui permet de sauvegarder la position actuelle du joueur dans l'attribut "old_position". Cette méthode sera appelée avant de déplacer le joueur, afin de sauvegarder sa position précédente

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def move_up(self): self.position[1] -= self.speed

    def move_down(self): self.position[1] += self.speed

    # move_right(), move_left(), move_up(), et move_down() sont des méthodes de déplacement du joueur qui mettent à jour la position de l'objet en modifiant les coordonnées x et y de l'attribut "position" en fonction de la direction de déplacement. La vitesse de déplacement du joueur est déterminée par la valeur de l'attribut "speed"

    def update(self):                             # définit une méthode "update()" qui est appelée pour mettre à jour la position de l'objet dans le jeu. Cette méthode met à jour la position du rectangle "rect" et de l'objet "feet" en fonction de la position actuelle de l'objet "position"
        self.rect.topleft = self.position         # met à jour la position du rectangle "rect" de l'objet en déplaçant son coin supérieur gauche à la position actuelle de l'objet "position"
        self.feet.midbottom = self.rect.midbottom # met à jour la position de l'objet "feet" en déplaçant son point milieu en bas à la position milieu en bas du rectangle "rect" de l'objet

    def move_back(self):                          # définit une méthode "move_back()" qui ne prend pas de paramètres, mais utilise "self" pour se référer à l'objet sur lequel la méthode est appelée
        self.position = self.old_position         # rétablit la position actuelle de l'objet "position" à la valeur de la position sauvegardée précédemment dans "old_position". Cela permet de revenir à la position précédente de l'objet avant un mouvement ou une collision
        self.rect.topleft = self.position         # met à jour la position du rectangle "rect" de l'objet pour correspondre à la nouvelle position restaurée
        self.feet.midbottom = self.rect.midbottom # met à jour la position du rectangle "feet" de l'objet pour correspondre à la nouvelle position restaurée

class Player(Entity):

    def __init__(self, name, path):
        super().__init__(f"{name}", 0, 0, path)