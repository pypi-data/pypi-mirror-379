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
    def texture(self, texture_path, position: Vector2i, uv: tuple[int, int, int, int] = (0, 0, -1, -1),
                size=Vector2i(32, 32),texture_size=Vector2i(16,16)) -> None:
        texture = self._load_texture(texture_path)

        # Basis-Tile
        tile = texture.subsurface(pygame.Rect(0, 0, texture_size.x, texture_size.y))
        tile_w, tile_h = tile.get_size()

        # --- Schritt 1: UV-Surface vorbereiten ---
        pos = position + self.position_offset
        ux, uy, uw, uh = uv
        if uw == -1:
            uw = texture_size.x
        if uh == -1:
            uh = texture_size.y

        uv_surface = pygame.Surface((uw, uh), pygame.SRCALPHA)

        # --- Schritt 2: Tile in uv_surface kacheln ---
        for yy in range(0, uh, tile_h):
            for xx in range(0, uw, tile_w):
                blit_w = min(tile_w, uw - xx)
                blit_h = min(tile_h, uh - yy)
                part = tile.subsurface(pygame.Rect(0, 0, blit_w, blit_h))
                uv_surface.blit(part, (xx, yy))

        # --- Schritt 3: uv_surface → size skalieren ---
        scaled = pygame.transform.scale(uv_surface, (size.x, size.y))

        # --- Schritt 4: zeichnen ---
        self.screen.blit(scaled, (pos.x, pos.y))

    import pygame

    def text(self, text: str, font: str, pos: "Vector2i", size: int, color=(0, 0, 0)):
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

