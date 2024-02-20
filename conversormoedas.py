import tkinter as tk
from forex_python.converter import CurrencyRates

class ConversorMoedas:
    def __init__(self, master):
        self.master = master
        self.master.title("Conversor de Moedas")

        # Lista de moedas disponíveis
        self.moedas = [
            "USD", "EUR", "GBP", "JPY", "CNY", "CAD", "CHF", "AUD", "SEK", "NZD",
            "BRL", "MXN", "INR", "RUB", "KRW", "ARS", "HKD", "TRY", "ZAR", "SGD",
            "THB", "MYR", "COP", "TWD", "CLP", "KWD", "ILS", "AED", "HUF", "DKK",
            "PHP", "UYU", "PLN", "MVR", "JOD", "IDR", "NOK", "DOP", "JMD", "DZD",
            "LBP", "ZMW", "SAR", "BBD", "BZD", "XOF", "LKR", "BSD", "CUP", "BND",
            "SRD", "ANG", "EGP", "KYD", "KES", "BOB", "BIF", "LRD", "TTD", "NPR",
            "ZWL", "PYG", "SZL", "FJD", "MGA", "TND", "BND", "BZD", "XAF", "GTQ",
            "XAF", "FJD", "BOB", "LRD", "KES", "FKP", "HNL", "LYD", "SGD", "SDG",
            "NAD", "GYD", "TWD", "BZD", "NZD", "COP",  # Adicione as demais moedas aqui
        ]

        # Variáveis de controle
        self.valor_origem = tk.DoubleVar()
        self.valor_destino = tk.StringVar()
        self.moeda_origem = tk.StringVar(value=self.moedas[0])
        self.moeda_destino = tk.StringVar(value=self.moedas[1])

        # Configuração da interface
        tk.Label(master, text="Valor:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(master, textvariable=self.valor_origem).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(master, text="De:").grid(row=1, column=0, padx=10, pady=10)
        tk.OptionMenu(master, self.moeda_origem, *self.moedas).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(master, text="Para:").grid(row=2, column=0, padx=10, pady=10)
        tk.OptionMenu(master, self.moeda_destino, *self.moedas).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(master, text="Converter", command=self.converter).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(master, text="Resultado:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(master, textvariable=self.valor_destino).grid(row=4, column=1, padx=10, pady=10)

    def converter(self):
        try:
            valor = float(self.valor_origem.get())
            moeda_origem = self.moeda_origem.get()
            moeda_destino = self.moeda_destino.get()

            # Obter taxa de câmbio
            c = CurrencyRates()
            taxa_cambio = c.get_rate(moeda_origem, moeda_destino)

            # Calcular valor convertido
            valor_convertido = round(valor * taxa_cambio, 2)

            # Atualizar a variável de controle
            self.valor_destino.set(f"{valor_convertido} {moeda_destino}")
        except ValueError:
            self.valor_destino.set("Erro: Insira um valor válido")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorMoedas(root)
    root.mainloop()
