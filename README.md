# Maju's Games 🎈

Jogos educativos para crianças, sem login e sem texto necessário para jogar (dá para uma criança que ainda não lê).

**Jogos:** memória · jogo da velha · pintura · escovar os dentes.

## Como rodar
É um site estático (HTML + CSS + JS, sem build). Para testar no computador:

```bash
python3 -m http.server 8000   # depois abra http://localhost:8000
```

Para abrir no celular, use o IP do computador na mesma rede Wi-Fi: `http://IP-DO-COMPUTADOR:8000`.

## Configurações no `index.html`
- `PORTFOLIO_URL`: URL do portfólio. Enquanto estiver vazia, "Criado por Rubens Victor" aparece sem link.
- `PIX_KEY`: chave PIX exibida e copiada na modal "Me pague um café".
- `assets/qr-pix.svg`: QR Code PIX. Para regenerar: `pip install segno && python3 tools/gerar_qr_pix.py`.

## Publicação
Deploy na Vercel como projeto estático (framework "Other", sem build command, raiz do repositório).

## Créditos e licenças
- Ilustrações dos animais: [Twemoji](https://github.com/jdecked/twemoji) — © Twitter, Inc. e contribuidores, licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (uso comercial permitido, com atribuição). Cópia da licença em `assets/LICENSE-twemoji-graphics.txt`.
