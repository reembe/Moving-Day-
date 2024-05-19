import pygame
import time
import random
from welcome import WelcomeChicken
from box import Box
from candy import Candy
from toys import Toys
from clothing import Clothes
from dishes import Dishes
from stationery import Stationery

pygame.init()
pygame.font.init()
bold_font = pygame.font.SysFont('comicsans', 40, bold=pygame.font.Font.bold)
font = pygame.font.SysFont('comicsans', 40)
sm_font = pygame.font.SysFont('comicsans', 30)
pygame.display.set_caption("Moving Day!")
start_time = time.time()
current_time = time.time()
elapsed_time = 0


# set up screen
SCREEN_HEIGHT = 840
SCREEN_WIDTH = 1160
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
final_time = 0

# rectangles
w_c = WelcomeChicken(0, 220, "latest.png")
w_t = WelcomeChicken(230, 320, "title.png")
level_boxes = WelcomeChicken(30, 470, "9k-removebg-preview.png")
b = Box(1000, 700)

# booleans
run = True
playing = False
just_starting = True
selection = False
level_1 = False
level_2 = False
level_3 = False
level_4 = False
item_tally = 0
score = 0
collected = False
results_screen = False
not_full = False


while run:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False

    if playing == False and just_starting == True:
        screen.blit(font.render("You're moving to Antarctica :O", True, (255, 255, 255)), (330, 50))
        screen.blit(font.render("Your mom's yelling at you to pack your things!", True, (255, 255, 255)), (210, 100))
        screen.blit(font.render("Learn about organization to prepare!", True, (255, 255, 255)), (265, 150))
        screen.blit(font.render("---> Press Enter to Begin <---", True, (255, 255, 255)), ((325, 210)))
        screen.blit(w_c.image, w_c.rect)
        screen.blit(w_t.image, w_t.rect)
        pygame.display.update()
        screen.fill((238, 190, 227))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            playing = True
            start_time = time.time()
            just_starting = False

    if playing == True and selection == False and results_screen == False:
        pygame.display.update()
        screen.fill((238, 190, 227))
        screen.blit(font.render("Select a level", True, (255, 255, 255)), (150, 100))
        screen.blit(font.render("Press <1> for Level 1", True, (255, 255, 255)), (100, 230)) # C,t
        screen.blit(font.render("Press <2> for Level 2", True, (255, 255, 255)), (100, 330)) # c,T,s
        screen.blit(font.render("Press <3> for Level 3", True, (255, 255, 255)), (100, 430)) # c,t,S,CL
        screen.blit(font.render("Press <4> for Level 4", True, (255, 255, 255)), (100, 530)) # C,t,s,cl,D
        screen.blit(sm_font.render("-> Use WASD to move", True, (255, 255, 255)), (650, 100))
        screen.blit(sm_font.render("-> Organize your box with ", True, (255, 255, 255)), (650, 200))
        screen.blit(sm_font.render("the correct item before", True, (255, 255, 255)), (650, 250))
        screen.blit(sm_font.render("timer runs out!", True, (255, 255, 255)),(650, 300))
        screen.blit(sm_font.render("<Watch out for items that", True, (255, 255, 255)), (650, 400))
        screen.blit(sm_font.render("don't belong in the box>", True, (255, 255, 255)), (650, 450))
        screen.blit(sm_font.render("-> Incorrect items result", True, (255, 255, 255)), (650, 550))
        screen.blit(sm_font.render("in a point deduction!", True, (255, 255, 255)), (650, 600))

        # rectangles according to level
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            selection = True
            level_1 = True
            c1 = Candy(50, 105, "candy1.png", True, False)
            c2 = Candy(700, 370, "candy2.png", False, True)
            c3 = Candy(200, 580, "candy3.png", False, False)
            t1 = Toys(1070, 90, "toy1.png", True, False)
            t2 = Toys(430, 350, "toy2.png", False, True)
            t3 = Toys(600, 630, "toy3.png", False, False)
            current_time = time.time()
            elapsed_time = round(current_time - start_time)
            start_time = time.time()

        if keys[pygame.K_2]:
            selection = True
            level_2 = True
            c1 = Candy(50, 105, "candy1.png", True, False)
            c2 = Candy(700, 370, "candy2.png", False, True)
            c3 = Candy(200, 580, "candy3.png", False, False)
            t1 = Toys(1070, 90, "toy1.png", True, False)
            t2 = Toys(430, 350, "toy2.png", False, True)
            t3 = Toys(600, 630, "toy3.png", False, False)
            s1 = Stationery(850, 100, "stationery1.png", False)
            s2 = Stationery(10, 330, "stationery2.png", True)
            s3 = Stationery(400, 715, "stationery3.png", False)
            current_time = time.time()
            elapsed_time = round(current_time - start_time)
            start_time = time.time()

        if keys[pygame.K_3]:
            results_screen = False
            selection = True
            level_3 = True
            c1 = Candy(50, 105, "candy1.png", True, False)
            c2 = Candy(700, 370, "candy2.png", False, True)
            c3 = Candy(200, 580, "candy3.png", False, False)
            t1 = Toys(1070, 90, "toy1.png", True, False)
            t2 = Toys(430, 350, "toy2.png", False, True)
            t3 = Toys(600, 630, "toy3.png", False, False)
            s1 = Stationery(850, 100, "stationery1.png", False)
            s2 = Stationery(10, 330, "stationery2.png", True)
            s3 = Stationery(400, 715, "stationery3.png", False)
            cl1 = Clothes(470, 85, "clothes1.png", False, True)
            cl2 = Clothes(230, 340, "clothes2.png", False, False)
            cl3 = Clothes(10, 710, "clothes3.png", True, False)
            current_time = time.time()
            elapsed_time = round(current_time - start_time)
            start_time = time.time()

        if keys[pygame.K_4]:
            selection = True
            level_4 = True
            c1 = Candy(50, 105, "candy1.png", True, False)
            c2 = Candy(700, 370, "candy2.png", False, True)
            c3 = Candy(200, 580, "candy3.png", False, False)
            t1 = Toys(1070, 90, "toy1.png", True, False)
            t2 = Toys(430, 350, "toy2.png", False, True)
            t3 = Toys(600, 630, "toy3.png", False, False)
            s1 = Stationery(850, 100, "stationery1.png", False)
            s2 = Stationery(10, 330, "stationery2.png", True)
            s3 = Stationery(400, 715, "stationery3.png", False)
            cl1 = Clothes(470, 85, "clothes1.png", False, True)
            cl2 = Clothes(230, 340, "clothes2.png", False, False)
            cl3 = Clothes(10, 710, "clothes3.png", True, False)
            d1 = Dishes(290, 120, "cup.png")
            d2 = Dishes(1000, 350, "plate.png")
            d3 = Dishes(825, 590, "chopsticks.png")
            current_time = time.time()
            elapsed_time = round(current_time - start_time)
            start_time = time.time()


    if selection == True and level_1 == True: # LEVEL 1
        if elapsed_time == 10:
            selection = False
            level_1 = False
            item_tally = 0
            elapsed_time = 0
            results_screen = True

        current_time = time.time()
        elapsed_time = round(current_time - start_time)
        pygame.display.update()
        screen.fill((150, 240, 200))
        screen.blit(sm_font.render("Time remaining: " + str(10 - elapsed_time), True, (255, 255, 255)), (0, 50))
        keys = pygame.key.get_pressed()
        b_x = b.get_x()
        b_y = b.get_y()

        if keys[pygame.K_d] and playing == True and b_x < 1050:
            b.move_direction("right")
        if keys[pygame.K_w] and playing == True and b_y > 0:
            b.move_direction("up")
        if keys[pygame.K_s] and playing == True and b_y < 760:
            b.move_direction("down")
        if keys[pygame.K_a] and playing == True and b_x > 0:
            b.move_direction("left")

        if b.rect.colliderect(c1.rect) and playing == True:
            c1.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(c2.rect) and playing == True:
            c2.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(c3.rect) and playing == True:
            c3.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(t1.rect) and playing == True:
            t1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t2.rect) and playing == True:
            t2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t3.rect) and playing == True:
            t3.move(10000, 100000)
            score -= 10

        if item_tally == 3:
            selection = False
            level_1 = False
            item_tally = 0
            final_time = 10 - elapsed_time
            elapsed_time = 0
            results_screen = True
            collected = True
            if score != 30:
                not_full = True



    if selection == True and level_2 == True: # LEVEL 2
        if elapsed_time == 15:
            selection = False
            level_1 = False
            item_tally = 0
            elapsed_time = 0
            results_screen = True

        current_time = time.time()
        elapsed_time = round(current_time - start_time)
        pygame.display.update()
        screen.fill((200, 215, 210))
        screen.blit(sm_font.render("Time remaining: " + str(15 - elapsed_time), True, (255, 255, 255)), (0, 50))
        keys = pygame.key.get_pressed()
        b_x = b.get_x()
        b_y = b.get_y()

        if keys[pygame.K_d] and playing == True and b_x < 1050:
            b.move_direction("right")
        if keys[pygame.K_w] and playing == True and b_y > 0:
            b.move_direction("up")
        if keys[pygame.K_s] and playing == True and b_y < 760:
            b.move_direction("down")
        if keys[pygame.K_a] and playing == True and b_x > 0:
            b.move_direction("left")

        if b.rect.colliderect(c1.rect) and playing == True:
            c1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(c2.rect) and playing == True:
            c2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(c3.rect) and playing == True:
            c3.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t1.rect) and playing == True:
            t1.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(t2.rect) and playing == True:
            t2.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(t3.rect) and playing == True:
            t3.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(s1.rect) and playing == True:
            s1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(s2.rect) and playing == True:
            s2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(s3.rect) and playing == True:
            s3.move(10000, 100000)
            score -= 10

        if item_tally == 3:
            selection = False
            level_2 = False
            item_tally = 0
            final_time = 15 - elapsed_time
            elapsed_time = 0
            results_screen = True
            collected = True
            if score != 30:
                not_full = True



    if selection == True and level_3 == True: # LEVEL 3
        if elapsed_time == 20:
            selection = False
            level_1 = False
            item_tally = 0
            elapsed_time = 0
            results_screen = True

        current_time = time.time()
        elapsed_time = round(current_time - start_time)
        pygame.display.update()
        screen.fill((150, 220, 255))
        screen.blit(sm_font.render("Time remaining: " + str(20 - elapsed_time), True, (255, 255, 255)), (0, 50))
        keys = pygame.key.get_pressed()
        b_x = b.get_x()
        b_y = b.get_y()

        if keys[pygame.K_d] and playing == True and b_x < 1050:
            b.move_direction("right")
        if keys[pygame.K_w] and playing == True and b_y > 0:
            b.move_direction("up")
        if keys[pygame.K_s] and playing == True and b_y < 760:
            b.move_direction("down")
        if keys[pygame.K_a] and playing == True and b_x > 0:
            b.move_direction("left")

        if b.rect.colliderect(c1.rect) and playing == True:
            c1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(c2.rect) and playing == True:
            c2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(c3.rect) and playing == True:
            c3.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t1.rect) and playing == True:
            t1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t2.rect) and playing == True:
            t2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t3.rect) and playing == True:
            t3.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(s1.rect) and playing == True:
            s1.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(s2.rect) and playing == True:
            s2.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(s3.rect) and playing == True:
            s3.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(cl1.rect) and playing == True:
            cl1.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(cl2.rect) and playing == True:
            cl2.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(cl3.rect) and playing == True:
            cl3.move(10000, 100000)
            score += 10
            item_tally += 1

        if item_tally == 6:
            selection = False
            level_3 = False
            item_tally = 0
            final_time = 20 - elapsed_time
            elapsed_time = 0
            results_screen = True
            collected = True
            if score != 60:
                not_full = True



    if selection == True and level_4 == True: # LEVEL 4
        if elapsed_time == 25:
            selection = False
            level_1 = False
            item_tally = 0
            elapsed_time = 0
            results_screen = True

        current_time = time.time()
        elapsed_time = round(current_time - start_time)
        pygame.display.update()
        screen.fill((205, 200, 245))
        screen.blit(sm_font.render("Time remaining: " + str(25 - elapsed_time), True, (255, 255, 255)), (0, 50))
        keys = pygame.key.get_pressed()
        b_x = b.get_x()
        b_y = b.get_y()

        if keys[pygame.K_d] and playing == True and b_x < 1050:
            b.move_direction("right")
        if keys[pygame.K_w] and playing == True and b_y > 0:
            b.move_direction("up")
        if keys[pygame.K_s] and playing == True and b_y < 760:
            b.move_direction("down")
        if keys[pygame.K_a] and playing == True and b_x > 0:
            b.move_direction("left")


        if b.rect.colliderect(c1.rect) and playing == True:
            c1.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(c2.rect) and playing == True:
            c2.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(c3.rect) and playing == True:
            c3.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(t1.rect) and playing == True:
            t1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t2.rect) and playing == True:
            t2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(t3.rect) and playing == True:
            t3.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(s1.rect) and playing == True:
            s1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(s2.rect) and playing == True:
            s2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(s3.rect) and playing == True:
            s3.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(cl1.rect) and playing == True:
            cl1.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(cl2.rect) and playing == True:
            cl2.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(cl3.rect) and playing == True:
            cl3.move(10000, 100000)
            score -= 10
        if b.rect.colliderect(d1.rect) and playing == True:
            d1.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(d2.rect) and playing == True:
            d2.move(10000, 100000)
            score += 10
            item_tally += 1
        if b.rect.colliderect(d3.rect) and playing == True:
            d3.move(10000, 100000)
            score += 10
            item_tally += 1

        if item_tally == 6:
            selection = False
            level_3 = False
            item_tally = 0
            final_time = 25 - elapsed_time
            elapsed_time = 0
            results_screen = True
            collected = True
            if score != 60:
                not_full = True


    if selection == True:
        screen.blit(b.image, b.rect)
        screen.blit(c1.image, c1.rect)
        screen.blit(c2.image, c2.rect)
        screen.blit(c3.image, c3.rect)
        screen.blit(t1.image, t1.rect)
        screen.blit(t2.image, t2.rect)
        screen.blit(t3.image, t3.rect)
        display_score = sm_font.render("Score: " + str(score), True, (255,255,255))
        screen.blit(display_score, (0, 0))
        if level_1 == True:
            screen.blit(font.render("Organize the candy!", True, (255, 255, 255)), (400, 0))
        if level_2 == True:
            screen.blit(font.render("Organize the toys!", True, (255, 255, 255)), (400, 0))
            screen.blit(s1.image, s1.rect)
            screen.blit(s2.image, s2.rect)
            screen.blit(s3.image, s3.rect)
        if level_3 == True:
            screen.blit(font.render("Organize the school supplies & clothes!", True, (255, 255, 255)), (300, 0))
            screen.blit(s1.image, s1.rect)
            screen.blit(s2.image, s2.rect)
            screen.blit(s3.image, s3.rect)
            screen.blit(cl1.image, cl1.rect)
            screen.blit(cl2.image, cl2.rect)
            screen.blit(cl3.image, cl3.rect)
        if level_4 == True:
            screen.blit(font.render("Organize the tableware & candy!", True, (255, 255, 255)), (300, 0))
            screen.blit(s1.image, s1.rect)
            screen.blit(s2.image, s2.rect)
            screen.blit(s3.image, s3.rect)
            screen.blit(cl1.image, cl1.rect)
            screen.blit(cl2.image, cl2.rect)
            screen.blit(cl3.image, cl3.rect)
            screen.blit(d1.image, d1.rect)
            screen.blit(d2.image, d2.rect)
            screen.blit(d3.image, d3.rect)


    if results_screen == True:
        b = Box(1000, 700)
        time.sleep(.10)
        screen.fill((238, 190, 227))
        pygame.display.update()
        if collected == True and not_full == False:
            screen.blit(font.render("Time remaining: " + str(final_time), True, (255, 255, 255)), (300, 230))
            screen.blit(font.render("You organized all the correct items before the time was up!", True, (255, 255, 255)), (30, 290))
            screen.blit(font.render("Score: " + str(score), True, (255, 255, 255)), (350, 360))
            screen.blit(level_boxes.image, level_boxes.rect)
            pygame.display.update()
            time.sleep(2)
            results_screen = False
            collected = False
            score = 0
        elif collected == True and not_full == True:
            screen.blit(font.render("Time remaining: " + str(final_time), True, (255, 255, 255)), (300, 230))
            screen.blit(font.render("You organized the wrong items!", True, (255, 255, 255)), (200, 290))
            screen.blit(font.render("Score: " + str(score), True, (255, 255, 255)), (350, 360))
            screen.blit(level_boxes.image, level_boxes.rect)
            pygame.display.update()
            time.sleep(2)
            results_screen = False
            collected = False
            not_full = False
            score = 0

        else:
            screen.blit(font.render("You ran out of time!", True, (255, 255, 255)), (275, 250))
            screen.blit(font.render("Score: " + str(score), True, (255, 255, 255)), (300, 315))
            screen.blit(level_boxes.image, level_boxes.rect)
            pygame.display.update()
            time.sleep(2)
            results_screen = False
            score = 0
            not_full = False


