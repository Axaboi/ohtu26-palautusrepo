- Tests executed with uv run pytest
- Code of ostos.py and tuote.py should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass
- Make changes so that the latest test passes and it does not affect other tests


# TDD
- Kirjoitetaan testiä sen verran että testi ei mene läpi. Ei siis luoda heti kaikkia luokan tai metodin testejä, vaan edetään yksi testi kerrallaan.

- Kirjoitetaan koodia sen verran, että testi saadaan menemään läpi. Ei yritetäkään heti kirjoittaa “lopullista” koodia.

- Jos huomataan koodin rakenteen menneen huonoksi (eli havaitaan koodissa esimerkiksi toisteisuutta tai liian pitkiä metodeja) refaktoroidaan koodin rakenne paremmaksi, ja huolehditaan koko ajan, että testit menevät edelleen läpi. Refaktoroinnilla tarkoitetaan koodin sisäisen rakenteen muuttamista siten, että sen rajapinta ja toiminnallisuus säilyy muuttumattomana.

- Jatketaan askeleesta 1