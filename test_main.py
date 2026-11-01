import pytest

import main


@pytest.mark.parametrize("saisie,attendu", [("1", 1), ("25", 25), (" 30 ", 30), ("130", 130)])
def test_lire_age_valide(saisie, attendu):
    assert main.lire_age(saisie) == attendu


@pytest.mark.parametrize("saisie", ["", "abc", "12.5", "0", "-3", "131"])
def test_lire_age_invalide(saisie):
    assert main.lire_age(saisie) is None


def test_creer_message():
    message = main.creer_message("Kenneth", 25)
    assert "Kenneth" in message
    assert "25 ans" in message
    assert "26 ans" in message


def test_demander_age_redemande_apres_une_erreur(monkeypatch, capsys):
    reponses = iter(["abc", "-3", "25"])
    monkeypatch.setattr("builtins.input", lambda _: next(reponses))
    assert main.demander_age() == 25
    assert capsys.readouterr().out.count("ERREUR") == 2


def test_demander_nom_ignore_les_reponses_vides(monkeypatch):
    reponses = iter(["", "   ", "Kenneth"])
    monkeypatch.setattr("builtins.input", lambda _: next(reponses))
    assert main.demander_nom() == "Kenneth"
