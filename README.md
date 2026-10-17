# 🎬 Fábrica de Vídeos Curtos com IA (Python + FFmpeg + ElevenLabs)

> 🔥 **NOVO (Outubro/2026 — Atualização Industrial v2.0 Anti-Jitter):**
> Descobrimos em produção por que vídeos gerados com `-loop 1 -tune stillimage` sofrem queda brutal de retenção nos primeiros 2 segundos (*optical flow zero*) e como corrigimos isso com **Super-Amostragem 2160x3840 (`zoompan` a 30fps) + Queima Nativa de Legendas Dinâmicas `.ASS` (`libass`)**:
> - 🛠️ **[Acessar Dossiê de Engenharia + Compilador Online Grátis (.ASS + FFmpeg Zoompan)](https://realmakeia.com/engenharia-video-vertical-ffmpeg-zoompan-legendas-ass-python/?utm_source=github&utm_medium=readme&utm_campaign=fabrica_repo)**
> - 🧮 **[Calculadora Interativa de Custos (R$ 0,22/vídeo) + Workshop Prático](https://realmakeia.com/criar-videos-curtos-ia-sem-aparecer/?utm_source=github&utm_medium=readme&utm_campaign=fabrica_repo)**
> - ⚡ **[Baixar o Pacote Completo v2.0 (`fabrica_video_automacao.py` + 20 Roteiros Testados de Alta Retenção — R$ 27,00 via Pix/Stripe)](https://buy.stripe.com/3cIdRbevndBwdYc35qebu03)**

---

## O Problema dos Geradores de Vídeo SaaS

Plataformas SaaS de geração de vídeos cobram entre **R$ 150 e R$ 390 por mês** apenas para executar um wrapper básico de FFmpeg sobre uma API de voz neural. Neste repositório disponibilizamos a prova de conceito aberta (`v1.0`) e documentamos a arquitetura completa (`v2.0`) que opera a **R$ 0,22 por vídeo renderizado**.

### Comparativo de Engenharia (`v1.0 Starter` vs `v2.0 Industrial`)

| Recurso Técnico | `montar_video_vertical.py` (v1.0 Aberto neste Repo) | `fabrica_video_automacao.py` (Pacote Completo v2.0) |
| :--- | :--- | :--- |
| **Vetor de Movimento (Optical Flow)** | Estático (`-loop 1 -tune stillimage`) | **Ken Burns Contínuo 2x (`2160x3840 -> 1080x1920` a 30fps sem trepidação subpixel)** |
| **Motor de Legendas** | Sem legenda nativa | **Gerador Automático `.ASS` (`libass`) com queima nativa e caixa semi-opaca** |
| **Sincronia de Áudio/Vídeo** | `-shortest` simples | **Leitura exata de duração via `ffprobe` + cálculo automático de frames (`d = ceil(seg * 30)`)** |
| **Roteiros Inclusos** | — | **20 Roteiros Integrais Validados com Marcação de Gancho e Retenção** |

---

## Como Executar o Script Básico (`v1.0`)

```bash
pip install -r requirements.txt
python montar_video_vertical.py --slide cena_vertical.jpg --audio narracao.mp3 --output video_final.mp4
```

## Dossiês Técnicos & Outros Experimentos Reais

1. **[Engenharia de Vídeo Vertical em Python: FFmpeg Zoompan (2160x3840) + Legendas .ASS](https://realmakeia.com/engenharia-video-vertical-ffmpeg-zoompan-legendas-ass-python/?utm_source=github&utm_medium=readme&utm_campaign=fabrica_repo)**
2. **[Stripe no WhatsApp sem VPS: Alertas de Vendas em 184ms com Cloudflare Pages Functions](https://realmakeia.com/webhook-stripe-whatsapp-serverless/?utm_source=github&utm_medium=readme&utm_campaign=fabrica_repo)**
3. **[Estudo de Caso: O que aconteceu quando submetemos 37 artigos gerados por 5 IAs ao Google AdSense](https://realmakeia.com/reprovacao-adsense-37-artigos-ia/?utm_source=github&utm_medium=readme&utm_campaign=fabrica_repo)**

---
*Mantido por [Real Make IA](https://realmakeia.com) · HELPSECS LTDA.*
