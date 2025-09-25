import pygame

class Code:
    def __init__(self, Sprite):
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.SCALED)
        self.running = True
        self.input_text = ""
        self.mouse_down = [False, (0, 0)]
        self.timer = pygame.time.get_ticks()

        self.sprite = []
        self.tasks = []
        self.sprites = pygame.sprite.Group()
        for i in range(len(Sprite)):
            self.sprite.append(Sprite[i](self.screen))

            self.start(i)
        
        for i in range(len(self.sprite)):
            self.sprite[i].all_sprite = self.sprite
    
    def start(self, i):
        self.tasks.insert(i, self.sprite[i].run())

        self.sprites.add(self.sprite[i].core.sprites)

    def restart(self):
        self.stop()

        self.sprites.empty()
        self.running = True

        for i in range(len(self.sprite)):
            self.start(i)

    def update(self):
        all_broadcast = []
        if self.running:
            self.sprites.empty()
            for i in range(len(self.sprite)):
                self.sprites.add(self.sprite[i].core.sprites)

                try:
                    next(self.tasks[i])
                except StopIteration:
                    pass
                except IndexError:
                    self.stop()
                except TypeError:
                    pass

                self.sprite[i].core.input_text = self.input_text
                self.sprite[i].core.input_key = pygame.key.get_pressed()
                for y in self.sprite[i].core.broadcast_list:
                    if not y in all_broadcast:
                        all_broadcast.append(y)
                self.sprite[i].core.broadcast_list = []
                self.sprite[i].core.all_broadcast_list = all_broadcast
                self.sprite[i].core.update_clones()

                self.sprite[i].core.mouse_down = False
                self.sprite[i].core.click_sprite = False
                if self.mouse_down[0]:
                    if not self.sprite[i].core.dragging:
                        if self.sprite[i].core.object.rect.collidepoint(self.mouse_down[1]):
                            self.sprite[i].core.click_sprite = True
                            if self.sprite[i].core.draggable:
                                self.sprite[i].core.dragging = True
                else:
                    self.sprite[i].core.dragging = False

                if self.sprite[i].core.dragging:
                    mouse = pygame.mouse.get_pos()
                    self.sprite[i].core.go_to(mouse[0], mouse[1])

                if not self.sprite[i].core.asking and self.input_text != "":
                    self.input_text = ""

                if not self.sprite[i].core.running:
                    self.stop()
                    break

            if self.running == False:
                self.stop()

            self.sprites.draw(self.screen)
    
    def stop(self):
        for i in range(len(self.sprite)):
            self.sprite[i].core.stop_all_sound()

        self.running = False