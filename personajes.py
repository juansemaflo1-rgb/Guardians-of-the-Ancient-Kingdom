import math
from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre debe ser un texto no vacío.")
        self._nombre = valor.strip()

    @property
    def vida(self) -> int:
        return self._vida

    @vida.setter
    def vida(self, valor: int):
        if not isinstance(valor, int):
            raise TypeError("La vida debe ser un número entero.")
        if valor < 0 or valor > 100:
            raise ValueError("La vida debe estar entre 0 y 100.")
        self._vida = valor

    @property
    def ataque(self) -> int:
        return self._ataque

    @ataque.setter
    def ataque(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El ataque debe ser un entero positivo.")
        self._ataque = valor

    @property
    def defensa(self) -> int:
        return self._defensa

    @defensa.setter
    def defensa(self, valor: int):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La defensa debe ser un entero no negativo.")
        self._defensa = valor

    def esta_vivo(self) -> bool:
        return self._vida > 0

    def recibir_danio(self, cantidad: int) -> int:
        if cantidad < 0:
            raise ValueError("La cantidad de daño no puede ser negativa.")

        danio_efectivo = min(self._vida, cantidad)
        self._vida -= danio_efectivo
        return danio_efectivo

    def mostrar_estado(self) -> str:
        return f"{self._nombre} | Vida: {self._vida}/100 | Ataque: {self._ataque} | Defensa: {self._defensa}"

    def _validar_ataque(self, objetivo: "Personaje"):
        if not self.esta_vivo():
            raise ValueError(f"{self.nombre} está derrotado y no puede atacar.")
        if not isinstance(objetivo, Personaje):
            raise TypeError("El objetivo debe ser un objeto de tipo Personaje.")
        if not objetivo.esta_vivo():
            raise ValueError(f"{objetivo.nombre} ya está derrotado.")

    @abstractmethod
    def atacar(self, objetivo: "Personaje") -> int:
        pass


class Guerrero(Personaje):
    def atacar(self, objetivo: Personaje) -> int:
        self._validar_ataque(objetivo)
        ataque_potenciado = math.floor(self.ataque * 1.20)
        danio_calculado = max(0, ataque_potenciado - objetivo.defensa)
        return objetivo.recibir_danio(danio_calculado)


class Mago(Personaje):
    def atacar(self, objetivo: Personaje) -> int:
        self._validar_ataque(objetivo)
        danio_calculado = self.ataque
        return objetivo.recibir_danio(danio_calculado)


class Arquero(Personaje):
    def atacar(self, objetivo: Personaje) -> int:
        self._validar_ataque(objetivo)
        danio_base = self.ataque - objetivo.defensa
        if danio_base > 0:
            danio_calculado = danio_base * 2
        else:
            danio_calculado = 0
        return objetivo.recibir_danio(danio_calculado)


class Combate:
    def __init__(self, p1: Personaje, p2: Personaje):
        if not isinstance(p1, Personaje) or not isinstance(p2, Personaje):
            raise TypeError("Ambos participantes deben ser instancias de Personaje.")
        self.p1 = p1
        self.p2 = p2
        self.atacante = p1
        self.defensor = p2
        self.ganador = None
        self.empate = False

    def cambiar_turno(self):
        self.atacante, self.defensor = self.defensor, self.atacante

    def verificar_ganador(self) -> bool:
        if not self.p1.esta_vivo():
            self.ganador = self.p2
            return True
        if not self.p2.esta_vivo():
            self.ganador = self.p1
            return True
        return False

    def iniciar(self, max_rondas: int = 50) -> Personaje:
        print("=== INICIO DEL COMBATE ===")
        print(f"Luchadores: {self.p1.nombre} vs {self.p2.nombre}\n")

        ronda = 1
        mismo_danio_cero = 0

        while ronda <= max_rondas and not self.verificar_ganador():
            print(f"--- Turno {ronda} ---")
            danio = self.atacante.atacar(self.defensor)
            print(f"{self.atacante.nombre} ataca a {self.defensor.nombre} causando {danio} de daño.")

            print(self.p1.mostrar_estado())
            print(self.p2.mostrar_estado())
            print("-" * 35)

            if danio == 0:
                mismo_danio_cero += 1
            else:
                mismo_danio_cero = 0

            if mismo_danio_cero >= 2:
                self.empate = True
                print("\n¡Empate técnico! Ambos participantes completaron una ronda sin infligir daño.")
                break

            if self.verificar_ganador():
                break

            self.cambiar_turno()
            ronda += 1

        if ronda > max_rondas and not self.verificar_ganador():
            self.empate = True
            print("\n¡Empate! Se alcanzó el límite máximo de 50 rondas sin un ganador.")

        self.mostrar_resultado()
        return self.ganador

    def mostrar_resultado(self):
        print("\n==============================")
        print("      RESULTADO FINAL        ")
        print("==============================")
        if self.empate:
            print("El combate ha terminado en EMPATE.")
        elif self.ganador:
            print(f"¡El ganador es {self.ganador.nombre}!")
        print("==============================\n")