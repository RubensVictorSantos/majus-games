"""Gera o QR Code PIX estático (BR Code) em assets/qr-pix.svg.

Uso:  pip install segno  &&  python3 tools/gerar_qr_pix.py
Edite as constantes abaixo se a chave, o nome ou a cidade mudarem.
"""
import segno

CHAVE = "3be7b45c-98f7-4d34-b26e-f852ec1cd418"
NOME = "RUBENS VICTOR"   # até 25 caracteres, sem acentos
CIDADE = "SAO PAULO"     # até 15 caracteres, sem acentos


def tlv(i, v):
    return f"{i}{len(v):02d}{v}"


def crc16(s):
    c = 0xFFFF
    for b in s.encode():
        c ^= b << 8
        for _ in range(8):
            c = ((c << 1) ^ 0x1021) if c & 0x8000 else c << 1
            c &= 0xFFFF
    return f"{c:04X}"


conta = tlv("00", "br.gov.bcb.pix") + tlv("01", CHAVE)
payload = (tlv("00", "01") + tlv("26", conta) + tlv("52", "0000") + tlv("53", "986")
           + tlv("58", "BR") + tlv("59", NOME) + tlv("60", CIDADE) + tlv("62", tlv("05", "***")) + "6304")
payload += crc16(payload)

segno.make(payload, error="m").save("assets/qr-pix.svg", scale=10, border=4, dark="#1d2b53",
                                     light="#ffffff", xmldecl=False, svgns=True, nl=False)
print(payload)
