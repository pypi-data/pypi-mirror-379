import pygame

import math
from better_math import Vector2i


class DrawContext:
    def __init__(self, screen: pygame.Surface, position_offset: Vector2i = Vector2i(0, 0)):
        self.screen = screen
        self.position_offset = position_offset
        self._rendered_texture_cache : dict[tuple[tuple[int, int, int, int],Vector2i,Vector2i,tuple[int,int,int]], pygame.Surface] = {}
    _texture_cache: dict[str, pygame.Surface] = {}
    def _load_texture(self, path: str) -> pygame.Surface:
        if path not in self._texture_cache:
            self._texture_cache[path] = pygame.image.load(path).convert_alpha()
        return self._texture_cache[path]

    def texture(
            self,
            texture_path: str,
            pos: Vector2i,
            uv: tuple[int, int, int, int] = (0, 0, -1, -1),
            size: Vector2i = Vector2i(32, 32),
            texture_size: Vector2i = Vector2i(16, 16),
            color: tuple[int, int, int] = (255, 255, 255),
    ) -> None:
        """
        Schnelle Version:
        - konvertierte Texturen & (tw,th)-Skalierung werden gecacht
        - Farbmultiplikation wird gecacht
        - Tiling via Surface.blits (Batch) statt Python-Doppelschleife
        - überspringt Arbeit in häufigen Trivialfällen
        """
        position = (int(pos.x + self.position_offset.x), int(pos.y + self.position_offset.y))
        cache_surface = self._rendered_texture_cache.get((uv, size, texture_size, color))
        if cache_surface is not None:
            self.screen.blit(cache_surface, position)
            return

        # --- kleine Helfer & Caches ---------------------------------------------
        # erzeuge Caches einmal z.B. im __init__: self._tile_cache = {}, self._color_cache = {}
        # self._load_texture(texture_path) sollte bereits convert_alpha() benutzen!
        def _get_scaled_tile(img, tw, th):
            key = (id(img), tw, th)
            surf = img if (img.get_width() == tw and img.get_height() == th) \
                else pygame.transform.scale(img, (tw, th))
            # wichtig: gleiche Pixel-Format für schnelle Blits
            if surf.get_bitsize() != self.screen.get_bitsize() or not surf.get_masks()[3]:
                surf = surf.convert_alpha()
            return surf

        def _get_colored_tile(tile, color):
            if color == (255, 255, 255):
                return tile
            key = (id(tile), color)
            surf = tile.copy()
            surf.fill((*color, 255), special_flags=pygame.BLEND_RGBA_MULT)
            return surf

        # ------------------------------------------------------------------------
        img = self._load_texture(texture_path)  # sollte convert_alpha liefern

        tw, th = int(texture_size.x), int(texture_size.y)
        if tw <= 0 or th <= 0:
            return

        u0, v0, uW, vH = uv
        if uW == -1: uW = tw
        if vH == -1: vH = th
        if uW <= 0 or vH <= 0:
            return

        # 1) Tile auf (tw,th) skalieren (aus Cache)
        base_tile = _get_scaled_tile(img, tw, th)

        # 2) Farbe anwenden (aus Cache)
        tile = _get_colored_tile(base_tile, color)

        # Fast-Path A: genau ein Tile, kein Offset → direkte Verwendung
        if (uW == tw and vH == th) and (u0 % tw == 0) and (v0 % th == 0):
            # ggf. auf Zielgröße skalieren
            if size.x != uW or size.y != vH:
                render_surface = pygame.transform.scale(tile, (int(size.x), int(size.y)))
                self.screen.blit(render_surface, position)
            else:
                self.screen.blit(tile, position)
            return

        # 3) Musterfläche (uW x vH) füllen (mit Offset) – per Batch-Blit
        pattern_surface = pygame.Surface((uW, vH), flags=pygame.SRCALPHA)

        # Startposition so wählen, dass das erste sichtbare Tile links/oben außerhalb beginnt
        offset_x = (-u0) % tw
        offset_y = (-v0) % th
        start_x = offset_x - tw
        start_y = offset_y - th

        tiles_x = (uW // tw) + 3
        tiles_y = (vH // th) + 3

        # Alle Zielpositionen vorab berechnen und in einem Rutsch blitten
        dests = []
        bx = start_x
        for ix in range(tiles_x):
            by = start_y
            for iy in range(tiles_y):
                dests.append((bx, by))
                by += th
            bx += tw
        # Batch-Blit (deutlich weniger Python-Overhead als Doppel-Schleife)
        pattern_surface.blits([(tile, d) for d in dests])

        # 4) Auf Zielgröße bringen (Nearest Neighbor)
        if size.x != uW or size.y != vH:
            render_surface = pygame.transform.scale(pattern_surface, (int(size.x), int(size.y)))
        else:
            render_surface = pattern_surface

        # 5) Zeichnen
        self._rendered_texture_cache[(uv, size, texture_size, color)] = render_surface
        self.screen.blit(render_surface, position)



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

