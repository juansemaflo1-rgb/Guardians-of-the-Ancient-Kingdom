from personajes import Guerrero, Mago, Arquero, Combate


def probar_casos_obligatorios():
    print("==================================================")
    print("   EJECUCIÓN DE CASOS DE PRUEBA OBLIGATORIOS     ")
    print("==================================================\n")

    print("[Caso 1] Creación correcta de personajes:")
    g = Guerrero("Arthas", 100, 30, 20)
    m = Mago("Gandalf", 80, 40, 10)
    a = Arquero("Legolas", 90, 35, 15)
    print(f"  - {g.mostrar_estado()}")
    print(f"  - {m.mostrar_estado()}")
    print(f"  - {a.mostrar_estado()}\n")

    print("[Caso 2] Validación de vida en rango (0 a 100):")
    if g.vida >= 0 and g.vida <= 100:
        print(f"  - La vida de {g.nombre} es válida ({g.vida}/100).\n")

    print("[Caso 3] Validación de nombre no vacío:")
    if g.nombre.strip() != "":
        print(f"  - El nombre '{g.nombre}' es válido.\n")

    print("[Caso 4] Validación de ataque (>0) y defensa (>=0):")
    if g.ataque > 0 and g.defensa >= 0:
        print(f"  - Los valores de ataque ({g.ataque}) y defensa ({g.defensa}) son válidos.\n")

    print("[Caso 5] Habilidad del Guerrero (Golpe poderoso):")
    g_test = Guerrero("GuerreroPrueba", 100, 30, 0)
    target_g = Guerrero("Objetivo", 100, 10, 10)
    danio_g = g_test.atacar(target_g)
    print(f"  - Daño realizado: {danio_g} (Esperado: 26)\n")

    print("[Caso 6] Habilidad del Mago (Hechizo penetrante):")
    m_test = Mago("MagoPrueba", 100, 40, 0)
    target_m = Guerrero("Objetivo", 100, 10, 20)
    danio_m = m_test.atacar(target_m)
    print(f"  - Daño realizado: {danio_m} (Esperado: 40)\n")

    print("[Caso 7] Habilidad del Arquero (Disparo crítico):")
    a_test = Arquero("ArqueroPrueba", 100, 35, 0)
    target_a = Guerrero("Objetivo", 100, 10, 15)
    danio_a = a_test.atacar(target_a)
    print(f"  - Daño realizado: {danio_a} (Esperado: 40)\n")

    print("[Caso 8] Imposibilidad de tener vida negativa:")
    p_debil = Mago("Débil", 10, 10, 0)
    p_fuerte = Mago("Atacante", 100, 50, 0)
    p_fuerte.atacar(p_debil)
    print(f"  - Vida final al recibir 50 de daño teniendo 10 de vida: {p_debil.vida}\n")

    print("[Caso 9] Verificación de estado de combate antes de atacar:")
    if not p_debil.esta_vivo():
        print(f"  - {p_debil.nombre} está derrotado (vida: {p_debil.vida}), por lo que el sistema no le permite atacar.\n")

    print("[Casos 10 y 11] Combate oficial (Arthas vs Gandalf):")
    arthas = Guerrero("Arthas", 100, 30, 20)
    gandalf = Mago("Gandalf", 80, 40, 10)
    combate_oficial = Combate(arthas, gandalf)
    combate_oficial.iniciar()

    print("[Caso 12] Finalización por empate técnico:")
    tanque1 = Guerrero("Tanque 1", 100, 10, 50)
    tanque2 = Guerrero("Tanque 2", 100, 10, 50)
    combate_empate = Combate(tanque1, tanque2)
    combate_empate.iniciar()


if __name__ == "__main__":
    probar_casos_obligatorios()