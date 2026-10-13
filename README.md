# ⚡ Fábrica de Vídeos Curtos com IA (Automação em Lote)

[![Licença MIT](https://img.shields.io/badge/licenca-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-produção-brightgreen.svg)]()
[![Processado por](https://img.shields.io/badge/gateway-Stripe%20Pix-6772e5.svg)](https://buy.stripe.com/fZu7sN5YR7d8aM0eO8ebu02)

Scripts abertos de automação desenvolvidos pelo laboratório **[Real Make IA](https://realmakeia.com)** (uma iniciativa oficial **HELPSECS LTDA**).

Este repositório contém a lógica de linha de comando para renderizar vídeos verticais sintéticos (1080x1920) para TikTok, Instagram Reels e YouTube Shorts por um custo marginal de aproximadamente **R$ 0,22 por vídeo**, combinando narração de voz neural (ElevenLabs / Whisper) com imagens estáticas verticais em alta definição via FFmpeg.

---

## 🏗️ Como Funciona o Pipeline

`
[Roteiro Viral] ➔ [Voz Neural MP3] + [3 Slides 1080x1920] ➔ [Script FFmpeg] ➔ [Vídeo Final MP4 60fps]
`

---

## 🚀 Como Executar Localmente

### 1. Pré-requisitos
- Python 3.10+
- FFmpeg instalado no sistema operacional

### 2. Clonar o repositório
`ash
git clone https://github.com/helpsecs-cmd/fabrica-videos-ia-scripts.git
cd fabrica-videos-ia-scripts
`

### 3. Executar o montador
`ash
python montar_video_vertical.py --slide imagem_vertical.png --audio narracao.mp3 --output video_final.mp4
`

---

## 📦 Pacote Completo de Roteiros Testados (Comercial)

Para criadores e empresas que desejam a esteira completa pronta para monetizar:
- **20 Roteiros Prontos de Alta Retenção** (formatados para canais escuros / documentários / curiosidades).
- **Scripts de Automação de Disparo em Lote**.
- **Prompts calibrados para Midjourney / Leonardo / DALL-E**.

👉 **[Adquira o Pacote Completo por R$ 27,00 (Pix Instantâneo ou Cartão)](https://buy.stripe.com/fZu7sN5YR7d8aM0eO8ebu02)**  
*Download imediato do arquivo .ZIP processado com segurança pela HELPSECS LTDA via Stripe.*

---

## 🌐 Tutorial Completo & Calculadora de Custos
Leia o estudo de caso completo e utilize a calculadora interativa em:  
👉 **[https://realmakeia.com/criar-videos-curtos-ia-sem-aparecer/](https://realmakeia.com/criar-videos-curtos-ia-sem-aparecer/)**
