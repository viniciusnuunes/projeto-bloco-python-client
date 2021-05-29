import cpuinfo
import psutil
import pygame
import properties as CONSTAT

cpu_info = cpuinfo.get_cpu_info()

def carrega_cpu_info(superior_surface, inferior_surface, tela, font):
    __mostra_info_cpu(superior_surface, tela, font)
    __mostra_uso_cpu(inferior_surface, tela)


def __mostra_info_cpu(surface, tela, font):
    surface.fill(CONSTAT.BRANCO)
    __mostra_texto(surface, "Nome:", "brand_raw", 10, font)
    __mostra_texto(surface, "Arquitetura:", "arch", 30, font)
    __mostra_texto(surface, "Palavra (bits):", "bits", 50, font)
    __mostra_texto(surface, "Frequência (MHz):", "freq", 70, font)
    __mostra_texto(surface, "Núcleos (físicos):", "nucleos", 90, font)
    tela.blit(surface, (0, 0))
    
def __mostra_texto(surface, nome, chave, pos_y, font):
    text = font.render(nome, True, CONSTAT.PRETO)
    surface.blit(text, (10, pos_y))

    if chave == "freq":
        textInfo = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        textInfo = str(psutil.cpu_count())
        textInfo = textInfo + " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:        
        textInfo = str(cpu_info[chave])

    text = font.render(textInfo, True, CONSTAT.CINZA)
    surface.blit(text, (200, pos_y))
    
def __mostra_uso_cpu(surface, tela):
    cpu_percent = psutil.cpu_percent(interval=0, percpu=True)
    surface.fill(CONSTAT.CINZA)

    num_cpu = len(cpu_percent)
    x = y = 10
    desl = 10
    alt = surface.get_height() - 2*y
    larg = (surface.get_width()-2*y - (num_cpu+1)*desl)/num_cpu
    d = x + desl

    for i in cpu_percent:
        pygame.draw.rect(surface, CONSTAT.VERMELHO, (d, y, larg, alt))
        pygame.draw.rect(surface, CONSTAT.AZUL, 	(d, y, larg, (1-i/100)*alt))
        d = d + larg + desl
    # parte mais abaixo da tela e à esquerda
    tela.blit(surface, (0, CONSTAT.ALTURA_TELA/5))