import psutil
import pygame
import properties as CONSTAT

disco_surface = pygame.surface.Surface(
    (CONSTAT.LARGURA_TELA, CONSTAT.ALTURA_TELA))

disco_info = psutil.disk_usage('.')


def exibeDiscoInfo(tela, font):
    __desenha_uso_hd(disco_surface, tela, font)


disk = psutil.disk_usage('/')
disk_total = disk[0]
disk_uso = disk[1]
disk_livre = disk[2]
disk_porcentagem = disk[3]


def __desenha_uso_hd(surface, tela, font):
    # Colocando o fundo inteiro como preto
    surface.fill(CONSTAT.PRETO)
    tela.blit(surface, (0, 0))

    # Desenhando a barra de uso por cima da barra de disco
    largura = (CONSTAT.LARGURA_TELA - 2 * 20) - int(disco_info.percent)
    largura2 = (CONSTAT.LARGURA_TELA - 2 * 20)
    pygame.draw.rect(surface, CONSTAT.CINZA, (20, 50, largura2, 30))
    pygame.draw.rect(surface, CONSTAT.AZUL, (20, 50, largura, 30))
    tela.blit(surface, (0, 90))

    # Capacidade total do disco
    texto_total = "Total do Disco: (" + \
        str(round(disk_total/(1024*1024*1024), 2))+" GB):"
    text = font.render(texto_total, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 10))

    # Desenhando o texto acima da barra de uso de disco
    texto_barra = "Usado: (" + str(disco_info.percent)+" %):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 40))

    # Espaço livre do disco
    texto_livre = "Livre: (" + str(round(disk_livre /
                                         (1024*1024*1024), 2))+" GB):"
    text = font.render(texto_livre, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 70))

    # Porcentagem de uso do disco
    texto_barra = "Porcentagem de uso de Disco: (" + \
        str(disco_info.percent)+" %):"
    text = font.render(texto_barra, 1, CONSTAT.BRANCO)
    tela.blit(text, (20, 100))
