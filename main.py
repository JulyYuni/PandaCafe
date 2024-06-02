
'''''''''''IMPORTS'''''''''

from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *




'''''''''''VARIÁVEIS'''''''''

# Variáveis Numéricas

    # Básicas
gamestate = 0
clicked  = 0
player_velocity = 500


# Definindo os sprites

    # Definindo os botões comuns
button_play = Sprite("assets/images/buttons/button-play.png", 1)
button_difficulty = Sprite("assets/images/buttons/button-difficulty.png", 1)
button_ranking = Sprite("assets/images/buttons/button-ranking.png", 1)
button_exit = Sprite("assets/images/buttons/button-exit.png", 1)

button_easy = Sprite("assets/images/buttons/button-easy.png", 1)
button_medium = Sprite("assets/images/buttons/button-medium.png", 1)
button_hard = Sprite("assets/images/buttons/button-hard.png", 1)

    # Definindo os botões em hover
button_play_hover = Sprite("assets/images/hover-buttons/button-play-hover.png", 1)
button_difficulty_hover = Sprite("assets/images/hover-buttons/button-difficulty-hover.png", 1)
button_ranking_hover = Sprite("assets/images/hover-buttons/button-ranking-hover.png", 1)
button_exit_hover = Sprite("assets/images/hover-buttons/button-exit-hover.png", 1)

button_easy_hover = Sprite("assets/images/hover-buttons/button-easy-hover.png", 1)       
button_medium_hover = Sprite("assets/images/hover-buttons/button-medium-hover.png", 1)
button_hard_hover = Sprite("assets/images/hover-buttons/button-hard-hover.png", 1)

    # Definindo backgrounds
background = Sprite("assets/images/backgrounds/background.png", 1)
background_menu = Sprite("assets/images/backgrounds/background-menu.jpg", 1)

    # Definindo personagens
player = Sprite("assets/images/objects/player.png", 1)


# Inicializando objetos

    # Recebendo a resolução da tela do usuário
resolution = pygame.display.Info()
screen_height_resolution = resolution.current_h
screen_width_resolution = resolution.current_w

    # Criando uma janela com a resolução total do usuário
screen = Window(screen_width_resolution, screen_height_resolution)

    #  Recebendo entrada do mouse e teclado
mouse_object = Window.get_mouse()
keyboard_object = Window.get_keyboard()

    #  Inicializando o relógio
clock = pygame.time.Clock()


# Variáveis auxiliares para o posicionamento dos botões

    # Largura e alturo dos botões
buttons_width = button_play.width
buttons_height = button_play.height

    # Posição de botões em x e valor de gap em y entre botões
buttons_x = screen.width/2 - (buttons_width/2)
buttons_y_gap = (screen.height - buttons_height *4) /5

    # Posições de botões que se repetem em y
buttons_difficulty_y = buttons_height *1 + buttons_y_gap *2
buttons_ranking_y =     buttons_height *2 + buttons_y_gap *3
buttons_exit_y =        buttons_height *3 + buttons_y_gap *4
button_medium_y =       (buttons_exit_y - buttons_y_gap )   /2


# Listas

    # Botões do menu principal
buttons_principal_menu = [button_play, button_difficulty, button_ranking, button_exit]
buttons_hover_principal_menu = [button_play_hover, button_difficulty_hover, button_ranking_hover, button_exit_hover]

    # Botões do menu dificuldades
buttons_difficulty_menu = [button_easy, button_medium, button_hard]
buttons_hover_difficulty_menu = [button_easy_hover, button_medium_hover, button_hard_hover]


# Bordas do player

player_border_up = 405 - player.height
player_border_down = screen_height_resolution - player.height
player_border_left = 0
player_border_right = screen_width_resolution - player.width


'''''''''''FUNÇÕES'''''''''

#1 Menu principal
def principal_menu():
    global gamestate
    global clicked  # Declarando clicked como global

    while gamestate == 0:

        # Gerando cenário
        positions()
        creating_scene()

        # Retorna se o usuário clickou em algum botão e em qual botão ele clickou
        clicked, click_left = click_hover(buttons_principal_menu, buttons_hover_principal_menu)

        # Se o botão já foi clickado, mas o usuário soltou o click
        if click_left == False and clicked > 0:
            
            # Botão play clickado, abre o jogo
            if clicked == 1:
                play()

                # Saiu do play, reseta para o menu principal
                gamestate = 0
                clicked = 0
       
            # Botão dificuldade clickado, abre o menu dificuldades
            elif clicked == 2:
                menu_difficulty()

                # Saiu do menu dificuldades, reseta para o menu principal
                gamestate = 0
                clicked = 0

            # Botão ranking clickado, abre ranking
            elif clicked == 3:
                print("Não habemos ranking ainda! :/")

            # Botão sair clickado, fecha o jogo
            elif clicked == 4:
                screen.close()
        
        #Atualiza a janela
        screen.update()



#2 Play
def play():
    global gamestate
    gamestate = 1
    
    # Define posições
    positions()

    while gamestate == 1:

        # Cenário é criado
        creating_scene()
        
        # Recebe entradas do teclado
        player_movement()

        # Não deixa o payer ultrapassar a borda
        keep_player_in_screen_bounds()

        # Imprime fps
        print_fps()

        # Atualiza janela
        screen.update()


        '''if player.y <= 410 - player.height:
            print(player.y)'''

        # Voltar para o menu
        if(keyboard_object.key_pressed("ESC")):
            break
        


#3 Menu de dificuldade (função que altera velocidade da nave e do tiro)
def menu_difficulty():
    global gamestate
    gamestate = 2

    # Gerando cenário
    positions()
    creating_scene()

    while gamestate == 2:

        # Retorna se o usuário clickou em algum botão e em qual botão ele clickou
        clicked, click_left = click_hover(buttons_difficulty_menu, buttons_hover_difficulty_menu)

        # Se o botão já foi clickado, mas o usuário soltou o click
        if click_left == False and clicked > 0:

            # Fácil
            if clicked == 1:
                print("Não acontece nada ainda")

            # Médio
            elif clicked == 2:
                print("Não acontece nada mesmo")

            # Difícil
            elif clicked == 3:
                print("Já tô ficando triste ;(")

        #Atualiza a janela
        screen.update()

        #Voltar para o menu
        if(keyboard_object.key_pressed("ESC")):
            break



#4 Função que gera o cenário
def creating_scene():

    #Cor da Janela
    screen.set_background_color([255,174,183])

    #Menu principal
    if gamestate == 0:
        background_menu.draw()
        button_play.draw()
        button_difficulty.draw()
        button_ranking.draw()
        button_exit.draw()
        #print("entrou 0")
    #Play
    if gamestate == 1:
        background.draw()
        player.draw()
        #print("entrou 1")
    
    #Menu dificuldades
    if gamestate == 2:
        background_menu.draw()
        button_easy.draw()
        button_medium.draw()
        button_hard.draw()



#5 Definição das posições de início de partida
def positions():

    # Botões menu principal
    button_play.set_position(buttons_x , buttons_y_gap)
    button_difficulty.set_position(buttons_x , buttons_difficulty_y)
    button_ranking.set_position(buttons_x , buttons_ranking_y)
    button_exit.set_position(buttons_x , buttons_exit_y)

    # Botões hover principal
    button_play_hover.set_position(buttons_x , buttons_y_gap)
    button_difficulty_hover.set_position(buttons_x , buttons_difficulty_y)
    button_ranking_hover.set_position(buttons_x , buttons_ranking_y)
    button_exit_hover.set_position(buttons_x , buttons_exit_y)

    # Botões menu dificuldades
    button_easy.set_position(buttons_x , buttons_y_gap)
    button_medium.set_position(buttons_x  , button_medium_y)
    button_hard.set_position(buttons_x , buttons_exit_y)

    # Botões hover menu dificuldades
    button_easy_hover.set_position(buttons_x , buttons_y_gap)
    button_medium_hover.set_position(buttons_x  , button_medium_y)
    button_hard_hover.set_position(buttons_x , buttons_exit_y)

    # Posição inicial player
    player.set_position(50, screen_height_resolution/2)


#6 Função que recebe as entradas do teclado
def player_movement():

    # Move nave para esquerda
    if(keyboard_object.key_pressed("LEFT") == True):
        if player.x > 0:
            player.x += - player_velocity * screen.delta_time()            

    # Move nave para direita
    if(keyboard_object.key_pressed("RIGHT") == True):
        if player.x < player_border_right:
            player.x += player_velocity * screen.delta_time()
    
    # Move player para cima
    if(keyboard_object.key_pressed("UP") == True):
        if player.y > player_border_up:
            player.y -= player_velocity * screen.delta_time()
            
    # Move player para baixo
    if(keyboard_object.key_pressed("DOWN") == True):
        if player.y < player_border_down:
            player.y += player_velocity * screen.delta_time()
                
    
#7 Contendo do player dentro da Janela sem ultrapassá-la
def keep_player_in_screen_bounds():

    # Se a posição y do player for menor ou igual que a parede de cima (0), reposicione-o no limite da borda
    if player.y < player_border_up:
        player.y = player_border_up
  
    # Se a posição y do player for maior que a parede de baixo, reposicione-o no limite da borda
    if player.y > player_border_down:
        player.y = player_border_down

    # Se a posição x do player for menor ou igual que a parede da esquerda (0), reposicione-o no limite da borda
    if player.x < player_border_left:
        player.x = player_border_left
    
    # Se a posição x do player for maior que a parede da direita, reposicione-o no limite da borda
    if player.x > player_border_right:
        player.x = player_border_right


#8 Click e hover nos botoes
def click_hover(buttons, buttons_hover):
    global clicked
    is_hover = []

    #Verificações do hover nos botoes
    for button in buttons:
        is_hover.append(mouse_object.is_over_object(button))

    #Verificacao do click no botao esquerdo do mouse
    click_left = mouse_object.is_button_pressed(1)

    #Para cada botão em tela, verificar
    for index, hover in enumerate(is_hover): 
        #Se o mouse estiver em cima do botão
        if hover == True:
            #Desenha e posiciona botão hover
            positions()
            buttons_hover[index].draw()        

            #Se clickou guarde essa informação
            if click_left == True:
                clicked = index+1         

        #Se o mouse não estiver em cima, desenhe o botão normal
        elif hover == False:
            positions()
            buttons[index].draw()

    return clicked, click_left

#9 Imprime fps na tela do jogo
def print_fps():
    global fps

    # Obtém o FPS atual
    fps = int(clock.get_fps())

    #Imprime o fps na tela
    screen.draw_text(f"FPS: {fps}", 100, 50, size=30, color=(151, 0, 71), font_name="Arial", bold=True, italic=True)

    # Limita a taxa de quadros por segundo
    clock.tick(60)  # Limite de 60 FPS


''' EXECUÇÃO '''

if __name__ == "__main__":
    principal_menu()  