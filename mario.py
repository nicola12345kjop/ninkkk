class Mario:
    def __init__(self):
        self.posicao = 0  # A posição de Mario (0 é o começo)
        self.pulando = False

    def andar(self, passos):
        """Faz Mario andar para a frente ou para trás."""
        self.posicao += passos
        print(f"Mario andou {passos} passos. Agora ele está na posição {self.posicao}.")

    def pular(self):
        """Faz Mario pular."""
        if not self.pulando:
            self.pulando = True
            print("Mario pulou!")
        else:
            print("Mario já está pulando!")

    def cair(self):
        """Faz Mario cair."""
        if self.pulando:
            self.pulando = False
            print("Mario caiu.")
        else:
            print("Mario não está pulando!")

    def verificar_posicao(self):
        """Verifica a posição atual de Mario."""
        if self.posicao < 0:
            print("Mario está fora do mapa!")
        else:
            print(f"Mario está na posição {self.posicao}.")

    def enfrentar_obstaculo(self):
        """Simula a interação com um obstáculo."""
        if self.posicao == 5:
            print("Mario encontrou um Goomba! Cuidado!")
        elif self.posicao == 10:
            print("Mario encontrou uma tartaruga!")
        else:
            print("Não há obstáculos aqui.")


def jogo_mario():
    mario = Mario()
    mario.andar(3)
    mario.pular()
    mario.andar(2)
    mario.verificar_posicao()
    mario.enfrentar_obstaculo()
    mario.cair()
    mario.andar(2)
    mario.verificar_posicao()
    mario.enfrentar_obstaculo()

if __name__ == "__main__":
    jogo_mario()
