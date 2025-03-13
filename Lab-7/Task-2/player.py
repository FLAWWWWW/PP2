import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)

_songs = ['Lab-7/Task-2/track01.mp3', 'Lab-7/Task-2/track02.mp3', 'Lab-7/Task-2/track03.mp3']
current_song_index = 0
is_playing = True

pygame.mixer.music.load(_songs[0])
pygame.mixer.music.load(_songs[1])
pygame.mixer.music.load(_songs[2])

def play_song():
    global is_playing
    pygame.mixer.music.unpause()
    is_playing = True

def start_song():
    global is_playing
    pygame.mixer.music.load(_songs[current_song_index])
    pygame.mixer.music.play()
    is_playing = True

def stop_song():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(_songs)
    start_song()

def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(_songs)
    start_song()

start_song()

done = False
while not done:

    pressed = pygame.key.get_pressed()

    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END and is_playing == True:
            print("the song ended!")
            play_next_song()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and ctrl_held:
                done = True
            if event.key == pygame.K_F4 and alt_held:
                done = True
            if event.key == pygame.K_ESCAPE:
                done = True
            
            if event.key == pygame.K_q and is_playing == True:
                print("Stop")
                stop_song()
            elif event.key == pygame.K_w and is_playing == False:
                print("Start")
                play_song()
            elif event.key == pygame.K_e:
                print("Next")
                play_next_song()
            elif event.key == pygame.K_r:
                print("Previous")
                play_previous_song()

    screen.fill((255, 255, 255))

    pygame.display.flip()