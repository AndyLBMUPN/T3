
def calcular_promedio(notas):
    if not notas:
        raise ValueError("No hay notas registradas")
    return round(sum(notas) / len(notas), 2)


def main():
    print("=== INNOVATEC EDUCATION ===")
    print("Sistema de Gestion Academica")

    notas = [15, 17, 18]
    promedio = calcular_promedio(notas)

    print("Notas:", notas)
    print("Promedio:", promedio)


if __name__ == "__main__":
    main()
