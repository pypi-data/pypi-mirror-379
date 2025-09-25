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

    import pygame
    from typing import Tuple

    Vector2i = Tuple[int, int]

    class Renderer:
        def __init__(self, target_surface: pygame.Surface):
            self.target = target_surface
            self._texture_cache: dict[str, pygame.Surface] = {}

        def _load_texture(self, texture_path: str) -> pygame.Surface:
            if texture_path not in self._texture_cache:
                self._texture_cache[texture_path] = pygame.image.load(texture_path).convert_alpha()
            return self._texture_cache[texture_path]

        def texture(
                self,
                texture_path: str,
                position: Vector2i,
                uv: tuple[int, int, int, int] = (0, 0, -1, -1),
                size: Vector2i = (32, 32),
                texture_size: Vector2i = (16, 16),
                color: tuple[int, int, int] = (255, 255, 255),
        ) -> None:
            """
            Rendert eine Textur mit UV in Texturkoordinaten (relativ zu texture_size),
            kachelt bei Bedarf und multipliziert anschließend die Farbe.

            - uv[2]/uv[3] == -1 → automatisch texture_size.
            - Tiling, wenn uv-Breite/Höhe > texture_size.
            - uv[0]/uv[1] sind Offsets (mod texture_size).
            - 'color' multipliziert die Pixel (BLEND_RGBA_MULT), 255 = keine Änderung.
            """
            img = self._load_texture(texture_path)

            tw, th = int(texture_size[0]), int(texture_size[1])
            if tw <= 0 or th <= 0:
                return

            u0, v0, uW, vH = uv
            if uW == -1:
                uW = tw
            if vH == -1:
                vH = th
            if uW <= 0 or vH <= 0:
                return

            # 1) Tile auf texture_size bringen (Nearest Neighbor, kein Blur)
            img_tile = img
            if img.get_width() != tw or img.get_height() != th:
                img_tile = pygame.transform.scale(img, (tw, th))

            # 2) Farb-Multiplikation auf die Kachel anwenden (einmalig, dann kacheln = effizient)
            if color != (255, 255, 255):
                r, g, b = color
                img_tile = img_tile.copy()
                img_tile.fill((r, g, b, 255), special_flags=pygame.BLEND_RGBA_MULT)

            # 3) Musterfläche (uW x vH) füllen (mit Offset)
            pattern_surface = pygame.Surface((uW, vH), flags=pygame.SRCALPHA)
            offset_x = (-u0) % tw
            offset_y = (-v0) % th
            start_x = offset_x - tw
            start_y = offset_y - th
            tiles_x = (uW // tw) + 3
            tiles_y = (vH // th) + 3

            for iy in range(tiles_y):
                for ix in range(tiles_x):
                    dst_x = start_x + ix * tw
                    dst_y = start_y + iy * th
                    pattern_surface.blit(img_tile, (dst_x, dst_y))

            # 4) Auf Zielgröße bringen (Nearest Neighbor)
            if size != (uW, vH):
                render_surface = pygame.transform.scale(pattern_surface, (int(size[0]), int(size[1])))
            else:
                render_surface = pattern_surface

            # 5) Zeichnen
            self.target.blit(render_surface, (int(position[0]), int(position[1])))



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

