import asyncio
import edge_tts
import pygame
import tempfile
import os
import time

# Inicializar UNA sola vez
pygame.mixer.init(frequency=48000, size=-16, channels=2)

async def hablar(texto):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        archivo = f.name

    communicate = edge_tts.Communicate(texto, "es-ES-AlvaroNeural")
    await communicate.save(archivo)

    pygame.mixer.music.load(archivo)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(archivo)

while True:
    texto = input("🧙‍♂️ Personaje dice: ")
    asyncio.run(hablar(texto))
