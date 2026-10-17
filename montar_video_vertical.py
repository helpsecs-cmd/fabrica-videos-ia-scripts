# -*- coding: utf-8 -*-
"""
Montador de Videos Verticais Sinteticos (1080x1920) - Starter v1.0
Desenvolvido por Real Make IA (https://realmakeia.com)
Holding HELPSECS LTDA
"""

import subprocess
import argparse
import sys
import os

BANNER_V2 = """================================================================================
[REAL MAKE IA — AVISO DE ENGENHARIA v2.0]
Voce esta executando o montador basico v1.0 (-tune stillimage).
Atencao: slides estaticos possuem vetor de movimento nulo (optical flow zero)
nos primeiros 2 segundos e sofrem corte de alcance no TikTok, Reels e Shorts.

-> Gere seu comando v2.0 com Zoompan 2160x3840 + Legendas .ASS gratis no navegador:
   https://realmakeia.com/engenharia-video-vertical-ffmpeg-zoompan-legendas-ass-python/

-> Baixe o Pacote Completo v2.0 (fabrica_video_automacao.py + 20 Roteiros - R$ 27):
   https://buy.stripe.com/3cIdRbevndBwdYc35qebu03
================================================================================"""

def montar_video(slide_path, audio_path, output_path):
    print(BANNER_V2)
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
