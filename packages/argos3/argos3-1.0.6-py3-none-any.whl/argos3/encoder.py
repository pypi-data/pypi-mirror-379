# """
# Codificação de canais I e Q usando NRZ e Manchester conforme o padrão PPT-A3.

# Referência:
#     AS3-SP-516-274-CNES (seção 3.2.4)

# Autor: Arthur Cadore
# Data: 28-07-2025
# """

import numpy as np
from .plotter import BitsPlot, SymbolsPlot, create_figure, save_figure

class Encoder:
    def __init__(self, method="NRZ"):
        r"""
        Inicializa o codificador de linha com o método de codificação especificado. 

        Args:
            method (str): Método de codificação desejado, $NRZ$ ou $Manchester$.

        Raises:
            ValueError: Se o método de codificação não for suportado.

        Example: 
            ![pageplot](assets/example_encoder_time.svg)

        <div class="referencia">
        <b>Referência:</b><br>
        AS3-SP-516-274-CNES (seção 3.2.4)
        </div>
        """
        method_map = {
            "nrz": 0,
            "manchester": 1
        }

        method = method.lower()
        if method not in method_map:
            raise ValueError("Método de codificação inválido. Use 'NRZ', 'Manchester'.")
                
        self.method = method_map[method]

    def encode(self, bitstream):
        r"""
        Codifica o vetor de bits usando o método especificado na inicialização. O processo de codificação de linha é dado pelas expressões abaixo correspondente a cada método. 

        $$
        \begin{equation}
        \begin{aligned}
        X_{\text{NRZ}}[n] &= 
        \begin{cases}
        +1, & \text{se } X_n = 1 \\
        -1, & \text{se } X_n = 0 ,
        \end{cases}
        &\quad\quad
        X_{\text{MAN}}[n] &=
        \begin{cases}
        +1,-1, & \text{se } X_n = 1 \\
        -1, +1, & \text{se } X_n = 0 .
        \end{cases}
        \end{aligned}
        \end{equation}
        $$

        Sendo:
            - $X_n$: Vetor de bits de entrada.
            - $X_{\text{NRZ}}[n]$ ou $X_{\text{MAN}}[n]$: Vetor de simbolos de saída.

        Args:
            bitstream (np.ndarray): Vetor de bits a ser codificado.

        Returns:
            out (np.ndarray): Vetor de simbolos codificados.
        """

        if self.method == 0:  # NRZ
            out = np.empty(bitstream.size, dtype=int)
            for i, bit in enumerate(bitstream):
                if bit == 0:
                    out[i] = -1
                elif bit == 1:
                    out[i] = +1

        elif self.method == 1:  # Manchester
            out = np.empty(bitstream.size * 2, dtype=int)
            for i, bit in enumerate(bitstream):
                if bit == 0:
                    out[2*i] = -1
                    out[2*i + 1] = +1
                elif bit == 1:
                    out[2*i] = +1
                    out[2*i + 1] = -1

        else:
            raise ValueError(f"Método de codificação não implementado: {self.method}")

        return out


    def decode(self, encodedstream):
        r"""
        Decodifica o vetor de simbolos usando o método especificado na inicialização. O processo de decodificação de linha é dado pelas expressões abaixo correspondente a cada método.

        $$
        \begin{equation}
        \begin{aligned}
        X_n &= 
        \begin{cases}
        1, & \text{se } X_{\text{NRZ}}[n] = +1 \\
        0, & \text{se } X_{\text{NRZ}}[n] = -1
        \end{cases}
        &\quad\quad
        X_n &=
        \begin{cases}
        1, & \text{se } X_{\text{MAN}}[n] = +1, -1 \\
        0, & \text{se } X_{\text{MAN}}[n] = -1, +1
        \end{cases}
        \end{aligned}
        \end{equation}
        $$
        
        Sendo: 
            - $X_{\text{NRZ}}[n]$ ou $X_{\text{MAN}}[n]$: Vetor de simbolos de entrada
            - $X_n$: Vetor de bits de saída.

        Args:
            encoded_stream (np.ndarray): Vetor codificado.

        Returns:
            out (np.ndarray): Vetor de bits decodificado.

        """

        if self.method == 0:  # NRZ
            n = encodedstream.size 
            decoded = np.empty(n, dtype=int)
            for i in range(n):
                if encodedstream[i] == -1:
                    decoded[i] = 0
                else:
                    decoded[i] = 1


        elif self.method == 1:  # Manchester
            n = encodedstream.size // 2
            decoded = np.empty(n, dtype=int)
            for i in range(n):
                pair = encodedstream[2*i:2*i + 2]
                if np.array_equal(pair, [-1, 1]):
                    decoded[i] = 0
                else:
                    decoded[i] = 1

        else:
            raise ValueError(f"Método de decodificação não implementado: {self.method}")

        return decoded

if __name__ == "__main__":

    Xn = np.random.randint(0, 2, 20)
    Yn = np.random.randint(0, 2, 20)
    print("Channel Xn: ", ''.join(str(int(b)) for b in Xn))
    print("Channel Yn: ", ''.join(str(int(b)) for b in Yn))

    # Inicializando o Encoder com o nome do método desejado ('NRZ' ou 'Manchester')
    encoder_nrz = Encoder(method="NRZ")
    encoder_man = Encoder(method="Manchester")

    Xnrz = encoder_nrz.encode(Xn)
    Yman = encoder_man.encode(Yn)

    # imprime +1 e -1 
    print("Channel X(NRZ)[n]:", ' '.join(f"{x:+d}" for x in Xnrz[:10]))
    print("Channel Y(MAN)[n]:", ' '.join(f"{y:+d}" for y in Yman[:10]))

    fig_encoder, grid = create_figure(4, 1, figsize=(16, 9))

    BitsPlot(
        fig_encoder, grid, (0, 0),
        bits_list=[Xn],
        sections=[("$X_n$", len(Xn))],
        colors=["darkgreen"],
        xlabel="Index de Bit", ylabel="$X_n$"
    ).plot()

    SymbolsPlot(
        fig_encoder, grid, (1, 0),
        symbols_list=[Xnrz],
        samples_per_symbol=1,
        colors=["darkgreen"],
        xlabel="Index de Simbolo",
        ylabel="$X_{NRZ}[n]$", 
        label="$X_{NRZ}[n]$"
    ).plot()

    BitsPlot(
        fig_encoder, grid, (2, 0),
        bits_list=[Yn],
        sections=[("$Y_n$", len(Yn))],
        colors=["navy"],
        xlabel="Index de Bit", ylabel="$Y_n$"
    ).plot()

    SymbolsPlot(
        fig_encoder, grid, (3, 0),
        symbols_list=[Yman],
        samples_per_symbol=2,
        colors=["navy"],
        xlabel="Index de Simbolo",
        ylabel="$Y_{MAN}[n]$", 
        label="$Y_{MAN}[n]$"
    ).plot()


    fig_encoder.tight_layout()
    save_figure(fig_encoder, "example_encoder_time.pdf")

    Xn_prime = encoder_nrz.decode(Xnrz)
    print("Channel X'n:", ''.join(str(int(b)) for b in Xn_prime))
    Yn_prime = encoder_man.decode(Yman)
    print("Channel Y'n:", ''.join(str(int(b)) for b in Yn_prime))

    print("Xn = X'n: ", np.array_equal(Xn, Xn_prime))
    print("Yn = Y'n: ", np.array_equal(Yn, Yn_prime))