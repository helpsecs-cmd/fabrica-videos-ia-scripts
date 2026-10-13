# -*- coding: utf-8 -*-
"""
Montador de Videos Verticais Sinteticos (1080x1920)
Desenvolvido por Real Make IA (https://realmakeia.com)
Holding HELPSECS LTDA
"""

import subprocess
import argparse
import sys
import os

def montar_video(slide_path, audio_path, output_path):
    if not os.path.exists(slide_path):
        print(f"[ERRO] Imagem nao encontrada: {slide_path}")
        sys.exit(1)
    if not os.path.exists(audio_path):
        print(f"[ERRO] Audio nao encontrado: {audio_path}")
        sys.exit(1)
        
    print(f"[*] Montando video vertical com {slide_path} e {audio_path}...")
    
    cmd = [
        'ffmpeg',
        '-y',
        '-loop', '1',
        '-i', slide_path,
        '-i', audio_path,
        '-c:v', 'libx264',
        '-tune', 'stillimage',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-pix_fmt', 'yuv420p',
        '-shortest',
        output_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"[OK] Video gerado com sucesso em: {output_path}")
    except Exception as e:
        print(f"[ERRO] Falha ao executar FFmpeg: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Montador de Videos Curtos IA')
    parser.add_argument('--slide', required=True, help='Caminho para a imagem vertical 1080x1920')
    parser.add_argument('--audio', required=True, help='Caminho para a narracao MP3')
    parser.add_argument('--output', default='video_final.mp4', help='Nome do arquivo de saida')
    
    args = parser.parse_args()
    montar_video(args.slide, args.audio, args.output)
