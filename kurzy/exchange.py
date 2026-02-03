import httpx
from colorama import Fore, Style, init

init(autoreset=True)

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"


def nacti_kurzy():
    response = httpx.get(URL)
    response.raise_for_status()

    radky = response.text.splitlines()
    kurzy = {"CZK": 1.0}

    for radek in radky[2:]:
        _, _, mnozstvi, kod, kurz = radek.split("|")
        kurz = float(kurz.replace(",", "."))
        mnozstvi = int(mnozstvi)

        kurzy[kod] = kurz / mnozstvi

    return kurzy


def nacti_menu(kurzy):
    print("Dostupné měny:")
    print(", ".join(sorted(kurzy.keys())))


def nacti_menu_kod(kurzy, text):
    while True:
        kod = input(text).upper()
        if kod in kurzy:
            return kod
        print("Neplatný kód měny.")


def nacti_castku():
    while True:
        try:
            return float(input("Zadejte částku: "))
        except ValueError:
            print("Neplatná částka.")


def main():
    kurzy = nacti_kurzy()
    nacti_menu(kurzy)

    zdroj = nacti_menu_kod(kurzy, "Zadejte měnu, ze které převádíte: ")
    cil = nacti_menu_kod(kurzy, "Zadejte měnu, do které převádíte: ")

    castka = nacti_castku()

    # převod přes CZK
    vysledek = castka * kurzy[zdroj] / kurzy[cil]

    print(
        Fore.GREEN
        + f"{castka:.2f} {zdroj} = {vysledek:.2f} {cil}"
        + Style.RESET_ALL
    )


if __name__ == "__main__":
    main()
