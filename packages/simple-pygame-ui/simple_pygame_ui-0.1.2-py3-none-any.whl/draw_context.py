import pygame

import math
from better_math import Vector2i


class DrawContext:
    def __init__(self, screen: pygame.Surface, position_offset: Vector2i = Vector2i(0, 0)):
        self.screen = screen
        self.position_offset = position_offset
    _texture_cache: dict[str, pygame.Surface] = {}
    def _load_texture(self, path: str) -> pygame.Surface:
        if path not in self._texture_cache:
            self._texture_cache[path] = pygame.image.load(path).convert_alpha()
        return self._texture_cache[path]

    def texture(
            self,
            texture_path: str,
            position: Vector2i,
            uv: tuple[int, int, int, int] = (0, 0, -1, -1),
            size: Vector2i = (32, 32),
            texture_size: Vector2i = (16, 16),
    ) -> None:
        """
        Rendert eine Textur mit UV in 'Textur-Koordinaten', die relativ zu 'texture_size' sind.

        - Wenn uv[2] oder uv[3] == -1, werden sie automatisch auf texture_size gesetzt.
        - Wenn uv-Breite/Höhe größer als texture_size sind, wird die Textur passend oft gekachelt.
        - uv[0], uv[1] wirken wie ein Offset/Scroll in Texturkoordinaten (werden modulo texture_size genommen).
        - Das Ergebnis wird auf 'size' skaliert und bei 'position' gerendert.
        """
        img = self._load_texture(texture_path)

        # 1) Tile-Größe in "UV-Pixeln" (logische Kachelgröße)
        tw, th = int(texture_size.x), int(texture_size.y)
        if tw <= 0 or th <= 0:
            return  # ungültige Größe

        # 2) UV-Rechteck vollständig auflösen
        u0, v0, uW, vH = uv
        if uW == -1:
            uW = tw
        if vH == -1:
            vH = th
        if uW <= 0 or vH <= 0:
            return

        # 3) Quelle an Tile-Größe anpassen: wir definieren EINE Kachel = texture_size.
        #    Wenn die Bildgröße != texture_size ist, skalieren wir die Textur auf texture_size.
        #    So ist die Logik "UV relativ zu texture_size" immer konsistent.
        img_tile = img
        if img.get_width() != tw or img.get_height() != th:
            img_tile = pygame.transform.smoothscale(img, (tw, th))

        # 4) Kachelmusterfläche der Größe (uW, vH) erzeugen und mit Offset (-u0%tw, -v0%th) füllen
        pattern_surface = pygame.Surface((uW, vH), flags=pygame.SRCALPHA)

        # Startoffsets (modulo) – erlauben "verschobenes" Tiling
        offset_x = (-u0) % tw
        offset_y = (-v0) % th

        # Wir beginnen oben/links so, dass die erste Kachel gerade noch das pattern_surface deckt
        start_x = offset_x - tw
        start_y = offset_y - th

        # Anzahl Kacheln, die sicher alles abdecken
        tiles_x = (uW // tw) + 3
        tiles_y = (vH // th) + 3

        for iy in range(tiles_y):
            for ix in range(tiles_x):
                dst_x = start_x + ix * tw
                dst_y = start_y + iy * th
                pattern_surface.blit(img_tile, (dst_x, dst_y))

        # 5) Auf Zielgröße skalieren
        if size != (uW, vH):
            render_surface = pygame.transform.scale(pattern_surface, (int(size.x), int(size.y)))
        else:
            render_surface = pattern_surface

        # 6) Auf Zieloberfläche zeichnen
        self.screen.blit(render_surface, (int(position.x), int(position.y)))



    def text(self, text: str, font: str, pos: Vector2i, size: int, color=(0, 0, 0)):
        """Zeichnet Text ab (pos.x, pos.y) mit pygame.font.SysFont(font, size)."""
        target = self.screen  # erwartet: pygame.Surface vorhanden
        fnt = pygame.font.SysFont(font, size)  # pygame.font ist bereits initialisiert

        x, y = int(pos.x), int(pos.y)
        lines = text.split("\n")
        line_h = fnt.get_linesize()

        for line in lines:
            if line == "":
                y += line_h
                continue
            surf = fnt.render(line, True, color)

            target.blit(surf, (x, y))
            y += line_h

